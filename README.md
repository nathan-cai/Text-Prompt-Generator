# Text-Prompt-Generator
Me and my friends created a typing test web app. These files and functions were used to get prompts of a certain length and randomly select one.

## How it Works
It interacts with the riot games api to get a list of all of the champions. Then using webscraping of the league lore site I got the lore of every champion. Then using string formating I was able to adjust the length of the prompts. Then I wrote them into a .txt file. 

the randomizer reads the .txt file through .readlines() which produces a list of all the prompts. Then a random int that from 0 to the number of objects in the list - 1 is chosen. and using list indexing the prompt is chosen and returned. 
