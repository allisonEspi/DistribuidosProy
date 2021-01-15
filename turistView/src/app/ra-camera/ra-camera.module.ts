import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { RaCameraPageRoutingModule } from './ra-camera-routing.module';

import { RaCameraPage } from './ra-camera.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RaCameraPageRoutingModule
  ],
  declarations: [RaCameraPage]
})
export class RaCameraPageModule {}
