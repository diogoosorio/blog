----
category: PHP
create_date: 2012-02-29
description: If you need to send SMS messages using PHP and CodeIgniter, look no further. I've developed a small library to communicate with Clickatel's API and made it publicly available.
title: Send SMS Messages Using PHP and CodeIgniter
excerpt: I had to develop a small library to interact with the Clickatel API. A couple of friends of mine immediately asked me to share the library with them and although the library itself doesn't do a lot, I thought it could be of used to anyone who wants to be able to quickly send an SMS message using CodeIgniter. I decided to make it publicly available, so if you need for your Web Application to send SMS messages, feel free to use it.
keywords: send sms php, send sms codeigniter, clickatel api codeigniter, clickatel api php, send sms clickatel
slug: send-sms-using-php-codeigniter-with-clickatel
----

A couple of days ago I had the necessity to develop a small library to
interact with Clickatel's API. The only feature that I required at the time
was to be able to send messages through the HTTP API and so I've written a
small, very simple CodeIgniter library to preform the task.

Yesterday a couple of friends asked me to share the library with them - I'm
guessing that it's a tough work going through the tiny manual provided by
Clickatel. Nevertheless I thought that maybe the class could be of use to more
people facing the same issue.

A note of advice - I did not test the library against a PHP4 server, so if you
are running a legacy system, please do your homework before using the class.

In order for the library to work you first need to register on
[Clickatell](http://www.clickatell.com/). I've registered as a developer and
although I'm not entirelly sure, I think that you need to register as a
developer in order to be granted access to the API. Upon registration you
should have an&nbsp_place_holder;**username**,&nbsp_place_holder;**password**
and&nbsp_place_holder;an **API ID** - and that's all you need.

At this point I'd also like to note that I highly recommend that you enable
the PHP cUrl extension before using the library. I communicate with
Clickatell's API via HTTP and cUrl does a great job in these kind of
situations. If you don't have cUrl enabled, the library should still work but
I haven't tested it thorougly enough to be sure that it will run flawlessly.

To use the library is quite simple. First you need to pass the username,
password and api id to the class. You can do so, inserting the parameters
directly on a configuration file and order CI to load it automatically or pass
the parameters as an argument to the constructor.

If you choose to use a configuration file, create a new file
under&nbsp_place_holder;_application/config/**clickatel.php**_. Here's my
template:

    
    <?php if(!defined('BASEPATH')) die('No direct access allowed!');
    /*
    |--------------------------------------------------------------------------
    | Clickatel API Information
    |--------------------------------------------------------------------------
    |
    | This file contains the configuration parameters that are used by the 
    | Clickate library. Please create an account on Clickatel and use the provided
    | information here.
    |
    | http://www.clickatel.com
    |
    | User 			=> Your account username.
    | Password		=> Your account password.
    | API ID		=> Upon registration, Clickatel will provide you an API key.
    |
    */
    $config['clickatel'] = array(
    							'user'		=> 'myuser',
    							'password'	=> 'mypassword',
    							'api_id'	=> 'myapiid'
    						);

Alternatively you can pass the parameters directly to the class constructors.
If you do whatever you may have set on the config file, will be overwritten:

    
    <?php
    class Demo extends CI_Controller{
    	
    	public function index(){
    		
    		// This will override any configuration parameters set on the config file
    		$params = array('user' => 'myuser', 'password' => 'password', 'api_id' => 'myid');	
    		$this->load->library('clickatel', $params);
    		
    		// Send the message
    		$this->clickatel->send_sms('3519333333', 'This is a test message');
    		
    		// Get the reply
    		echo $this->clickatel->last_reply();
    		
    		// Send message to multiple numbers
    		$numbers = array('351965555555', '351936666666', '351925555555');
    		$this->clickatel->send_sms($numbers, 'This is a test message');
    	}
    }

If you face any problem, get in touch and I'll try to help. You can download
the library from my&nbsp_place_holder;[**Git
Repository**](https://github.com/diogoosorio/diogo-ci-libraries). Have fun!

