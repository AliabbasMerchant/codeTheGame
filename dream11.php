<html>
    <head>
        <title>
            Dream XI
        </title>
        <style type="text/css">
            p {
                font-family: sans-serif;
                display:inline-block;
                margin: 3px;
                margin-bottom: 0px; 
                position: relative;
                left: 50%;
                margin-right: -50%;
                transform: translate(-50%, 0%);
                text-align: center;
                font-size: 150%;
            }
            button {
                font-size: 80%;
            }
            body {
                background-color: aliceblue;
            }
            .header {
                font-size: 200%;
                color: red;
            }
            #yellowgreen {
                color: yellowgreen
            }
            #title {
                font-size: 80%;
                color:violet;
            }
            #ul {
                text-decoration: underline;
            }
            table {
                color: #333; /* Lighten up font color */
                font-family: Helvetica, Arial, sans-serif; /* Nicer font */
                width: 100%;
                font-size: 150%;
                border-collapse: collapse;
                border-spacing: 0;
                border-style: double;
                border-width: 2px;
            }
            td, th {
                border: 1px solid #CCC;
                height: 40px;
            }
            th {  
                background: #F3F3F3;
                font-weight: bold;
            }
            td {  
                background: #FAFAFA;
                text-align: center;
            }
            #names {
                font-style: italic;
                font-size: 100%;
            }
        </style>
    </head>
    <body>
        <div class = "header">
            <p>
                <span id = "ul">Code The Game</span><br>
                <span id = "yellowgreen">CO1531</span><br>
            </p>
        </div>
        <div>
            <p id = "names">
                (Swapnil Parekh, Harsh Chedda, Aliabbas Merchant)
            </p>
        </div>
        <br>
        <div class = "header">
            <p>
                <span id = "title">DREAM XI</span>
            </p>
        </div>
        <table class="myTable" id = "dream">
            <tr>
                <th> Player Name </th>
                <th> Role </th>
                <th> Team </th>
                <th> Points </th>
            </tr>
            <?php
                $str = file_get_contents('dream11.json');
                $json = json_decode($str, true); // decode the JSON into an associative array
                foreach ($json as $field => $value) {
                    $name = $value['name'];
                    $role = $value['role'];
                    $team = $value['team'];
                    $points = $value['points'];
                    echo "<tr><td><a href='player.php?name=".$name." '> ",$name,"</a></td><td>",$role,"</td><td>",$team,"</td><td>",$points,"</td></tr>" ;
                }
            ?>
        </table>
    </body>
</html>
