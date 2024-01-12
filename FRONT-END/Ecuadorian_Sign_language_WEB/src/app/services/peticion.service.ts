import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PeticionService {
  public API: string = 'http://34.125.169.178:4200/';

  constructor(private clienteHttp: HttpClient) { }

  private createRequestOptions() {
    let headers = new HttpHeaders({
      "accept": "application/json"
    });
    return headers;
}


  // Métodos genéricos para hacer peticiones al API
  postData(data: any, route: string): Observable<any> {
    let options = this.createRequestOptions();
    console.log(this.API + route)
    return this.clienteHttp.post(this.API + route, data, { headers: options });
  }

  getData(route: string): Observable<any> {
    return this.clienteHttp.get(this.API + route);
  }

  // Métodos específicos para cargar imágenes para el carrusel
  cargarImagenes(): Observable<any> {
    const urlAPI = "ruta/del/api/para/imagenes"; // Modifica esto a la ruta correcta
    return this.getData(urlAPI);
  }

  analyzeText(text: string): Observable<any> {
    const urlAPI = `${this.API}logic/analyze-text/?text=${encodeURIComponent(text)}`;
    return this.clienteHttp.post(urlAPI, {}); 
  }

  addWord(palabraAux: string, descripcionAux: string, wordData: FormData): Observable<any> {
    return this.clienteHttp.post(`${this.API}crud/palabra/video/?palabraAux=${palabraAux}&descripcionAux=${descripcionAux}`, wordData);
  }


  wordExists(word: string): Observable<any> {
    return this.clienteHttp.get(`${this.API}crud/palabra/exist/${word}`);
  }

  getAllPalabras(): Observable<any> {
    return this.getData('crud/palabra/');
  }

  // Método para obtener todos los caracteres
  getAllCaracteres(): Observable<any> {
    return this.getData('crud/caracter/');
  }

  updatePalabraVideo(id_palabra: number, palabra_text: string, descripcion: string, palabraData: FormData): Observable<any> {
    const url = `${this.API}crud/palabra/video/${id_palabra}/?palabra_text=${palabra_text}&descripcion=${descripcion}`;
    return this.clienteHttp.put(url, palabraData);
  }

  updateCaracterVideo(id_caracter: number, caracter_text: string, caracterData: FormData): Observable<any> {
      const url = `${this.API}crud/caracter/video/${id_caracter}/?caracter_text=${caracter_text}`;
      return this.clienteHttp.put(url, caracterData);
  }

  getDatabaseConfig(): Observable<any> {
    const url = "logic/database_config"; 
    return this.getData(url);
  }

  updateDatabaseConfig(data: any): Observable<any> {
    const route = `logic/set_database_config?USER=${data.USER}&PWD=${data.PWD}&DB_NAME=${data.DB_NAME}`;  
    let options = this.createRequestOptions();
    return this.clienteHttp.put(this.API + route, {}, { headers: options });
  }

  analyzeTextForVideos(text: string): Observable<any> {
    const urlAPI = `${this.API}logic/analyze-text-videos/?text=${encodeURIComponent(text)}`;
    return this.clienteHttp.post(urlAPI, {}); 
  }

  login(email: string, password: string): Observable<any> {
    const route = 'crud/login/';
    return this.postData({ email, password }, route);
  }
  

   
}

