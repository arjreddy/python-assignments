# prints range from 1 to num.
def printRange(num):
    if num==0:
        return;
    printRange(num-1)
    print(num)

def main():
    num=int(input('Enter a number: '))
    print("Range from 1 to ",num," is:")
    printRange(num)
    
if __name__=='__main__':
    main()
