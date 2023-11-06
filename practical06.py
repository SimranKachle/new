import random

def quicksort(arr):
    if len(arr)<=1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if pivot>=x]
    right = [x for x in arr[1:] if pivot <x]

    return quicksort(left)+[pivot]+quicksort(right)

def randomized_qs(arr):
    if len(arr) <= 1:
        return arr


    pivot_index = random.randint(0,len(arr)-1)

    pivot = arr[pivot_index]


    left = [x for x in arr[:pivot_index]+ arr[pivot_index+1:] if pivot >= x]
    right = [x for x in arr[:pivot_index]+ arr[pivot_index+1:] if pivot < x]

    return randomized_qs(left) + [pivot] + randomized_qs(right)


def analyze_quicksort(arr,variant="Deterministic"):
    if variant == "Deterministic":
        s=quicksort(arr)
    else:
        s=randomized_qs(arr)

    return s

def main():
    arr=[]

    n = int(input("Enter number of items: "))


    for i in range(n):
        element = int(input(f"Enter Element {i}: "))
        arr.append(element)

    print("original Array is : ",arr)

    sorted_array = analyze_quicksort(arr.copy(),variant="Deterministic")
    sorted_array2 = analyze_quicksort(arr.copy(), variant="randomized")

    print(sorted_array)
    print(sorted_array2)


if __name__ == "__main__":
    main()