import { Component, OnInit } from "@angular/core";
import { AuthService } from "src/app/services/auth.service";
import { RestService } from "../services/rest.service"; 

@Component({
  selector: "app-notificaciones",
  templateUrl: "./notificaciones.page.html",
  styleUrls: ["./notificaciones.page.scss"],
})
export class NotificacionesPage implements OnInit {

  notificaciones = [];
  constructor(private authservice: AuthService, public rest: RestService) {}

  ngOnInit() {
    this.getNotificaciones()
  }

  getNotificaciones() { 
    this.rest.getNotificaciones().subscribe( data => {    
      console.log(data)  
      for (var elemento of data.results){
        let notificacion = elemento['notificacion']
        console.log(notificacion)
        this.notificaciones.push(notificacion);
      }
    })
  }

  logout() {
    this.authservice.logout();
  }
}
