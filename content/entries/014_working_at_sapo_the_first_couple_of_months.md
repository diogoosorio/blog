----
category: Work
create_date: 2012-07-15
description: For the last couple of months I've been working at SAPO. These are my first impressions of the company and projects I've been envolved in.
title: Working at Sapo - The first couple of months
excerpt: For the last couple of months I've been working at SAPO. For those who the name doesn't ring a bell, SAPO is pretty much the biggest "web centered" Portuguese company - it's owned by Portugal Telecom and if you look it up on Alexa you'll probably find SAPO's homepage figuring on the top 5 most visited websites of Portugal (right after Facebook, Google and Youtube).  <p>I've been integrated on the SAPO channels team. We basically develop and mantain all those "satellite" websites that are owned by SAPO - from recipes, to gossip, sports, ... you pick a topic and it's very likelly that SAPO owns an website dedicated to the matter.</p>  <p>These are my first impressions of the company and projects I've been envolved in.</p>
keywords: sapo, working at sapo
slug: working-at-sapo-the-first-couple-of-months
----

As you might have deducted from my last post, I've been working at SAPO for
the past couple of months. For those who don't know SAPO, it's basically the
biggest "web centered" Portuguese company. It's owned by the "giant" Portugal
Telecom and its one of the references when it comes to Web Development here in
Portugal.

Another peculiarity of the company is that the Open Source ideal is deeply
rooted into SAPO's DNA. With a couple of small exceptions virtually every
project that's created at SAPO is supported by one or more Open Sourced
technologies. As an "almost direct consequence", Open Source programming
languages also rule at SAPO - from PHP, to Python, Java, Ruby, Perl, ... name
a language and you'll probably find someone who's an expert at it there (if
not a contributor for the language).

I'm the most recent collaborator at SAPO's channels team. My team is
responsible for developing and maintaing a set of websites that gravitate
around SAPO - usually involving a set of external partners for content and
whatnot. A couple of examples (where I can proudly say that a isty bitsy
amount code behind them was developed by me) are [SAPO
Sabores](http://sabores.sapo.pt/) and [SAPO Fama](http://fama.sapo.pt/).

We usually deal with small, "isolated" websites and like all things in life
this has both positive and negative consequences.

The best thing is that we're not "stuck" on any project for too long. There's
always a new challenge a couple of months from now and a new chance to start
things from scratch and do things better than we did last time.

Obviously this kind of work also has his own downsides. Projects with a short
development times also mean that there's not much room to mess around with new
stuff. As much as I'd love to make use of that "want to try-out technology
pool" consistently at work, there's pretty much a recipe laid out in front of
me - a way that things should be done and a set of tools that should be used.
Every project has that specific challenge that you need to address (the "fun"
part), but at the present time for those typical "CRUD" websites we have an
"almost mature" framework* (*officially it's just a set of libraries, but it
has grown into a pretty decent framework - the guy who wrote it doesn't like
to see it called a framework though) that abstracts most of the headaches and
gives us foundations for pretty much everything we'll be needing.

The fun part is that you're invited to pitch in and develop whatever you
consider fit to enter the set of tools that lay the foundation for every
website. I've personally started by writing some tests for the "framework"
I've mentioned before and most recently I've written a "code generation"
utility that tries to look at your database schema and spit out the basic
skeleton of a model class for every table (round 2 will be to automatically be
able to generate the relations among the Models just by taking a look at the
constrains that are in place on the database).

&nbsp_place_holder;

#### But enough about me, so how's it like to work at SAPO?

Well for the first week or so, I must confess its a bit intimidating. I mean,
I'm an interested guy and although I'm no *genius* I see myself as an fairly
intelligent guy. I'm a decent learner, I love to try out new stuff and what
truly makes me want jump out of bed in the morning is to have one of those "I
have no f*cking clue how I'll solve that" type of problems.

And yet I'm surrounded by people who are truly great at what they do. For the
most part, if you want to know what an highly skilled, motivated, self-
confident software engineer can do - just walk a couple of minutes within SAPO
and you'll know. To be called a "geek" is the greatest compliment you can get
there and I think that that says a lot.

So I must confess for the first week or so I've panicked a little. Looking
back I was introduced to a LOT of new stuff in a very short timespan - new
CMS, new framework, new search server, new javascript library, new queue
messaging system, new bug tracking software, ... I confess that it happened to
me oftenly to be having a conversation about something that at the time I
thought I should know about, just to discover a couple of minutes after that
it was pretty much the first mention I've heard of that
platform/technology/whatever.

SAPO is a big reality, with a lot of stuff going on - both internal and third-
party projects are deeply rooted into the organization and you're welcomed to
use many of them on your own projects. To have a clear overview of everything
that's going on takes a bit of time.

After getting past that initial blockage and get a hold of how stuff works, I
can honestly say I've been having fun. We are currently working in teams of 2
(I'm trying to implement code-review habits in my "micro-team", unsuccessfully
so far I might add), where each team is assigned to a project.

We regularly have training sessions that cover an wide range of topics - from
Regular Expressions, to Python evangelization, to statistics, ... - although I
must confess I'm having an hard time finding out when these are happening (my
current guess is that they are announced in a very SPAM prone mailing list).

Social skills are definitely not my strong suit, but with a minor exception so
far everyone has been extremely accessible. Everyone truly seems eager to
produce awesome services, products and websites. If you happen to have been to
any [Codebits](https://codebits.eu/), I can attest that the environment
produced there is pretty much a reflection of what SAPO is - a bunch of people
interested in hacking their way through whatever problem its thrown in their
way.

&nbsp_place_holder;

#### So what now?

Well I've taken my first "big project" in hands (until now I've been fixing
wholes and adding features in already existing applications). I've been toying
around with [Bricolage](http://bricolagecms.org/) and consequentially burning
my eyes out with Perl (programming languages with onions as their logo do that
to you, true story).

I was hoping to be allowed to preform a small "hack" on Bricolage's source
code and integrate an internal service within the CMS, unfortunately the guy
who has already done this one for another project is back from his vacation
and therefore my solution won't be used (we're in a tight schedule and I'd
take some time to get this right - I don't know Bricolage nor am I familiar
with Perl for that matter).

I'm prepping up a data migration from an old, old, old CMS (and when I mean
old, I mean its code base is 12 years old) into Bricolage via its SOAP API.
During the process all the images that are currently stored on a folder in the
filesystem are also to be migrated to a new internal service (via yet another
web service).

As the website's frontend won't be directly served by Bricolage (yeah, it kind
of trims down what the CMS can do for us, but right now its a battle I'm still
not confident enough to take on), I'm also drafting the data model for the
stuff I need to store on my side.

From there the plan is to write out a decent API to sit on top of the ORM
we're using and build up the rest of the application from there.

Looking at the "bigger picture" for now the objective is to consolidate my
position within my team. I'm still the "new guy" and I'm the youngest (and I'm
pretty sure I'm also the least experienced) developer in my team.

And for now, that's all folks. Stay tuned for further news... :)

