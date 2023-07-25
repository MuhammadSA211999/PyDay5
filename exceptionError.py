# exception hocce runtime error:
'''
typeError
valueError
syntexError
zeroDivisionError
indexError

Python e **runtime error orthath **exception handle korar jonno **try-except block and finally block use kora hoy.
**try except and finally code block er odhine zoto code ache segulu run korbe.
'''
list=[34,0,40]
try:
    # result=list[0]/list[1]
    result=list[0]/list[3] #IndexError
    # print(result)
except ZeroDivisionError:
    print("Can't possible be something divided by zero")
except IndexError:
   print('list index out of range')
finally:
#  print("It's run under finally")

 def voter(age):
    if age<18:
       raise ValueError('Need to 18 years')
    return 'You are allowed to vote'

try:
   result=voter(17)
   print(result)
except ValueError as error:
   print(error)
finally:
   print('code run in finally')

# Another function 
def dueMoney(money):
   if money<3090:
      raise ValueError("I can't handle")
   else:
      return "It's clear! No more remaing to due."
try:
   dueInfo=dueMoney(float(input('Enter the amount: ')))
   print(dueInfo)
except (ValueError,TypeError,ZeroDivisionError,SyntaxError,IndexError) as error:
   print(error)
finally:
   print('Code run in finally block')
