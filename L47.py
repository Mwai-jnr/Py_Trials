#functions

#example
# defining a function.
#def invite():
 #   print('you have jus been invited to visit')
    
#print('am outside the function')

#calling the function

#invite()
#print('am also outside the function')

#First Function.

#def hello(fname, lname):
  #  print ('hello %s %s' % (fname, lname))
 #   
#hello('Victor', 'Mwai')


#arithmetic Function

#def deduction(pay, nhif):
  #  pay_month = pay - nhif
 #   print(pay_month)
    
#deduction(500 , 10)

  # using return.
  # def deduction(pay, nhif):
  #     return pay - nhif
      
  # print(deduction(500 , 10))

# variable scope. Lesson 52
#calling a varible outside of a function <!---- third_num---->

# third_num = 3
# def my_multiplication():  
#   first_num = 3
#   second_num = 10  
#   return first_num * second_num -third_num
# print( my_multiplication())
# print(third_num)

#return statements Lesson 53

# def sqr(num):
  
#  return num * num
  
# print(sqr(3))


#Power with functions lesson 54

# def power_rule(base,power):
#   result = 1
#   for i in range (power):
#     result = result * base
#   return result

# print (power_rule(4,3))

#Random with functions
# import random
# def getNum(enterNum) :
#    if enterNum == 1 :
#      return 'you got $5'
#    elif enterNum == 2 :
#      return 'you are out of the game'
#    elif enterNum == 3 :
#      return 'you got another chance'
#    elif enterNum == 4 :
#      return 'you got nothing'
   
# r = random.randint(1,4)
# fortune = getNum(r)
# print (fortune)
 
 
 #HANDLING ERRORS
 
# try:
#   def num_var(divider) :
#     return 45 / divider
#   print(num_var(0))
# except ZeroDivisionError:
#   print('Invalid Number')


#NUMBER GUESSING GAME.

# import random

# secretNumber = random.randint(1,20)
# print ('i am thinking of a number between 1 and 20')

# for guesses in range (1,7):
#   guess = int(input('Take a guess: '))
  
#   if guess < secretNumber:
#     print ('Select a higher number')
#   elif guess > secretNumber:
#     print ('Select a lower number')
#   else:
#     break
  
# if guess == secretNumber:
#    print('Good job you have selected the number from' + str(guesses) + 'guesses')
# else:
#    print('The number i was thinking of is ' + str (secretNumber) +  ' Thankyou for trying')
   
# END OF GUESSING GAME


# DICE GAME 

# import random

# def roll(sides,dice):
#   result = 0
  
#   for roll in range (0,dice):
#     result += random.randint(1,sides)
#   return result
  
# print (roll(6,3))

# END OF DICE GAME

#BMI(body mass index) CALCULATOR START.

# def bmical():
#   w = float(input('Input your weight: '))
#   h = float(input('Input your height: '))
#   result = w/ h**h
#   if result < 18.5:
#     print("you BMI is low")
#   elif result >= 18.5 and result <25:
#     print('your BMI is okay')
#   elif result >= 25:
#     print("you are over weight")
#   else:
#     print("invalid Body Mass Index")
#   return result

# print(bmical())

#BMI CALCULATOR END.


#EXCEPTION HANDLING START.
 
def rationalnum(Divideby):
  try:
    return 50/ Divideby
  except ZeroDivisionError:
    print('invalid number')
print(rationalnum(0))