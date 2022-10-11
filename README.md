# MicroMotion-modbus-reader
A Quick n Dirty program to read the values from an old MicoMotion flow meter. I don't remember the model save it's from the late 90s or early 2000s.

A place I used to work had a very old flow meter that was used for simple calibrations. This meter was made by MicroMotion, now a part of Emerson. Like all things this company did, they never bothered progressing beyond using the heavy application provided with the meter to collect data, and when the program started to become obsolete and difficult to run on anything other than XP, they did the usual thing: ignored it and hoped it would go away. 

At the time, I had almost no python experience and no modbus experience, but was able to come up with this solution that did nothing more than read the parameters the meter currently had in memory, and write them to a file for later processing. It took some coordination with the tech team at Emerson, who were somewhat interested in knowing that you could read the unit with python. Another employee did some minimal plotter code, and we plumbed it in (this was removed since I didn't write that.) After doing some prove in, it was presented to the engineering manager / CEO / owner / etc. 

The only thing I can tell you about that is this person was deathly afraid of anything that he didn't understand, which surprised me as he was about 20 years younger than me. His thing was LabView, and if it wasn't written in LabView by one of his hand-selected people, then he wasn't interested. A half-hour presentation netted me one comment.

"Can't you write that in LabView?"

Nope.

It wasn't that I was unwilling, but I knew he wasn't willing to allot me the time to learn enough LabView to do anything with, and that he would sieze any little bug as proof that the job couldn't be done.

Here it is for you. It's nothing special, but to me it was an illuminating moment that taught me a few things about how both Python and Modbus worked.
