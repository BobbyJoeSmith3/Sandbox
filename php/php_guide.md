#PHP and MySQL Cheatsheet
The purpose of this document is to store commonly used commands and code snippets for php and mysql development.

##Terminal Commands
The Apache server is referenced in Unix as `httpd` which is short for *Hyper Text Transfer Protocol Daemon*. A Daemon is a program that sits waiting to respond to requests, which is exactly what Apache is doing for web requests.

 __Check current version of apache installed on machine:__
 ```unix
 $ httpd -v
 ```
 __Check if apache is running:__
 ```unix
 $ ps aux | grep httpd
 ```
 If the only thing that is returned is the search command you just entered, then apache is not running.

 __Start, Stop, and Restart apache:__
 ```unix
 $ sudo apachectl start
 $ sudo apachectl stop
 $ sudo apachectl restart
 ```
To __give apache access to a directory__ making it the root directory, navigate to the directory in the command terminal then create a configuration file:
```unix
$ sudo nano yourusername.conf
```
Then type into the file:
```unix
<Directory "/Users/YourUserName/Sites/">
    Options Indexes MultiViews
    AllowOverride All
    Order allow,deny
    Allow from all
</Directory>
```
Now we need to change the permissions on this file to make sure Apache has permission to read it.
```
$ sudo chmod 644 yourusername.conf
```
Enter in your password and then restart apache with `$ sudo apachectl restart`

NOTE: If you're working on Mac OS 10.10, otherwise known as Yosemite or a version of Mac OS after that then that last step may not have worked for you. And the reason why, is because Apple changed some of their default configurations for Apache. So if you tried to get your document root and you tried to load up your user directory and instead you got "Not Found" then you'll want to try these steps.
1. Navigate to the Apache configuration directory `$ cd/etc/apache2`. In that directory you'll see the configuration file for apache httpd.conf.
2. Edit that file using the highest level of privileges `$ sudo nano httpd.conf`
3. The httpd.conf file has a lot of code in it, so you will want to search the document for the code we need by using the 'Where is' function in the nano text editor by typing `ctrl + w`. Search for `userdir` and it will go right to the line that contains the userdir module, which is the code Apache needs to work with user directories like the one we are trying to create.
4. You will see that the `userdir` module has been commented out. Uncomment this line by removing the hashtag:
```
#LoadModule userdir_module libexec/apache2/mod_userdir.so
```
5. Do another search with `ctrl + w` and look for `httpd-userdir`. You will come up with a line that says Include and then list a place for userdir config file. Uncomment that as well. Now, when our main Apache configuration file loads up, it's going to load up the code having to deal with user directories and then it's going to include this configuration file. Notice the path to that configuration file. It's inside our apache2 directory, inside extra and then you'll see the name is httpd-userdir.conf.
6. Exit the file and save the changes.
7. Now we are going to want to make changes to the httpd-userdir.conf file in the 'extra' directory. Type `sudo nano extra/httpd-userdir.conf` into the command line.
8. Go to the commented out line `#Include /private/etc/apache2/users/*.conf`. This line tells Apache to not only load up it's default configuration, but to go and get my customizations out of the users directory. Exit out and save.
9. Now we are going to want to restart Apache, but first run a configuration test to make sure the syntax is okay.
```
$ sudo apachectl configtest
```
If everything clears, you should receive a message that says `Syntax OK`.
10. Restart the Apache server.
11. There were changes in the way permissions work in Apache 2.4 which was released with Yosemite, so now we have to make changes related to that. Navigate inside of the Apache2 directory and edit the Apache config file. Search for `authz_core`. Make sure the `LoadModule authz_core_module ...` line is NOT commented out.
12. Search for `authz_host` and make sure that line is not commented out as well. These are the two modules we are going to need to use the new authorization scheme built into Apache 2.4.
13. Now we have to make one more change to our user config file. Open up the file. Delete the two lines Order and Allow (you can cut out an entire line by hitting `ctrl + k`), and replace it with `Require all granted`. Exit and save. Do a config test and the restart the server.

This was a two step process that re-enabled the things that Apple turned off in its defaults and then we needed to upgrade our configuration for Apache 2.4. Now that we've done that, we'll have a document root that we can use for our PHP projects.

__Activate PHP__
PHP is installed and we have version 5.5. But it's not active yet. We need to tell Apache, hey Apache, you need to be prepared for some PHP files, be prepared to process those.

And you do that by loading up one of your modules that knows how to interpret PHP. That module's included. It's just not turned on. So, in order to do that, we need to do some configuration to Apache.

