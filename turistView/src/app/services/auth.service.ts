import { Injectable } from '@angular/core';
import { AngularFireAuth } from '@angular/fire/auth'
import { GooglePlus } from '@ionic-native/google-plus/ngx'
import { Router } from "@angular/router";
import { Facebook, FacebookLoginResponse } from '@ionic-native/facebook/ngx';



@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor( private google : GooglePlus, 
    private AFauth: AngularFireAuth, 
    private router : Router,
    private fb: Facebook){}

    login(email:string, password:string){

    return new Promise((resolve, rejected) =>{
    this.AFauth.signInWithEmailAndPassword(email, password).then(user => {
    resolve(user);

    }).catch(err => rejected(err));
    });


    }

    register(email : string, password : string, name : string){

    return new Promise ((resolve, reject) => {
    this.AFauth.createUserWithEmailAndPassword(email, password).then( res =>{
    console.log(res.user.uid);      

    resolve(res)
    }).catch( err => reject(err))
    })
    }

    resetPassword(email: string){
    return this.AFauth.sendPasswordResetEmail(email);
    }

    logout(){
    this.AFauth.signOut().then(() => {
    this.google.disconnect();
    this.router.navigate(['/login']);
    })
    }
    loginWithGoogle(){
      alert("Ocurrio un error inesperado");
    }

    loginWithFacebook(){
    alert("Ocurrio un error inesperado");
  

    }

    
    

  }

