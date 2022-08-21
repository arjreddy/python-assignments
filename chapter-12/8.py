# The ackermann function.
def ackermann(m,n):
    if (m<0) or (n<0):
        raise Exception('Exceeds recursion limit')
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))

def main():
    print("ackermann function")
    n = int(input("Enter first number: "))
    m = int(input("Enter second number: "))
    try:

       ans = ackermann(m,n)
       print(f'ackermann({m},{n}) = {ans}')
    except Exception as error:
        print("Error occurred: ", error.args)
      

if __name__=='__main__':
    main()
