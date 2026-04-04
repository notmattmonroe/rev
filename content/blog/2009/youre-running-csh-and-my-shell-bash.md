Title: You're running csh and my shell is bash
Date: 2009-04-08 14:36
Slug: youre-running-csh-and-my-shell-bash
Category: personal
Status: published

If for some reason you want your applications to reside somewhere other than /Applications for some reason (space in my case) you will still want to have links to them in /Applications.  For Apple applications, updates are likely to fail if the applications aren't located there, and tools like AppFresh only search that location.  Creating a bunch of aliases is tedious, so here's a quick terminal trick (which I didn't think would work, as it doesn't under Linux):cd /Applicationsln -s /path/to/apps/* .That's it.
