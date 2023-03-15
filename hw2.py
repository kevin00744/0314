# Define HCF(x, y) to calculate and return the highest
# common factor of two numbers.
# • Hint: Find factors of the smaller of x and y, and then
# check if the factor is also a factor of the larger of x
# and y. 
def calculate(x,y):
    if x == y:
        return x 
    elif x > y :
        return calculate(x-y, y)
    else:
        return calculate(x, y-x)
def HCF(x=0, y=0):
    x = int(input('Please enter first number\n>'))
    y = int(input('Please enter second number\n>'))
    if x == 0 and y == 0 :
        print('Is undefinded')
    else:
        print ('The %s and %s larger common factor is %s'%(x, y, calculate(x, y)))
HCF()
