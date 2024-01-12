import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrudWordComponent } from './crud-word.component';

describe('CrudWordComponent', () => {
  let component: CrudWordComponent;
  let fixture: ComponentFixture<CrudWordComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CrudWordComponent]
    });
    fixture = TestBed.createComponent(CrudWordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
