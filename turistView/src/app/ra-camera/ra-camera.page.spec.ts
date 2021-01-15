import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { RaCameraPage } from './ra-camera.page';

describe('RaCameraPage', () => {
  let component: RaCameraPage;
  let fixture: ComponentFixture<RaCameraPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RaCameraPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(RaCameraPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
