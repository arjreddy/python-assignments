# Returns multiplication of two integers.
def multiplication(x, y):
    if y==0:
        return 0
    return x + multiplication(x, y-1)

def main():
    x=int(input("Enter first integer number : "))
    y=int(input("Enter second integer number : "))
    # Call to multiplication function.
    multi = multiplication(x, y)
    print(f'Multiplication of two numbers is: {x} * {y} = {multi}')

if __name__=='__main__':
    main()
