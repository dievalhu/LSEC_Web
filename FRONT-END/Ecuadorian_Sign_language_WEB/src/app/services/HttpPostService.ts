import { HttpClient,HttpHeaders } from '@angular/common/http';
import { PeticionService } from './peticion.service';

export class HttpPostService {

    private serverUrl = this.peticionservice.API;
    
    constructor(private http: HttpClient, private peticionservice: PeticionService) { }
    
    postData(data: any, route: string) {
        let options = this.createRequestOptions();
        console.log("DATA:",data)
        return this.http.post(this.serverUrl + route, data, { headers: options });
    }
    
    private createRequestOptions() {
        let headers = new HttpHeaders({
            "accept": "application/json",
            "Content-Type": "application/json"
        });
        return headers;
    }
}