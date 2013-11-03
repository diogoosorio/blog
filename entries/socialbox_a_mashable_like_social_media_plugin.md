----
category: Javascript
create_date: 2011-12-19
description: SocialBox allows you to quickly place a Social Media bar similar to Mashable's. It supports Facebook, Google +1, Twitter and StumbleUpon and can be easily customizable.
title: SocialBox a "Mashable like" Social Media Plugin
keywords: social media plugin, social media widget, social networking plugin, mashable social bar, mashable social media bar, mashable social media plugin
slug: socialbox-a-mashable-like-social-media-plugin
----

To have an easy way for users to quickly share any content of your website on
the various Social Media platforms is absolutelly essential. Furthermore you
have to make sure that the submission process is **simple and accessible** -
the button that enables the "share" must be always at hand.

One of the websites that I keep track of quite often is
[Mashable](http://www.mashable.com/) - if one wants to know how blogging
should be done, they are undoubtedly a reference. Not only that but Mashable
is also an usefull resource for finding out what's happending on the Social
Media realm.

One of the things that captured my attention on Mashable was the use of a neat
**Social Media Box**:

&nbsp_place_holder;

![Mashable Social Media Bar](../../public/images/blog/mashable-social.jpg)

&nbsp_place_holder;

So I decided to create a **social media plugin** that I (and anyone else for
that matter) could use.

&nbsp_place_holder;

## Presenting SocialBox

**SocialBox** is a really simple, easy to install, easy to customize Javascript plugin that you can quickly add to any page.

It currently supports **Facebook Like**, **Google +1**, ******StumbleUpon
Share** and **Twitter**** Share**. Hopefully you can see it working on this
page (to the left).

&nbsp_place_holder;

## Installing SocialBox

Installing **SocialBox** is pretty straightforward. You just need to include
the corresponding javascript file and call the _init_() method. Something like
this should do the trick:

    
    <html>
    <head>
    	<title>SocialBox Demo</title>
    </head>
    <body>
    	<div id="box" style="min-height: 800px;"></div>
    	<script type="text/javascript" src="../path/to/socialbox/socialbox.js"></script>
    	<script type="text/javascript">
    		socialBox.init();								// Initialize SocialBox
    	</script>
    </body>

This quite simply will add the social box to the end of your document and will
share the current page.

## Configuring SocialBox

For a more advanced setup there are a couple of things that you can adjust,
namelly the plugin's presentation and the element to which it should be
appended. Here's a more complete example:

&nbsp_place_holder;

    
    <html>
    <head>
    	<title>SocialBox Demo</title>
    </head>
    <body>
    	<div id="box" style="min-height: 800px;"></div>
    	<script type="text/javascript" src="../path/to/socialbox/socialbox.js"></script>
    	<script type="text/javascript">
    		socialBox.disableFacebook();					// Disables Facebook Like
    		//socialBox.disableTwitter();					// Disables Twitter
    		//socialBox.disableStumbleUpon();				// Disables StumbleUpon
    		//socialBox.disableGooglePlus();				// Disables G+
    		socialBox.setUrl('http://www.google.com/');		// Sets the URL to be shared
    		socialBox.setStyle('background', 'red');		// Override a CSS rule
    		
    		socialBox.setStyle({							// You may also override CSS rules
    			padding: '10px 15px 10px 15px',				// passing an object as argument to 
    			border: 'none'								// this method
    		});
    		
    		socialBox.setParent('box');						// Set the element to which the social box
    														// will be appended
    
    		socialBox.init();								// Initialize SocialBox
    	</script>
    </body>

Still pretty accessible. There are a couple of features that I want to add,
but for now this will suffice. As I mentioned before the code is released
under no license at all, so do whatever you like with it. If you can post a
backlink here, I'd appreciate it.

&nbsp_place_holder;

## Download SocialBox

You may download the plugin here:

  * [http://www.diogoosorio.com/public/downloads/socialbox/socialbox.js ~ 6.5KB](http://www.diogoosorio.com/public/downloads/socialbox/socialbox.js)

