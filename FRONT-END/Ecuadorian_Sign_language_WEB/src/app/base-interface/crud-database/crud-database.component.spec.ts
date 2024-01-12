import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrudDatabaseComponent } from './crud-database.component';

describe('CrudDatabaseComponent', () => {
  let component: CrudDatabaseComponent;
  let fixture: ComponentFixture<CrudDatabaseComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CrudDatabaseComponent]
    });
    fixture = TestBed.createComponent(CrudDatabaseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
