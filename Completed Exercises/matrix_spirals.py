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
    counter = 1
    start_column = 0
    end_column = n-1
    start_row = 0
    end_row = n-1
    x=0
    # N Subarrays with default value of 0 [[0,0,0,...,0],[],...,[]]
    while x<n:
        results.append([0]*n)
        
        x+=1

    while (start_column <= end_column) and (start_row <= end_row):
        # Fill first row
        for i in range(start_column,end_column+1):
            results[start_row][i] = counter
            counter+=1
        start_row+=1
        # Fill right column
        for j in range(start_row, end_row+1):
            results[j][end_column] = counter
            counter +=1
        end_column -=1
        # Fill bottom row
        for k in range(end_column, start_column-1,-1):
            results[end_row][k] = counter
            counter+=1
        end_row-=1
        # Fill left side (1rst column)
        for l in range(end_row, start_row-1,-1):
            results[l][start_column] = counter
            counter+=1
        start_column+=1
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