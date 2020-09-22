def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
def hangman():
  word="secret"
  turns=len(word)
  guess=["_" for i in range(turns)]
  print(" You have ",turns,"turns")
  print("Start guessing the word*****")
  while(turns>0):
    uchar=input("Enter guess \n")
    turns=turns-1
    if uchar not in word:
      print("The guess is wrong")
    else:
      for i in find(word,uchar):
        guess[i] = uchar
      
      s = ''
      for i in guess:
        s+=i
      print('The guessed word is ', s)
      if s==word:
        print('You got the word right !!')
        break
    if(turns==0):
      print('out of turns sucker !')

   

hangman()
