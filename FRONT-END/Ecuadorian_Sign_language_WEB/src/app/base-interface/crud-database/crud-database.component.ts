import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { PeticionService } from 'src/app/services/peticion.service';
import { MatDialog } from '@angular/material/dialog';
import { PopupComponent } from 'src/app/popup/popup.component';


@Component({
  selector: 'app-crud-database',
  templateUrl: './crud-database.component.html',
  styleUrls: ['./crud-database.component.css']
})

export class CrudDatabaseComponent {
  txt_dbname: string = '';
  txt_username: string = '';
  txt_password: string = '';

  constructor(private router: Router,private peticionService: PeticionService, private dialog: MatDialog ) { }

  ngOnInit(): void {
    this.loadDatabaseConfig();
  }

  loadDatabaseConfig(): void {
    this.peticionService.getDatabaseConfig().subscribe(data => {
        this.txt_dbname = data.DB_NAME;
        this.txt_username = data.USER;
        this.txt_password = data.PWD;
    });
  }

  updateDatabaseConfig(): void {
    const data = {
        USER: this.txt_username,
        PWD: this.txt_password,
        DB_NAME: this.txt_dbname
    };

    this.peticionService.updateDatabaseConfig(data).subscribe(response => {
        // Abre el popup con un mensaje de éxito
        const dialogRef = this.dialog.open(PopupComponent, {
            width: '300px', // O el ancho que desees
            data: {
                title: 'Success',
                message: 'Database Configuration Updated Successfully'
            }
        });

        // Escucha el evento de cierre del popup y redirige al usuario
        dialogRef.afterClosed().subscribe(() => {
            this.router.navigate(['/init']);
        });

    }, error => {
        // Maneja el error aquí, por ejemplo, muestra un mensaje de error.
        console.error(error);
    });
  }


  onCancelClick(): void {
    this.router.navigate(['/init']); // suponiendo que '/init' es la ruta a la que quieres ir
  }
}
