select clave_producto, venta, venta_empleado from datos.ventas;
select * from datos.productos;
select Fecha, clave_producto, venta from datos.ventas;
select * from datos.ventas_detalle where Tipo="llevar";
select * from proveedores.pago_orden where Cantidad >=300 and Cantidad <= 700;
select Nombre, Direccion from proveedores.proveedores where Ciudad="Guadalajara" or Ciudad="Monterrey"