import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateWordComponent } from './update-word.component';

describe('UpdateWordComponent', () => {
  let component: UpdateWordComponent;
  let fixture: ComponentFixture<UpdateWordComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [UpdateWordComponent]
    });
    fixture = TestBed.createComponent(UpdateWordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
