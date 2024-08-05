import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module'; // Importa el módulo de enrutamiento
import { ReactiveFormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { VentaComponent } from './components/venta/venta.component';
import { ProductosComponent } from './components/productos/productos.component';
import { ClientesComponent } from './components/clientes/clientes.component';

@NgModule({
  declarations: [
    AppComponent,
    VentaComponent,
    ProductosComponent,
    ClientesComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
