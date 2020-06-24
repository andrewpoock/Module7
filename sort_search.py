def list():
    x = [2, 4, 1, 3]
    print(search_list(x))
    sort_list(x)


def sort_list(x):
    x.sort()
    print(x)
    return x #included return so I can print the sorted list from the main list function


def search_list(x):
    try:
        index = x.index(14)
        return ('The index of 14 is ' + str(index))
    except:
        return -1


if __name__ == '__main__':
    list()
