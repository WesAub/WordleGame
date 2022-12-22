# we're making wordle in python
# make an empty list that holds the five letters of the correct word
# append the letters of the word of the day(WOD) to a list
# take input from the user, if any of the letters entered matches one, depending on the position, highlight the word
# if the letter is correct but the position is wrong highlight it yellow
# if the letter is correct and the position is correct highlight it green
# if a highlighted letter is entered more than once (e.g. FLOOD) but only one of the O's is in the word, do not highlight
# ... the second repeated letter, unless the WOD does have those two repeated letters then refer to comments 5&6.
# if all the entered letters match the WOD perfectly, print good job and end the game
# if after 6 entries the word doesn't match the WOD, game over.
# to do this, create an entry counter variable
# the WOD must be changed per game: you need a 5-letter word dictionary


import random as ran

#creating arbitrary 5 letter word library
#imprive by inclludinig a morensophisticated list/ library of genetating 5 letter words

WOD_dictionary = ["hater","loser", "doves", "clove","arise","cloak"] # use a real 5 letter word generator so that you can use letters with x.


WOD_letterList = []
#WOD_letterSet = {}
WOD = WOD_dictionary[ran.randint(0, len(WOD_dictionary)) - 1]
#print(WOD)

for i in WOD:
   WOD_letterList.append(i)
   #WOD_letterSet.add(i)
#print(WOD_letterList)


entryCount = 0
attempt_letterList = []
#attempt_letterSet = set(attempt_letterList)

while entryCount < 6:
    attempt = input("WORDLE WORDLE\n\nenter a 5 letter word\n")
    if len(attempt) == 5:
        entryCount += 1
        if attempt == WOD:
            if entryCount == 1:
                print("Genius!")
            elif entryCount == 2:
                print("Awesome!")
            elif entryCount == 3:
                print("Brilliant!")
            elif entryCount == 4:
                print("Splendid!")
            elif entryCount == 5:
                print("Phew!")

            break
        else :
            for i in attempt:
                attempt_letterList.append(i)
            #print(attempt_letterList)
            temp_Letterlist = []
            WOD_letterCounter = 0                       #love[]
            print(WOD_letterCounter)
            for i in attempt_letterList :
                if i == WOD_letterList[WOD_letterCounter]:
                    temp_Letterlist.append(i.upper())
                    WOD_letterCounter += 1
                elif i != WOD_letterList[WOD_letterCounter] and i in WOD:
                    temp_Letterlist.append(i)
                    WOD_letterCounter += 1
                else:
                    temp_Letterlist.append("__")
                    WOD_letterCounter += 1
            print(temp_Letterlist)
            attempt_letterList = []
    else:
        print("Not in the word list")
print("GAME OVER")
# for i in list, for k in i
# wordEntry = str(input("text"))
# letterList = []
# if len(wordEntry) == 5:
#     for i in wordEntry:
#         letterList.append(i)
#
# elif len(wordEntry) != 5:
#     print("Entry too long")
#
# print(letterList)








# import urllib2

# word_site = "http://www.instructables.com/files/orig/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt"
# response = urllib2.urlopen(word_site)
# txt = response.read()
# WORDS = txt.splitlines()
# randomword=(random.choice(WORDS))
# print(randomword)

#WORDS = txt.splitlines()
#WORDS_5_or_less = list(filter(lambda x: len(x) <= 5, WORDS))
