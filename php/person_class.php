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

								//constructor method
								public function __construct($firstname, $lastname, $age) {
									$this->firstname = $firstname;
									$this->lastname = $lastname;
									$this->age = $age;
								} //__construct

								//Write a greeting
								public function greet() {
									echo "Hello, my name is {$this->firstname} {$this->lastname}. Nice to meet you! :-)";
								}

            } //Person

						//Instances of class Person
            $teacher = new Person("Viola", "Swamp", 48);
            $student = new Person("Bradly", "Cooper", 12);

						//Tests
						//Check living status of teacher
						//echo $teacher->isAlive; //should return 1
						//Check age of student
						//echo $student->age;
						//Echo greeting
						$teacher->greet();


        ?>
      </p>
    </body>
</html>
