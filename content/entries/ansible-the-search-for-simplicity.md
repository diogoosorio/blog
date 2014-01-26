----
category: DevOps
create_date: 2014-01-26
description: Ansible is a simple (yet powerful) provisioning tool. Having worked with Puppet for the past couples of months, for a guy like me (who's not a sysadmin nor a devops) it felt like a breath of fresh air.
title: Ansible - The search for simplicity
keywords: ansible, vagrant, puppet, provisioning
slug: ansible-the-search-for-simplicity
----

I'd like to start off by saying that I'm a developer - I'm not a sysadmin, nor am I any sort of devops. This article specifically exposes how **Ansible** is proving itself as being an awesome solution within this context. :)

Unless you've been living under a rock for the past couple of years, you've certainly heard about ***provisioning automation tools*** - Puppet, Chef, Salt, ...

As you're probably also aware, one of the main huge benefits of adopting these tools, when you integrate an web-development team (and looking at them by a developer's perspective), is the capability they offer to provide a consistent development environment for every member and every project developed by your team.

Succinctly, you write a recipe that declares how to install all the software stack required by the project once and then you can guarantee that everyone will work under the exact same environment.

Within my team, there has been a small movement to give some awareness on how virtualization effectively does help to avoid surprises caused by the fact that every single one of the developers builds its own software stack. Without any "recipe", without even an hint of what the production environment looks like. Consistency and standardization are two wonderfully nonexistent concepts at this level.

My team also happens to manage a lot of websites. I might be working on a project I'm quite familiar with this week, and next week be called to fix something on a codebase I've never even heard about. And this poses a challenge, as every project has its tweaks and quirks to get running correctly - I don't have statistics, but if I had to shoot an estimate, I'd say that it usually takes (at least) one morning/afternoon just to bootstrap the project and get it running locally.

So we've been toying around Vagrant and Puppet a bit, to see if we can offer a solution that unarguably adds value to everyone - we're talking about directly affecting **HOW** people work and this change (as you also might imagine) is received with an enormous resistance.

Anyhow, your first approach was with Vagrant + Puppet. The experience hasn't been the greatest one, Puppet works nicely, but I feel that it has a bit of a steep learning curve - we haven't really nailed the process of working with the tool yet.

So today I had to create a new "provisioning recipe" and I decided to look for alternatives. And boy, I'm glad I did. Enters **Ansible**.


## Beautiful simplicity

So what does **Ansible** introduce that I couldn't really find in **Puppet**? Simplicity mostly.

We did get to a point where we had a solid codebase that handled most of the most common scenarios (both using community-powered recipes and recipes written by ourselves), but every time something new was needed, my immediate thought would be - "Here I go again to start a fight with Puppet".

Don't get me wrong, the tool is unarguably one of the more powerful tools you'll find for managing a set of servers and offers a lot of things that **Ansible** does not. But this has a cost - it took me a couple of days just to get my first recipe working.

Things should be as simple as they can be. After trying out **Ansible** for a couple of hours, I've been left with the feeling that I've been using a bazooka to solve a problem that could be solved with a nail gun.

It took me a couple of hours to write a very similar recipe to the one it took me a couple of days to get right with **Puppet**.



## It's all YAML

Puppet has its own declarative language. It's a Ruby based DSL and is quite extensive, which I guess it would suite you right if you're a sysadmin (and the time you'll put into learning and decorating the whole lexicon of the DSL will be greatly compensated by the time you'll save in the medium-run).

But for a guy like myself who's purpose for the tool is not to automate the provisioning/management of a large server ecosystem, but to be able to bootstrap a local development environment on a consistent and efficient way, it's an overkill.

With Ansible, books (aka recipes) are written in YAML. By other words, you can declare how to provision a whole machine in YAML which is nice (not so say fucking awesome) - we use YAML all the time within our projects, it's simple, flexible and widely known (which means that there are a LOT of libraries for parsing/manipulating files in this format). Not only that, but the syntax of the books are quite expressive:

```
---
tasks:
    - name: create the www directory
      file: path=/workspace/www owner=www-data group=www-data permissions=0644
```

Want to declare a loop?

```
---
tasks:
    - name: install dependencies
      apt: pkg={{ item.pkg }} state={{ item.state }}
      with_items:
          - {pkg: 'vim', state: 'latest'}
          - {pkg: 'tmux', state: 'present'}
```

My point is - you don't need to know practically nothing about Ansible to have a pretty accurate idea of what's going, just by looking to the yaml files.



## Straightforward order of execution

If you've dealt with Puppet, one of the first things you'll notice is that the execution order of the recipe is not as straightforward as you'd think. The whole recipes get "compile" and only then Puppet decides on how it'll execute the provisioning tasks.

In a Puppet recipe for each resource you declare its dependencies - you basically say 'this task right here, depends on that one having already run'. And this solution is elegant and ultimately it encourages a more modular approach.

On the other hand... As your recipe grows, I find it harder to read. Furthermore if you happen to declare the same resource (or invoke the same task) in more than one place, Puppet will nicely tell you to go fuck yourself and rewrite the recipe correctly. You'll probably scale your recipes in a more correct manner, but with the cost being a steeper learning curve and a whole lot of head bagging.

One really cool thing in Puppet is that it has the concept of inheritance, so you can virtually extend any recipe already out there. But I'm digressing... :)

So once again, if you look at an Ansible recipe the order of execution is very straightforward - it's the order declared on the YAML file. Do you happen to include another file? Just open it up and you know that all the tasks you'll be run in that exact order.



## SSH all the things

Ansible has a different approach on how it deploys its stuff, when compared with Puppet or Chef. I've never used this feature in Puppet/Chef, but the overall concept is that each managed server is running a daemon (an agent) responsible for probing the 'master' server for changes and applying them as needed.

With Ansible you simply SSH all the things. The host machine is responsible for pushing the changes over to all the managed servers via SSH. In our work flow this is great - we don't do continuous deployment, we do have autonomy to deploy to our development and staging environment, but to update our production environment is a task that needs to be done by our ops team (this is a whole thing, we don't even have access to our application logs, we actively need to ask for a dump of the logs).

So we do like to have a manual trigger for any update, but to have the actual process automated is (in my opinion) a great asset. But back to Ansible, if we declare a hosts file like so:

```
[local]
127.0.0.1

[development]
192.168.88.33
```

And have a playbook like so:

```
---
- hosts: local
  user: sapodev
  roles:
        - install apache
        - install postgresql
        - install php
        - deploy project schema
        - deploy project vhost
        - restart apache
        - pull the project changes
        - apply project database migrations

    vars:
        postgres:
            host: 127.0.0.1
            user: local
            password: local_password

- hosts: development
  user: sapodev
    tasks:
        - pull the project changes
        - apply project database migrations
    postgres:
        host: 127.0.0.1
        user: devuser
        password: dev_password
```

Each role can be seen as a "module" that encapsulates a number of operations.

As you might already figured out, what we're stating above is that we want to do a full provisioning on the local environment, but on the development environments we want to just update the application and apply any database migration that may be pending.

You see where I'm getting.


## Wrapping up

Automation is great, we are developers because we love automation - it's in our blood, repetitive tasks are our fierce enemy. To have a mechanism able to quickly provide an adequate, consistent development environment to your team is also great (as you can make it as approximate as the production environment as you want). To be able to use the same tool to automate deployment is the cherry on top of the cake.

If you're thinking of trying out Chef/Puppet out, but the task to actually learn their DSL and the way the tool operates seems daunting, my honest, heartfelt recommendation is that you try out Ansible - it's simple, power and it simply works. :)
