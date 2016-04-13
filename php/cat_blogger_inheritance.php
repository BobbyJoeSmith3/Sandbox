<html>
  <head>
    <title></title>
  </head>
  <body>
    <p>
      <?php
      class Person {
        static public function say() {
          echo "Here are my thoughts!";
        }
      }
      class Blogger extends Person {
        const cats = 50;
      }
      Blogger::say();
      echo Blogger::cats;
      ?>
    </p>
  </body>
</html>
