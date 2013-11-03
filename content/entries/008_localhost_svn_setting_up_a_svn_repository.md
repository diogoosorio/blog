----
category: Linux
create_date: 2012-02-18
description: In this article, I'll give a brief explanation about what is SVN and how to create a private SVN repository, under Linux Mint / Ubuntu Oneric.
title: Localhost SVN - setting up a svn repository
excerpt: Code revision systems are crucial for any developer. I cannot count how many times SVN has rescued me for tedious hours of repairing something that either were poorly planned (and therefore ended up braking things), poorly implemented, or was an extra feature that I simply never did complete. In this article, I'll give a brief explanation about what is SVN and how to create a private SVN repository, under Linux Mint / Ubuntu Oneric.
keywords: svn localhost, setting up a svn repository, creating svn local repository, svn repository, local svn
slug: localhost-svn-setting-up-a-svn-repository
----

Code revision systems are crucial for any developer. I cannot count how many
times SVN has rescued me for tedious hours of repairing something that either
were poorly planned (and therefore ended up braking things), poorly
implemented, or was an extra feature that I simply never did complete.

To gain the habit or using a code revision system can be a daunting task,
specially for those who didn't quite assimilate the concept behind these kind
of systems. Before I get started, I'd like to point out that I usually use SVN
when I want to setup a local repository just for myself, so this article will
be focusing on SVN.

This will be a "straight" to the point kind of tutorial, I won't go very deep
on every option that SVN offers and rather focus on explaining on how you can
quickly get a private repository up and running.

Although the SVN commands are transversal to all operating systems, I'm
running Linux Mint so the installation part of the article should be adapted
to the the Linux flavour of your choice (except for Ubuntu, if you're running
Ubuntu Oneric, this whole article should also apply). If you happen to have an
Windows system,
check&nbsp_place_holder;[TortoiseSVN](http://tortoisesvn.net/).

&nbsp_place_holder;

## What is SVN and what's it for?

The concept behind SVN and all the other code revision systems is to establish
"checkpoints" during your application development process. These checkpoints
are called "revisions" and they basically enable you to "rollback" your code
to any given checkpoint.

![](../../public/images/svn1.jpg)

To establish a quick paralellism (and for a simpler, more concrete
explanation), imagine a computer game. From time to time you are usually
greated with a "checkpoint", or a place where you can save the current state
of the game before proceding to fight that nasty boss. These checkpoints would
be equivalent to a revision - if you tackle the boss fight on a wrong way, you
are confident that you can rollback and start over.

Other handy feature that's at your disposal when you use a revision system is
the possibility to branch-out your code. This means that at any given point
you decide to try something radically different (a new feature that you're so
sure about, a new UI for a certain area of your application, ...) you can
simply create a completely different branch where you'll try to implement
whatever you want, without affecting the "main" code. Further down the line,
you may decide to integrate this new feature with the "main" branch (therefore
you&nbsp_place_holder;_merge_ the two branches) or simply drop whatever you're
trying to achieve.

![](../../public/images/svn2.jpg)

From the image above, you can see the main "trunk" that has 3 releases (1.0,
2.0 and 2.1). Right after launching the application, you get feedback from
your users stating that a "**Shiny new feature**" would be awesome. Although
at that point you aren't quite confident on what technology would suit better
for this new feature, you decide to have a go at it, as long as it won't
disrupt the development on the main trunk.

So at that time you create a branch. Meanwhile you release version 2.0. After
a couple of months, you finally are able to implement the "**Shiny new
feature**" and therefore decide it should become a part of your main trunk. So
you&nbsp_place_holder;**Merge** the the branch with the main trunk.

&nbsp_place_holder;

## Hands-on - how to install subversion, create a repository and start working
with it?

Let's move on to how you create a repository and how to use it. Under Ubuntu
Oneric / Mint Lisa, you can use&nbsp_place_holder;_aptitude_
or&nbsp_place_holder;_apt_ to install subversion:

    
    sudo aptitude install subversion

And as simple as that you're on your way. The second step would be to create a
repository. Now a common practice is to have all the repositories under one
folder on your file system. In my case, I'll host my repositories
under&nbsp_place_holder;**/home/diogo/svnrep/**.

So my repository will be placed
under&nbsp_place_holder;**/home/diogo/svnrep/myapp/**:

    
    mkdir ~/svnrep
    cd ~/svnpre
    svnadmin create myapp

And you now have a working, fully operational repository. The third step is to
impor your project's current files so that they start getting revised. For
demonstration purposes, let's imagine that my project is located
under&nbsp_place_holder;**/home/diogo/projects/myapp**:

    
    svn import /home/diogo/projects/myapp file:///home/diogo/svnrep/myapp/trunk -m "Initial import."

So now my repository now has a initial version of all my files. But the
project folder itself isn't associated with my repository, so you won't be
able to _commit_&nbsp_place_holder;new revisions quite yet. First you need to
checkout a working version of your repository:

    
    svn co file:///home/diogo/svnrep/myapp/trunk /home/diogo/projects/myapp_work

We now have an actual working copy of the repository. Future work on the main
trunk should be done there. Everytime you make a change in a file that's
under&nbsp_place_holder;**/home/diogo/projects/myapp_work**, you can simply
issue the command:

    
    cd /home/diogo/projects/myapp_work
    svn commit -m "This would be the message of the new commit."

And that's it. For a broader explanation of SVN features and good practices,
visit the [project's documentation](http://subversion.apache.org/docs
/community-guide/).

&nbsp_place_holder;

## SVN Mini Quick Reference

  * _add -&nbsp_place_holder;_Add a new file to the repository (ex. _svn add mynewfile.php_)  
&nbsp_place_holder;

  * _branch_ - Usually refers to a fork (a copy) of the main trunk, whose purpose is to be subjected to some modifications, without interfering with the roadmap of the main trunk  
  

  * _checkout_&nbsp_place_holder;_-&nbsp_place_holder;_Creates an working copy of a repository  
&nbsp_place_holder;

  * _commit&nbsp_place_holder;_- Create a new repository version, by submitting the changes you've made to the working copy.  
  

  * _delete -&nbsp_place_holder;_To remove a file from the repository from that point on (it will still be present on the versions prior to the delete command).  
&nbsp_place_holder;

  * _diff_ - Shows the differences between two revisions on a given file.  
  

  * _log_ - Show the revision history of &nbsp_place_holder;a given file or folder  
  

  * _merge&nbsp_place_holder;_- The proccess through which changes from the repository (ex. branch) are included on the main trunk.  
  

  * _repository_ - A central "folder" where all the versions are stored and the changes are tracked.  
  

  * _revision_ - The result of a _commit_. Represents the state of the repository at a given time.  
  

  * _update_ - Update your working copy with the most recent version of the files stored on the repository.  
  

  * _working copy_ - The place where you actually should make the changes. The files under the working copy should be subject to revision.&nbsp_place_holder;

