import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PreloadService {

  constructor() { }

  preloadImage(url: string): Promise<void> {
    return new Promise((resolve, reject) => {
      const image = new Image();
      image.src = url;
      image.onload = () => {
        console.log(`Carga exitosa de la imagen: ${url}`);
        resolve();
      };
      image.onerror = () => {
        console.error(`Error al cargar la imagen: ${url}`);
        reject();
      };
    });
  }

  preloadVideo(url: string): Promise<void> {
    //console.log(`Iniciando carga del video: ${url}`);
    return new Promise((resolve, reject) => {
      const video = document.createElement('video');
      const onVideoLoad = () => {
        video.removeEventListener('canplaythrough', onVideoLoad);
        //console.log(`Carga exitosa del video: ${url}`);
        resolve();
      };
      video.addEventListener('canplaythrough', onVideoLoad, false);
      video.onerror = () => {
        console.error(`Error al cargar el video: ${url}`);
        reject();
      };
      video.src = url;
    });
  }
}
