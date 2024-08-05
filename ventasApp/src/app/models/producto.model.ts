export interface Producto {
    codigo: string;            // Código del producto (clave primaria)
    nombre: string;            // Nombre del producto
    valorventa: number;        // Valor de venta del producto
    isiva: boolean;            // Indica si el producto incluye IVA
    porcentajeiva: number;    // Porcentaje de IVA aplicado al producto
  }
  