def make_list():
    z = []
    for x in range(1,4):
            z = z + [get_input()]
    print(z)

def get_input():
    num = int(input('please enter a number'))
    return num

if __name__ == '__main__':
    make_list()
