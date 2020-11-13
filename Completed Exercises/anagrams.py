# --- Directions
# Check to see if two provided strings are anagrams of eachother.
# One string is an anagram of another if it uses the same characters
# in the same quantity. Only consider characters, not spaces
# or punctuation.  Consider capital letters to be the same as lower case
# --- Examples
#   anagrams('rail safety', 'fairy tales') --> True
#   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
#   anagrams('Hi there', 'Bye there') --> False

def build_dictionary(str):
    dict_string = {}
    for letter in str:
        if letter in dict_string:
            dict_string[letter] += 1
        else:
            dict_string[letter] = 1
    return dict_string


def anagrams(stringA, stringB):
    anagram = True
    modified_stringA = ''.join(filter(str.isalnum, stringA)).lower() 
    modified_stringB = ''.join(filter(str.isalnum, stringB)).lower()

    dict_stringA = build_dictionary(modified_stringA)
    dict_stringB = build_dictionary(modified_stringB)
    x = 0

    if(len(dict_stringA) != len(dict_stringB) ):
        anagram = False

    for x in dict_stringA:
        if dict_stringA.get(x) != dict_stringB.get(x):
            anagram = False
    return anagram

def anagrams2(stringA, stringB):
    anagram = False
    modified_stringA = ''.join(filter(str.isalnum, stringA)).lower()
    modified_stringB = ''.join(filter(str.isalnum, stringB)).lower()
    sorted_charactersA = sorted(modified_stringA)
    sorted_charactersB = sorted(modified_stringB)
    a_string = "".join(sorted_charactersA)
    b_string = "".join(sorted_charactersB)
    if a_string == b_string:
        anagram = True

    return anagram

def main():
    print("Compare strings and check if anagram")
    string1 = str(input("Input first string:"))
    string2 = str(input("Input second string:"))
    is_anagram = anagrams2(string1, string2)
    if(is_anagram) == True:
        print("It's an anagram!")
    else:
        print("It's not an anagram :c")

main()

