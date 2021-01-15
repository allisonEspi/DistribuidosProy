import { Component, OnInit } from '@angular/core';
import { AngularFireAuth } from "@angular/fire/auth";
import { RestService } from "src/app/services/rest.service";


@Component({
  selector: 'app-contactenos',
  templateUrl: './contactenos.page.html',
  styleUrls: ['./contactenos.page.scss'],
})
export class ContactenosPage implements OnInit {

  constructor( private AFauth: AngularFireAuth,private rest:RestService, ) { }

  usuario : String;
  ngOnInit() {
    this.getPerfil()
  }

  getPerfil(){
    return this.AFauth.currentUser.then(auth =>{
      return this.rest.getPerfil(auth.email).subscribe( infoUsuario => {
        console.log(infoUsuario);
        this.usuario = infoUsuario["username"]
    });
    });
  }

}
