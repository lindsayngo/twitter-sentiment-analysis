import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HttpClientXsrfModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SignupComponent } from './signup/signup.component';
import { RegisterComponent } from './register/register.component';

const appRoutes: Routes = [
  { path: "", component: SignupComponent },
  { path: "register", component: RegisterComponent },
]

@NgModule({
  declarations: [
    AppComponent,
    SignupComponent,
    RegisterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(
      appRoutes
    ),
    HttpClientXsrfModule.withOptions({ cookieName: 'csrftoken', headerName: 'X-CSRFToken' })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