1. Navigate to the Apache configuration directory `$ cd /etc/apache2` and edit the httpd.conf file.
2. Search for 'php' to locate the php5_module. This is the module that gives Apache the knowledge to interpret php code, but it's not loaded, so uncomment the line. Next time apache loads, it will load the PHP interpreter module as well. Exit and save the changes to the file.
3. Restart Apache.

__Configure PHP__
Configure the error reporting, the output buffering, and the default timezone.

To find out where our PHP config file lives, open up the my_phpinfo.php page and see what it says under the table field 'Loaded Configuration File'. You will also want to look for the directory path indicated under 'Scan this dir for additional .ini files', since we actually have configuration stored in two places - in our main ini file and these extra files inside this other directory. This directory happens to be in my /etc directory as php.ini.default

1. Search for `Display_errors` in ini file. We will know we got to the right line because there wont be a semicolon in front of it. Lines that don't have semicolons are the real active lines with the actual configurations going on. You can see that it actually gives me some helpful information. It tells me what the default value is, the development value, production value that you'd want to have. Now, for in development, we want to see our errors. We want to know what went wrong so we can fix it, we want as much information as possible. But when we actually deploy it to the real world, we are not going to want to give all sorts of server information to people so we are going to turn off the errors in that case. But you want to make sure that right now, display errors is on.
2. Search for `error_reporting`. You should see `E_All` which states that you want to see all errors. If you want to add things to be seen, type `E_ALL | E_AdditionalErrors`. If you don't want certain errors use `& ~E_AdditionalErrors`. Types of errors include Strict, Notices, Deprecations (code that's going to be going away soon). You want to turn deprecation and strict off for production, but you want them on during development.
3. Search for `html_errors` and make sure ti's turned on. This says that when we do see errors, give them to us in an HTML format.
4. Search for `output_buffering`. This has a value of 4096, which is how much data it will buffer before it outputs. You can turn this off, but you'll often want to have it on during development.
5. Search for `timezone`. The line that we want is `;date.timezone =` and it is currently commented out. Uncomment it. Insert the appropriate timezone in quotes based on the format specified by php. It will be important to have a timezone set when working with date in php to avoid warnings.
6. Exit and save file. Restart Apache.


__Configure MySQL__
Add MySQL to PATH, Set root password (default is no password). The first task is that we want to set up MySQL so that it's accessible from our PATH. The path is a list of directories that UNIX uses in order to locate programs on the machine that it can run. We can take a look at the list of directories UNIX uses to find programs by typing `$ echo $PATH`. This will return a variable that contains a list of the directories it's going to check in with colons in between each one of those in order of priority until it finds what we're looking for. It will go through all of those and not find MySQL, so we need to add our location for that. The directory MySQL will be located in is `/usr/;pca;/mysql/bin`. We need to add this path to one of our bash configuration files `.bash_profile`.

In the .bash_profile type in `export PATH="/usr/local/mysql/bin:$PATH"` That's going to echo back the value of PATH that we just saw. But before we echo it, we're also going to append to it, user/local/mysql/bin:. So it's basically saying the path now is going to be equal to this new directory, followed by whatever was previously set by the operating system.

We want to use another program that's in that same folder to set the root password, and that's going to be the MySQL admin program. This is the program that lets us set passwords, among other things. Mysqladmin and the user we want to set it for is our root user. Root is the name of the sort of most powerful user on any Unix system, and it's true for MySQL as well. `$ mysqladmin -u root password`. If a password is already set, use `$ mysqladmin -u root -p password`.

##PHP
__Embed PHP in HTML__
```PHP
<$php ...?>
```
White space doesn't matter. Every line will need to end in a semicolon. The HTML file will need to end in .php instead of .html, so that the Apache webserver will know to look out for php tags. Then, when it sees a php tag it turns on it's PHP module, starts processing the php until we close the php section.

echo is the most important php command or function that you will need to know. Echo is going to return whatever we say, back to the user, like an echo. We say something, that's what gets echoed back to the user so that they see it. You can think of it like printing it to the users browser and we'll use it inside our PHP tags with whatever we want to echo back. For example: `<?php echo "Hello world"; ?>`

__Request Response Cycle__
Browser makes a request to the web server. The request is interecepted by web server software called a HTTP Daemon installed on the web server, in this case Apache. Apache searches through the file system on the web server for a file that will help respond to the request. If it finds the file and sees that it's a .php file, Apache will go about interpreting/processing the php. While processing, it may need to make multiple requests to the database. Once Apache is done processing the PHP, it moves on to the final step which is assembling the HTML that's going to be returned and shipped back to the browser. There is no chance to process PHP after the HTML has been completely generated, or once it has gotten to the user's browser.

