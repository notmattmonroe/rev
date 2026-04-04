Title: Gone, gone, gone
Date: 2006-12-18 03:29
Slug: gone-gone-gone
Category: personal
Status: published

So the sidequotes are back. I finally found five minutes to delve into the issue at hand, turns out whrandom was deprecated back in python 2.1. When I did the app server upgrade I jumped about a dozen Zope releases and a half dozen python releases and of course didn't read the release notes for each increment. I figured I'd do the upgrade and go back and figure out what was broken after the fact. Kind of like we do at work.<br /><br />So replacing<br /><br /><pre><font><font face="Lucida,Courier New"><font color="#000000">wRandom</font> <font color="#000000">modules</font><font color="#0000c0" class="operator">/</font><font color="#000000">whrandom</font><font color="#0000c0" class="operator">;</font></font></font></pre><br /><br />with the much more elegant and correct<br /><br /><pre><font><font face="Lucida,Courier New"><font color="#000000">random python:modules['random']</font><font color="#0000c0" class="operator" /></font></font></pre><br />makes it all happy again. Because I know you care.<br />
