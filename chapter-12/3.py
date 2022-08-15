def printStars(n):
    if n==0:
        return
    printStars(n-1)
    for x in range(n):
        print('*', end="")
    print()
      
def main():
    n=int(input("Enter n: "))
    printStars(n)


if __name__=='__main__':
    main()