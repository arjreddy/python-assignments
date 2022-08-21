# Calculates sum of first n natural numbers and returns it.
def getSum(n):
    if n<=0:
        return 0
    return n + getSum(n-1)

def main():
    n = int(input('Enter an integer number: '))
    # call function to find sum of first n natural numbers.
    sum = getSum(n)
    print(f'Sum of first {n} natural numbers is {sum}')

if __name__=='__main__':
    main()
