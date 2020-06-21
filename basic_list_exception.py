def make_list():
    z = []
    for x in range(1,4):
        y = get_input()
        if type(y) == str or type(y) == int and y >= 1 and y <= 50:
            z = z + [y]
            continue
        else: raise ValueError
    print(z)

def get_input():
    num = int(input('please enter a number'))
    return num

if __name__ == '__main__':
    make_list()
