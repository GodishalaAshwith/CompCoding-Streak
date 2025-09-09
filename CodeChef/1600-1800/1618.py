# cook your dish here
for _ in range(int(input())):
    vertices,sources,sinks=map(int,input().split())
    common=sources+sinks-vertices
    if common>0:
        vertices=vertices-common
        sources=sources-common
        sinks=sinks-common
    a=vertices*(vertices-1)//2
    b=sources*(sources-1)//2
    c=sinks*(sinks-1)//2
    print(a-b-c)