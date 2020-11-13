# --- Directions
# Given a string, return a new string with the reversed
# order of characters
# --- Examples
#   reverse('apple') === 'elppa'
#   reverse('hello') === 'olleh'
#   reverse('Greetings!') === '!sgniteerG'

def reversal(string):
    list =[] 
    list[:0]=string 
    list = list[::-1]
    reversed = ''.join(list)
    return reversed

def reversal_s(string):
    return string[::-1]


def main():
    string  = str(input("Input a string to be reversed:"))
    reversed_string = reversal_s(string)
    print(reversed_string)

main()
