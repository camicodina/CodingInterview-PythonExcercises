# --- Directions
# Given an integer, return an integer that is the reverse
# ordering of numbers.
# --- Examples
#   reverseInt(15) === 51
#   reverseInt(981) === 189
#   reverseInt(500) === 5
#   reverseInt(-15) === -51
#   reverseInt(-90) === -9


def reverse_int(n):
    positive = False
    negative = False
    zero = False
    str_number = str(n)
    reversed = ""

    sign = 1 if n < 0 else 0
    if sign == 1:
        negative = True
    else: #n>=0
        positive = True
    
    if zero == True:
        return n
     
    if positive == True:
        reversed = str_number[::-1]

    if negative == True:
        without_sign = str_number.replace('-', '')
        reversed = "-" + without_sign[::-1]
        

    int_reversed = int(reversed)
    return int_reversed

def reverse_int_short(n):
    str_n = str(abs(n))
    reversed = str_n[::-1]
    sign = lambda x: -1 if x<0 else 1
    return int(reversed) * sign(n)
    

def main():
    number  = int(input("Input an integer to be reversed:"))
    reversed_input = reverse_int_short(number)
    print(number, "=", reversed_input)

main()