#AND, OR, NOT
#Mostrar información conjunta en 

select * from datos.ventas where ID_local=2 and clave_producto="pzz";

#mostrar las ventas del local 2 y 4
select * from datos.ventas where ID_local=2 or ID_local=4;

#mostrar todas las ventas que no sean de pizza
select * from datos.ventas where clave_producto!="pzz";
select * from datos.ventas where NOT clave_producto="pzz";

#Mostrar ventas que no son pizzas ni tampoco local 2
select * from datos.ventas where NOT (clave_producto="pzz" or ID_local=2);
select * from datos.ventas where NOT ID_local=2 and NOT clave_producto="pzz";


select * from datos.ventas where venta >=500 and venta <=1000;
select * from datos.ventas where venta between 500 and 1000;
#Empleando sin IN 
select * from datos.ventas where clave_producto="pzz" or clave_producto="clz" or clave_producto="qsd";
select * from datos.ventas where clave_producto IN ("pzz","clz","qsd");