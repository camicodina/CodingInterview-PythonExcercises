# --- Directions
# Write a program that console logs the numbers
# from 1 to n. But for multiples of three print
# “fizz” instead of the number and for the multiples
# of five print “buzz”. For numbers which are multiples
# of both three and five print “fizzbuzz”.
# --- Example
#   fizzBuzz(5);
#   1
#   2
#   fizz
#   4
#   buzz

def fizzbuzz(n):
    list_of_numbers = []
    i = 1
    while (i<=n):
        if(i%3 == 0 and i%5 == 0):
            list_of_numbers.append("fizzbuzz")
        elif(i%3 == 0):
            list_of_numbers.append("fizz")
        elif(i%5 == 0):
            list_of_numbers.append("buzz")
        else:
            list_of_numbers.append(i)
        i+=1
    return list_of_numbers
    

def main():
    print("Fizzbuzz!")
    number = int(input("Input a number:"))
    print_em = fizzbuzz(number)
    print("The List of Natural Numbers from 1 to {} are".format(number))
    for x in print_em:
        print(x)

main()