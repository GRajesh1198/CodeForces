try:
    #6->15,8->20,10->25
    t=int(input())
    for i in range(t):
        n=int(input())
        print(max(6,n+1)//2 * 5)
except:
    pass
