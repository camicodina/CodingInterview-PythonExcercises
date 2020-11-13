# --- Directions
# Given a string, return true if the string is a palindrome
# or false if it is not.  Palindromes are strings that
# form the same word if it is reversed. *Do* include spaces
# and punctuation in determining if the string is a palindrome.
# --- Examples:
#   palindrome("abba") === true
#   palindrome("abcdefg") === false

def palindrome(string):
    reversed = string[::-1]
    palindrome = False
    if (reversed == string):
        palindrome = True
    return palindrome


def palindrome2(string):
    #Issue: double comparison
    palindrome = False
    list_string =[] 
    list_string[:0]=string 
    i = 0
    for character in list_string:
        if(character == list_string[len(list_string)-i-1]):
            palindrome = True
        else:
            return palindrome
        i+=1
    return palindrome


def main():
    string  = str(input("Input a string to be reversed:"))
    is_palindrome = palindrome2(string)
    if is_palindrome == True:
        print("It's a palindrome!")
    else:
        print("It's not palindrome :/")

main()