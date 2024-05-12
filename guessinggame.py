import random
guess = random.randint(1,9)
chances = 0
while chances < 5:
     n = int(input('enter a number'))
     if n==guess:
          print('Congratulations YOU WON!!!')
          break
     else:
        print('Incorrect guess, TRY AGAIN!!!')
        chances += 1
        if n > guess:
            print('Please enter a smaller number')
        else:
            print('Please enter a bigger number')
if chances == 5:
    print('The number is ',guess)       
     