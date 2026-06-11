# Classic loop examples 

def triangle(height):

    for i in range(1,height+1):
        for j in range(i):
            print('*',end='')
        print()

def rectangle(side_a, side_b):
    for i in range(side_a):
        for j in range(side_b):
            print('*',end='')
        print()

def main():
    print('triangle: \n')
    triangle(5)
    print()
    print('rectangle: \n')
    rectangle(5,7)


main()