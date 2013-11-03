----
category: PHP
create_date: 2012-02-16
description: The singleton design pattern aims to guarantee an exclusive access to a given resource throughout your application. Understand how to apply the singleton design pattern and what's its use.
title: Understanding the Singleton Design Pattern with PHP
excerpt: The singleton pattern is a very widespread design pattern. It aims to guarantee an exclusive access to a given resource throughout your application - in other words it makes sure that you are only able to instantiate a certain class one and one time only. I'll apply the concept to a class that establishes a connection to a database.
keywords: singleton pattern, singleton php, understand singleton pattern, implementing the singleton design pattern with php
slug: understanding-the-singleton-design-pattern-with-php
----

The singleton pattern is a very common design pattern. In this article, I'll
implement it using PHP, but the implementation shown here is also valid to
pretty much any programming language.

The purpose of the singleton pattern is to guarantee that one and only one
instance of a certain class is instantiated throughout your application. It's
typically used when you want to guarantee that that particular resource is
exclusive.

The typical example are database connections. To establish a connection with
the database is a resource consuming task - therefore should only be done once
and that same connection should be used throughout your application. To create
a singleton class that handles the connection to the database is a great way
to achieve this goal.

Lets follow up with some code:

    
    <?php
    
    class DbConnection
    {
    	private $_conn = null;
    	
    	private function __construct()
    	{
    		$dsn 	= 'mysql:host=localhost;dbname=root';
    		$user	= 'root';
    		$pass	= '';
    		
    		$this->_conn = new PDO($dsn, $user, $pass);
    	}
    	
    	
    	public function getConnection(){
    		return $this->_conn;
    	}
    }

Notice how the constructor's visibility is set to **private**. If you try to
directly instantiate an object of the class, you'll get something like this:

    
    Fatal error: Call to private DbConnection::__construct() from invalid context in /home/diogo/www/db.php on line 22 Call Stack: 0.0005 646256 1. {main}() /home/diogo/www/db.php:0

That's exactly what you want - to forbide for someone to directly instantiate
the class, which would ultimatelly lead to multiple connections established to
the database (one per instance). Lets develop the class a bit more:

    
    <?php
    
    class DbConnection
    {
    	private $_conn = null;
    	private static $_instance = null;
    	
    	private function __construct()
    	{
    		$dsn 	= 'mysql:host=localhost;dbname=hdd';
    		$user	= 'root';
    		$pass	= '';
    		
    		$this->_conn = new PDO($dsn, $user, $pass);
    	}
    	
    	
    	public function getConnection(){
    		return $this->_conn;
    	}
    	
    	
    	public static function getInstance(){
    		if(!isset(self::$_instance)){
    			self::$_instance = new DbConnection();
    		}
    		
    		return self::$_instance;
    	}
    }
    
    $db1 = DbConnection::getInstance();
    $db2 = DbConnection::getInstance();
    
    if($db1 === $db2){
    	echo "DB1 and DB2 reference the same instance. \n";
    }
    
    if($db1->getConnection() === $db2->getConnection()){
    	echo "DB1->_conn and DB2->_conn reference the same instance. \n";
    }

The idea here is instead instantiating the class directly at any given point
in your code, you'd call the **DbConnection::getInstance()** method instead.
This method would evaluate the static property that should hold the only
instance of the class - if the instance is already set, it simply returns the
object stored as a property.

During the next week I'll try to follow this post with a couple more of design
patterns commonly used in any program. If you have any question, just leave a
comment, I'll try to reply as soon as I can. :)

