import { Component, OnInit } from '@angular/core';
import { VentaService } from '../../services/venta.service';
import { FormBuilder, FormGroup, FormArray, Validators } from '@angular/forms';
import { ProductoService } from '../../services/productos.service';
import { ClienteService } from '../../services/clientes.service';
import { Cliente } from '../../models/cliente.model';

/**
 * Este componente maneja toda la parte de las ventas, desde crear una nueva, asignar clientes,
 * elegir productos hasta la gestion misma de las ventas.
 * 
 */
@Component({
  selector: 'app-ventas',
  templateUrl: './venta.component.html',
  styleUrls: ['./venta.component.css']
})
export class VentaComponent implements OnInit {
  ventas: any[] = [];
  clientes: any[] = [];
  ventaForm: FormGroup;
  productos: any[] = [];
  productosSeleccionados: any[] = [];
  clienteSeleccionado: Cliente | null = null;
  detalles: any[] = []; 
  detallesVisible: { [key: number]: boolean } = {};

  constructor(private ventaService: VentaService, private productoService: ProductoService,
     private clienteService: ClienteService, private fb: FormBuilder) {
    this.ventaForm = this.fb.group({
      fecha: [new Date().toISOString().slice(0, 16)],
      cliente: [''],
      totalventa: [{ value: 0, disabled: true }],
    });

   }

  ngOnInit(): void {
    this.obtenerClientes();
    this.obtenerProductos();
    
  }
  /**
 * Metodo para obtener los clientes 
 * 
 */
  obtenerClientes(): void {
    this.clienteService.getClientes().subscribe(data => {
      this.clientes = data;
    });
  }

/**
 * Metodo para obtener las ventas 
 * 
 */
  obtenerVentas(): void {
    this.ventaService.getVentas().subscribe(data => {
      this.ventas = data;
    });
  }

  /**
 * Metodo para obetner los productos 
 * 
 */
  obtenerProductos(): void {
    this.productoService.getProductos().subscribe(
      data => {
        this.productos = data; 
      },
      error => {
        console.error('Error al obtener productos:', error);
      }
    );
  }

/**
 * funcion para detectar y guardar aquellos productos que tengan cantidad mayor a 0 
 * 
 */
  onCantidadChange(producto: any,  event: Event): void {
    const input = event.target as HTMLInputElement;
    const cantidadNumero = +input.value; // se convierte a numero la cantidad

    if (cantidadNumero > 0) {
      const productoExistente = this.productosSeleccionados.find(p => p.productocodigo === producto.codigo);
      if (productoExistente) {
        productoExistente.cantidad = cantidadNumero;
        productoExistente.iva = (producto.valorventa * producto.porcentajeiva / 100) * cantidadNumero;
      } else {
        const ivaCalculado = (producto.valorventa * producto.porcentajeiva / 100) * cantidadNumero;
        this.productosSeleccionados.push({
          productocodigo: producto.codigo,
          valorproducto: producto.valorventa,
          iva: ivaCalculado,
          cantidad: cantidadNumero
        });
      }
    } else {
      this.productosSeleccionados = this.productosSeleccionados.filter(p => p.productocodigo !== producto.codigo);
    }
    this.ventaForm.get('totalventa')?.setValue(this.calcularTotalVenta());
  }

  /**
 * funcion para enviar los datos de la venta del formulario
 * 
 */
  onSubmit(): void {
    if (this.ventaForm.valid) {
      const nuevaVenta = this.ventaForm.value;
      nuevaVenta.totalventa = this.calcularTotalVenta(); 
      nuevaVenta.detalles = this.productosSeleccionados;
      if (this.clienteSeleccionado) { 
        nuevaVenta.cliente = this.clienteSeleccionado.cedula;
    } else {
        console.error('No se ha seleccionado un cliente');
        return; 
    }

      this.ventaService.createVenta(nuevaVenta).subscribe(
        data => {
          console.log('Venta creada:', data);
          this.ventaForm.reset();
          this.productosSeleccionados = [];
        },
        error => {
          console.error('Error al crear la venta:', error);
        }
      );
    } else {
      console.log('Formulario inválido');
    }
    
  }
/**
 * funcion para calcular el total de la venta
 * 
 */
  calcularTotalVenta(): number {
    return this.productosSeleccionados.reduce((total, producto) => total + (producto.valorproducto * producto.cantidad), 0);
  }
/**
 * funcion para seleccionar el cliente al que se le va a hacer la venta
 * 
 */
  seleccionarCliente(cliente: Cliente): void {
    this.clienteSeleccionado = cliente;
    this.ventaForm.patchValue({ cliente: cliente.cedula });
  }
  /**
 * funcion para consultar los detalles relacionados por consecutivo
 * 
 */
  Detalles(consecutivo: number): void {
    if (this.detallesVisible[consecutivo]) {
      this.detallesVisible[consecutivo] = false;
      this.detalles = [];
    } else {
      this.ventaService.getDetalles(consecutivo).subscribe(data => {
        this.detalles = data;
        this.detallesVisible[consecutivo] = true;
      });
    }
  }

  
 
}
