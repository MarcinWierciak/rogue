"""Write a function 'avg_by_letter(dictionary, starts_with)' where the argument 'dictionary' contains a dictionary where:
- a key is the name of a city
- a value is the amount of grocery stores in the city
for example:
{ 'new york':4590, 'paris':3200, 'warsaw':1200, 'poznan': 1230 }

The Function should return the average number of grocery stores in the cities which name starts with a letter passed as 'starts_with' argument.

For example for:
dic = { 'new york':4590, 'paris':3200, 'warsaw':1200, 'poznan': 1230 }
avg_by_letter(dic,'p')
should return 2215.0

NOTE: The result should NOT be rounded to an integer number."""

def avg_by_letter(dictionary, starts_with):
    number = 0
    for key,value in dictionary.items():
        for i in key:
            if key[i] in dictionary.starts_with(starts_with):
                print('jfjf')
            number += value
    return number




dic = { 'new york':4590, 'paris':3200, 'warsaw':1200, 'poznan': 1230 }
print(avg_by_letter(dic,'p'))
#print({v for k, v in dic.items() if k.startswith('p')})
