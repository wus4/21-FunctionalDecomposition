"""
Hangman.

Authors: Shixin Wu.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# done: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random

def main():
    word=initate()
    print('_ ' * len(word))
    att = int(input('Please enter your attempts: '))
    res = game(word,att)
    result(res, word)
    while play_again()=='y':
        w = initate()
        res=game(word,att)
        result(res,word)



def initate():
    with open('words.txt') as f:
        f.readline()
        string=f.read()
        words=string.split()
    r=random.randrange(0,len(words))
    word=words[r]
    # word='apple'
    return word


def game(word,att):
    lose=0
    win=0
    blank=list('_'*len(word))
    loset=0
    lastletter=True
    while lose<att and win<len(word):
        letter=input('Please guess a letter: ')

        while lastletter==letter:
            letter = input('Please guess another letter: ')
        lastletter = letter
        for k in range(len(word)):
            if word[k]==letter:
                win=win+1
                blank[k]=word[k]
            else:
                loset=loset+1
        print(' '.join(blank))

        if loset==len(word):
            lose=lose+1
            print('wrong! attempts left: ',att-lose)
        else:
            print('correct! attempts left:', att - lose)
        loset=0
    return (win,lose)

def result(res,word):
    if res[0]==len(word):
        print('win')
    else:
        print('lose. The correct word is: '+word)




def play_again():
    if input('play again: y/n?')=='y':
        return 'y'
    else:
        print('Thank you for playing hangman!')
main()

