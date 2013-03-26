Hello.

This file is a python script to normalize "Library of Congress call numbers." The way that you use it is you open up terminal, and you type "python yourlist.csv renamedlist.txt"

Then it will take the list and convert it so that it will sort properly and microsoft excel, or any other spreadsheet program.

Then, import it back into excel.  It's delimited by commas.

A few specication I'd like to add:

1. The list should be cleaned up.  If there are Dewey decimals in there, or any other erroneous entries, locnormalize.py will produce an error.

2.  The script is specified for my institution's specifications.  If the script doesn't seem to work, perhaps your list of call numbers follows another convention. 
 Our convention is as follows (@ = alpha character, and # = numeric character).
  @@@.####.# .@###### @#### ####
Good luck.
