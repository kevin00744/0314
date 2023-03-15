# Define Fibonacci(n) to print the first n Fibonacci
# numbers as follows.
# • 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …
# • Hint: Using recursive equation: F(n)=F(n-1)+F(n-2)
# with initial conditions F(1)=1 and F(2)=1.
def Fibonacci(n=1):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
def print_Fibonacci(n=1):
    n = int(input('Input how many number you want to see\n>'))
    for i in range (1,n):
        print ('%s,' % Fibonacci(i),  sep = "", end = "")
    print (Fibonacci(n))
print_Fibonacci()

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

# Define GCContent(s) that takes a DNA sequence as
# input and output the GC content, i.e., the percentage
# of bases that is G or C. Then do the following.
# • Hint: You can use for loop on a string s and that will
# go through each base of the string.
def GCContent(S):
    s = str(input('Please input you DNA sequence(Must use capital ATCG)\n>'))
    sum = 0
    for i in range (len(s)):
        if s[i] == 'C':
            sum +=1
        elif s[i] == 'G':
            sum +=1
    content = sum / len(s)
    print ('GC content of %s is %s.' % (s , content))
GCContent(1)

# Define RockScissorPaper() to prompt for an input of
# rock(1), scissor(2), and paper (3). Then let computer
# randomly pick one of rock, scissor, and paper. Show
# the computer result, compare the two, and say who
# wins.
import random as rd
def RockScissorPaper():
    r = 'rock'
    s = 'scissor'
    p = 'paper'
    def user():
        user = input('Please enter rock(1), scissor(2), or papper(3)\n>')
        if user == r or user == 1:
            user = 1
            uc = r
        elif user == s or user == 2:
            user = 2
            uc = s
        elif user ==  p or user == 3:
            user = 3
            uc = p
        else:
            print('please enter the vaild input!(Don\'t use any Capital letter!)')
            return None, None
        return user, uc 
    def computer():
        computer = rd.randint(1,3)
        if computer == 1:
            cc = r
        elif computer == 2:
            cc = s
        elif computer == 3:
            cc = p
        return computer, cc

    while True:
        user_chose, user_chose_str = user()
        computer_chose, computer_chose_str = computer()
        if user_chose is None:
            continue
        print ('User chose %s' % user_chose_str)
        print ('Computer chose %s' % computer_chose_str)
        if user_chose == computer_chose:
            print('Tie')
        elif user_chose == 1 and computer_chose == 2 or user_chose == 2 and computer_chose == 3 or user_chose == 3 and computer_chose == 1:
            print ('You Win!! Computer lose!')
        else:
            print ('You lose! Computer win!')
        play_again = input('Do you want to play again?(y/n)\n>')
        if play_again != 'y':
            break
RockScissorPaper()