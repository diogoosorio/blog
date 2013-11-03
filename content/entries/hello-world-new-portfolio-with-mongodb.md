----
category: Freelancer
create_date: 2011-12-07
description: A much needed revamp on my portfolio was made. During the process I decided to give MongoDB a try. Here are my thoughts about it.
title: Hello World - Revamped portfolio w\ MongoDB
keywords: new portfolio, revamp portfolio, mongodb portfolio
slug: hello-world-new-portfolio-with-mongodb
----

### Hello World

After two intense design\development weeks, it's with great pleasure that I
introduce my new [personal website](http://diogoosorio.com) /
[blog](http://diogoosorio.com/blog) /
[portfolio](http://diogoosorio.com/portfolio) to the World! The change was
long due - amongst so many other things I had going one, I confess that I
neglected my personal website.

Although I had a great run with WordPress on the last version of my site, I
decided to seize this oportunity, extend the development period a bit longer
and learn something new.

On one of the classes I'm taking this semester, the **"NoSQL" **topic arouse.
Needless to say that I got curious - I mean I had heard about it before (I
don't live under a rock), but I never had the time\chance to dig into it.

### Hello MongoDB

I had my mind set - I would support the new version of my site on a "NoSQL"
database system. After reading about **MongoDB** and **CrouchDB**, both Open
Source, well documented, widelly spread document-oriented database systems, I
decided to stick with **Mongo** mostly because of their _sharding_ feature (I
too share the opinion that replication should be used for redundancy and not
for scaling) and because it's written in **C++** (a language I'm familiar
with).

After giving both [Mongo's
documentation](http://www.mongodb.org/display/DOCS/Home) and it's [PHP
driver](http://pt.php.net/manual/en/book.mongo.php) I started the process of
planning the "schema" design for the website. Let me start of my saying that
wrapping my head around some of the key concepts of the system took me a while
and produced a couple (a lot) of redesign's\recoding.

The way how you plan to store, modify and access your data needs to be
detached from the way you do it in a traditional relational database system.
You are storing documents in collections, you aren't dealing with tables,
tuples and records.

So what were the conclusions after this process:

  1. A schema-free database system (like Mongo) is flexible. I can easily understand how it would become easy to extend\change an application built around a tool like Mongo.  

  2. Mongo is [light](http://mysqlha.blogspot.com/2010/09/mysql-versus-mongodb-yet-another-silly.html) (resource wise).  

  3. Storing information in a key/val data structure is simply put - awesome.  

  4. I don't see this kind of system as an alternative to conventional RDBMS systems. I do see them as a complement.

Regarding the site itself, I'm pleased with the final result. But there's a
lot of things that I still want to implement - as soon as I have time for it,
there is. :)

Feel free to browse around or shoot me an email if you want to discuss
something!

