import array as arr


def yeah():
    x = arr.array('i', [2, 4, 1, 3])
    print(search(x))
    sort(x)


def sort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
    print(arr)
    return arr  # included return so I can print the sorted list from the main list function


def search(x):
    try:
        index = x.index(4)
        return ('The index of 14 is ' + str(index))
    except:
        return -1


if __name__ == '__main__':
    yeah()
