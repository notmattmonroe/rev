Title: And now my memory's full
Date: 2008-09-24 18:49
Slug: and-now-my-memorys-full
Category: personal
Status: published

Two key quotes (neither directed at me) that I took away from the status meeting:<br /><br/>Never explain in production.<br /><br />You aren't allowed to talk!  You are read-only for this meeting!<br /><br />The first may require some decrypting.  There is a tool in IBM's DB2 database server (and probably other databases, I'm not a DBA nor do I play one on the internet) called 'explain' which does just that when run against a database object (stored procedure, table, blah blah blah you don't care).  Fun tip:  running this creates a new schema to store the output of the explain, but the user that creates it <em>does not have permissions to delete it</em>.  <br /><br />That's sort of like saying "Oh, yea, you have permission to create a new Word document on your desktop, but you have to get a system administrator to delete it for you."
