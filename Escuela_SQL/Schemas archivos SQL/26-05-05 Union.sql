#trabajar con varias tablas
select*
from empleados e
join local l 
on e.ID_empleado=l.ID_empleados;


select*
from ventas v 
join local l
on v.ID_local=l.ID_local
join empleados e
on v.venta_empleado=e.ID_empleado;

select
v.clave_producto,
v.venta,
v.venta_empleado,
e.Nombre,
e.Apellido,
e.Telefono
from ventas v 
join empleados e 
on v.venta_empleado=e.id_empleado;

#realiza una consulta mostrando venta id, fecha, direccion (local), clave de producto venta total, nombre y apellido del empleado
#Expandir con tabla de otro esquema
select
p.periodo1_id,
p.Fecha,
e.Nombre,
e.Apellido,
l.Direccion,
p.local,
p.Turno_Completo
from periodo1 p
join datos.empleados e
on p.ID_empleado=e.ID_empleado
join datos.local l
on l.Letra_zona = p.local;

#SELF JOIN
#Jesus Angelo es gerente y jefe de todos
Select*
from empleados e
join empleados p 
on e.id_gerente = p.id_empleado;

select
e.id_empleado,
e.Nombre,
e.apellido,
e.telefono,
e.edad,
e.domicilio,
p.Nombre
from empleados e
join empleados p
on e.ID_Gerente=p.ID_empleado;

#UNION. UNIR DIFERENTES CONSULTAS
SELECT 
    producto
FROM
    productos 
UNION SELECT 
    ingredientes
FROM
    ingredientes;

#UTILIZANDO USING PARA UNIR COLUMNAS QUE TIENEN EL MISMO NOMBRE
Select
p.periodo1_id,
p.fecha,
e.Nombre,
e.Apellido,
l.direccion,
p.local,
p.turno_completo
From periodo1 p
join datos.empleados e
using (ID_empleado)
join datos.local l
on l.Letra_zona=p.local