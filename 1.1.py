input_string = input('Enter a String:')
vowels = 0
consonants = 0
spaces = 0
other = 0

for ch in input_string:
    if ch in 'aeiou':
        vowels += 1
    elif 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':  
        consonants += 1 
    elif ch.isspace():
        spaces += 1
    else: 
        other += 1


print('Vowels:', vowels)
print('Consonants:', consonants)
print('Spaces:', spaces)
print('Other Characters:', other)

'''
Enter a String:Vian Rotciv 
Vowels: 4
Consonants: 6
Spaces: 2
Other Characters: 0
'''