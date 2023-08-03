import random
import hangman_image
import hangman_word

print(hangman_image.logo)
endgame=False
lives= 6
word_selection=random.choice(hangman_word.word_list)
word_len=len(word_selection)
print(f"The selected word here is :\n {word_selection}")
#
display=[]
for letter in word_selection:
    display+='_'
print(display)

while not endgame:
    guess=input("Enter a Letter:\n").lower()
    for position in range(len(word_selection)):
        letter=word_selection[position]
        if letter==guess:
            display[position]=letter
    if guess not in word_selection:
        lives-=1
        print(f"{hangman_image.hangman_pic[lives]}")
        if lives==0:
            endgame=True
            print(f"You Lose\n{hangman_image.lose}")
    print(f"{''.join(display)}")

    if '_' not in display:
        endgame=True
        print(f"You Win\n{hangman_image.win}")