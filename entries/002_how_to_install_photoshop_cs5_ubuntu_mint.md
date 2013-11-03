----
category: Linux
create_date: 2011-12-14
description: This is a quick guide with instructions to install Adobe Photoshop CS5 on Ubuntu 11.10 (Oneric Oncelot) or Linux Mint 12 (Lisa).
title: How to Install Photoshop CS5 on Ubuntu 11.10 (Oneric Ocelot) and Mint 12 (Lisa)
keywords: photoshop cs5 ubuntu, install photoshop cs5 ubuntu, photoshop cs5 linux mint, install photoshop cs5 linux mint, install photoshop cs5 ubuntu 11
slug: how-to-install-photoshop-cs5-ubuntu-mint
----

As it turns out the new [Linux Mint 12
(Lisa)](http://www.linuxmint.com/download.php) has a pretty decent support for
my Broadcom wireless network card.

Since I got my current laptop I had been struggling a lot to be able to
connect to any WLAN network. At certain point I said enough and returned to
Windows Vista (yeah, I know). It was one of those things - everyday I booted
up my PC and turned on a VirtualBox virtual machine running Debian inside my
Windows installation.

Then I would switch between the OS'es depending of the task I was preforming -
if I was developing something (either in PHP, Java or Python) I switched to
Debian, if I was messing around Photoshop (slicing up future to be CSS
layouts) I switched to Windows.

The realisation that a Debian based distro had (finally) decent support to my
network card made me come back to Linux permanently. To be honest it was one
of the most pleasurable things I did in the last couple of months - sweeping
of my Windows partition. :)

Anyway I got my workstation up and running and I needed to install [Adobe
Photoshop CS5](../../blog/entry/how-to-install-photoshop-cs5-ubuntu-mint) on
my new Linux Mint installation.

Turns out that [Wine](http://www.winehq.org/) has a [great support
](http://appdb.winehq.org/objectManager.php?sClass=version&iId=20158)for this
application. But under Ubuntu Oneric and Linux Mint 12 the installer doesn't
work - but there's a quick and simple turnaround.

&nbsp_place_holder;

## Installing Wine on Ubuntu 11 / Linux Mint 12

So the first thing you have to do is to install wine and winetricks. You may
use _apt-get_ to do so:

    
    sudo add-apt-repository ppa:ubuntu-wine/ppa
    sudo apt-get update
    sudo apt-get install wine1.3 winetricks

&nbsp_place_holder;

## Configuring Wine

You'll need to use winetricks in order to install some dependencies, before
you start installing **Photoshop** itself.

    
    winetricks gdiplus ie6 msxml3 vcrun2005sp1 vcrun2008

## &nbsp_place_holder;

## Getting Adobe Photoshop CS5 Files

As I mentioned before the Adobe Photoshop CS5 installer won't work directly
under Ubuntu 11 or Linux Mint 12. In order to get the files and the registry
information of the application you'll need to get access to a Windows machine
with the 32 bit version of Adobe Photoshop CS5.

Start off by dumping the registry information of the application. To do so
open _regedit_ (**Start** -> **Run** -> _regedit_) and find the key:
HKEY_LOCAL_MACHINE\Software\Adobe

Once you find it, right click on it and select **Export**.

Save the resulting _.reg_ file somewhere.

Now you'll need to copy some files from the Windows computer to the main OS:
**C:\Program Files\Adobe\**, **C:\Progr****am Files\Common Files\Adobe**,
**C:\Users****\your_use****r\AppData\Roaming\Adobe**,
**C:\Windows\System32\odbc32.dll** and **C:\Windows\System32\odbcint.dll**

![](../../public/images/blog/registry.jpg)

&nbsp_place_holder;

The copied folders should be placed on the following locations:

    
    C:\Program Files\Adobe\ >> "~/.wine/drive_c/Program Files/Adobe"
    C:\Program Files\Common Files\Adobe >> "~/.wine/drive_c/Program Files/Common Files/Adobe"
    C:\Users\your_user\AppData\Roaming\Adobe >> "~/.wine/drive_c/users/your_user/Application Data/Adobe"
    C:\Windows\system32\odbc32.dll >> "~/.wine/drive_c/windows/system32/odbc32.dll"
    C:\Windows\system32\odbcint.dll >> "~/.wine/drive_c/windows/system32/odbcint.dll"

Then you have to impor the registry entries that you've obtained earlier.
Supposing that you named your registry file **photoshop_cs5.reg**, issue the
following command:

    
    wine regedit photoshop_cs5.reg

Finally you just have to override the _odb32_ and _odbcint_ libraries as
native. To do so run:

    
    winecfg

Choose the **Libraries**, type _odbc32_ in the **New override for library**
box and hit **Add**. Do the same for _odbcint__._

![](../../public/images/blog/winecfg.png)

&nbsp_place_holder;

## Launch Photoshop CS5

Finally to launch Photoshop CS5, issue the command:

    
    wine "~/.wine/drive_c/Program Files/Adobe/Adobe Photoshop CS5/Photoshop.exe"

&nbsp_place_holder;

## Bonus - Error when selecting the Type Tool

If the selecting the **Type Tool** causes the application to crash, try to
download [this file](../../public/files/5.1.2.225__atmlib.zip), extract it and
copy it to _~/.wine/drive_c/windows/system32/_.

After that override that dll as native on the _winecfg_ tool, just like you
did above with the _odbc32 _and _odbcint_ dll's.

&nbsp_place_holder;

## Wrapping Up

Although it's not a quick procedure, by following these instructions you can
have **Adobe Photoshop CS5 **up and running under ******Ubuntu Oneric **or
**Linux Mint**. It runs smoothly and it really haven't given any problem at
all (so far).

The printscreen bellow is from my actual Desktop, **Linux Mint 12** running
**Photoshop CS5 **while writting this post**.**

![](../../public/images/blog/photoshop_cs5_linux_mint.jpg)

