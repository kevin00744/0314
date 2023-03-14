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