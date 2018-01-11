<html>
    <head>
        <title>
            <?php

            ?>
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
        <!-- <script type = "text/javascript">
            document.getElementById("Dream11").onclick = function() {
                window.open('dream11.html');
                // <a href = ""> </a>
            }
        </script> -->
    </head>
    <body>
        <div class = "header">
            <p>
                <span id = "ul">Code The Game</span><br>
                <span id = "yellowgreen">CO1531</span>
            </p>
        </div>
        <div>
            <p id = "names">
                (Swapnil Parekh, Harsh Chedda, Aliabbas Merchant)
            </p>
        </div>
        <br>
        <br>
        <!-- <div id = "upload" >
            <p>
                Upload a file to view the analysis: &emsp;
                <button id = "Browse">Browse</button> &emsp;
                <button id = "Anlayse">Anlayse</button>            
            </p>
        </div>
        <br>
        <br>
        <div>
            <p id = "analyse">
                <button id = "New">Anlayse New Data</button> &emsp;
                <button id = "Old">Anlayse Old Data (of given 10 matches)</button> &emsp;
                <button name = "All">Anlayse All Data</button>
            </p>
        </div>
        <br>
        <br> -->
        <div>
            <p>
            <button id = "Dream11" onclick="window.open('dream11.php');">Dream XI</button>
            </p>
        </div>
        <br>
        <br>
        <table class="myTable">
            <tr>
                <th> Player Name </th>
                <th> Role </th>
                <th> Team </th>
                <th> Points </th>
            </tr>
            <?php
                $str = file_get_contents('consolidated_data.json');
                $json = json_decode($str, true); // decode the JSON into an associative array
                foreach ($json as $field => $value) {
                    $name = $value['name'];
                    $role = $value['role'];
                    $team = $value['team'];
                    $points = $value['points'];
                    echo "<tr><td><a href='player.php?name=".$name." '> ",$name,"</a></td><td>",$role,"</td><td>",$team,"</td><td>",$points,"</td></tr>" ;
                }
                // $temperatureMin = $json['daily']['data'][0]['temperatureMin'];
                // echo "<tr><td> Player Name </td><td> Role </td><td> Team </td><td> Points </td></tr>" ;
            ?>
        </table>
    </body>
</html>