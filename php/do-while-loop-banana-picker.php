
<html>
    <head>
		<title>Your own do-while</title>
        <link type='text/css' rel='stylesheet' href='style.css'/>
	</head>
	<body>
    <?php
        //write your do-while loop below
        //Global Variables
        $fruitsPicked = 0;
        $bananaCount = 0;
        $appleCount = 0;
        $orangeCount = 0;
        $targetNum = 3;
        $intMin = 1;
        $intMax = $targetNum;
        $bananaStreak = 0;
        // pick fruit while banana streak is less than three
        do {
          $fruit = mt_rand($intMin, $intMax);
          $fruitsPicked++;
          switch($fruit){
            case 1:
              $bananaCount++;
              $bananaStreak++;
              echo "<span>banana, </span>";
              break;
            case 2:
              $appleCount++;
              $bananaStreak = 0;
              echo "<span>apple, </span>";
              break;
            case 3:
              $orangeCount++;
              $bananaStreak = 0;
              echo "<span>orange, </span>";
              break;
            default:
              echo "There's always money in the banana stand.";
          } //end switch
        } while ($bananaStreak < $targetNum);
        echo "<br /><br /> It took {$fruitsPicked} picked fruits to get {$targetNum} bananas in a row, including {$appleCount} apples and {$orangeCount} oranges.";

    ?>
    </body>
</html>
