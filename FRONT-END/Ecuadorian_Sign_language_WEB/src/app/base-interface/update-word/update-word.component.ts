import { Component, OnInit } from '@angular/core';
import { PeticionService } from 'src/app/services/peticion.service';
import { PopupComponent } from 'src/app/popup/popup.component';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { concatMap } from 'rxjs/operators';
import { Observable } from 'rxjs';


interface Word {
  id_palabra: number;
  palabra: string;
  descripcion: string;
  video: string;
}

interface Character {
  id_caracter: number;
  caracter: string;
  video: string;
}

@Component({
  selector: 'app-update-word',
  templateUrl: './update-word.component.html',
  styleUrls: ['./update-word.component.css']
})
export class UpdateWordComponent implements OnInit {

  selectedType: 'palabra' | 'caracter' = 'palabra';
  wordsList: Word[] = [];
  caracterList: Character[] = [];
  selectedWord: string = '';
  txt_description: string = '';
  gifPath: string = '';
  itemList: string[] = [];
  selectedDescription: string = '';
  selectedGifPath: string = '';
  selectedFile: File | null = null;
  toText: string = '';


  constructor(
    private peticionService: PeticionService,
    private dialog: MatDialog,
    private router: Router
 ) { }

  ngOnInit(): void {
    this.fetchWordsAndCaracteres();
    
  }

  updateDescription(): void {
    if (this.selectedType === 'palabra') {
      const selectedWordObj = this.wordsList.find(wordObj => wordObj.palabra === this.selectedWord);
      this.selectedDescription = selectedWordObj ? selectedWordObj.descripcion : '';
    } else {
      this.selectedDescription = '';
    }
  }

  fetchWordsAndCaracteres(): void {
    this.peticionService.getAllPalabras().pipe(
      concatMap(palabras => {
        this.wordsList = palabras;
        //console.log('Palabras obtenidas:', this.wordsList);  // <-- Añadido
        this.itemList = this.wordsList.map(p => p.palabra);
        return this.peticionService.getAllCaracteres();
      })
    ).subscribe(caracteres => {
      this.caracterList = caracteres;
      //console.log('Caracteres obtenidos:', this.caracterList);  // <-- Añadido
      this.itemList = this.caracterList.map(c => c.caracter);
      this.onTypeChange();
    });
  }

  onTypeChange(): void {
    if (this.selectedType === 'palabra' && this.wordsList.length > 0) {
        this.itemList = this.wordsList.map(p => p.palabra);
        this.selectedWord = this.itemList[0];
        this.selectedGifPath = this.peticionService.API + `videos/palabras/${this.wordsList[0].video}`;
        this.gifPath = this.wordsList[0].video;  // Aquí asignas el nombre del archivo
    } else if (this.selectedType === 'caracter' && this.caracterList.length > 0) {
        this.itemList = this.caracterList.map(c => c.caracter);
        this.selectedWord = this.itemList[0];
        this.selectedGifPath = this.peticionService.API + `videos/caracteres/${this.caracterList[0].video}`;
        this.gifPath = this.caracterList[0].video;  // Aquí asignas el nombre del archivo
    }
    this.updateDescription();
  }

  onWordChange(): void {
      if (this.selectedType === 'palabra') {
          const selectedWordObj = this.wordsList.find(wordObj => wordObj.palabra === this.selectedWord);
          this.selectedDescription = selectedWordObj ? selectedWordObj.descripcion : '';
          this.selectedGifPath = this.peticionService.API + `videos/palabras/${selectedWordObj?.video}`;
          this.gifPath = selectedWordObj?.video ?? '';  // Aquí asignas el nombre del archivo
      } else {
          const selectedCaracterObj = this.caracterList.find(carObj => carObj.caracter === this.selectedWord);
          this.selectedDescription = '';
          this.selectedGifPath = this.peticionService.API + `videos/caracteres/${selectedCaracterObj?.video}`;
          this.gifPath = selectedCaracterObj?.video ?? '';  // Aquí asignas el nombre del archivo
      }
  }


  selectGif(): void {
    // Lógica para seleccionar un GIF
  }

  openDialog(title: string, message: string): void {
    this.dialog.open(PopupComponent, {
      width: '300px',
      data: { title: title, message: message }
    });
  }

  onCancelClick(): void {
    this.router.navigate(['/init']);
  }

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
  
    if (input.files && input.files.length) {
        const file = input.files[0];
        const fileType = file.type;
  
        // Comprueba si el tipo de archivo es .webm
        if (fileType === 'video/webm') {
            this.selectedFile = file;
            // Si deseas actualizar la variable gifPath con el nombre del archivo:
            this.gifPath = file.name;
        } else {
            this.openDialog('Error', 'Por favor, sube solo archivos .webm');
            // Reset the input field if needed
            if (input) {
                input.value = '';
            }
            this.selectedFile = null;
        }
    }
  }

  updateVideo(): void {
    console.log('Iniciando actualización...');  // <-- Añadido
    if (!this.selectedFile) {
        this.openDialog('Error', 'Por favor, selecciona un archivo .mp4 para subir');
        return;
    }

    const wordOrCharToUpdate = this.toText ? this.toText : this.selectedWord;
    console.log('Elemento a actualizar:', wordOrCharToUpdate);  // <-- Añadido

    const formData: FormData = new FormData();
    formData.append('video', this.selectedFile, this.selectedFile.name);

    let uploadObservable: Observable<any> | undefined;

    if (this.selectedType === 'palabra') {
        const selectedWordObj = this.wordsList.find(wordObj => wordObj.palabra === this.selectedWord);
        if (selectedWordObj) {
            console.log('Actualizando palabra:', selectedWordObj);  // <-- Añadido
            uploadObservable = this.peticionService.updatePalabraVideo(selectedWordObj.id_palabra, wordOrCharToUpdate, this.selectedDescription, formData);
        }
    } else if (this.selectedType === 'caracter') {
        const selectedCaracterObj = this.caracterList.find(carObj => carObj.caracter === this.selectedWord);
        if (selectedCaracterObj) {
            console.log('Actualizando caracter:', selectedCaracterObj);  // <-- Añadido
            uploadObservable = this.peticionService.updateCaracterVideo(selectedCaracterObj.id_caracter, wordOrCharToUpdate, formData);
        }
    }

    if(uploadObservable) {
        uploadObservable.subscribe(
          (response: any) => {
            console.log('Respuesta de la actualización:', response);  // <-- Añadido
            this.fetchWordsAndCaracteres();
            //location.reload();
            this.openDialog('Éxito', 'Video actualizado exitosamente');
          },
          (error: any) => {
              console.error('Error en la actualización:', error);  // <-- Añadido
              const entityType = this.selectedType === 'palabra' ? 'de la palabra' : 'del caracter';
              this.openDialog('Error', `Hubo un error al actualizar el gif ${entityType}`);
          }
        );
    } else {
        console.error("uploadObservable no está definido");
    }
  }

  
}
