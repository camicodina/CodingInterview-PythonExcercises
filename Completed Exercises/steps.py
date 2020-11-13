# --- Directions
# Write a function that accepts a positive number N.
# The function should console log a step shape
# with N levels using the # character.  Make sure the
# step has spaces on the right hand side!
# --- Examples
#   steps(2)
#       '# '
#       '##'
#   steps(3)
#       '#  '
#       '## '
#       '###'
#   steps(4)
#       '#   '
#       '##  '
#       '### '
#       '####'


def steps(n):
    list_of_numbers = []
    i = 1
    while (i<=n):
        list_of_numbers.append("#"*i+"_"*(n-i))
        i+=1
    return list_of_numbers
    

def main():
    print("Steps")
    number = int(input("Input a positive number:"))
    if number >0:
        print_em = steps(number)
        for x in print_em:
            print(x)
    else:
        print("Error")
    
main()