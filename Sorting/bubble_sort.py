"""
Bubble Sort Algorithm
"""

def bubble_sort(arr:list[int]) -> list[int]:
    """
    Function to perform bubble sort on an unsorted list of integers.

    Arguments
    ---------
        arr (list[int]): Unsorted list of integers.

    Returns
    -------
        Sorted list of integers.
    """
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped is False:
            break

    return arr

if __name__ == "__main__":
    list_of_integers = [5, 2, 7, 1, 3, 8, 4]
    print(f"Sorted Array = {bubble_sort(arr=list_of_integers)}")