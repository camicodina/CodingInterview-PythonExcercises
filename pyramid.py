# --- Directions
# Write a function that accepts a positive number N.
# The function should console log a pyramid shape
# with N levels using the # character.  Make sure the
# pyramid has spaces on both the left *and* right hand sides
# --- Examples
#   pyramid(1)
#       '#'
#   pyramid(2)
#       ' # '
#       '###'
#   pyramid(3)
#       '  #  '
#       ' ### '
#       '#####'

def pyramid(n):
    list_of_numbers = []
    # Your code here
    return list_of_numbers
    

def main():
    print("Pyramid")
    number = int(input("Input a positive number:"))
    if number >0:
        print_em = pyramid(number)
        for x in print_em:
            print(x)
    else:
        print("Error")
main()