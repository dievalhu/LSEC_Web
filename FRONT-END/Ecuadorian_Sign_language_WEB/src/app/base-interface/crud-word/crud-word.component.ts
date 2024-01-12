import { Component, OnInit } from '@angular/core';
import { PeticionService } from 'src/app/services/peticion.service';
import { PopupComponent } from 'src/app/popup/popup.component';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';


@Component({
  selector: 'app-crud-word',
  templateUrl: './crud-word.component.html',
  styleUrls: ['./crud-word.component.css']
})

export class CrudWordComponent implements OnInit {

  // Añade estas líneas
  txt_wordname: string | undefined;
  txt_description: string | undefined;
  txt_gif: string | undefined;
  selectedFile: File | null = null;

  constructor(private peticionService: PeticionService, private dialog: MatDialog,private router: Router) { }

  ngOnInit(): void {
  }

  onFileSelected(event: Event): void {
      const input = event.target as HTMLInputElement;

      if (input.files && input.files.length) {
          const file = input.files[0];
          const fileType = file.type;

          // Comprueba si el tipo de archivo es .webm
        if (fileType === 'video/webm') {
            this.selectedFile = file;
            // Aquí puedes agregar más lógica si necesitas hacer algo más con el archivo
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


  addWord(): void {
    if (this.txt_wordname && this.txt_description && this.selectedFile) {
        // Primero verificar si la palabra ya existe
        this.peticionService.wordExists(this.txt_wordname).subscribe(response => {
            if (response.exists) {
                // La palabra ya existe
                this.openDialog('Advertencia', 'La palabra ya existe en la base de datos.');
            } else {
                // La palabra no existe, proceder a agregar
                this.addWordToDatabase();
            }
        });
    } else {
        console.error("Missing required fields");
    }
  }

  openDialog(title: string, message: string): void {
      this.dialog.open(PopupComponent, {
          width: '300px',
          data: { title: title, message: message }
      });
  }

  addWordToDatabase(): void {
    const formData = new FormData();    

    if (this.txt_wordname && this.txt_description && this.selectedFile) {
      const formData = new FormData();
  
      // Añade la palabra, descripción y archivo al FormData
      formData.append('palabra', this.txt_wordname);
      formData.append('descripcion', this.txt_description);
      formData.append('video', this.selectedFile, this.selectedFile.name);
  
      this.peticionService.addWord(this.txt_wordname, this.txt_description, formData).subscribe(
          response => {
              // Abre el popup con un mensaje de éxito
              const dialogRef = this.dialog.open(PopupComponent, {
                  width: '300px',
                  data: { title: 'Éxito', message: 'Palabra agregada exitosamente.' }
              });

              // Escucha el evento de cierre del popup y redirige al usuario
              dialogRef.afterClosed().subscribe(() => {
                  this.router.navigate(['/init']);
              });

          },
          error => {
              console.error("Hubo un error:", error);
              this.openDialog('Error', 'Hubo un error al agregar la palabra.');
          }
      );
    }
    }


  onCancelClick(): void {
    this.router.navigate(['/init']); // suponiendo que '/init' es la ruta a la que quieres ir
  }


    
}




