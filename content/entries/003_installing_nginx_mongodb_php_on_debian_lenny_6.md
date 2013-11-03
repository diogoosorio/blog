----
category: Linux
create_date: 2011-12-19
description: In this entry I'll install and configure a LNMP (Linux + Nginx + MongoDB + PHP) stack on Debian Lenny.
title: Installing Nginx + MongoDB + PHP FPM on Debian Lenny (6.0)
excerpt: For anyone interested in developing for the web it's critical to be able to configure a machine to serve as a development environment for any project. On this entry I'll install a machine running Debian "Squeeze" (6.0) with a LNMP stack (LNMP meaning - Linux + Nginx + MongoDB + PHP). Although the configuration would need to be (heavily) tweaked on for a production environment, this will show how to quickly get things running.
keywords: install lnmp, install nginx debian, install mongo debian, install mongodb debian
slug: installing-nginx-mongodb-php-on-debian-lenny-6
----

Recently I had to reinstall my operating system from scratch. I had a very
tough battle to get [Photoshop CS5 running on Linux Mint under
wine](../blog/entry/how-to-install-photoshop-cs5-ubuntu-mint). An easier task
was to quickly configure a development environment for myself.

So I'll try to explain how to install a **LNMP Stack** (Linux + Nginx +
MongoDB + PHP FPM) under **Debian "Lenny" (6.0)**.

&nbsp_place_holder;

## Step 1 - Installing nginx

The first step is to install [Nginx](http://nginx.org/). Nginx is a "free,
open-source, high-performance HTTP server and reverse proxy, as well as an
IMAP/POP3 proxy server".

From my personal experience I can tell you that it's an excellent solution for
providing the static content of your website (although showing actual proof of
the previous statement falls out of the scope of this article).

Counting that you have the _apt _package manager installed, only only need to
issue the following command to install Nginx:

  

    
    aptitude install nginx

&nbsp_place_holder;

&nbsp_place_holder;

## Step 2 - Installing PHP-FPM

In order to install PHP-FPM we'll add the [DotDeb](http://www.dotdeb.org/)
repository:

    
    echo "deb http://php53.dotdeb.org stable all" >> /etc/apt/sources.list
    echo "deb http://packages.dotdeb.org stable all" >> /etc/apt/sources.list
    echo "deb-src http://packages.dotdeb.org stable all" >> /etc/apt/sources.list
    wget http://www.dotdeb.org/dotdeb.gpg
    cat dotdeb.gpg | sudo apt-key add -

Then just update _apt_ and install the following packages:

    
    apt-get update
    apt-get install php5-cli php5-common php5-suhosin php5-cgi php5-curl php5-fpm php5-json php5-mcrypt php5-mysql php5-sqlite php5-dev php-pear php-apc 

And add the [MongoDB PHP Driver](http://php.net/manual/en/book.mongo.php) via
[PECL](http://pecl.php.net/package/mongo) and instruct PHP to load the
extension:

    
    pecl install mongo
    echo "extension=mongo.so" >> /etc/php5/fpm/php.ini

&nbsp_place_holder;

## Step 3 - Install MongoDB

Installing MongoDB is also pretty straightforward:

    
    install mongodb mongodb-server

&nbsp_place_holder;

&nbsp_place_holder;

## Step 4 - Configure Nginx

Finally we have to configure Nginx to play nicelly with PHP-FPM. Just edit the
file _/etc/nginx/sites-available/default_ - here is a sample configuration
file:

    
    server {
    	listen   80;
    	server_name  diogoosorio.com *.diogoosorio.com;
    	root /var/www;
    	access_log off;
    	index index.html index.php index.html;
    	
    	# Set expiration information for assets
    	location ~*\.(ico|css|js|gif|jpe?g|png)(\?[0-9]+)?$ {
    		expires max;
    		log_not_found off;
    	}
    	
    	location ~*\.php$ {
    		fastcgi_pass 127.0.0.1:9000;
    		fastcgi_index index.php;
    		fastcgi_split_path_info ^(.+\.php)(.*)$;
    		include fastcgi_params;
    		fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    		fastcgi_intercept_errors on;
    		fastcgi_ignore_client_abort off;
    		fastcgi_connect_timeout 60;
    		fastcgi_send_timeout 180;
    		fastcgi_read_timeout 180;
    		fastcgi_buffer_size 128k;
    		fastcgi_buffers 4 256k;
    		fastcgi_busy_buffers_size 256k;
    		fastcgi_temp_file_write_size 256k;
    	}
    }
    

&nbsp_place_holder;

&nbsp_place_holder;

## Step 5 - Wrapping up

Just restart the nginx and php-fpm services and you should be ready to go:

    
    service nginx restart
    service php5-fpm restart

