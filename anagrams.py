# --- Directions
# Check to see if two provided strings are anagrams of eachother.
# One string is an anagram of another if it uses the same characters
# in the same quantity. Only consider characters, not spaces
# or punctuation.  Consider capital letters to be the same as lower case
# --- Examples
#   anagrams('rail safety', 'fairy tales') --> True
#   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
#   anagrams('Hi there', 'Bye there') --> False

def anagrams(stringA, stringB):
    anagram = True
    # Your code here
    return anagram

def main():
    print("Compare strings and check if anagram")
    string1 = str(input("Input first string:"))
    string2 = str(input("Input second string:"))
    is_anagram = anagrams(string1, string2)
    if(is_anagram) == True:
        print("It's an anagram!")
    else:
        print("It's not an anagram :c")

main()

