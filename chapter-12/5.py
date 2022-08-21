# calculates sum of all the elements in a list recursively and returns it.
def findSumRec(lst, n):
    if n==0:
        return 0
    return lst[n-1] + findSumRec(lst, n-1)

def main():
    lst=[]
    n=int(input("Enter a number: "))
     # prompt for n inputs.
    print("We will prompt you enter ",n, " numbers.")
    for x in range(n):
        lst.append(int(input("Enter a Number : ")))
    sum = findSumRec(lst, len(lst))
    print(f'sum of all the elements of {lst} is {sum}')

if __name__=='__main__':
    main()
