import { Component, OnInit } from '@angular/core';
//import { BarcodeScanner } from '@ionic-native/barcode-scanner/ngx';
import { ModalController } from '@ionic/angular';
import { AuthService } from "src/app/services/auth.service";


@Component({
  selector: 'app-scanner',
  templateUrl: './scanner.page.html',
  styleUrls: ['./scanner.page.scss'],
})
export class ScannerPage implements OnInit {

  constructor(private modalCtrl: ModalController,private authservice:AuthService) {}


  ngOnInit() {
  }

  ionViewWillLeave(){
    let elem: any = <HTMLElement>document.getElementById('scanner-space');
    
      elem.style = "display: none";
      console.log(elem);
  }
  
  close(){
    this.modalCtrl.dismiss();
  }
  logout(){
    this.authservice.logout();
  }

}
