<!DOCTYPE html>
<html>
    <head>
		<title>A loop of your own</title>
        <link type='text/css' rel='stylesheet' href='style.css'/>
	</head>
	<body>
    <?php
  	//Add while loop below
  	$bananaCount = 0;
  	$appleCount = 0;
  	$orangeCount = 0;
  	$fruitPicked = 0;
    $targetNumber = 3;
    //maximum and minimum integers for mt_random function
    $minNum = 1;
    $maxNum = $targetNumber;
  	while ($bananaCount < $targetNumber) {
  	    $fruitPicked++;
  	    $fruit = mt_rand($minNum,$maxNum);
  	    if ($fruit == 1) {
          $bananaCount++;
          echo "<span>banana, </span>";
        } elseif ($fruit == 2) {
          $appleCount++;
          $bananaCount = 0;
          echo "<span>apple, </span>";
        } else {
          $orangeCount++;
          $bananaCount = 0;
          echo "<span>orange, </span>";
        }
        /*
        //samething using a switch 
        $fruitPicked++;
  	    $fruit = mt_rand($minNum,$maxNum);
  	    switch($fruit) {
  	        case 1:
            $bananaCount++;
            echo "<span>banana, </span>";
            break;
            case 2:
            $appleCount++;
            $bananaCount = 0;
            echo "<span>apple, </span>";
            break;
            case 3:
            $orangeCount++;
            $bananaCount = 0;
            echo "<span>orange, </span>";
            break;
            default:
                echo "something went wrong";
        }
        */

  	}
    echo "<br /><br />It took {$fruitPicked} picked fruit to get {$targetNumber} banana's in a row, including {$appleCount} apples, and {$orangeCount} oranges."

    ?>
    </body>
</html>
