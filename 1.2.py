string = input('Enter string that containing digits:')
sum = 0

for ch in string:
    if ch.isdigit():
        sum += int(ch)
        
        print('Sum of digits',sum)
#output:

# Enter string that containing digits:9
# Sum of digits 9