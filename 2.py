def multiplication(x, y):
    if y==0:
        return 0
    return x + multiplication(x, y-1)

def main():
    x=int(input("Enter x : "))
    y=int(input("Enter y : "))
    multi = multiplication(x, y)
    print(f'{x} * {y} = {multi}')

if __name__=='__main__':
    main()