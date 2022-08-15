def getSum(n):
    if n<=0:
        return 0
    return n + getSum(n-1)

def main():
    n = int(input('Enter n: '))
    sum = getSum(n)
    print(f'Sum of first {n} natural numbers is {sum}')

if __name__=='__main__':
    main()