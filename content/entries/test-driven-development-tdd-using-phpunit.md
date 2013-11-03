----
category: PHP
create_date: 2012-01-24
description: Test Driven Development (TDD) is a programming process in which you write tests, before touching any actual code. In this post I'll tell you a bit about Unit Testing using PHPUnit.
title: Test Driven Development (TDD) using PHPUnit
keywords: phpunit, php tdd, test driven development php, tdd phpunit, test driven development phpunit
slug: test-driven-development-tdd-using-phpunit
----

It has happened way too many times. You develop your application, everything
seems to be working smoothly - all the features that you wanted are in place
and all the application's logic seems to be working perfectly. Yes, you've
developed a great piece of code and you're ready to deploy it to your
production server.

Happy as a monkey, you deploy the application to the production environment.
You start to get some visits to your web application and everything looks
great. You're an happy developer!

A couple of weeks pass and you receive a call from your client. After
deciphering your client's yells, you understand that seems to be a problem
with the application. Wrong information is being shown, the application's
logic isn't working. After those 30 horrific minutes over the phone, you open
up your browser to check what the fuss is all about - the problem certainly
must certainly be sitting between the computer and the chair, as you witnessed
the application running flawlessly while it was sitting on your development
environment.

A couple of minutes are enough for you to reach a conclusion, the unthinkable
has happened and its your fault! Your code is not behaving as it should and by
now, not only should you be antecipating a long night without sleep, but you
should also be contemplating to put up a lot of hours on the project that you
wasn't expecting - just to solve the mess...

### Enters TDD - Test Driven Development

Well if the situation I've posted above rings any bell, well you'll be as
happy as I did when I read about **Test Driven Development**. So what exactly
is TDD?

TDD is a development process in which you write snippets of code whose purpose
is to test all the situations that your actual code might be subjected to
(well, not ALL of the situations, usually you use extreme situations), when
it's deployed to production.

In simpler terms, you give some input to your code\give it an order and then
you test the outcome it provides (comparing it to what the result should be).

![TDD Flow](/static/images/blog/tdd_flow.gif)

In TDD you actually write the tests before you write the code itself. So when
you start writing your actual code you should already have a set of tests, all
of which should be failing.

After the code is developed, you run the tests yet again (hopefully some of
them should pass this time) and you simply work through the code that is not
passing the tests, until you get it right.

### Why use TDD?

Well, the main reasons I'd point out would be:

  1. It makes you think about what you're about to write, before you write it. In order to write the tests you need to know what methods\functions you're going to need, what will those methods receive as an input and what they should reeturn.  
  
Usually the final outcome is better, more expressive and well structured code.

  
  

  2. It tests your code (DUH!). You should test your code for [edge cases](http://en.wikipedia.org/wiki/Edge_case), invalid inputs and general cases - that means that you should not only write tests that handle what you'd consider "normal" situations, but also extreme situations and even situations where the input given to your method\function are purelly invalid (ex. passing a String to a method that expects an Int as argument).  
  
  

  3. It can turn you into a more productive person. Yeah, that's right [studies](http://theruntime.com/blogs/jacob/archive/2008/01/22/tdd-proven-effective-or-is-it.aspx) show that by using TDD you end up, not only creating better software, but also (or may I say, consequently?) are more productive.  
  
  

  4. It can be fun! I usually try to write the tests for a method or function and then write the code itself. When it the test turns green, I move on to writing tests for the next method\function, ...  
  
When I get into this cycle, programming becomes like a game. I first try to
"break" the code I haven't even written yet and then I neatly try to get
things working. :)

### Meet PHPUnit

