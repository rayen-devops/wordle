
def guessword(word):
    print("the word is ",len(word), "caracters long")
    guess = input("enter ur guess word : ")
    while len(guess)!=len(word):
        guess = input("invalide length , please enter a word with the same length lenght : ")
    return guess.lower()


def verify(word,guess):
    """newword = ""
    for i in range(len(word)):
        newword = newword + word[i] + " "
    newword = newword[:-1]"""

    while True :
        score = 0
        guessindic = ""
        old = ""
        for i in range(len(guess)):
            
            if (i+1) != len(guess) and guess[i] == guess[i+1] and not(guess[i] in word and word.find(guess[i]) == i):
                guessindic = guessindic + guess[i] + "(red)" + " "
                continue
            elif guess[i+1:].find(guess[i]) != -1 and not(guess[i] in word and word.find(guess[i]) == i):
                guessindic = guessindic + guess[i] + "(red)" + " "
                continue
            else :
                if guess[i] in word and word.find(guess[i]) == i:
                    guessindic = guessindic + guess[i] + "(green)" + " "
                    
                    score += 1
                elif guess[i] in word and word.find(guess[i]) != i :
                    guessindic = guessindic + guess[i] + "(yellow)" + " "
                else :
                    guessindic = guessindic + guess[i] + "(red)" + " "

        if score == len(word):
            print(guessindic)
            print("-----------------success-----------------")
            break
        else :
            print(guessindic[:-1])
            guess = input("try again :")
            while len(guess)!=len(word):
                    guess = input("invalide length , please enter a word with the same length lenght : ")






def main ():
    
    word = "horse".lower()
    guess = guessword(word)
    verify(word,guess)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye ! thanks for trying my project !")
        pass