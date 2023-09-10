<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    if (isset($_POST["message"])) {
        $message = $_POST["message"];

        // Verificar se o diretório "messages" existe ou criar se não existir
        if (!is_dir("./messages")) {
            mkdir("./messages");
        }

        $files = scandir("./messages");
        $num_files = count($files) - 2; // . e ..

        $fileName = "msg-{$num_files}.txt";

        $file = fopen("./messages/{$fileName}", "x");

        if ($file) {
            fwrite($file, $message);
            fclose($file);
            header("Location: index.php");
        } else {
            echo "Não foi possível criar o arquivo.";
        }
    } else {
        echo "O campo 'message' não foi enviado.";
    }
} else {
    echo "Este script deve ser acessado via método POST.";
}
?>
