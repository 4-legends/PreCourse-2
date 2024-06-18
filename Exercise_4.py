# Python program for implementation of MergeSort 
def merge(arr, left, right, mid):
    arr_size1 = mid - left + 1
    arr_size2 = right - mid
    left_arr = [0] * arr_size1
    right_arr = [0] * arr_size2

    for i in range(0, arr_size1):
        left_arr[i] = arr[left + i]
    
    for i in range(0, arr_size2):
        right_arr[i] = arr[mid + i + 1]
    
    sorted_index_left = 0  # Initial index of first sub-array
    sorted_index_right = 0  # Initial index of second sub-array
    merged_array_index = left  # Initial index of merged array

    # Merge the temp arrays back into array[left..right]
    while sorted_index_left < arr_size1 and sorted_index_right < arr_size2:
        if left_arr[sorted_index_left] <= right_arr[sorted_index_right]:
            arr[merged_array_index] = left_arr[sorted_index_left]
            sorted_index_left += 1
        else:
            arr[merged_array_index] = right_arr[sorted_index_right]
            sorted_index_right += 1
        merged_array_index += 1

    # Copy the remaining elements of left[], if any
    while sorted_index_left < arr_size1:
        arr[merged_array_index] = left_arr[sorted_index_left]
        sorted_index_left += 1
        merged_array_index += 1

    # Copy the remaining elements of right[], if any
    while sorted_index_right < arr_size2:
        arr[merged_array_index] = right_arr[sorted_index_right]
        sorted_index_right += 1
        merged_array_index += 1

def mergeSort(arr, left, right):
    if left >= right:
        return 
    mid = left + (right - left) // 2
    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)
    merge(arr, left, right, mid)


# Code to print the list 
def printList(arr): 
    for element in arr:
        print(element)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 300, 13, 5, 6, 7]
    left = 0
    right = len(arr) - 1  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, left, right) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
