
def findSumRec(lst, n):
    if n==0:
        return 0
    return lst[n-1] + findSumRec(lst, n-1)

def main():
    lst=[]
    n=int(input("Enter n: "))
    for x in range(n):
        lst.append(int(input()))
    sum = findSumRec(lst, len(lst))
    print(f'sum of {lst} is {sum}')

if __name__=='__main__':
    main()