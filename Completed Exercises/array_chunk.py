# --- Directions
# Given an array and chunk size, divide the array into many subarrays
# where each subarray is of length size
# --- Examples
# chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

def chunk(array, size):
    chunked_array = []
    for element in array:
        if chunked_array:
            last = chunked_array[len(chunked_array)-1]
            if not last or len(last)==size:
                chunked_array.append([element])
            else:
                last.append(element)
        else:
            chunked_array.append([element])
    return chunked_array

def chunk2(array,size):
    chunked_array = []
    i=0
    while i<len(array):
        chunked_array.append(array[i:i+size])
        i += size

    return chunked_array
    

def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    chunk_size = int(input("Input the size for the subarrays:"))
    print(chunk2(array, chunk_size))

main()