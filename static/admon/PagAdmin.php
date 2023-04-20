<!DOCTYPE html>

<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oficina virtual</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<?php
session_start();
$username= $_SESSION['username'];
$rol= $_SESSION['rol'];

if (!isset($username)) {	
	header("location: index.html");	
}else{
	if($rol!== 1)
		{
		header("location: index.html");
		}
	}
?>
    <!--Menu plantilla body-->
    <div class="container">
        <div class="navigation">
            <ul class="menu">
                <li>
                    <a href="#">
                        <span class="icon"><ion-icon name="logo-apple"></ion-icon></span>
                        <span class="title">Fenrir Tech Solutions</span>
                    </a>
                </li>
                <li>
                    <a href="pag_admin.php">
                        <span class="icon"><ion-icon name="home-outline"></ion-icon></span>
                        <span class="title">Inicio</span>
                    </a>
                </li>
                <li> 
                    <a href="Acciones/Inventario.html">
                        <span class="icon"><ion-icon name="folder-outline"></ion-icon></span>
                        <span class="title">Inventario</span>
                    </a>
                </li>
                <li>
                    <a href="Acciones/registro_usuarios.php">
                        <span class="icon"><ion-icon name="documents-outline"></ion-icon></span>
                        <span class="title">Nuevo Registro</span>
                    </a>
                </li>
                <li>
                    <a href="Acciones/Aplicaciones.html">
                        <span class="icon"><ion-icon name="document-text-outline"></ion-icon></span>
                        <span class="title">Aplicaciones</span>
                    </a>
                </li>
                <li>
                    <a href="Acciones/Reporte_de_Ventas.html">
                        <span class="icon"><ion-icon name="file-tray-outline"></ion-icon></span>
                        <span class="title">Reporte de Ventas</span>
                    </a>
                </li>
               
                <li>
                    <a href="Acciones/Estadisticas.html">
                        <span class="icon"><ion-icon name="stats-chart-outline"></ion-icon></span>
                        <span class="title">Estadisticas</span>
                    </a>
                </li>
                <li>
                    <a href="../salir.php">
                        <span class="icon"><ion-icon name="log-out-outline"></ion-icon></span>
                        <span class="title">Sing out</span>
                    </a>
                </li>
            </ul>
        </div>
        <!-- Principal -->
        <div class="main">
            <div class="topbar">
                <div class="toggle">
                    <ion-icon name="menu-outline"></ion-icon>
                </div>
                
                <div class="user">
                    <img src="imagenes/user.jpg">
                </div>
            </div>
            <!-- Contenido -->
            <div class="graficas">
                rgpjreigeog
            </div>
        </div>
    </div>

    <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>

    <script src="http://code.jquery.com/jquery-1.12.0.min.js"></script>
    <script src="../js/main.js"></script>

    <script>
        //MenuToggle
        let toggle = document.querySelector('.toggle');
        let navigation = document.querySelector('.navigation');
        let main = document.querySelector('.main');

        toggle.onclick = function(){
            navigation.classList.toggle('active');
            main.classList.toggle('active');
        }

        let list = document.querySelectorAll('.navigation li');
        function activelink(){
            list.forEach((item)=> item.classList.remove('hovered'));
            this.classList.add('hovered');
        }
        list.forEach((item) => item.addEventListener('mouseover', activelink));
    </script>
</body>
</html>
