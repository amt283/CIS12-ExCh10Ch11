# CIS-12, Chapter 10 & 11 Exercises

<h2>Exercise 10.11.2</h2>
My version and the instructor's are the same, more or less, though mine has the old version of value_counts that was 
improved on with new_value_counts(). 

<h2>Exercise 10.11.3</h2>
My version and the instructor's are the same, more or less, but the instructor's separates the value_counter and the 
has_duplicates function. However, I combined the two so that way the loop would stop counting values and return TRUE 
if anything went over the value of 1, so instead of two loops there'd only be one. So, for this reason, I think my 
version is a bit more efficient.

<h2>Exercise 10.11.4</h2>
My version and the instructor's are the same, more or less.

<h2>Exercise 10.11.5</h2>
For this one, I almost matched the instructor's code - though I didn't realize (until too late) that my version is 
adding like-keys together and ignoring any keys that only appear in one list. To improve my code, I'd essentially just 
have to change my add_counters() function to match the instructor's version instead.

<h2>Exercise 10.11.6</h2>
My version and the instructor's are the same, more or less, though they differ in that I didn't realize that the 
exercise wanted us to use the wordlist (but I can see it now after reviewing the exercise) so I used some hardcoded 
words. That and I got a little carried away with the exercise and decided to add some functionality to check whether 
the word is an actual English word (and it's spelled correctly) before checking to see if it's an interlocking word. 
That was mostly for fun and because I figured that if you scrambled a bunch of letters together you could trick the 
program into believing the "word" was interlocking and the only way to get around that would be to verify the word 
itself - a feature Python doesn't have, surprisingly! It took some time and some trial and error to find a module that 
worked/is still supported before I finally stumbled on nltk.

<h2>Exercise 11.11.2</h2>
My version and the instructor's are the same, more or less, though I made a separate list with just one element (6) 
and then concatenated it with list1 a new tuple. I did this because I tried to append the number 6 as: 
<i><b>t = t[1].append(6)</i></b> and got an error message that tuples are not mutable, which led me to believe that 
concatenation was the only way to do it, and it'd need a new tuple. Understandably, I think the instructor's version is 
much more efficient considering it doesn't use as many lines as mine does. To improve my code, I'd just have to remove 
the unneeded extra list, remove the extra tuple and append directly to list1 instead.

<h2>Exercise 11.11.3</h2>

<h2>Exercise 11.11.4</h2>

<h2>Exercise 11.11.5</h2>

<h2>Exercise 11.11.6</h2>

<h2>Exercise 11.11.7</h2>