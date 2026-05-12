select product_name, product_code, list_price, category from northwind.products where discontinued=0 and (category in ('Sauces','Oil', 'Dried Fruits & Nuts')) and (list_price >= 10000 or list_price <= 15000) order by list_price asc;

select company,last_name,first_name,mobile_phone from northwind.customers where last_name regexp'e' and job_title='Purchasing Manager';

select Nombre, Estado, Direccion, email from proveedores.proveedores where Nombre regexp 'x' and termino_pago >= 20 and termino_pago <= 50;

select Nombre, Apellido, Telefono, Domicilio from datos.empleados where Apellido regexp 'o' and edad >=30 and edad <= 35;

select clave_producto, venta, venta*0.16 as IVA from datos.ventas where clave_producto not in ('clz', 'brr') and not venta_empleado=2310967;