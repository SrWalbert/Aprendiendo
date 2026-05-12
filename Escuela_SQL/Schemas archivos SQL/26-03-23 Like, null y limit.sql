#like sirve para buscar patrones

select * from datos.ventas where clave_producto like "__z";
select * from datos.ventas where clave_producto like "__r";

#todos los que empiezen en a
select * from datos.empleados where Nombre like "a%";
select * from datos.empleados where Nombre like "%a";


select * from datos.empleados where Nombre like "a%" order by Nombre asc;
select * from datos.empleados where Nombre like "a%" order by Nombre desc;

select * from datos.empleados where Nombre like "a%" order by Apellido asc;
select * from datos.empleados where Nombre like "a%" order by Apellido desc;


# Buscar dónde hay datos vacios en domicilio de empleados
select * from datos.empleados where Domicilio is Null;
select * from datos.empleados where Domicilio is not Null; 


select * from datos.ventas limit 3; #muestra primeros 3
select * from datos.ventas limit 3,9; #omite primeros 3 y muestra siguientes 9
select clave_producto, venta, venta*0.16 AS IVA FROM datos.ventas;