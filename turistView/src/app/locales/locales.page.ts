import { Component, OnInit } from '@angular/core';
import { AuthService } from "src/app/services/auth.service";
import { RestService } from '../services/rest.service'; //importamos nuestro service


@Component({
  selector: 'app-locales',
  templateUrl: './locales.page.html',
  styleUrls: ['./locales.page.scss'],
})
export class LocalesPage implements OnInit {

  categorias =[];
  locales = [];
  constructor(public rest : RestService, private authservice:AuthService) { }

  ngOnInit() {
    this.getCategorias()
  }

  getCategorias() { //llamamos a la funcion getPost de nuestro servicio.
    this.rest.getCategorias().subscribe( data => {      
      for (var elemento of data.results){
        let tipo = elemento['tipo']
        this.categorias.push(tipo);
        let localesxCat =[];
        let categoria = elemento['id_categoria']
        this.rest.getLocales().subscribe( data => {
            for (var elemento of data.results){
              let nombreComercial = elemento['nombre_comercial']
              let idCat = elemento["categoria"]
              let idLocal = elemento["id_local"]
              let logo = elemento["src_logo"]
              let descripcion = elemento["descripcion"]
              if (idCat == categoria){
                localesxCat.push(
                  {nombreComercial:nombreComercial,
                    idLocal:idLocal,
                    logo:logo,
                    descripcion:descripcion
                });
              }
      
                
            }
            this.locales.push(localesxCat);
          })
      }
    })
  }
  
  

}
