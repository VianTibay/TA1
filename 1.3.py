#  A program that will display the following given output. (for a. use nested for statement and for b. use nested while statement)
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + ''.join(str(j) for j in range(1, i + 1)))

print("\n") 

n = 1
while n <= 7:
    if n % 2 == 1:  
        print(' ' * (7 - n) + str(n) * n)
    n += 1

'''
output:


  1
   12
  123
 1234
12345


      1
    333
  55555
7777777
'''