__Comments__
Single-line comments `//` or less commonly used `#`.
`/* Double-line comments are written like this */`.
Comments are not nested.

__Variables__
```php
<?php
  $var1 = 10;
  echo $var1;

  //we can put html inside of a string
  echo "<br/>";

  $var2 = "Hello world <br/>";
  echo $var2;

  $greeting = "Hello";
  $target = "World";
  $phrase = $greeting . " " . $target;
  echo $phrase
?>
```

In PHP, there's some rules about the kinds of names that we can give to variables.

They need to start with a dollar sign, that needs to be followed by either letter or an underscore, they can contain letters, numbers, underscores or dashes. They cannot contain any spaces and they are case sensitive. It makes a difference whether we use an upper case letter or a lowercase letter.

Examples:
```php
$item
$Item
$myVariable
$this_variable
$this-variable
$product3
$_book
$__bookPage
```
All of these examples are valid, however some formats are better than others. Steer away from using a hyphen like in `$this-variable`, because it looks like a minus sign.

Multiple underscores make it difficult to tell how many are there, like in `$__bookPage`.

Variables with a single underscore at the beginning, as in `$_book` need to be used with caution because they generally have a special connotation to both PHP and other developers. We're going to see that PHP has some special variables. They're named with this underscore at the beginning, and some developers use this underscore for special cases. They want to denote the fact that a variable has certain access privileges, that certain people can or can't access things by putting that underscore in front of it. Because it has this special meaning both to PHP and to other developers, it's best to stay away from it for general use.

PHP actually has some words that are reserved, words that you're not allowed to use for different things, and it's a good idea to take a review of this list, and then stay away from those words as much as possible. Sometimes, it's not a problem to use it for a variable name, but it might be a problem to use it in other contexts. It's basically just names with special meaning to PHP that we don't want to use. You can view them at <http://www.php.net/manual/en/reserved.php>.

You can put variables and html inside of strings, but it only works with double quotes.
```php
<?php
  $phrase = "Hello World";
  echo "$phrase Again<br />";
  //outputs "Hello World Again"
?>
```

You can differentiate a variable from a non-variable with curly brackets.
```php
<?php
  $phrase = "Hello World";
  echo "{$phrase}Again<br />";
  //outputs "Hello WorldAgain"
?>
```

You can escape a value like a curly brace or quotation mark with a `\`.

You can concatenate and assign at the same time with `.=`:
```php
<?php
  $first = "The quick brown fox";
  $second = " jumped over the lazy dog.";

  $third = $first;
  $third .= $second;
  echo $third;
  //outputs "The quick brown fox jumped over the lazy dog."
?>
```

__Arrays__
```php
<?php
  $numbers = array(4,8,15,16,23,42);
  echo $numbers[1]; //outputs: 8
?>
```

If you just try to print an array by echoing the variable name assigned to the array, PHP will simply tell you that an array exists there instead of printing everything that's in the array. If you want to print the contents of an array use `print_r` which stands for print readable:
```php
<?php
  $mixed = array(6, "fox", "dog", array("x", "y", "z"));
  echo print_r($mixed);
?>
```
Which outputs `Array([0] => 6 [1] => fox [2] => dog [3] => Array([0] => x [1] =>y [2] => z))1`

If you put html `<pre> </pre>` tags around the php code.
```php
  <pre>
    <?php echo print_r($mixed); ?>
  </pre>
```
outputs:
```
      Array
(
  [0] => 6
  [1] => fox
  [2] => dog
  [3] => Array
    (
      [0] => x
      [1] => y
      [2] => z
    )
  )
```

If you want just one value from an array:
```php
<?php
  echo $mixed[3][1];
  //outputs: y
?>
```
Put values in an array:
```php
<?php
  $mixed[2] = "cat"; //replaces the value stored at index 2
  $mixed[4] = "mouse"; // adds value to that empty index
  $mixed[] = "horse"; //appends value to the end of the array
?>
```

PHP 5.4 has a short array syntax, allowing you to just use brackets instead of typing `array()`:
```php
<?php
  $array = [1,2,3];
