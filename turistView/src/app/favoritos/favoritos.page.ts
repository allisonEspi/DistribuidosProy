import { Component, OnInit } from "@angular/core";
import { AuthService } from "src/app/services/auth.service";
import { RestService } from "../services/rest.service"; //importamos nuestro service
import { ActivatedRoute } from "@angular/router";
import { AngularFireAuth } from "@angular/fire/auth";

@Component({
  selector: "app-favoritos",
  templateUrl: "./favoritos.page.html",
  styleUrls: ["./favoritos.page.scss"],
})
export class FavoritosPage implements OnInit {
  public user: string;
  locales = [];
  constructor(
    private route: ActivatedRoute,
    private authservice: AuthService,
    public rest: RestService,
    private AFauth: AngularFireAuth
  ) {}

  ngOnInit() {
    this.user = this.route.snapshot.paramMap.get("user");
    console.log(this.user);
    this.getFavoritos();
  }

  getFavoritos() {
    //llamamos a la funcion getPost de nuestro servicio.
    return this.AFauth.currentUser.then((auth) => {
      this.rest.getFavoritos().subscribe((data) => {
        console.log(data);
        for (var elemento of data.results) {
          let local = elemento["id_local"];
          let usuario1 = elemento["id_usuario"];
          this.rest.getLocal(local).subscribe((data) => {
            let nombreComercial = data["nombre_comercial"];
            let idLocal = data["id_local"];
            let logo = data["src_logo"];
            let descripcion = data["descripcion"];
            let direccion = data["direccion"];
            let slogan = data["slogan"];
            let indice = auth.email.indexOf("@");
            let usuario = auth.email.substring(0, indice);
            if (usuario == usuario1) {
              this.locales.push({
                nombreComercial: nombreComercial,
                idLocal: idLocal,
                logo: logo,
                descripcion: descripcion,
                direccion: direccion,
                slogan: slogan
              });
            }
          });
        }
      });
    });
  }
}
