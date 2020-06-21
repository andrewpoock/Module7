def list():
    x = [65, 18, 22, 14, 34]
    print(search_list(x))
    print(sort_list(x))


def sort_list(x):
    return x.sort() #included return so I can print the sorted list from the main list function


def search_list(x):
    try:
        index = x.index(14)
        return 'The index of 14:', index
    except:
        return -1


if __name__ == '__main__':
    list()
