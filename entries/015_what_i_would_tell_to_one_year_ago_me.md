----
category: Work
create_date: 2013-05-18
description: Being the weird guy that I am, I've been thinking what would be the most important lessons I would tell myself, if I had the chance to go back on year and talk to myself.
title: What I would like to tell to 'one-year-ago' me
keywords: programming, sapo, working, developer
slug: what-i-would-tell-to-one-year-ago-me
----

Hi there Diogo from one year ago. You've just got that sweet gig at Sapo and
you're super hyped to get started and build all those awesome web
applications, I'm really glad for you, you'll have a blast. :)

While we're on that topic, I think it would be cool if I'd share some pointers
with you, there are certainly a lot of things that would love to tell 'one
year ago me', so listen up - this is going to bail you out from some major
headaches.

&nbsp_place_holder;

### They're not geniouses

They're just really, really smart. Your co-workers, I mean. They are not CS
gods, they just know a lot more than you. So here's the first advice - _listen
to them closely, learn what you can from them but be aware that you're also
entitled to your own opinion_.

Sure, most of the time you won't even have a solid opinion on the matter. You
probably haven't faced that particular problem yet (you probably will, don't
worry). So just listen closely and do think about what you're told. If you
happen to disagree with that opinion, formulate very well the reasons why you
disagree and please have the courage to raise the subject again - they'll
probably give you a hard time at first (just because), but they're cool,
they'll listen and they'll make sure they throw every single one of your
arguments to the ground. If they don't, congratulations you've just won that
argument, give yourself a pat on your back.

&nbsp_place_holder;

### Communication is paramount

Guess what, your greatest day-to-day challenge won't be code related. It will
be dealing with the product management team. One thing you need to realize
right now is that** they don't speak the same language that you do**. So when
in doubt, just assume they're aliens and deal with the subject accordingly.

You'll loose hours of sleep because you have misinterpreted a spec. You'll
loose hours of sleep because your product manager was too lazy to even write a
spec. You'll loose hours of sleep because you *thought* you've explained the
problem clearly (and your product manager went to their place without having a
clue).

Assume nothing. Also be very aware that the vast majority of the time, the
product manager doesn't have a clue about what they're talking about.

They have a concept, a prototype, but they haven't thought (not even remotely)
about all the scenarios, about all the possibilities. You'll be able to get
them with conflicting ideas or present them with a logical fallacy pretty
easily (just try). Its your job to help them out turn that concept in a
concrete, feasible feature - embrace this fact, don't fight it (you'll be that
much productive if you do).

