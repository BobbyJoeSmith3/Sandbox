<html>
  <p>
	<?php
	// Create an array and push on the names
  // of your closest family and friends
    $fnf = array();
  array_push($fnf, "Tracy");
  array_push($fnf, "Christian");
  array_push($fnf, "Tessa");
  array_push($fnf, "Friday");
  array_push($fnf, "Grandma");
  array_push($fnf, "Grandpa");
  array_push($fnf, "Lizzy");
  array_push($fnf, "Bobby Joe");


	// Sort the list
	sort($fnf);

	// Randomly select a winner!
	$minInt = 0;
	//subtract maxInt by 1 to account for 0-indexing of arrays
	$maxInt = count($fnf) - 1;
	$winner = $fnf[mt_rand($minInt, $maxInt)];


	// Print the winner's name in ALL CAPS
	print "And the winner is: " . strtoupper($winner) . "!";
	?>
	</p>
</html>
