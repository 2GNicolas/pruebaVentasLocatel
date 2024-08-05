import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Producto } from '../models/producto.model';
/**
 * Servicio para el manejo de productos
 * 
 */
@Injectable({
  providedIn: 'root'
})
export class ProductoService {
  private apiUrl = 'http://localhost:8000/productosApp/productos/'; // Cambia esta URL a la de tu backend

  constructor(private http: HttpClient) { }
/**
 * CRUD completo para los clientes
 * 
 */
  getProductos(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  addProducto(producto: Producto): Observable<Producto> {
    return this.http.post<Producto>(this.apiUrl, producto);
  }

  updateProducto(producto: Producto): Observable<Producto> {
    return this.http.put<Producto>(`${this.apiUrl}${producto.codigo}/`, producto);
  }

  deleteProducto(codigo: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}${codigo}/`);
  }
}
