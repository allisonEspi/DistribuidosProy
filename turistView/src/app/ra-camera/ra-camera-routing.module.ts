import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { RaCameraPage } from './ra-camera.page';

const routes: Routes = [
  {
    path: '',
    component: RaCameraPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class RaCameraPageRoutingModule {}
