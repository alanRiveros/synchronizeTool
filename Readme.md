* Herramienta de sincronizacion  
=======================================================  
para que funcione el script hay que instala pyinotify  
https://github.com/seb-m/pyinotify/wiki/Install  
=======================================================  
esta basado en linux  
=======================================================  
en el quipo remoto instalar la llave publica del nuestro equipo personal  
$> ssh-copy-id -i .ssh/id_rsa.pub <user>@<host>  
nos pide el password y listo  
aconsejo tener el directorio padre creado en el equipo remoto ya que no probe que pasa si no existe  
=======================================================  
**modo de uso  
=======================================================  
$> python syncTool.py <carpeta que quieras sincronizar>  
--ejemplo  
$> python syncTool.py /home/alanRiveros/superCodigo  

