import re

def see_regex():
    sentence = 'The quick fox jumped over the fence'

    match = re.search(r'fox', sentence)
    if match:
        print(f"Found: {match.group()}")
    else:
        print("I've seen nothing related to that")

see_regex()


# let's try to use split, it sounds interesting

text = "my quick book was quicked from the shelf quickly"

splitted = re.split('quick', text)
print(splitted)
# this was the output ['my ', ' book was ', 'ed from the shelf ', 'ly']

text = 'I have something important that I want to show you.'
new_text = re.sub('something','nothing', text)
print(new_text)

use_of_find_all = "I wook wooked in to the wook and found wook"
matches = re.findall('wook', use_of_find_all)
print(f"Matches(using find all) are {matches}")


# this doesn't seem to work


# use_of_matchs = ['many people like eating a banana', 'bananas are so sweat']
# num = 1
# index = 0
# for use_of_match in use_of_matchs:
#     n_match = re.match('banana',use_of_matchs[index])
#     print(f"{num} th is having this match: {n_match.group()}")
#     num += 1
#     index += 1
    
