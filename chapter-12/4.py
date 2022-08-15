def findMax(lst, index):
    if index==len(lst)-1:
        return lst[index]
    elem=lst[index]
    maxInLaterHalf = findMax(lst, index+1)
    return elem if (elem > maxInLaterHalf) else maxInLaterHalf

def main():
    lst=[]
    n=int(input("Enter n: "))
    for x in range(n):
        lst.append(int(input()))
    max=findMax(lst,0)
    print(f'maximum element in {lst} is {max}')


if __name__=='__main__':
    main()