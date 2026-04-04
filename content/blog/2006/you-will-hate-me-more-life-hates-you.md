Title: You will hate me more than life hates you
Date: 2006-01-20 11:00
Slug: you-will-hate-me-more-life-hates-you
Category: personal
Status: published

Sparing the sordid details: We've been trying to get our DB upgraded to the latest version (which has been out for like two years now).  This requires among other things a kernel upgrade and converting the databases from the old format to the new one format and there has been much rewriting of stored procedures and views and triggers.  We created clean test regions and made sure the applications would still work as expected etc etc.  We've been twiddling our thumbs on implementing until there was a 'convenient' time for a system outage.  <br /><br />Last Friday there was a big ass meeting where we were given 5 business days to implement in cert, regression and integration test, and deploy to production.  Oh, and we have to deploy the newest fixpack for one of our major applications at the same time even though the users haven't signed off on it yet.  Nor have the developers finished testing it.  We're deploying to production over the weekend.<br /><br />Update:  Oh yea, griz reminds me we have a power outtage this weekend.  One of the team leads not affected by this commented &quot;What, you figured there weren't enough points of failure so you had to throw in a power outtage as well?&quot;<br />  
