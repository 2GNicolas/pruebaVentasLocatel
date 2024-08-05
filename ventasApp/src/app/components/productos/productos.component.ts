import { Component, OnInit } from '@angular/core';
import { ProductoService } from '../../services/productos.service';
import { Producto } from '../../models/producto.model';
/**
 * Este componente maneja toda la parte de los productos, todo el CRUD respectivo.
 * 
 */
@Component({
  selector: 'app-productos',
  templateUrl: './productos.component.html',
  styleUrl: './productos.component.css'
})
export class ProductosComponent implements OnInit{
  productos: Producto[] = [];
  newProducto: Producto = { codigo: '', nombre: '', valorventa: 0, isiva: false, porcentajeiva: 0 };
  editingProducto: Producto | null = null;

  constructor(private productoService: ProductoService) { }

  ngOnInit(): void {
    this.loadProductos();
  }
  /**
 * Metodo para cargar los productos 
 * 
 */
  loadProductos(): void {
    this.productoService.getProductos().subscribe(
      data => this.productos = data,
      error => console.error('Error fetching productos', error)
    );
  }
/**
 * Metodo para añadir los productos 
 * 
 */
  addProducto(): void {
    this.productoService.addProducto(this.newProducto).subscribe(
      data => {
        this.productos.push(data);
        this.newProducto = { codigo: '', nombre: '', valorventa: 0, isiva: false, porcentajeiva: 0 };
      },
      error => console.error('Error adding producto', error)
    );
  }
/**
 * Metodo para generar una copia del producto en edicion
 * @param producto - producto que se va a editar
 */
  editProducto(producto: Producto): void {
    this.editingProducto = { ...producto };
  }
/**
 * Metodo para editar un producto
 * 
 */
  updateProducto(): void {
    if (this.editingProducto) {
      this.productoService.updateProducto(this.editingProducto).subscribe(
        data => {
          const index = this.productos.findIndex(p => p.codigo === data.codigo);
          this.productos[index] = data;
          this.editingProducto = null;
        },
        error => console.error('Error updating producto', error)
      );
    }
  }
/**
 * Metodo para eliminar un producto
 * @param codigo - Codigo por el cual se identifica el producto a borrar
 */
  deleteProducto(codigo: string): void {
    this.productoService.deleteProducto(codigo).subscribe(
      () => this.productos = this.productos.filter(producto => producto.codigo !== codigo),
      error => console.error('Error deleting producto', error)
    );
  }
/**
 * Metodo para cancelar la edicion
 * 
 */
  cancelEdit(): void {
    this.editingProducto = null;
  }
}
