# --- Directions
# Given a string, return the character that is most
# commonly used in the string.
# --- Examples
# maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"

"""
Similar questions you might be asked for and where you can use this implementation:
- Does String A have the same characters as String B? Is it an anagram (see more at "anagrams.py")
- Does the given string have any repeated characters in it?
"""

def max_char(string):
    dict_string = {}

    for letter in string:
        if letter in dict_string:
            dict_string[letter] += 1
        else:
            dict_string[letter] = 1
    most_used= max(dict_string, key=lambda x: dict_string[x])
    return most_used


def max_char2(string):
    dict_string = {}
    max = 0
    max_char = ""

    for letter in string:
        if letter in dict_string:
            dict_string[letter] += 1
        else:
            dict_string[letter] = 1
    
    for char in dict_string:
        if(dict_string[char] > max):
            max = dict_string[char]
            max_char = char

    return max_char
    

def main():
    print("Get character that is most commonly used in the string")
    string  = str(input("Input a string:"))
    get_char = max_char2(string)
    print(get_char)

main()