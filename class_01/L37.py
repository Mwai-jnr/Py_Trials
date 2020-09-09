# Loops.

# For Loop.
#Example 1

#for x in range (0,10):
 #   print('hello')
    
#Example 2

#print(list(range(10,20)))
# the last no is not included when looping through a list

#Example 3

#for x in range(0,5):
   # print('Hello %s' % x)
    # %s acts as a placeholder in strings
    #it is used when you want to insert something in a string in our case numbers 0-5.
    
    
    # while loop
    #Example 1
password = 'victor'
enter_pass = ''

pass_count = 0
pass_limit = 3
pass_out_limit = False
    
while enter_pass != 'victor' and not (pass_out_limit):
    if pass_count < pass_limit:
        enter_pass = input('Enter Password: ')
        pass_count  += 1
    else:
        pass_out_limit = True
        
if enter_pass == 'victor':
    
    print('welcome to the site')
else:
    print('try again later')
        
       
    
    