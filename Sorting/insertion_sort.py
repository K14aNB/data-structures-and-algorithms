"""
Insertion Sort Algorithm
"""

def insertion_sort(arr:list[int]) -> list[int]:
    """
    Function to perform Insertion sort on an unsorted list of integers.

    Arguments
    ---------
        arr (list[int]): Unsorted list of integers.

    Returns
    -------
        Sorted list of integers.
    """

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr


if __name__ == "__main__":
    list_of_integers = [5, 2, 7, 1, 3, 8, 4]
    print(f"Sorted Array = {insertion_sort(arr=list_of_integers)}")
