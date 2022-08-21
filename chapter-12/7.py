# calculates n power e and returns it.
def power(n, e):
    if e==0:
        return 1
    return n * power(n, e-1)

def main():
    n = int(input("enter a number: "))
    pow = int(input("enter an exponent: "))
    ans = power(n, pow)
    print(f'{n} ^ {pow} = {ans}')

if __name__=='__main__':
    main()
