import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductosComponent } from './components/productos/productos.component';
import { ClientesComponent } from './components/clientes/clientes.component';
import { VentaComponent }  from './components/venta/venta.component'

const routes: Routes = [
  { path: '', redirectTo: '/ventas', pathMatch: 'full' },
  { path: 'ventas', component: VentaComponent },
  { path: 'productos', component: ProductosComponent },
  { path: 'clientes', component: ClientesComponent },
  { path: '**', redirectTo: '/ventas' } // Ruta comodín para redirigir a /ventas si la ruta no existe
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
