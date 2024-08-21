n=int(input("n ni kiriting="))
fac=1
fac2=1*2
S=fac+fac2
newfac=fac2
for i in range(3, n+1):
    newfac=newfac*i
    S+=newfac;
print(n," faktorial",S," ga teng!")