?>
```

__Associative Arrays__
An associative array is an object-indexed collection of objects and it's very similar to what we saw for the definition of a regular array, except it's not ordered. Instead of being integer-indexed it is object-indexed, that is, they're going to be indexed by a label of some sort.

We call the label on each of these pockets the key, and the contents of what's inside the pocket the value. The combination of the label and the value is referred to as the key value pair. We'll always have a series of keys and values that make up our associative array.

Example:
```php
<?php
  $assoc = array("first_name" => "Kevin", "last_name" => "Skoglund");
  echo $assoc["first_name"] . " " . $assoc["last_name"];
  //outputs: Kevin Skoglund

  //assignment
  $assoc["first_name"] = "Larry";
  echo $assoc["first_name"] . " " . $assoc["last_name"];
  //output: Larry Skoglund
?>
```
Keys can be both strings and numbers.

__Array Functions__
<http://php.net/manual/en/ref.array.php>
Examples:
```php
<html>
<body>
  <?php $numbers = array(8,23,15,42,16,4); ?>

  Count:        <?php echo count($numbers); ?><br />
  Max value:    <?php echo max($numbers); ?><br />
  Min Value:    <?php echo min($numbers); ?><br />
  <br />

  <pre>
  Sort:         <?php sort($numbers); print_r($numbers); ?><br />
  Reverse sort: <?php rsort($numbers); print_r($numbers); ?><br />
  </pre>
  <br />

  <!-- Take the values in an array and string them together using a specified separator. Takes two arguments, the symbol to separate each value and the array. -->
  Implode:      <?php echo $num_string = implode(" * ", $numbers); ?><br />
  <!-- Does the opposite of explode(), taking a string and separating it into values that can be placed in an array.
  Explode:      <?php print_r(explode(" * ", $num_string)); ?><br />
  <br />

  15 in array?: <?php echo in_array(15, $numbers); // returns T/F ?><br />
  19 in array?: <?php echo in_array(19, $numbers); // returns T/F ?><br />


</body>
</html>
```

Some array functions are destructive. For example, `the sort()` function. Notice one thing about sort, which is that it actually sorted the array in place. We didn't do any kind of assignment, we didn't have to say numbers equals a sorted version of that. It changed it in place, it's a destructive function. So, our old version, our old, unsorted version, doesn't exist anymore. It sorted them in place.

__Null and Empty__
`NULL` is a fancy term for nothing, for not having a value. It's not zero. It's not an empty string. It's the actual lack of a value. And if we can set a value into a variable, we also have to have some way to talk about the fact that variable might not have a value at all. Null allows us to do that.

So that's what null is, null is just the lack of having a value. That's a pretty easy concept. But I think this is also a good spot for us to talk about a function in PHP called Empty. And as you would expect, empty returns a boolean, true or false, for whether a variable is considered to be empty. What you might not expect though, are the things that it considers to be empty. In PHP, empty is going to be an empty string, null, 0, 0.0 - meaning, a float in which the value is zero - a string with a zero inside of it, false, or an empty array.
`empty: "", null, 0, 0.0, "0", false, array()`

__Type Juggling and Casting__
We've seen a few times when PHP converted a value from one type to another type for us. For example we were able to add a string to an integer and we saw that PHP converted a Boolean true to be the string one when it was output to our webpage. This process is referred to as `Type Juggling` when PHP does it on the fly for us.

We can also explicitly set a type ourselves. For example, converting a string one into the integer one. And when we do it, it's called `Type Casting`. We can type cast in two ways. We can do it using a function `settype($var, "integer")` with two arguments - the item that's being typecast into another, and the type we want to set it to. The other way we can set type is by simply writing the name of the desired type in parentheses before the item being cast `(integer) $var`.

`settype($var)` recasts the variable in place, making a permanent change. `(datatype) $var` only makes the change as it is assigned, which is an impermanent change.

`gettype($var)` returns the datatype of the variable.

__Constants__
A constant is the opposite of a variable, as they do not change or vary. Constants are going to be recognizable on PHP because they're always written in all capital letters and there's no dollar sign in front of them. In addition, the only way to set a constant is to use a function -- the define function -- whereas with variables you can just use an `=` sign.

```php
<?php
//variable
$max_width = 980;

