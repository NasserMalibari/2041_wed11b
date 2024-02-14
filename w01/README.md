# Week 1

# 6

Write a regex to match:

a. C preprocessor commands in a C program source file.

b. All the lines in a C program except preprocessor commands.

c. All lines in a C program with trailing white space (one or more white space at the end of line).

d. The names "Barry", "Harry", "Larry" and "Parry".

e. A string containing the word "hello" followed, some time later, by the word "world".

f. The word "calendar" and mis-spellings where 'a' is replaced with 'e' or vice-versa.

g. A list of positive integers separated by commas, e.g. 2,4,8,16,32

h. A C string whose last character is newline.


# 7



When should you use:

- fgrep/grep -F

- grep/grep -G

- egrep/grep -E

- pgrep/grep -P

# 8 


grep takes many options (see the manual page for grep).

- man 1 grep
    

Give 3 (or more) simple/important options grep takes and explain what they do.


# 9 


Why does this command seem to be taking a long time to run:

- grep -E hello
    
# 10 

Why won't this command work:

```grep -E int main program.c```
    

# 11

 Give five reasons why this attempt to search a file for HTML paragraph and break tags may fail.

```grep <p>|<br> /tmp/index.html```
    



For each of the regular expression below indicate how many different strings the pattern matches and give some example of the strings it matches.
If possible these example should include the shortest string and the longest string.

a. ```Perl```


b. `Pe*r*l`


c. `Full-stop.`

d. `[1-9][0-9][0-9][0-9]`


e. `I (love|hate) programming in (Perl|Python) and (Java|C)`


# 13

This regular expression `[0-9]*.[0-9]*` is intended to match floating point numbers such as '42.5'

Is it appropriate? 
                
# 14




What does the command `grep -Ev .` print and why?

Give an equivalent `grep -E` command with no options,
in other words: without the `-v`.

# 15

Write a grep -E command which will print any lines in a file ips.txt containing an IP addresses in the range 129.94.172.1 to 129.94.172.25









