# Define HCF(x, y) to calculate and return the highest
# common factor of two numbers.
# • Hint: Find factors of the smaller of x and y, and then
# check if the factor is also a factor of the larger of x
# and y. 
def HCF(x, y):
    if x == y:
         return x 
    elif x > y :
        return HCF(x-y,y)
    else:
        return HCF(x, y-x)
x = int(input('Please enter first number\n>'))
y = int(input('Please enter second number\n>'))
print ('The %s and %s larger common factor is %s'%(x, y, HCF(x, y)))