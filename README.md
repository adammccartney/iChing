## iChing readme
----------------

# Possibilities

Okay, so this is a small project to practice using some developer tools before
burning the house down on some larger project. 

The iChing is the old chinese text known as the book of changes. In essence, it
is a philosophical system, where a philosopher (that's anyone who reads the
book, by the way) reflects upon a specific question about a set of
circumstances of which they are currently aware. 

Such a reflection is created by using a chance based systemm, traditionally
either coin tosses or stick throws to divine a path to a specific part of the
text. 

# Divine a what? 

Okay, so woowoo aside, the text of the iChing consists of 64 **hexagrams**. Each
hexagram consists of two **trigrams** and each trigram consists of three
**lines**. The lines can be **broken** or **unbroken**, **changing** or
**unchanging**.

The reader builds a hexagram by tossing three coins to generate numerical
values 

    Heads (H) is worth 3
    Tails (T) is worth 2
   
it follows that:    
 
    HHH = 9
    lineHHH = "-o-"
    
    HHT = 8 
    lineHHT = "- -"
    
    HTT = 7  
    lineHTT = "---"

    TTT = 6
    lineTTT = "-x-"


As there are already in existence many wonderful translations of this text,
this program is not initially geared at their reproduction, instead the
idea is to use it to generate a hexagram for the reader. 

There are at least two versions of the text which are worth finding. 
I think most translations into European languages refer to the Richard Wilhelm
version at one point or another. There is a good version of this version, with
an introduction by Carl Jung that is widely available. 
The other version that I would recommend is by Thomas Cleary, it iss published by
Shambhala and seems to stick pretty close to the Taoist origins at the core of
the text. So if you like experience to be brief and crispy, with a certain
levity, of a different sort to that of say, the long-winded ramblings of Confuscious 
or the music of Wagner, then the Cleary translation is for you! 
The version with the introduction by Jung includes two versions of the text,
one that is fairly bare bones and tries to stick to the taoist way of doing
things and the another that includes the Confucian commentary. Also there are
some really good appendixes in this one that go into detail about the nature of
the system used to create readings. 


## Update002
10.5.2020
Second Update

Refactored and extended hexagram class 



## Update001 
5.5.2020
Added an enum class to iching.py 

Cleaned up the hexagram class, renamed members

Use cleaner function to read line values in hexagram 

```python

myQuestion = Hexagram()
myQuestion.getLinevalues()

```
### To Do 

 + Write generator function for self.printHexImage() in Hexagram class.
 + ~implement a function to return a visual depiction of the cast hexagram~
 + implement a test to check that the lineValues are being mapped to the
   right linePositions 
 + implement a command line interface to ask question and use it as an instance
   name for the hexagram


## Initial commit 
4.5.2020
The inital commit is a single file containing a hexagram class, which can be
instantiated with a question in an interactive session. The reading is
generated by calling a member function. Generally, something like 

```python

myQuestion = Hexagram()
myQuestion.printReading()

```

will return a very simple graphical representation (of chars) to the console. 



