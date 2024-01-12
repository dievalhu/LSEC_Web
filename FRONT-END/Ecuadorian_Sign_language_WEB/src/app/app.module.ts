import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

// COMPONENTS
import { PopupComponent } from './popup/popup.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';

//MODELS
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { InitComponent } from './home/init/init.component';
import { CrudWordComponent } from './base-interface/crud-word/crud-word.component';
import { CrudDatabaseComponent } from './base-interface/crud-database/crud-database.component';
import { AuthService } from './services/auth.service';
import { AuthGuard } from './services/auth.guard';
import { UpdateWordComponent } from './base-interface/update-word/update-word.component';
import { NgImageSliderModule } from 'ng-image-slider';
import { MatDialogModule } from '@angular/material/dialog';

@NgModule({
  declarations: [
    AppComponent,
    InitComponent,
    CrudWordComponent,
    CrudDatabaseComponent,
    PopupComponent,
    UpdateWordComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpClientModule,
    NgImageSliderModule,
    MatDialogModule
  ],  
  providers: [AuthService, AuthGuard],
  bootstrap: [AppComponent]
})
export class AppModule { }
