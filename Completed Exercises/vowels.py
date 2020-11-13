# --- Directions
# Write a function that returns the number of vowels
# used in a string.  Vowels are the characters 'a', 'e'
# 'i', 'o', and 'u'.
# --- Examples
#   vowels('Hi There!') --> 3
#   vowels('Why do you ask?') --> 4
#   vowels('Why?') --> 0

def vowels(string):
    number_of_vowels = 0
    vowels = ["a","e","i","o","u"]
    modified_string = ''.join(filter(str.isalnum, string)).lower()
    for element in modified_string:
        if element in vowels:
            number_of_vowels +=1 
    return number_of_vowels

def main():
    print("Check for number of vowels")
    string = str(input("Input string:"))
    n_vowels = vowels(string)
    print("Number of vowels:",n_vowels)
main()