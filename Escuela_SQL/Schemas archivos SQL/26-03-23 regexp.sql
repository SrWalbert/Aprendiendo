#Expresiones regulares
#Consultas de empleados con nombre terminado en "a"
select * from datos.empleados where nombre like "%a";

#Consulta de todos los empleados con apellido que termine en Z
select * from datos.empleados where apellido regexp "ez";
select * from datos.empleados where apellido like "%ez%"; #esta opcion es menos precisa

select * from datos.empleados where apellido regexp "e";

# ^ busca la coincidencia al principio del string
#consulta todos los empleados que nombre inicie en A
select * from datos.empleados where nombre regexp "^A";
#consulta todos los nombres que terminen en o
select * from datos.empleados where nombre regexp "o$";
#todos los nombres que tengan ez ó iz ó inicien con B
select * from datos.empleados where apellido regexp "ez|iz|^B";


# UNIR TABLAS
SELECT * FROM datos.ventas v JOIN datos.empleados e ON v.venta_empleado = e.Id_empleado;
# No queremos toda la info
SELECT v.clave_producto, v.venta, e.Id_Empleado, e.Nombre, e.Apellido, e.Telefono  FROM datos.ventas v JOIN datos.empleados e ON v.venta_empleado = e.Id_empleado;