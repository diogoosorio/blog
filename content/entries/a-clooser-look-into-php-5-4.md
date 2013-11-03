----
category: PHP
create_date: 2012-03-11
description: PHP 5.4 version introduces a number of new feature and a couple of long needed corrections to the language. The use of Traits, a built-in web server, some array syntactic sugar are some of the new features.
title: A clooser look into PHP 5.4
keywords: php 5.4, php latest version, php 5.4 features, php 5.4 new features
slug: a-clooser-look-into-php-5-4
----

While **PHP6** still lies ahead in a far distant future, **PHP** **5.4** just
got released and it brings a cool set of new features to "play with". The
major ones are definetly the inclusion of Traits on the language and the
built-in web server - but they are no the only ones. Check out the new
features.

### Traits

What are Traits you may ask? A Trait is a simple mechanism that tries to
overcome the fact that PHP is a single inheritance language - you can only
"extend" one parent class. While a Trait cannot be instantiated, you can
include an undefinite number of Traits on any class and use the methods
defined within the traits freely.

Here's a quick example:

    
    <?php
    trait Hello {
        public function sayHello() {
            echo 'Hello ';
        }
    }
    
    trait World {
        public function sayWorld() {
            echo 'World';
        }
    }
    
    class MyHelloWorld {
        use Hello, World;
        public function sayExclamationMark() {
            echo '!';
        }
    }
    
    $o = new MyHelloWorld();
    $o->sayHello();
    $o->sayWorld();
    $o->sayExclamationMark();

### Built-in Web Server

Tired of creating a vhost each time you want to start a new project? Well
that's not longer needed, PHP 5.4 includes a new built-in web server that can
be started/stoped freely and without much hassle:

    
    php -S localhost:8080 -t /home/diogo/project1/

Will be enough to get your server up and running. Check out the [docs
page](http://php.net/manual/en/features.commandline.webserver.php) for more
information.

### New Array Syntatic Sugar

While one of the simplest new features this is definitly one of my favourites.
Remember how you had to use "temporary" variables whenever you wanted to work
with arrays?

    
    <?php
    $name 	= explode(' ', 'Diogo Osorio');
    $fname	= $name[0];

Never again! This was one of those things I trully envied Java for - in PHP
5.4 the code bellow is also valid:

    
    <?php
    $fname = explode(' ', 'Diogo Osorio')[0];
    $lname = dummy[1];
    
    function dummy(){
    	return array('Diogo', 'Osorio');
    }

A new way of initializing arrays was also introduced:

    
    <?php
    $names 	= ['Diogo', 'Osorio'];
    $scores	= [
    			'Diogo'	=> 100,
    			'Osorio'	=> 200
    		  ];

### <?= Enabled by Default

Not much to add here. The shorthand for the echo function is now enabled "out
of the box".

### Binary Number Representation

You can now represent binary numbers in PHP:

    
    <?php
    $hex			= 0x20;		// Hexadecimal number
    
    $ten			= 0b1010;	// Binary number
    $seven		= 0b111;
    $five			= 0b101;

### Callable TypeHint

While PHP is a loosly typed language, typehints were introduced to enable a
more "strongly typed" programming style. Until now only Objects and Arrays
could be typehints. With PHP 5.4 [callable](https://wiki.php.net/rfc/callable)
is introduced as a valida typehint, therefore the code bellow will be valid:

    
    <?php
    function my_name(){
    	return 'Diogo Osorio';
    }
    
    function my_function(callable $x){
    	return $x();
    }
    
    echo my_function('my_name');
    echo my_function(function(){ return 'Diogo Osorio'; });

### High Precision Timer

_$_SERVER['REQUEST_TIME_FLOAT'] _was introduced and it will containt the
timestamp with microsecond precision of the time that the request was started
(usefull for benchmarking and whatnot).

### UTF-8 as Default Charset

This was a no brainer. ISO-8859-1 was dropped as the default charset and UTF-8
took its place. This means that the "mandatory" meta tag to inform the browser
of the page encoding is no longer necessary.

### $this in Anonymous Functions

The _$this_ scope was altered in PHP 5.4. Now the code bellow is valid:

    
    class Foo
    {
        function hello() {
            echo 'Hello World!';
        }
     
        function anonymous()
        {
            return function() {
                $this->hello();
            };
        }
    }
     
    class Bar
    {
        function __construct(Foo $o)
        {
            $x = $o->anonymous();
            $x();
        }
    }
    new Bar(new Foo);

### That's it

Well that pretty much sums up what PHP 5.4 brings to the table. While PHP 6
doesn't arrive (Unicode support!!!) and without being an huge leap on the
languages' progress, PHP 5.4 introduces some new, valid and usefull features.
Code on and have fun with them!

