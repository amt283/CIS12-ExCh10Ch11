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
<i><b>t = t[1].append(6)</i></b> 

This gave me an error message that tuples are not mutable, leading me to believe that concatenation was the only way 
to do it and it'd need to be assigned to a new tuple in the process. Understandably, I think the instructor's version 
is much more efficient considering it doesn't use as many lines as mine does. To improve my code, I'd just have to 
remove the unneeded extra list, remove the extra tuple and append directly to list1 instead.

<h2>Exercise 11.11.3</h2>
My version and the instructor's are the same, more or less.

<h2>Exercise 11.11.4</h2>
My version and the instructor's are the same, more or less, though I used the less efficient version of the 
count_value() value function (grabbed from the chapter), so I could definitely improve my code by using the version I 
created in the chapter 10 exercises. I could also make my code more efficient by removing the for loop in my 
most_frequent_letters() function and replacing it with the sort function that the instructor used instead.

<h2>Exercise 11.11.5</h2>
I couldn't figure out how to even start this exercise, so unfortunately I ended up with nothing getting done. :( I had 
though about asking Chatgpt for help, but with how lost I was with this, I felt that chatgpt would basically be doing 
all the heavy lifting and it wouldn't really help me learn how to actually think critically of what would be needed.
At the very least, I figure I can just look through the instructor's solution to see what was done and, if I still 
don't understand I can ask about it during class/office hours.

<h2>Exercise 11.11.6</h2>
Right away, I'd say the instructor's version is the better one compared to mine. It's very clearly more efficient, 
uses less line and, as a result, is much more readable. Though I'm not sure how to improve my code (outside of just 
copying and pasting the instructor's version) because I don't really understand what the sum() function is doing with 
the for loop inside of it. So, even though I think the instructor's version is better, I like my version better because 
I can follow along a little better.

<h2>Exercise 11.11.7</h2>
Like 11.11.5, I couldn't figure out how to even start this exercise and just ended up leaving it as-is. At the very 
least, I figure I can just look through the instructor's solution to see what was done and, if I still don't 
understand I can ask about it during class/office hours.