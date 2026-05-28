from typing import List


def isSorted(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False

    return True


class BubbleSort:
    def sort(arr: List[int]) -> None:
        pass


class SelectionSort:
    def sort(arr: List[int]) -> None:
        pass


class InsertionSort:
    def sort(arr: List[int]) -> None:
        pass


class MergeSort:
    def sort(arr: List[int]) -> None:
        pass

    def merge(arr1, arr2):
        pass


class QuickSort:
    def sort(self, arr: List[int]) -> None:
        """Sorts input array using quicksort algorithm

        Args:
            arr (List[int]): Input array to be sorted
        """
        p = self.partition(arr, 0, len(arr)-1)
        self._sort(arr, 0, p-1)
        self._sort(arr, p+1, len(arr)-1)

    def _sort(self, arr: List[int], left: int, right: int):
        """Private recursive sort method to hide bound parameters from interface.

        Args:
            arr (List[int]): Input array of integers to be sorted
            left (int): Start bound (inclusive) of arr to be sorted
            right (int): End bound (inclusive) of arr to be sorted
        """
        if left >= right:
            return

        p = self.partition(arr, left, right)

        self._sort(arr, left, p-1)
        self._sort(arr, p+1, right)

    def partition(self, arr: List[int], left: int, right: int) -> int:
        """Picks an arbitrary pivot value. After execution, all values to the left of this pivot value will be less than or equal to the pivot. All values to the right of the pivot will be greater than the pivot.

        Args:
            arr (List[int]): Array of values to be sorted
            left (int): Start bound (inclusive) of arr to be sorted
            right (int): End bound (inclusive) of arr to be sorted

        Returns:
            int: Sorted index position of the arbitrary pivot
        """
        pivot = arr[right]
        bound = left-1
        for i in range(left, right+1):
            if arr[i] <= pivot:  # put the elementon the left of the pivot boundary
                bound += 1
                arr[i], arr[bound] = arr[bound], arr[i]
        print(arr, bound)
        return bound


def main():
    arr = [5, 1, 10, 9, 6, 3, 2, 4, 8]
    print(sorted(arr))
    QuickSort().sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
