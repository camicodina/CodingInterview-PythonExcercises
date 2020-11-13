# --- Directions
# Write a function that accepts an integer N
# and returns a NxN spiral matrix.
# --- Examples
#   matrix(2)
#     [[1, 2],
#     [4, 3]]
#   matrix(3)
#     [[1, 2, 3],
#     [8, 9, 4],
#     [7, 6, 5]]
#  matrix(4)
#     [[1,   2,  3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10,  9,  8, 7]]

def matrix(n):
    results = []
    # Your code here
    return results


def main():
    print("Matrix Spirals")
    number = int(input("Input a number:"))
    if number >0:
        print_em = matrix(number)
        for x in print_em:
            print(x)
    else:
        print("Error")
main()