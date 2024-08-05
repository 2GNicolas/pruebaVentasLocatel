import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
/**
 * Servicio para el manejo de las ventas, con sus cabeceras y detalles
 * 
 */
@Injectable({
  providedIn: 'root'
})
export class VentaService {
  private apiUrl = 'http://localhost:8000/ventasApp/ventas/'; 
  
  private urlDetalles = 'http://127.0.0.1:8000/ventasApp/detalleventas/';

  constructor(private http: HttpClient) { }
/**
 * listar todas las ventas
 * @returns Observable con la lista de ventas.
 */
  getVentas(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }
/**
 * Crear una nueva venta
 * @returns Observable con la respuesta de la creacion de la venta.
 */
  createVenta(venta: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, venta);
  }
/**
 * obtener los detalles por consecutivo
 * @returns Observable con la lista de detalles.
 *  @param consecutivo - El consecutivo de la venta para la cual se deben mostrar los detalles.
 */
  getDetalles(consecutivo: number): Observable<any> {
    return this.http.get<any>(`${this.urlDetalles}?consecutivo=${consecutivo}`);
  }
}