Finally if your product manager isn't interested explaining why they want that
feature implemented (just do what I've asked kind of person), run away from
that project as soon as you can. Believe me when I tell you that if you think
that a bad code base is your worst nightmare, to have a uninterested product
manager that sends you cryptic emails and doesn't have the availability to
explain what he/she wants, that is the absolute nightmare - you'll feel no
motivation whatsoever to get up from bed those days. And yeah, these kind of
people also exist in Sapo.

Be consistent, be realistic. _Give a precise notion of what implies to make
that change._ I still think that omitting what you can and cannot do is plain
wrong (when I'm asked if I can do it, I still tell everyone that I can do
everything - I'm that awesome). But do make them see that that small UI change
that impacts your database schema and has repercussions deep within three or
four domain objects, it needs time to be done. Time, is that simple - make
them see the light.

&nbsp_place_holder;

### Clean code matters

The deadline absolutely does not justify everything. Always remember that the
code that you're writing today is the code you'll be maintaining tomorrow -
there's a very thin line separating what is an acceptable shortcut from a bad
decision that will shame you while the code of the project is being used.

You'll reach the conclusion that, most of the time, the fact that you're
feeling compelled to not do the right thing TM, is a direct consequence of a
poor design. For this reason you'll start to understand why a poor
design/architecture is a much bigger and deeper problem than a bad
implementation.

While we're on the design topic, I'll also warn you that you'll start valuing
much more those around you that are able to turn a complex concept into an
elegant, simple and modular design. Although those epic code one-liners that
solve those micro-problems efficiently and elegantly are awesome, you'll
understand that what makes (or breaks) a project is your team's ability to
design a solution. Look around you, you have a couple of engineers (with a
capital E) that are awesome at this.

Getting back at the code level per se, here are some other more specific
pointers: DRY and SRP principles are really, really important (and on the vast
majority of times can and should be applied). Also remember that meta-
information is one of your absolute best friends - be on the lookout for
places in your code that are volatile and turn that variable information into
somekind of meta-information. Try not to "hard-code" anything, it'll come back
later to bite you in the ass.

&nbsp_place_holder;

### Choose well when to refactor

As a programmer you have a major flaw - you don't know when to refactor. Today
I look at your one-year-old code and I immediately think that it could be much
better. You need to shift that mindset, your code isn't and will never be
perfect (right now I'm thinking that if you reach to the conclusion that your
one year old code is perfect, then you haven't evolved that much during that
past year). Embrace this reality.

Having said that choose wisely when to refactor (either your code or anyone
else's code). When looking at a 1300 line controller, you are allowed to shrug
and curse a bit - after that (and for God's sake) think long and hard before
allowing that "I must refactor this" feeling to kick in.

It will take longer and it'll be harder than it seems. You'll loose days
trying to refactor that hyper-mega-super-duper class that does everything
(including your breakfast) and you won't be able to finish (something more
important will come along). Worst than that you won't be able to justify what
you have been doing for the past couple of days (if they can't see it in the
UI, it didn't happen you slacker).

Common sense will help you. Does that nasty piece of code impact the
application's performance? What exactly will you gain be refactoring whatever
you're looking at right now (besides being able to sleep without constantly
thinking that you should have implode that class)? Will you be introducing a
new feature that will require that you decompose that nasty class into a more
modular solution? Bottom line - don't refactor just because.

&nbsp_place_holder;

### Testing your code is great, but...

Don't give in to the hype. Yeah unit/behavioral testing is great, but don't
write a test for every fart you take. I know that right know you're thinking
I'm wrong (I remember when I used to think that I had to test absolutely
everything, one year old me).

Some code desperately needs you to write extensive tests, some code is simply
not worth it. Having said that, do make an effort to write more tests -
looking back I can clearly tell you that I haven't tested my code as much as I
should - you'll also learn this the hard-way (you'll cut pretty much all the
articles of the new Meo website in half because of some untested regexp base
replaces that you'll throw against the database on the site's launch day -
you'll shit yourself as you never had before).

Oh and another thing, keep in mind that you won't be able to test your code
with every possible input dataset that the code will have to handle in
production. As always people have a way to surprise you regarding on how
creative they can be inserting new data into your application. So do try to
spot places where your code has a probability to break and deal with the
problem accordingly (log relevant information and guarantee that no data is
lost/gets corrupted).

&nbsp_place_holder;

### Keep studying!

There'll be always someone that'll make you feel dumb, don't worry. They'll
mention some ancestral design pattern book you've never heard of, or try to
discuss a new technology you have absolutely no clue about - when this
happens, keep doing your thing and pick up a book to learn something new (this
is one of the few things that I can compliment you about).

Also if someone on your team picks up a new technology, don't get behind -
that's a freaking golden opportunity to piggy back on that guy knowledge and
get some sense of what they're doing, you'll even feel that you're having kind
of a free ride (just by talking with the guy next to you, you'll probably save
2 hours of banging your head agains your table and cursing to whoever wrote,
whatever you're trying to learn).

One 'not-so-good' aspect of what you'll be doing is that you'll work pretty
much with the same technological stack for the whole year. This won't be a
problem at first, you have a lot to learn about scaling an application and
maintaining an infrastructure able to maintain the websites you'll be working
on. But as time passes, you'll feel kind of stuck using the same tools over
and over again.

So if you happen to have an opportunity to look at some Python code, do it. If
you happen to have to write a small script to do whatever, write it in Python.
If you have to provision a machine, go learn Puppet or Chef. Make a personal
thing to break the (technological) routine.

&nbsp_place_holder;

### Trust your team

Another thing that you'll learn is that is absolutely essential to trust your
team. Its a very bad feeling delegating something to someone and not being
>80% sure that the output will be enough (or even worse immediately get that
refactor tingling feeling that we've talked about above).

If you're dealing with an hard problem, discuss it, you'll receive a lot of
valuable input. When you do ask help, run things thoroughly through your mind,
think really hard about you're about to ask - if you need to, write a quick
prototype before asking for help.

I'm telling you this because what seems a big question to you, will probably
have a very obvious solution to the guy next to you. Most of the time this
will purely be a (lack of) experience thing. Try running through some already
made code that might address a similar problem, before asking - you'll loose
some additional time, but you won't make a fool of yourself and you might
learn something else during the process.

Finally see that guy that's right next to you and pretty much wrote the whole
framework you work with on a day-to-day basis. Yeah, that guy... He'll be
gone. And sooner or later most of the guys you look up to will also be gone,
so exploit the shit out of them while you can - absorb every piece of
knowledge they have to offer before its too late. You'll learn stuff that
doesn't come in your precious books and you'll learn stuff much faster.

&nbsp_place_holder;

### Have fun!

It'll be a great year, so lay back and do your thing. You'll be A-OK (trust me
on this). :)

