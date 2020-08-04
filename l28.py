#if statements

## start

name = "victor"

if name == "victor":
    print("you are welcome")
else:
    print('you are not welcome')
    
# example 2

age = '15'

if age <= '17':
    print("you are under age")
else:
    print("you can visit the site")
    
    
# example 3
# two if statements
age = '17'

if age <='17':
     print('you are under age')
     if age >= '13' and age < '20':
         print('you are a teenager')
else:
    print('you can visit the site')
    
    
#example 4
age = '20'

if age <='17':
     print('you are under age')
     if age >= '13' and age < '18':
         print('you are a teenager')
else:
    if age >= '19' and age < '35':
        print("you are an older guy ")
    print('you can visit the site')