import { Component, OnInit } from '@angular/core';
import { IonSlides } from "@ionic/angular";
import { Router } from "@angular/router"



@Component({
  selector: 'app-tutorial',
  templateUrl: './tutorial.page.html',
  styleUrls: ['./tutorial.page.scss'],
})
export class TutorialPage implements OnInit {

  constructor(private router : Router) { }

  ngOnInit() {
  }

  texts = ["PASO 1","PASO 2","PASO 3"];

  slideOptions = {
    initialSlide: 1,
    speed: 400,
  };
  slidesDidLoad(slides: IonSlides) {
    slides.startAutoplay();
  }

  exitTutorial(){
    this.router.navigate(['/politicas']);
  }

}