//constant
define("MAX_WIDTH", 980);
echo MAX_WIDTH;
?>
```
Only need to you quotation marks when defining the constant, not to use after. You cannot change or redfine the value of the constant variable. It remains defined for the duration of the PHP script, so once the script is executed it can be redefined when the script is called again.

__Comparison Operators__
Equal: `==`
Identical: `===`

The difference between equal and identical is that there are some things that are considered equal because they're roughly equal. For example, the number `123` is considered equal to the string `"123"`, because if we convert the types, then they are considered equal but they are not considered identical. Identical, they have to be of the same type as well. So, it just goes a little bit further in the check to make sure that they are absolutely 100% the same.

__Array Pointers__
PHP maintains a pointer that points to one of the items in an array. That item is referred to as the current item. By default, that's always the first item in the array. When we start looping through arrays using something like Foreach, PHP moves the pointer down the array as it assigns each value to the loop's variable. Moving the pointer to the next value is how PHP keeps track of which item you're working with now and what the next item is that it should give you after that.

But loops are not the only way to move pointers around. You can use various functions to locate the pointer and manually move it around. This will be helpful when working with databases later, as functions we use to iterate through php arrays like `foreach()` will not be able to be used when working with a database.
```php
<?php
  $myArray = array(1,2,3,4,5);
  //check the current position of the pointer
  echo current($myArray); //output: 1

  //next: move the pointer forward
  //similar to using 'continue' inside a loop
  next($myArray);
  echo current($myArray) //output: 2

  //Move the pointer forward two more times
  next($myArray);
  next($myArray);
  echo current($myArray); //output: 4

  //prev: move the pointer backward
  prev($myArray);
  echo current($myArray); //output: 3

  //reset: move the pointer to the first element
  reset($myArray);
  echo current($myArray); //output: 1

  //end: move the pointer to the last element
  end($myArray);
  echo current($myArray); //output: 5

  //Move the pointer past the last element
  next($myArray);
  echo current($myArray); //output: (null)

 ?>
 ```

 How to use a while loop to move the pointer through the array similar to foreach
 ```php
 <?php
  while($value = current($myArray)) {
    echo $value . ", ";
    next($myArray);
  }
  ?>
  ```
Notice that in the condition of our while loop we're doing an assignment, not a comparison. That is a single equal sign, not a double equals. We're assigning a value from current to ``$value`, and we're also testing then to see if that assignment was successful. If it returned a value, then the expression is going to evaluate to true. But if it returned null, in other words we got to the end of it, then this expression will evaluate to a Boolean false.

Null will be considered false. And so at that point it will exit. So what we're essentially saying is, get the item that the array pointer points to, assign it to `$value`, and if that is an item, if you successfully got one, then execute the loop. If you did not successfully get an item, well then exit the loop. Then we iterate with `next($myArray)`.

__User Defined Functions__
A function is code that performs a specific task, which is then packaged up into a single unit that can then be called upon whenever that task is needed.

Functions follow this basic format:
```php
function name($arg1, $arg2) {
  statement;
}

//call function to execute
name($arg1, $arg2);
```
Function names are very much like the variable names that we assign -- they can have letters, numbers, underscores, and dashes, but cannot have any spaces, and they must start with either a letter or an underscore. Unlike variable names though, function names are case insensitive.

Declaring a function and calling a function do not have to happen sequentially in versions of PHP after version 3, however it is good practice to do so because it's more readable. The page is pre-processed to find all of the functions first.

Once we've defined a function we can't redefine it.

We must always call functions with the same number of arguments and in the same order as specified in the function definition, unless default values are specified. Null is an acceptable replacement for an argument.

When you return a value in a function, it exits the function immediately, similar to how a `break` works. `return` says "let's exit the function and return this value. This is the thing that needs to be passed out of the function. No more processing required.". Even if we put `return` inside loops or switch statements that are in the function, it will immediately exit from all of those as well.

Functions can only return a single value. But what if we need to return multiple values? Since fucntions can only return one entity, we can use an array which stores multiple values as a single entity.

Ex.
```php
<?php
function add_subt($val1, $val2) {
  $add = $val1 + $val2;
  $subt = $val1 - $val2;
  return array($add, $subt);
}

$result_array = add_subt(10,5);
//add
echo $result_array[0]; //output: 15
//subtract
echo $result_array[1]; //output: 5

//You can also use list instead of array
list($add_result, $subt_result) = add_subt(10,5);
echo $add_result; //output: 15
echo $subt_result; //output: 5
?>
```

Using list is a little less clunky than using array. List is super-handy because it allows us to take all those elements that we just packaged up into an array to get out of the function, and immediately break them back down, unpack it, and assign them two variables that have good, common sense names that are easier to identify than result_array[1].

To use a global variable outside of a function into the function, you have to use the keyword `global`. The keyword `global` allows you to bring in a globally scoped variable for use inside a local scope.
