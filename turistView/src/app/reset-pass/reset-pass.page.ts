import { Component, OnInit } from '@angular/core';
import { AuthService } from "../services/auth.service";
import { Router } from "@angular/router"
import { ToastController } from '@ionic/angular';


@Component({
  selector: 'app-reset-pass',
  templateUrl: './reset-pass.page.html',
  styleUrls: ['./reset-pass.page.scss'],
})
export class ResetPassPage implements OnInit {

  public email: string;
  constructor(private authService: AuthService,  private router : Router, private toastC: ToastController) { }

  ngOnInit() {
  }

  async toastMessage(){
    const toast = await this.toastC.create({
      message: "Mensaje Enviado",
      duration: 2000
    });

    toast.present();
  }

  sendLinkReset(){
    this.authService.resetPassword(this.email).then(()=>{
      console.log("Enviado")
      this.toastMessage();
      this.router.navigate(['/login']);
      

    }).catch(()=>{
      console.log("error")
    })

  }

}