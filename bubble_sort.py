# https://www.geeksforgeeks.org/python-program-for-bubble-sort/

def bubbleSort(arr):
    n = len(arr)
<<<<<<< HEAD

    for i in range(n):
        for j in range(0, n-i-1):

    # Traverse through all array elements
=======
>>>>>>> 2db0858 (Fix! Strip bubbleSort comments)
    for i in range(n):
        for j in range(0, n-i-1):
<<<<<<< HEAD

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element

=======
>>>>>>> 2db0858 (Fix! Strip bubbleSort comments)
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
