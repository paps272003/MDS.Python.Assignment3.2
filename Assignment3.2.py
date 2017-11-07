x=[s for s in 'ACADGILD']
print(x)

x=[i*j for i in ['x','y','z'] for j in [1,2,3,4] ]
print(x)

x=[i*j for i in [1,2,3,4] for j in ['x','y','z'] ]
print(x)

x=[[j+y] for y in range(3) for j in range(2,5)]
print(x)

x=[[j+y,j+1+y,j+2+y,j+3+y] for y in range(1) for j in range(2,6)]
print(x)

x=[(y,x) for x in range(1,4) for y in range(1,4)]
print(x)