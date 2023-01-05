<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Containerized LEMP stack by Mischa van den Burg</title>
        <style>
            body {
                font-family: "Arial", sans-serif;
                font-size: larger;
            }

            .center {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 50%;
            }
        </style>
    </head>
    <body>
        <img src="https://www.technative.nl/wp-content/uploads/2021/10/TechNative_logo_colour_RGB.svg" alt="Hallo van Technative" class="center">
	<center>
	<h1>
	<br>
	Hello, this is the test page of the LEMP stack.<br>
	This application is running in 4 separate containers.<br>
	PHP, MySQL, PHPMyAdmin and NGINX as the webserver.<br>
	Installed / deployed with Ansible.<br>
	Mischa van den Burg<br><br><br>
	</h1>
	</center>
        <?php
        $connection = new PDO('mysql:host=mysql;dbname=demo;charset=utf8', 'root', 'root');
        $query      = $connection->query("SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'demo'");
        $tables     = $query->fetchAll(PDO::FETCH_COLUMN);

        if (empty($tables)) {
            echo '<p class="center">There are no tables in database <code>demo</code>.</p>';
        } else {
            echo '<p class="center">Database <code>demo</code> contains the following tables:</p>';
            echo '<ul class="center">';
            foreach ($tables as $table) {
                echo "<li>{$table}</li>";
            }
            echo '</ul>';
        }
        ?>
    </body>
</html>