[PHPUnit is a framework](http://www.phpunit.de/manual/current/en/) whose
purpose is exactly allow you to write tests in which you assert that every
output is what it should be. It also includes an way for you to run the tests
- while I suppose it would be fun to write my own Unit Testing framework,
PHPUnit provides pretty much everything you need and it's a stable, rock-
solid, piece of sofware (so why reivent the wheel?).

### TDD Demonstration (Sample Code)

Lets get to the fun part and get our hands dirty with some code. In this
example, lets assume that we want to write a simple authentication class that
contains two methods - **login(****) **and **isLogged()**.

The first method (**login****()**) should accept two arguments - an _username_
and a _password_. It should also throw an exception if the arguments passed
happen to be the wrong data type.

The second method (**isLogged()**) should return TRUE if the user has logged
in successfully previously and FALSE if not.

So here's a sample test:

    
    <?php
    require_once('authentication.php');
    
    class AuthenticationTest extends PHPUnit_Framework_TestCase
    {
    	/**
    	 * Tests the isLogged method
    	 */
    	public function testIsLogged(){
    		$auth = new Authentication();
    		
    		// The method should return FALSE, as we haven't logged in yet
    		$this->assertFalse($auth->isLogged());
    		
    		// Lets login with some invalid credentials, the method should return
    		// FALSE
    		$auth->login('abc', '123');
    		$this->assertFalse($auth->isLogged());
    		
    		// Lets login with valid credentials. True is expected after this
    		$auth->login('user', 'password');
    		$this->assertTrue($auth->isLogged());
    	}
    	
    	
    	/**
    	 * Tests the login method
    	 *
    	 * @expectedException InvalidArgumentException
    	 */
    	public function testLogin(){
    		$auth = new Authentication();
    		
    		// As we've tested the actual login system on the test above,
    		// lets just try to pass invalid arguments to the method
    		$auth->login(123, 'abc');
    	}
    }

And the initial class:

    
    <?php
    class Authentication
    {
    	/**
    	 * Checks if the user is logged in
    	 * 
    	 * @return boolean
    	 */
    	public function isLogged(){
    	
    	}
    	
    	/**
    	 * Logs the user in.
    	 *
    	 * @param String $user		The username
    	 * @param String $pass		The password
    	 * @throws InvalidArgumentException
    	*/
    	public function login($user, $pass){
    	
    	}
    }

If we run the test now, it should return nothing but failures. Just enter
_phpunit authenticationtestt.php_. Here's the output:

    
    PHPUnit 3.6.5 by Sebastian Bergmann.
    
    FF
    
    Time: 0 seconds, Memory: 4.25Mb
    
    There were 2 failures:
    
    1) AuthenticationTest::testIsLogged
    Failed asserting that null is false.
    
    /home/diogo/www/temp/test.php:13
    
    2) AuthenticationTest::testLogin
    Expected exception InvalidArgumentException
    
    
    FAILURES!
    Tests: 2, Assertions: 2, Failures: 2.

So we now have the tests written and a class that fails every test. So, lets
complete the class in order for it to be able to pass the tests:

    
    <?php
    class Authentication
    {
    	private $correctPassword = 'password';
    	private $correctUsername = 'user';
    	private $isLogged = FALSE;
    
    	/**
    	 * Checks if the user is logged in
    	 * 
    	 * @return boolean
    	 */
    	public function isLogged(){
    		return $this->isLogged;
    	}
    	
    	/**
    	 * Logs the user in.
    	 *
    	 * @param String $user		The username
    	 * @param String $pass		The password
    	 * @throws InvalidArgumentException
    	*/
    	public function login($user, $pass){
    		
    		// Test if the arguments are valid
    		if(!is_string($user) || !is_string($pass)){
    			throw new InvalidArgumentException("Login method expects two strings as argument.");
    		}
    		
    		// Test if the authentication information is correct
    		if(!strcmp($user, $this->correctUsername) && !strcmp($pass, $this->correctPassword)){
    			$this->isLogged = TRUE;
    		}
    		
    	}
    }

After running the cases yet again, you'll see that this time every test gets
passed:

    
    PHPUnit 3.6.5 by Sebastian Bergmann.
    
    ..
    
    Time: 0 seconds, Memory: 4.25Mb
    
    OK (2 tests, 4 assertions)

I hope that this small example is sufficient for anyone to understand how TDD
works. If you have any problem or want to make any comment, feel free to do
so. :)

