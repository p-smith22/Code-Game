# Code-Game
Required library -- colorama

Download by typing "pip install colorama" into your terminal window

A fun game to play with a friend! Similar to wordle, each of you will chose a code and try to guess each others. The game will tell you how many guesses were the right number in the right position.  

The game works by prompting the user to input a code. It will send this value to a function and ensure that the input code is 1) all numbers and 2) 4 digits. The game will then ask the user to input their opponents guess. The game will automatically calcualte how many numbers match both of the following parameters: 1) are the correct value and 2) are in the correct position. The game will then ask the primary user for their guess, and the other player will do the inverse of what we just described. They will then read the number correct back to the primary user, and they can input the value. The game will alter back and forth in this fashion, and there are many funcitons to check all values and make sure they are valid. 

In addition, the game includes a skip function. This allows the user to simply skip their turn. Keep in mind, this still counts as a guess! However, since this game is supposed to be played with another individual, both of them cannot start first. So, the skip function does not have a guess penalty. It simply counts as a defer and lets the other player start first. 

The game ends when it detects that either player got all 4 digits correct. It will tell which player won, as well as how many guesses it took for that player to win. The terminal is very user friendly, and is color coded and has descripive prompts to assist the user through the game.

Hope you enjoy!
