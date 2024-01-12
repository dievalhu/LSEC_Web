import { ChangeDetectorRef, Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { AuthService } from 'src/app/services/auth.service';
import { PopupComponent } from 'src/app/popup/popup.component';
import { PeticionService } from 'src/app/services/peticion.service';
import { PreloadService } from 'src/app/services/preload.service';
import videojs from 'video.js';

interface VideoInfo {
  url: string;
}

@Component({
  selector: 'app-init',
  templateUrl: './init.component.html',
  styleUrls: ['./init.component.css']
})
export class InitComponent implements OnInit {

  loggedIn: boolean = false;

  @ViewChild('videoPlayer') videoPlayer!: ElementRef;

  textInput: string = "";
  videos: VideoInfo[] = [{ url: '' }];
  currentVideoIndex: number = 0;
  private _slideSpeed: number = 1;
  public initialized: boolean = false;
  speedValues: number[] = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2];
  translationInProgress: boolean = false;

  set slideSpeed(value: number) {
    this._slideSpeed = value;
    this.adjustPlaybackRate();
  }

  get slideSpeed(): number {
    return this._slideSpeed;
  }

  constructor(
    private peticionService: PeticionService,
    private cdRef: ChangeDetectorRef,
    private preloadService: PreloadService,
    private dialog: MatDialog,
    private authService: AuthService) { }

  ngOnInit(): void {
    // Comprobar si el usuario ya está autenticado al cargar el componente
    this.loggedIn = this.authService.isLoggedIn();

    
  }

  onSlideSpeedChange(event: any) {
    this.slideSpeed = this.speedValues[event.target.value];
  }

  async analyzeTextInput() {
    this.translationInProgress = true;
    this.videos = [{ url: '' }];
    this.currentVideoIndex = 0;
    this.initialized = false;
    this.initialized = true;
    this.stopVideos();  // Aseguramos que los videos se detengan antes de iniciar una nueva análisis
    this.peticionService.analyzeTextForVideos(this.textInput as string).subscribe(async response => {
      //console.log("response",response)
      const newVideos = this.extractVideosFromTokens(response.tokens);
      if (newVideos.length > 0) {
        this.videos = newVideos;
        await this.playVideos();
      }
    },
      (error: any) => {
        console.error("Hubo un error al analizar el texto", error);
      });
    this.translationInProgress = false;
  }

  private async playVideos() {
    if (this.videos.length > 0) {
      const firstVideo = this.videos[0];
      await this.preloadService.preloadVideo(firstVideo.url);
  
      if (this.videoPlayer) {
        this.videoPlayer.nativeElement.src = firstVideo.url;
        this.videoPlayer.nativeElement.playbackRate = this.slideSpeed;
        const playPromise = this.videoPlayer.nativeElement.play();
  
        playPromise.catch((error: any) => {
          console.error("Error al reproducir el video: ", error);
        });
      }
  
      // Continuar precargando los videos restantes en segundo plano
      for (let i = 1; i < this.videos.length; i++) {
        this.preloadService.preloadVideo(this.videos[i].url);
      }
    }
  }
  

  videoEnded() {
    if (this.currentVideoIndex + 1 < this.videos.length) {
      this.currentVideoIndex++;
      setTimeout(() => {
        const playPromise = this.videoPlayer?.nativeElement.play();
        if (playPromise) {
          playPromise.then(() => {
            this.adjustPlaybackRate();
          }).catch((error: any) => {
            console.error("Error al reproducir el video: ", error);
          });
        }
      }, 200);
    } else {
      this.stopVideos();
      this.initialized = false;
    }
  }

  adjustPlaybackRate() {
    if (this.videoPlayer) {
      this.videoPlayer.nativeElement.playbackRate = this._slideSpeed;
    }
  }

  private extractVideosFromTokens(tokens: any[]): VideoInfo[] {
    let allVideos: VideoInfo[] = [];
    tokens.forEach(token => {
      if (token.video.urls) {
        token.video.urls.forEach((url: string) => {
          allVideos.push({
            url: url,
          });
        });
      } else if (token.video.url) {
        allVideos.push({
          url: token.video.url,
        });
      }
    });
    return allVideos;
  }

  stopVideos() {
    if (this.videoPlayer) {
      this.videoPlayer.nativeElement.pause();
      this.videoPlayer.nativeElement.currentTime = 0;
    }
    this.currentVideoIndex = 0;
  }

  Reset() {
    this.textInput = "";
    this.initialized = false;
  }

  getVideoName(url: string | undefined): string {
    if (!url) return "";
    const name = url.split('/').pop()?.split('.')[0]; // Modificación aquí
    return name || "";
  }
  

  openLoginDialog(): void {
    const dialogRef = this.dialog.open(PopupComponent, {
      width: '400px',
      data: {
        title: 'Inicio de sesión',
        message: 'Por favor, ingrese sus credenciales',
        isLoginForm: true
      }
    });

    dialogRef.afterClosed().subscribe(result => {
      this.loggedIn = this.authService.isLoggedIn();
    });
  }

  logout() {
    this.authService.logout();
    this.loggedIn = false;
  }
}
