import { Component, OnInit } from '@angular/core';
import { ClienteService } from '../../services/clientes.service';
import { Cliente } from '../../models/cliente.model';
/**
 * Este componente maneja toda la parte de los clientes, todo el CRUD respectivo.
 * 
 */
@Component({
  selector: 'app-clientes',
  templateUrl: './clientes.component.html',
  styleUrls: ['./clientes.component.css']
})
export class ClientesComponent implements OnInit {
  clientes: Cliente[] = [];
  newCliente: Cliente = { cedula: '', nombre: '', direccion: '', telefono: '', email: '' };
  editingCliente: Cliente | null = null;

  constructor(private clienteService: ClienteService) { }

  ngOnInit(): void {
    this.loadClientes();
  }
/**
 * Método para cargar los clientes.
 * 
 * Este método utiliza el servicio `clienteService` para obtener la lista de clientes 
 * desde el backend y luego asigna los datos a la variable `clientes`. En caso de error, 
 * se muestra un mensaje de error en la consola.
 */
  loadClientes(): void {
    this.clienteService.getClientes().subscribe(
      data => this.clientes = data,
      error => console.error('Error fetching clientes', error)
    );
  }
/**
 * Metodo para añadir los clientes 
 * 
 */
  addCliente(): void {
    this.clienteService.addCliente(this.newCliente).subscribe(
      data => {
        this.clientes.push(data);
        this.newCliente = { cedula: '', nombre: '', direccion: '', telefono: '', email: '' };
      },
      error => console.error('Error adding cliente', error)
    );
  }
/**
 * Metodo para hacer una copia del cliente en edicion
 * @param cliente - cliente que se va a editar
 */
  editCliente(cliente: Cliente): void {
    this.editingCliente = { ...cliente };
  }
/**
 * Metodo para actualizar los clientes 
 * 
 */
  updateCliente(): void {
    if (this.editingCliente) {
      this.clienteService.updateCliente(this.editingCliente).subscribe(
        data => {
          const index = this.clientes.findIndex(c => c.cedula === data.cedula);
          this.clientes[index] = data;
          this.editingCliente = null;
        },
        error => console.error('Error updating cliente', error)
      );
    }
  }
/**
 * Metodo para eliminar los clientes 
 * @param cedula - cedula que identifica al cliente a borrar
 */
  deleteCliente(cedula: string): void {
    this.clienteService.deleteCliente(cedula).subscribe(
      () => this.clientes = this.clientes.filter(cliente => cliente.cedula !== cedula),
      error => console.error('Error deleting cliente', error)
    );
  }
/**
 * Metodo para cancelar la edicion 
 * 
 */
  cancelEdit(): void {
    this.editingCliente = null;
  }
}
