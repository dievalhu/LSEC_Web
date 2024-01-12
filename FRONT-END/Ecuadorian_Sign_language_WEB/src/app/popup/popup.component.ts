import { Component, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { PeticionService } from 'src/app/services/peticion.service';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-popup',
  templateUrl: './popup.component.html',
  styleUrls: ['./popup.component.css']
})
export class PopupComponent {
    loginEmail: string = '';
    loginPassword: string = '';

    constructor(
      public dialogRef: MatDialogRef<PopupComponent>,
      @Inject(MAT_DIALOG_DATA) public data: { title: string, message: string, isLoginForm?: boolean },
      private authService: AuthService,
      private peticionService: PeticionService // Inyectar el PeticionService
    ) {}
    
    login() {
      this.peticionService.login(this.loginEmail, this.loginPassword).subscribe(res => {
        if (res && res.email && res.role) {
          this.authService.login(res.role);  // Aquí utilizamos la respuesta del servidor para pasar el rol al AuthService
          this.closeDialog();
        } else {
          // Aquí deberías manejar el error o mostrar un mensaje al usuario en caso de que la autenticación falle
          console.error("Error al iniciar sesión");
        }
      }, err => {
        console.error("Error al iniciar sesión:", err);
        // Mostrar un mensaje de error aquí si el inicio de sesión no es exitoso
      });
    }
    
    closeDialog(): void {
      this.dialogRef.close();
    }
}
