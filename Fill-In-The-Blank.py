global blank1,blank2,blank3 

song = " Song Name - Attention , Artist - Charlie Puth \n \
      \n I know that dress is _____ , perfume regret \n You got me thinking bout when you were ____, ooh \
       \n And now I'm all up on ya, what you expect? \n  But you're not coming home with me ____"
print(song)
blank1 = input("Blank 1: ")
blank2 = input("Blank 2: ")
blank3 = input("Blank 3: ")                           

print(f" Song Name - Attention , Artist - Charlie Puth \n \
      \n I know that dress is {blank1} , perfume regret \n You got me thinking bout when you were {blank2}, ooh \
       \n And now I'm all up on ya, what you expect? \n  But you're not coming home with me {blank3}")
def checkanswer():
    answer1 = "karma"
    answer2 = "mine"
    answer3 = "tonight"
    if blank1.lower() == answer1.lower() and blank2.lower() == answer2.lower() and blank3.lower() == answer3.lower():
        print("Correct")
    else:
        print("Incorrect, The Correct Lyrics are :- \n  \
        \n I know that dress is [-karma-] , perfume regret \n You got me thinking bout when you were [-mine-], ooh \
       \n And now I'm all up on ya, what you expect? \n  But you're not coming home with me [-tonight-]")
checkanswer()
   