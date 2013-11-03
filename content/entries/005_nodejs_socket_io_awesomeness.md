----
category: Javascript
create_date: 2012-01-02
description: I've been introduced to the power of WebSockets, the Socket.IO library and Node.js. So I decided to create a small prototype to test it, here's what I did (full source-code included).
title: Introducing Socket.IO and Node.js - how to write a small app.
excerpt: <p>From time to time you find a website that introduces something truly different from everything you've seen. It happened to me a couple of months ago here - http://economico.sapo.pt/. It took me a while understanding what was happening behind the scenes: no AJAX requests were being made, how the heck were they updating the information on the website (and how did they do it so quickly). Then I found that the HTML5 standard had a neat feature called WebSockets - combine the feature with Node.js and you have a great foundation for developing awesome Web Apps.</p>   <p>I had to try it, so I developed a tiny prototype. Come check it out (full source code included).</p>
keywords: websockets, socket.io, node.js, socket.io tutorial, node.js tutorial, server side javascript
slug: nodejs-socket-io-awesomeness
----

From time to time you find a technology that introduces something trully new,
something that amazes you. When you do find something that fits the
description, the first thing you obviously need to do is to find how the heck
is that being done. The second thing is to develop a small prototype to
introduce yourself to this new, awesome technology.

What I've described above happened to me a couple of months ago. I was
browsing a Portuguese news website -
[http://economico.sapo.pt](http://economico.sapo.pt/) - and saw that they were
using a so called "Real Time" technology developed by yet another Portuguese
company [IBT](http://www.ibt.co/) (yeah I know, despite what you might be
seeing on the news, we the Portuguese people rock).

&nbsp_place_holder;

## How the heck are they doing that?

So the first question arises. They are updating a bunch of stats on the
website without making any AJAX requests - what kind of sourcery is this?

Being a proprietary solution, the Javascript code on the website was obviously
obfuscated (and I'm not one of those guys that's into cracking what clearly is
to be kept "secret") so no luck there. Step 2, Google it - and so I did.

HTML5 introduces a series of new features, one of them being
[WebSockets](http://dev.w3.org/html5/websockets/). After giving the
specification a quick read, lets check what browsers support the technology -
FF, Chrome, Opera and Safari support it natively (IE once again doesn't keep
up).

I've been reading about Node.js for a while, but I didn't really had the
opportunity to give it a try. I instantly remembered that it would be a
perfect match to this project and someone probably had already written a cool
library to release me from all of the standard overhead and cross-browser
compability issues.

A bit more on Google and I found this absolutelly awesome library called
[Socket.IO](http://socket.io/). I'm set, lets do this.

&nbsp_place_holder;

## Lets build a prototype!

So a couple of months ago I had a chat with a fellow colleague Web Designer -
[Bruno Afonso](http://www.facebook.com/kinesthai) - he had an idea for one
project that we may be working together at: basically he wanted to graphically
show in a real time manner who would be online at any given time on the
website (using an Avatar for each person or something like that).

So what I wante to do here is to demonstrate (to myself mostly) that it would
be possible to pass along information betweent the server and the clients in
real time. Should one user log in to the website, all the others should be
updated and receive some information about the guy (namelly the avatar).

Cool, but I didn't want to put up a login system and what not. To be able to
transfer information to all the clients when someone opened up the website
would suffice for now.

To present the info on a graphical manner, I decided to ask for permission to
track the user location (using yet another HTML5 feature - [Geo
Location](http://dev.w3.org/geo/api/spec-source.html). Then pin down the users
on a map as they landed on the page.

&nbsp_place_holder;

## Server side

As I mentioned before, Node.js + Socket.IO were used, here's the code:

    
    (function(out){
    
    	var PORT = 9090;
    	var clients = [];
    	var io;
    	var factory = require('./rtcclient');
    	var sendCount = false;
    	var sendLog = false;
    	
    	
    	// -------------- Utilities Class -------------- //
    	var utils = {
    		
    		// Check if value is an integer
    		//
    		// @param mixed val		The value to be inspected
    		// @return boolean
    		isInt: function(val) {
    			return parseFloat(val) == parseInt(val) && !isNaN(val) ? true : false; 
    		},
    		
    		// Returns the current time in an Human readable format
    		//
    		// @return string		The current time in a YYYY-mm-dd H:i:s format
    		getPresentTime: function(){
    			var today = new Date();
    			var dd = today.getDate();
    			var mm = today.getMonth() + 1;	// Wtf? January is 0?
    			var H = today.getHours();
    			var i = today.getMinutes();
    			var s = today.getSeconds();
    			
    			var yyyy = today.getFullYear();
    			if(dd < 10) dd = '0' + dd;
    			if(mm < 10) mm = '0' + mm;
    			if(H < 10) H = '0' + H;
    			if(i < 10) i = '0' + i;
    			if(s < 10) s = '0' + s;
    			
    			today = yyyy + '-' + mm + '-' + dd + ' ' + H + ':' + i + ':' + s;
    			
    			return today;
    		}
    	};
    	// ------------- Utilities Class -------------- //
    		
    	
    	// Initializes event bindings of the server
    	var initBindings = function(){
    		
    		// Connect and disconnect bindings
    		io.sockets.on('connection', function(socket){ 
    			var client = newConnection(socket);
    			
    			// On disconnect remove the user from the user list
    			socket.on('disconnect', function(){ killConnection(client); });
    			
    			// User provided some info about him
    			socket.on('myDetails', function(data){ client.setDetails(data); updateClients(client); });
    		});
    	};
    	
    	
    	// Resyncs information about a client with all the other
    	// clients.
    	//
    	// @param RTCClient client	The client who changed his information
    	var updateClients = function (client){
    	
    		// Am I suppose to log it to the user?
    		if( sendLog ) io.sockets.emit('logMessage', { type: "connect", client: client.getDetails(), time: utils.getPresentTime() });
    	
    	};
    	
    	
    	// Removes a client from the currently connected clients
    	//
    	// @param RTCClient client		The client that is getting removed
    	var killConnection = function (client){
    	
    		// Remove the client from the list
    		clients.splice(client.id, 1);
    		
    		// Am I suppose to send the user count to the clients?
    		if( sendCount ) io.sockets.emit('userCount', { count: clients.length });
    		
    		// Am I suppose to log it to the user?
    		if( sendLog ) io.sockets.emit('logMessage', { type: "disconnect", client: client.getDetails(), time: utils.getPresentTime() });
    	};
    	
    	
    	// Handles the connection of a new socket
    	//
    	// @param object mySocket		An instance of socket.io Socket object
    	var newConnection = function (mySocket) {
    
    		// Register new client
    		var client = factory.create(mySocket);
    		client.id = clients.length;
    		clients.push(client);
    		
    		// Am I suppose to send the user count to the clients?
    		if( sendCount ) io.sockets.emit('userCount', { count: clients.length });
    		
    		return client;
    	};	
    	
    	
    	// Start the server
    	//
    	// @param int port		The port to which the server will listen to
    	var start = function(port){
    		
    		// Set new port if defined
    		if( utils.isInt(port) ) PORT = port;
    		
    		// Initialize the server
    		io = require('socket.io').listen(PORT);
    		
    		// Initialize bindings
    		initBindings();
    	};
    	
    	
    	// Instructs the server to send the user count number
    	// to the client.
    	var sendUserCount = function(){
    		sendCount = true;
    	};
    	
    	
    	// Instructs the server to send the log messages to 
    	// the clients
    	var sendLogMessages = function(){
    		sendLog = true;
    	};
    	
    	out.start = start;
    	out.sendUserCount = sendUserCount;
    	out.sendLogMessages = sendLogMessages;
    })(exports);

The code is pretty much self explanatory. Basically I listen to 3 events -
connect, disconnect and a request to update a client information.

I created a small auxiliary class to represent a client on the server side
(although I didn't, I probably could just serialize these objects and pass
them around through the socket connection - I'll check that latter):

    
    (function(out){
    	
    	var RTCClient = function(newSocket) {
    		this.socket = newSocket;
    		this.isAdmin = false;
    		this.params = {};
    		
    		
    		// Set the user details. If the object passed as argument
    		// contains a key that's valid, set the property.
    		//
    		// @param object params		A key:val object containing the client information
    		this.setDetails = function(params){
    			var index;
    					
    			// Iterate throught the given parameters and store
    			// as property the ones that are valid
    			for(index in params){
    				this.params[index] = params[index];
    			};
    		};
    		
    		
    		// Returns a JSON string with the set user information
    		//
    		// @return string		A JSON string containing the user information
    		this.getDetails = function(){
    			return JSON.stringify(this.params);
    		};
    	};
    	
    	
    	// Public method that creates a new RTCClient
    	var create = function(newSocket){
    		return new RTCClient(newSocket);
    	};
    	
    	out.create = create;
    })(exports);

On the client side I created a small library to work with the server:

    
    var libRTC = function(){
    
    	var address = '127.0.0.1';
    	var port = '9090';
    	var properties;
    	var loaded = false;
    	var connected = false;
    	var socket;
    	var info;
    	var initialCallback;
    	var appendToMap = false;
    	var gMap = null;
    	var mapDiv;
    	var markers = [];
    
    
    	// Loads the socket IO library
    	//
    	// @param function callback		The callback function
    	var loadSocketIO = function(callback){
    	
    		// Prepare things
    		var source = 'http://' + address + ':' + port + '/socket.io/socket.io.js';
    		var script = document.createElement('script');
    		script.type = 'text/javascript';
    	
    		// Add listener to the library load
    		if( script.readyState ) {	// IE
    			script.onreadystatechange = function(){
    				if( script.readyState === "complete" || script.readyState === "loaded" ){
    					script.onreadystatechange = null;
    				
    					// Warn the object that the library was loaded
    					loaded = true;
    				
    					// Do callback
    					callback();
    				};
    			};
    		} else {					// Others
    			script.onload = function(){
    				loaded = true;
    				callback();
    			};
    		};
    	
    	
    		// Append it to the document
    		script.src = source;
    		document.body.appendChild(script);
    	};
    
    
    	// Returns a basic information about the client. Tries to get
    	// the user location via its browser.
    	//
    	// @return object		An object containing information about the client
    	var getClientInformation = function(){
    		var myInfo = {}; 
    	
    		// Set useragent information
    		myInfo.userAgent = navigator.userAgent;
    	
    		// Try to get the user location
    		if( navigator.geolocation) {
    			navigator.geolocation.getCurrentPosition(function(position){
    			
    				// Resend this stuff as the user will probably have to allow the app to get the position
    				socket.emit("myDetails", {location: [position.coords.latitude, position.coords.longitude]});
    			});
    		};
    	
    		return myInfo;
    	};
    
    
    	// Connects to the server
    	var connect = function(callback){			
    	
    		var callback = typeof callback === "undefined" ? initialCallback : callback;
    	
    		// If the socket.io library wasn't loaded, load it
    		if(!loaded){
    			initialCallback = callback;
    			loadSocketIO(connect);
    			return;
    		}
    	
    		// Double check if I have access to the io object
    		if( typeof io === 'undefined' ){
    			console.error("Couldn't reach the socket io library. Is the server up?");
    			return;
    		}
    	
    		// Connect
    		var connectStr = 'http://' + address + ':' + port;
    	
    		try{
    			socket = io.connect(connectStr);
    			connected = true;
    		} catch(e){ 
    			console.error("Couldn't connect to the server.");
    			return;
    		}
    	
    		// Provide my information to the server
    		info = getClientInformation();
    		socket.emit("myDetails", info);
    	
    		// Trigger the callback
    		if( typeof callback === 'function' ) callback();
    	};
    
    
    	// Adds text to a given element on the DOM
    	//
    	// @param string elementID		The element ID name
    	// @param string html			The information to append to the element
    	var addToElement = function(elementID, html){
    		var el = document.getElementById(elementID);
    		el.innerHTML = html;
    	};
    
    
    	// Appends text to a given element on the DOM
    	//
    	// @param string elementID		The element ID name
    	// @param string html			The text to be appended
    	// @param boolean preppend		Should it be preppended?
    	var appendToElement = function(elementID, html, preppend){
    		var el = document.getElementById(elementID);
    	
    		if(typeof preppend !== 'undefined' && preppend){
    			var children = el.children;
    			var num = children.length - 1;
    			console.log(num);
    			(num >= 0) ? el.insertBefore(html, children[num]) : el.appendChild(html);
    		} else {
    			el.appendChild(html);
    		}
    	};
    	
    	
    	// Appends the user to the map
    	//
    	// @param object info		An object containing the a "location" key
    	var pinPointUser = function(info){
    		
    		// Create map from Google' API
    		if(gMap === null){
    			gMap = new GMap2(document.getElementById(mapDiv));
    		};
    		
    		// Create marker
    		var point = new GLatLng(info.location[0], info.location[1]);
    		var marker = new GMarker(point);
    		gMap.addOverlay(marker);
    		markers.push(marker);
    	};
    
    
    	return {
    	
    		// Connects to the server
    		//
    		// @param function callback
    		init: function(callback){
    			connect(callback);
    		},
    	
    	
    		// Sets the server address
    		//
    		// @param String newAddress		The server address
    		setAddress: function(newAddress){
    			address = newAddress;
    		},
    	
    	
    		// Listen on the total number of connected clients
    		// count.
    		//
    		// @param String elementID		If provided, the method will append the count to the DOM.
    		// @return String 				The user number count
    		listenUserCount: function(elementID){
    			socket.on("userCount", function(data){
    				addToElement(elementID, data.count);
    			});
    		},
    	
    	
    		// Listen to log messages sent by the server.
    		//
    		// @param string elementID		The elementID to which the messages will be appended to
    		listenLogMessages: function(elementID){				
    			socket.on("logMessage", function(data){
    				var p = document.createElement('p');
    				var strBuilder = '<strong>(' + data.time + ')</strong> - ';
    				var info = JSON.parse(data.client);
    			
    				switch(data.type){
    					case 'connect':
    						strBuilder += 'New client connected or changed information: ';
    						break;
    					
    					case 'disconnect':
    						strBuilder += 'A client as disconnected: ';
    						break;
    				};
    			
    				strBuilder += info.userAgent;
    				p.innerHTML = strBuilder;
    				appendToElement(elementID, p, true);
    				
    				// Show user on map?
    				if(appendToMap && typeof info.location !== 'undefined') pinPointUser(info);
    			});
    		},
    	
    		// Sets the server listening port
    		//
    		// @param String newPort			The server port
    		setPort: function(newPort){
    			port = newPort;
    		},
    		
    		// Defines if the geo information should be appended to 
    		// GoogleMaps
    		appendToMap: function(elementID){
    			appendToMap = true;
    			mapDiv = elementID;
    		},	
    	
    		// Set a client property.
    		// 
    		// If both arguments are strings, the method will append
    		// the the information directly to the info property. 
    		// 
    		// If the first argument is an object, the method will merge
    		// it with the info property.
    		//
    		// @param mixed key			The property name or an object
    		// @param String val		The property value
    		setClientInformation: function(key, val){
    			if( typeof key === 'string' && typeof val === 'string' ){
    				info[key] = val;
    			} else if (typeof key === 'object') {
    				var x;
    				for(x in key){
    					info[x] = key[x];
    				}
    			}
    		}
    	};
    }();

It basically handles the connect information and upon receival of a client
update request, pin points him on a Google Maps.

&nbsp_place_holder;

## The final result

I had a lot of fun writting this. I even disregarded my girlfriend for an
entire weekend in order to do this (sorry Sandra). You can check the final
result here: [http://diogoosorio.com/play/socket.io/](../../play/socket.io/).

If you have any suggestion for improving the code (or found something I did
wrong), leave a comment - I'm aware that I'm not a Javascript guru of any
kind. If you liked the end result, please leave a
**Like**/**G+********/****Retweet**. :)

Oh and you can download the entire thing here:&nbsp_place_holder;[http://diogo
osorio.com/public/downloads/rtcserver/rtcserver.zip](../../public/downloads/rt
cserver/rtcserver.zip)

