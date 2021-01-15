import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { RestService } from '../services/rest.service'; //importamos nuestro service
import { ToastController } from '@ionic/angular';
import { AngularFireAuth } from "@angular/fire/auth"


@Component({
  selector: 'app-local',
  templateUrl: './local.page.html',
  styleUrls: ['./local.page.scss'],
})
export class LocalPage implements OnInit {

  public idLocal: string;

  public nombreComercial : string;
  public logo : string;
  public descripcion : string;
  public direccion : string;
  public vistas : string;
  public like : string;
  public slogan: string;
  public existeRegistro: boolean;
  public idFav : string;
  public estadoReg :boolean;
 
  constructor(private toastC: ToastController,private route: ActivatedRoute,public rest : RestService,private AFauth: AngularFireAuth) { }

  ngOnInit() {
    this.idLocal = this.route.snapshot.paramMap.get("id");
    this.getInfoLocal();
    this.isFavorite();
  }
  getInfoLocal() { //llamamos a la funcion getPost de nuestro servicio.
    this.rest.getLocal(this.idLocal).subscribe( infLocal => {
      console.log(infLocal)
        this.nombreComercial = infLocal['nombre_comercial']
        this.logo = infLocal["src_logo"]
        this.descripcion = infLocal["descripcion"]
        this.direccion = infLocal["direccion"]
        this.vistas = infLocal["vistas"]
        this.like = infLocal["likes"]
        this.slogan = infLocal["slogan"]
        

      
    })
  }

  async toastMessage(message: string){
    const toast = await this.toastC.create({
      message: message,
      duration: 2000
    });

    toast.present();
  }

  addFavorite(){
    if (this.existeRegistro){
      return this.AFauth.currentUser.then(auth =>{
        let indice = auth.email.indexOf('@');
        let usuario2 = auth.email.substring(0,indice);
        return this.rest.putFav(this.idFav,this.idLocal,usuario2, !this.estadoReg).then( ()=>{
          this.toastMessage("Agregado a Favoritos");
          if (!this.estadoReg){
            let elem: any = <HTMLElement>document.getElementById('fav');
                elem.style = "color: red;";
                this.estadoReg = !this.estadoReg
          }else{
            let elem: any = <HTMLElement>document.getElementById('fav');
                elem.style = "color: blue;";
                this.estadoReg = !this.estadoReg
          }
          
        });
        
      });
    }
    else{
      return this.AFauth.currentUser.then(auth =>{
        let indice = auth.email.indexOf('@');
        let usuario2 = auth.email.substring(0,indice);
        return this.rest.postFav(this.idLocal, usuario2).then( ()=>{
          this.toastMessage("Agregado a Favoritos");
          this.isFavorite();

        });
      });
    }
    

  }

  isFavorite(){
    
      return this.AFauth.currentUser.then(auth =>{
        let indice = auth.email.indexOf('@');
        let usuario2 = auth.email.substring(0,indice);
        return this.rest.getFavoritos().subscribe( favs => {
          for (var elemento of favs.results){
            let idLocal2 = elemento["id_local"];
            let usuario = elemento["id_usuario"];
            let activo = elemento["estado"];
            if (idLocal2 == this.idLocal && usuario == usuario2 ){
              if (activo){
                let elem: any = <HTMLElement>document.getElementById('fav');
                elem.style = "color: red;";
              }
              this.existeRegistro=true;
              this.estadoReg =activo,
              this.idFav = elemento["id_favorito"]
              
            }
            
          }
      });
      });
    
  }

}