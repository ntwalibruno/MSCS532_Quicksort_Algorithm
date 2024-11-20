import random

#Deterministic quicksort
def Quicksort(array):
    def quicksort(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            quicksort(array, low, pi - 1)  
            quicksort(array, pi + 1, high)  

    def partition(array, low, high):
        pivot = array[high]
        i = low - 1  

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]  

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1  

    quicksort(array, 0, len(array) - 1)
    
    return array


def is_array_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
        
    return True

if __name__ == "__main__":
    arr = [random.randint(1, 20) for _ in range(20)]

    print("Original array:", arr)
    print("Sorted:", is_array_sorted(arr))

    Quicksort(arr)
    print("\n")

    print("Sorted array:",arr)
    print("Sorted:", is_array_sorted(arr))