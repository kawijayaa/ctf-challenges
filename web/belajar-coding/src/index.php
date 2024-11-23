<html>
    <body>
        <h1>Learn programming languages with me!</h1>
        <a href="?page=lang/python">Python</a>
        <a href="?page=lang/java">Java</a>
        <a href="?page=lang/cpp">C++</a>
        <p>
            <?php
                if (isset($_GET['page'])) {
                    if (preg_match("/^lang\/[^.]+$/", $_GET['page'])) {
                        include(urldecode($_GET['page']));
                    } else {
                        print("Don't hack me pls");
                    }
                }
            ?>
        </p>
    </body>
</html>