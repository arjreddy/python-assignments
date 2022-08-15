def power(n, e):
    if e==0:
        return 1
    return n * power(n, e-1)

def main():
    n = int(input("enter n: "))
    pow = int(input("enter pow: "))
    ans = power(n, pow)
    print(f'{n} ^ {pow} = {ans}')

if __name__=='__main__':
    main()