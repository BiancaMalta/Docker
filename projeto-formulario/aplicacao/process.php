<?php

function mysqlConnect()
{
  $db_host = "db";
  $db_user = "root";
  $db_password = "root";
  $db_name = "banco_de_dados";

  // dsn é apenas um acrônimo de database source name
  $dsn = "mysql:host=$db_host;dbname=$db_name;charset=utf8mb4";

  $options = [
    PDO::ATTR_EMULATE_PREPARES => false, // desativa a execução emulada de prepared statements
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // ativa o modo de erros para lançar exceções
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // altera o modo padrão do método fetch para FETCH_ASSOC
  ];

  try {
    $pdo = new PDO($dsn, $db_user, $db_password, $options);
    return $pdo;
  } 
  catch (Exception $e) {
    //error_log($e->getMessage(), 3, 'log.php');
    exit('Ocorreu uma falha na conexão com o BD: ' . $e->getMessage());
  }
}


function mysqlConnect2(){
  $hostname = "localhost";
  $bancodedados = "banco_de_dados";
  $usuario = "root";
  $senha = "";
  $mysqli = new mysqli($hostname, $usuario, $senha, $bancodedados);
  if($mysqli->connect_errno) {
    echo "Falha ao conectar: (" . $msqli->connect_errno . ")" . $mysqli->connect_error;
    }
}

$pdo = mysqlConnect();

$nome = $_POST["nome"] ?? "";
$cpf = $_POST["cpf"] ?? "";
$email = $_POST["email"] ?? "";
$senha = $_POST["senha"] ?? "";
$estadocivil = $_POST["estadocivil"] ?? "";
$datanascimento = $_POST["datanascimento"] ?? "";

// calcula um hash de senha seguro para armazenar no BD
$hashsenha = password_hash($senha, PASSWORD_DEFAULT);

try {

  $sql = <<<SQL
  -- Repare que a coluna Id foi omitida por ser auto_increment
  INSERT INTO cliente (nome, cpf, email, hash_senha, 
                       data_nascimento, estado_civil)
  VALUES (?, ?, ?, ?, ?, ?)
  SQL;

  // Neste caso utilize prepared statements para prevenir
  // ataques do tipo SQL Injection, pois precisamos
  // cadastrar dados fornecidos pelo usuário 
  $stmt = $pdo->prepare($sql);
  $stmt->execute([
    $nome, $cpf, $email, $hashsenha,
    $datanascimento, $estadocivil,
  ]);

  header("location: index.html");
  exit();
} 
catch (Exception $e) {
  //error_log($e->getMessage(), 3, 'log.php');
  if ($e->errorInfo[1] === 1062)
    exit('Dados duplicados: ' . $e->getMessage());
  else
    exit('Falha ao cadastrar os dados: ' . $e->getMessage());
}

?>
