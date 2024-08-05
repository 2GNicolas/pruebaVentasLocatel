import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Cliente } from '../models/cliente.model';
/**
 * Servicio para el manejo de clientes
 * 
 */
@Injectable({
  providedIn: 'root'
})
export class ClienteService {
  private apiUrl = 'http://localhost:8000/clientesApp/clientes/'; // Ajusta la URL de tu API

  constructor(private http: HttpClient) { }
/**
 * CRUD completo para los clientes
 * 
 */
  getClientes(): Observable<Cliente[]> {
    return this.http.get<Cliente[]>(this.apiUrl);
  }

  addCliente(cliente: Cliente): Observable<Cliente> {
    return this.http.post<Cliente>(this.apiUrl, cliente);
  }

  updateCliente(cliente: Cliente): Observable<Cliente> {
    return this.http.put<Cliente>(`${this.apiUrl}${cliente.cedula}/`, cliente);
  }

  deleteCliente(cedula: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}${cedula}/`);
  }
}
