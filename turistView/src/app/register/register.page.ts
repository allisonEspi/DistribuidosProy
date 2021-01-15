import { Component, OnInit } from '@angular/core';
import { AuthService } from "../services/auth.service";
import { Router } from "@angular/router"
import { ActionSheetController } from '@ionic/angular';
import { RestService } from "../services/rest.service"; //importamos nuestro service



@Component({
  selector: 'app-register',
  templateUrl: './register.page.html',
  styleUrls: ['./register.page.scss'],
})
export class RegisterPage implements OnInit {

  email: string;
  password: string;
  rpass:string;
  nombre: string;
  apellido: string;
  telefono: string;

  

  
  constructor(public rest: RestService,private authService: AuthService,  private router : Router, public actionSheetController: ActionSheetController) { }
  

  doRegister()
  {
    if (this.email!=null && this.password !=null && this.nombre!=null && this.apellido!=null && this.telefono!=null){
      this.authService.register(this.email, this.password, this.nombre+" "+this.apellido).then( () =>{
        this.router.navigate(['/tutorial']);
        this.rest.postPerfil(this.email,this.password,this.nombre,this.apellido,this.telefono).then(() =>{
          console.log("Se registro en pythonanywhere");
        }).catch(err => {
          alert(err);
        });
      }).catch(err => {
        if (err = "Error: The email address is already in use by another account."){
          alert("Usuario Registrado")
        }else{
          alert(err);
        }
        
      });
    }
    else{
      alert("Datos incompletos!!")
    }
  }

  
  ngOnInit() {
  }

  async selectImagen(){
    const actionSheet = await this.actionSheetController.create({
      header: 'Foto de perfil',
      cssClass: 'my-custom-class',
      buttons: [{
        text: 'Escoger Foto',
        role: 'destructive',
        icon: 'image',
        handler: () => {
          console.log('Delete clicked');
        }
      }, {
        text: 'Tomar Foto',
        icon: 'camera',
        handler: () => {
          console.log('Share clicked');
        }
      }, {
        text: 'Cancel',
        icon: 'close',
        role: 'cancel',
        handler: () => {
          console.log('Cancel clicked');
        }
      }]
    });
    await actionSheet.present();
  }
  

}
