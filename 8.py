def ackermann(m,n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))

def main():
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    ans = ackermann(m,n)
    print(f'ackermann({m},{n}) = {ans}')

if __name__=='__main__':
    main()