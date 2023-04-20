<?php
    include_once 'conexionBD.php';
    
    session_start();

    if(isset($_GET['cerrar_sesion'])){
        session_unset(); 

        // destroy the session 
        session_destroy(); 
    }
    
    if(isset($_SESSION['rol'])){
        switch($_SESSION['rol']){
            case 1:
                header('location: pag_admin.php');
            break;

            case 2:
            header('location: index.html');
            break;

            default:
        }
    }
	

    if(isset($_POST['username']) && isset($_POST['password'])){
        $username = $_POST['username'];
        $password = $_POST['password'];

        $db = new Database();
        $query = $db->connect()->prepare('SELECT *FROM users WHERE nombre_user = :username AND password = :password');
        $query->execute(['username' => $username, 'password' => $password]);

        $row = $query->fetch(PDO::FETCH_NUM);

		$_SESSION['username'] = $username;

		echo $_SESSION['username'];

        
        if($row == true){
            $rol = $row[4];
            
            $_SESSION['rol'] = $rol;
            switch($rol){
                case 1:
                    header('location: pag_admin.php');
                break;

                case 2:
                header('location: Principal.php');
                break;

                default:
            }
        }else{
            // no existe el usuario
            echo "Nombre de usuario o contraseña incorrecto";
        }
        

    }

?>
