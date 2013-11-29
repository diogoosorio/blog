----
category: development
create_date: 2013-11-28
description: Here's to you, doers. The special ones who can do things 10x faster than any other engineer. Chin up, be proud. The product team loves you, and why shouldn't they? You know that a satisfied customer is the ultimate goal, nothing else matters.
title: A tale about technical debt
keywords: technical debt
slug: a-tale-about-technical-debt
----

Here's to you, doers. The special ones who can do things 10x faster than any other engineer.

Chin up, be proud. The product team loves you, and why shouldn't they? You know that a satisfied customer is the ultimate goal, nothing else matters.

Any time spending designing a correct(ish) solution is time wasted. God forbid that you become one of those guys who start scribbling a class diagram every time someone asks them to implement something new.

Slugish, dumb code monkeys. You know you just have to write the code once to come up with 'the' perfect solution.

You pity those guys who actually stop to think, before writing anything. If they were any good, they would come with an awesome solution right there, on the spot.

You know prototyping is for losers. As an hard-core 'coder' like yourself proudly ships every single line of code you've ever written into production. That's how you get to be that much productive than anyone else.

'Clean code' is a subjective matter and you know it. After all that's YOUR code, a rock star's code, why the f\*ck should anyone have a saying in how your work looks like? Fuck\*ng adapt... That's what you do and you're awesome, everybody loves you.

Being arrogant just comes with the job. They actually force you to be that way in order to get the job done right. How would you dismiss those no-good colleagues of yours, always yielding unasked for opinions, always pointing out the poor design choices you're making. Jealousy, they're all fuck*ng jealous, that's all.

Go ask the marketing department who they love the most. You're a doer so they can take their 'design principles' and shove them up their asses. The things these guys come up with to justify laziness...

Yeah, the product team hates them. You've even heard (more than once, actually) colleagues asserting that that new feature asked for doesn't make sense. 

Stupid bastards! You'd do that in a couple of days, just serialize the data and stick it in the username database column. That column isn't being used anyway, who would even notice that you're storing data in there? You wouldn't even need to mess around with the schema.

Normalization, constraints, ... Those are all luxuries you can't afford. That's what gives you the edge. That's what makes you 10x's more productive than anyone else.

At the end of the day your code is pretty accessible. For starters it is all on the same place.

3 files to host your code usually suffice. Doesn't any of these fuckers have a find feature on their IDE? Who cares that each file has 10k lines or so? Who cares about abstracting stuff into routines, modules, classes? The code is right THERE in front of you, just read it and figure it out.

----

F*ck you've just released the service yesterday - the demo with the product team went all right (you made sure it would) - but now those no good colleagues of yours are telling you that it's broken.

Yeah your REST(ish) service has state. You store session information in a cookie, the request comes directly from the client's browser.

It only took one day of your and your colleague's work to figure it out. There's a collision of the cookie's name. 

All good, it's fixed now. And even with this delay you were orders of magnitude faster than anyone else who might have been asked to implement that puppy.

Oh gosh it's that guy again. What now?

The requests are being cached by the browser. The f*ck do I care? Oh that's right he's trying to preform an action, not to retrieve information. A POST request would make more sense, but at the time you didn't even have had the time to think stuff like this through.

He wants you to change the code on your side. Funny guy, I'm accessing the request parameters through a global variable. The sheer number of places I'd have to touch my code to fix this invalidates his proposal of a solution.

Yeah, no you'll just add a no-cache header to the response. That should do it.

Oh man, not again. Your widget is breaking under IE9?

Who in Earth still uses IE9? Yeah, OK I'll fix it.

Let the debugging games begin. May the odds be ever on my side. Damn this is tad chaotic, the amount of repeated code isn't helping me to find the problem.

It only took you a couple of extra days to find the issue. Some fucked up, complex business logic.

You'll just need a couple of more days to find and replace all the copy/pasted code you've duplicated to accelerate the development of the service.

----

It took you a couple of more iterations to get the las fix right. To worsen the situation you're asked to modify some of the logic and, once again had to replace all that code that does the exact same thing that is splattered throughout your code. But its done.

The bad news is that amongst your colleagues your service has now the reputation of being simply broken. Erratic behaviors appear now and then, but they're spontaneous, so you're having a tough time pinning out what the real issue(s) are.

Worst than that, your manager is telling you that you're taking way too much time with the project. Instead of the couple of days you've asked for, you've been around it for a couple of weeks now - and you even weren't asked to add anything new, you're just fixing your own mess.

The thing that your manager doesn't understand is that you've done it that way because of him! He wanted a quick solution, so you've provided one. The stupid prick...

----

Oops a new feature request. You're on the verge of launching your next masterpiece to the World and you clearly won't have time to deal with this.

No problem, your manager reassigns the task to the another guy... And now you're having a tough time. You've been overhearing colleagues talking about the mess your code is in.

The guy responsible of implementing the new feature says it has nightmares about your code everyday.

He takes 10x more time he usually would to get anything done (or so he says). Not only that, he found out what was causing one of the intermittent bugs - a data manipulation goes wrong when a global variable contains a given value (it's one of the ~15 different code flows available on that file).

It gets worst, tampered, incorrect data is being stored on the database. There goes a bunch of 'business value' down the drain.

Your manager is pissed, he's stating that he should have known better. No one on Earth would be able to pull off what he asks for in just a couple of days  with the minimum quality standards 

You've just heard, the project is getting redone from scratch. Impressive on how something fairly simple was able to give so many headaches to so many people.

Every single one of your colleagues is saying that the code is so f*cked up, even Dijkstra would have a tough time maintaining it.

Well I guess that you can't win them all.

----

PS - It's a satire, for those of you who might have missed it. I don't think this will get enough exposure, but just in case I would like to tell that I do think that adding business value is our #1 responsibility as programmers.

I often do compromise quality because of a deadline (or just because I don't know any better at the time).

I also believe that those compromises should be exceptions, not the norm. And believe me, it is possible (I've already seen it happening). What I'm trying to support here is that:

*   You should not be one of the seven dwarfs and follow blindly what you're told to do. We're lucky enough to work on one of the areas who are globally recognizable as being hard enough for your opinion to be heard.

*   At the end of the day you're a professional. Be proud of the code you produce, sure it has to work properly, sure you have to deliver it on time, but try to leave your code the way you'd like to find the code of someone else's project code you'd have to maintain.
    Be proud when someone praises your tidiness. It's a clear sign of professionalism.

*   If you're constantly 'breaking windows'/'cutting corners' in your project in order to keep up with deadlines, something is (structurally) wrong either with you, your team, or your company. Work on fixing that.

    A corner cut should be an exception and (if you're doing it right) it's something that should throb on the back of your mind for the rest of the project's life.
