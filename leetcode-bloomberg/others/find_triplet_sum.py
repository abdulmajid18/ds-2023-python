# A simple Python 3 program
# to find three elements whose
# sum is equal to zero

# Prints all triplets in
# arr[] with 0 sum


def findTriplets(arr, n):
    found = False
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if arr[i] + arr[j] + arr[k] == 0:
                    print(arr[i], arr[j], arr[k])
                    found = True

    # If no triplet with 0 sum
    # found in array
    if found == False:
        print(" not exist ")


# Driver code
arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)


# Python3 program to find triplets
# in a given array whose sum is zero

# function to print triplets with 0 sum


def findTriplets(arr, n):
    found = False
    for i in range(n - 1):

        # Find all pairs with sum
        # equals to "-arr[i]"
        s = set()
        for j in range(i + 1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                found = True
            else:
                s.add(arr[j])
    if not found:
        print("No Triplet Found")


# Driver Code
arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)


# python program to find triplets in a given
# array whose sum is zero

# function to print triplets with 0 sum


def findTriplets(arr, n):
    found = False

    # sort array elements
    arr.sort()

    for i in range(0, n - 1):

        # initialize left and right
        l = i + 1
        r = n - 1
        x = arr[i]
        while (l < r):

            if x + arr[l] + arr[r] == 0:
                # print elements if it's sum is zero
                print(x, arr[l], arr[r])
                l += 1
                r -= 1
                found = True

            # If sum of three elements is less
            # than zero then increment in left
            elif x + arr[l] + arr[r] < 0:
                l += 1

            # if sum is greater than zero then
            # decrement in right side
            else:
                r -= 1

    if (found == False):
        print(" No Triplet Found")


# Driven source
arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)
