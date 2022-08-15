def printRange(num):
    if num==0:
        return;
    printRange(num-1)
    print(num)

def main():
    num=int(input('Enter a number: '))
    printRange(num)
    
if __name__=='__main__':
    main()
