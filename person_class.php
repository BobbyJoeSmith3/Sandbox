<!DOCTYPE html>
<html>
	<head>
	  <title>Reconstructing the Person Class</title>
      <link type='text/css' rel='stylesheet' href='style.css'/>
	</head>
	<body>
      <p>
        <!-- Your code here -->
        <?php
            class Person{
								//properties
                public $isAlive = true;
								public $firstname;
								public $lastname;
								public $age;

            } //Person

						//Instances of class Person
            $teacher = new Person();
            $student = new Person();

						//Check living status of teacher
						echo $teacher->isAlive; //should return 1

        ?>
      </p>
    </body>
</html>
