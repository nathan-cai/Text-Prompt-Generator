# Text-Prompt-Generator
Scrape a website to get prompts to use.

## How it Works
It interacts with the riot games api to get a list of all of the champions. Then using webscraping of the league lore site I got the lore of every champion. Then using string formating I was able to adjust the length of the prompts. Then I wrote them into a .txt file. 

The randomizer reads the .txt file through .readlines() which produces a list of all the prompts. Then a random int that from 0 to the number of objects in the list - 1 is chosen. and using list indexing the prompt is chosen and returned. 
