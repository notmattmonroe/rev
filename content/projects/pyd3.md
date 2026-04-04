Title: pyd3
Date: 2002-08-16 21:13
Slug: pyd3
Category: projects
Template: project
Status: published
URL: projects/pyd3/
Save_as: projects/pyd3/index.html

This is a project I started backwhen I first started learning python, and I haven't done much with itsince. There are several py tools that do ID3 manipulation (all builton Ben Gertzfield's ID3.py). In trying to organize the MP3 server andall that sort of nonsense I'm thinking of maybe finishing this up ;).<br><br>So far it just uses ID3.py to get info, but I plan on adding a few moredetails (bitrate, time, filesize) to what ID3 gives and then pipe it toMySQL. Nothing fancy or difficult, just need to find time to getpython-mysql installed and write the damn thing. This is what I did wayback in the day.<br><br>import glob, getopt, string, re, sys<br>from ID3 import *<br>#get volume name/starting point from args else currentdir need os, file<br><br># this needs to walk tree/files instead.&nbsp; fix.<br>for file in glob.glob('*/*.[M,m][P,p]3'):&nbsp;&nbsp; &nbsp;<br>&nbsp;&nbsp; &nbsp;id3info = ID3(file)<br><br>&nbsp;&nbsp; &nbsp;print id3info<br><br>Yes, glob is ugly. Deal with it.
