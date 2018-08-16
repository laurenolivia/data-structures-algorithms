#Write a program that implements Selection Sort on an array of numbers

#finds smallest val and stores index
def findSmallest(arr):
    min_num = arr[0]
    min_num_index = 0

    for i in range(1, len(arr)):
        if arr[i] < min_num:
            min_num = arr[i] 
            min_num_index = i

    return min_num_index

#sorts arr by finding next smallest val
def selectionSort(arr):
    newArr = []

    for i in range(len(arr)):
        min_num = findSmallest(arr)
        newArr.append(arr.pop(min_num))

    return newArr

