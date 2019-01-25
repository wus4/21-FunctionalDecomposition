"""
Hangman.

Authors: PUT_YOUR_NAME_HERE and YOUR_PARTNERS_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######
def main():
    w=initate()
    game(w)
    play_again()




def initate():
    word='apple'
    return word



def game(word):
    lose=0
    win=0
    blank=list('_ '*len(word))
    print('_ '*len(word))
    while lose<5 or win<5:
        letter=input('Please guess a letter: ')
        for k in range(len(word)):
            if word[k]==letter:
                win=win+1
                blank[k]=word[k]
            else:
                lose=lose+1
        # print('you have ',lose,'times of failure.')
        print(''.join(blank), ' ')
    if lose==-5:
        print('lose')
    if win==5:
        print('win')

def play_again():
    if input('play again: y/n?')=='y':
        game(w)
    else:
        print('out')
main()

