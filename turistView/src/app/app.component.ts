import { Component, OnInit } from '@angular/core';
import { AngularFireAuth } from "@angular/fire/auth"
import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
import { AuthService } from "src/app/services/auth.service";
import { ActivatedRoute } from '@angular/router';
import { TranslateService } from '@ngx-translate/core';
import { RestService } from "src/app/services/rest.service";



@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss']
})
export class AppComponent implements OnInit {
  public selectedIndex = 0;
  public user: string;
  public appPages = [];

  constructor(
    private platform: Platform,
    private rest:RestService,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private authservice:AuthService,
    private translate: TranslateService,
    private route: ActivatedRoute,
    private AFauth: AngularFireAuth 
  ) {
    this.initializeApp();
  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
      this.translate.setDefaultLang('en');
    });
  }

  ngOnInit() {
    this.appPages = [
      {
        title: 'RA-360',
        url: '/ra-camera',
        icon: 'location'
      },
      {
        title: 'Scanner',
        url: '/scanner',
        icon: 'scan'
      },
      {
        title: 'Locales',
        url: 'locales',
        icon: 'business'
      },
      {
        title: 'Notificaciones',
        url: 'notificaciones',
        icon: 'notifications'
      },
      {
        title: 'Favoritos',
        url: 'favoritos',
        icon: 'heart'
      },
      {
        title: 'Perfil',
        url: 'perfil',
        icon: 'person'
      },
      {
        title: 'Centro de Ayuda',
        url: 'contactenos',
        icon: 'call'
      }
    ];
    const path = window.location.pathname.split('folder/')[1];
    if (path !== undefined) {
      this.selectedIndex = this.appPages.findIndex(page => page.title.toLowerCase() === path.toLowerCase());
    }
  }

  logout(){
    this.authservice.logout();
  }

  

  ionViewWillLeave(){
    let elem: any = <HTMLElement>document.getElementById('menu');
    
      elem.style = "display: none";
      console.log(elem);
  }
}
