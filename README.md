Hello.

This file is a python script to normalize "Library of Congress call numbers." The way that you use it is:
1. Download the script.
2. Put it in the same directory as your un-normalized call number list.  Your un-normalized call number list should be a simple text file, one call number per line, no commas necessary
3. Open up the LOCnormalize.py script in a text editor, change the "openy" variabel to point to your un-normalized text file.
4. Open up terminal and change it to directory where you put the LOCnormalize.py script and un-normalized call number list text file.
5. type the following into terminal:

python locnormalize.py newlistname.txt

"newlistname.txt" can be renamed whatever you want.

Then it will take the list and convert it so that it will sort properly and microsoft excel, or any other spreadsheet program.

Then, import it back into excel.  It's delimited by commas.

A few specication I'd like to add:

1. The list should be cleaned up.  If there are Dewey decimals in there, or any other erroneous entries, locnormalize.py will produce an error.

2.  The script is specified for my institution's specifications.  If the script doesn't seem to work, perhaps your list of call numbers follows another convention. 

 Our convention is as follows (@ = alpha character, and # = numeric character).
 

 @@@.####.# .@###### @#### ####


Good luck.
