"""
Quick Sort Algorithm
"""

def partition(arr:list[int], low:int, high:int) -> int:
    """
    Function to partition the given list of integers based on the given index of pivot.

    Arguments
    ---------
        arr (list[int]): Unsorted list of integers.
        low (int): Index of smaller element compared to pivot.
        high (int): Index of pivot.

    Returns
    -------
        Index of new pivot after partition
    """

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr:list[int], low:int, high:int) -> None:
    """
    Function to perform quick sort on an unsorted list of integers.

    Arguments
    ---------
        arr (list[int]): Unsorted list of integers.
        low (int): Starting index of left partition.
        high (int): Ending index of right partition.

    Returns
    -------
        None
    """

    if low < high:
        pi = partition(arr=arr, low=low, high=high)

        quick_sort(arr=arr, low=low, high=pi - 1)
        quick_sort(arr=arr, low=pi + 1, high=high)



if __name__ == "__main__":
    list_of_integers = [5, 2, 7, 1, 3, 8, 4]
    quick_sort(arr=list_of_integers, low=0, high=len(list_of_integers) - 1)
    print(f"Sorted Array = {list_of_integers}")