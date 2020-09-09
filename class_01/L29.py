# Multiple  conditions

#example 1

score = 70

if score == 100:
    print('you have scored 100')
if score == 90:
    print ('you have scored 90')
if score == 80:
    print ('you have scored 80')
    
else:
    print  ('you scored below 80')
    
    
    #example 2 
    # using  elif statement.
    
#score = 100

if score == 100:
    print('you have scored 100')
elif score == 90:
    print ('you have scored 90')
elif score == 80:
    print ('you have scored 80')
    
else:
    print  ('you scored below 80')
    
    
    #example 3
score = 95

if score > 90 and score <= 100:
    print('you have scored between 91 and 100')
elif score == 90:
    print ('you have scored 90')
elif score == 80:
    print ('you have scored 80')
    
else:
    print  ('you scored below 80')