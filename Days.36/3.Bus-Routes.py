# Bus Routes
'''
You have given bus number as indexes and bus stops as list
src,dest--> source and destination
we have to take minimum number of buses for reaching dest from src
if we don't find any route return -1
'''
from collections import deque

def BusRoutes(n,src,dest,routes):
    busstops={}
    for i in range(n):
        for val in routes[i]:
            if val in busstops:
                busstops[val].append(i)
            else:
                busstops[val]=[i]
    buses=set()
    stops=set()
    dq=deque()
    dq.append(src)
    level=-1
    stops.add(src)
    while dq:
        size=len(dq)
        level+=1
        for _ in range(size):
            u=dq.popleft()
            if u==dest:
                return level
            for bus in busstops[u]:
                if bus not in buses:
                    buses.add(bus)
                    for stop in routes[bus]:
                        if stop not in stops:
                            stops.add(stop)
                            dq.append(stop)
    return -1
                    



def main():
    n=int(input())
    routes=[]
    for i in range(n):
        routes.append(list(map(int,input().split())))
    src,dest=map(int,input().split())
    ans=BusRoutes(n,src,dest,routes)
    print(ans)



if __name__=='__main__':
    main()