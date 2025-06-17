def resta (*nums:float)->float:# funcion resta
    res=nums[0]
    for valor in nums:
        res-=valor
    return res

def suma (*nums:float)->float:# funcion de suma de n catidades de numeros
    res=0
    for valor in nums:
        res+=valor
    return res

def mult (*nums:float)->float: #funcion multiplicacion
    res=0
    for valor in nums:
        res*=valor
    return res

def div (n1:float,n2:float)->float:# funcion div y residuo
    res=n1/n2
    sobra=n2%n2
    return res, sobra
