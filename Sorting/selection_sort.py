"""
Selection Sort Algorithm
"""

def selection_sort(arr:list[int]) -> list[int]:
    """
    Function to perform selection sort on an unsorted list of integers.

    Arguments
    ---------
        arr (list[int]): Unsorted list of integers.

    Returns
    -------
        Sorted list of integers.
    """

    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

if __name__ == "__main__":
    list_of_integers = [5, 2, 7, 1, 3, 8, 4]
    print(f"Sorted Array = {selection_sort(arr=list_of_integers)}")

