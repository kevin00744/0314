# Define RockScissorPaper() to prompt for an input of
# rock(1), scissor(2), and paper (3). Then let computer
# randomly pick one of rock, scissor, and paper. Show
# the computer result, compare the two, and say who
# wins.
import random as rd
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
# print('You chioce %s,computer chioce %s, qq = %d ,%d' % (user_chioce_str, computer_chioce_str, user_chioce,computer_chioce))
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
