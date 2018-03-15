'''
L = list(range(10))
for i in L:
    for j in L:
        if j <= i:
            print(j,end='')
    print(' ')
'''

A = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
'''
for i in range(len(A)):
    for j in range(len(A)):
        if j <= i:
            print(A[j], end='')
    print()
'''

'''#不正确
i = 0          
while i < 9:
    for j in range(4):   
        while j < 9-i:        
            print(A[j], end='')
            j = j+1
    i = i+1
    print()
'''   

'''
#可行
import itertools
A = [1,2,3,4,5,6,7,8,9]
for r in range(9):
    for item in itertools.combinations(A, r):
        print(item)
'''

#求和函数
'''
def add_i(L):
    n = 0
    i = 0
    while i < len(L)-1:
        n = n + L[i]
        i = i +1
    print(n)
'''

#一行求和
#from functools import reduce; print(reduce(lambda x,y:x+y, range(10**2)))


#判断回文
s = input('输入')
count = 1
i = 0
a = len(s)
while i < (a/2):
    if s[i] == s[a-1-i]:
        count = 1
        i = i + 1
    else:
        count = 0
        break
if count == 1:
    print('yes')
else:
    print('no')
