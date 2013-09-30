
'''
Created on 2012-5-21

@author: shd101wyy
'''
from sympy import solve,Symbol
def countNumber(elem,reac):
    length=len(elem)
    co=0
    index=reac.find(elem)
    while index+length-1<len(reac) and index!=-1:
        #if at the last positon
        if index+length==len(reac):
            co=co+1
        #no at the last position
        else:
            #behind is char
            #behind is lowercase
            if reac[index+length].islower():
                if length==1:
                    co=co+0
                if length==2:
                    print("error occured")
            #behind is upper
            elif reac[index+length].isupper():
                co=co+1
            #behind is digit:
            else:
                count=index+length
                number=''
                while count<len(reac):
                    #if it is not digit
                    if not reac[count].isdigit():
                        break
                    #else
                    if reac[count].isdigit():
                        number=number+reac[count]
                    count+=1
                if str(number).isdigit():
                    co=co+int(number)
        index=reac.find(elem,index+1)
    return co

def getContent(reac):
    content=[]
    contentDic={}
    indexOfL=reac.find('(')
    if indexOfL==-1:
        content.append('Has no ()')
    else:       
        content.append(reac[0:indexOfL])
        while indexOfL!=-1:
            indexOfR=reac.find(')',indexOfL)
            content.append(reac[indexOfL+1:indexOfR])
            indexOfL=reac.find('(',indexOfR)
            if indexOfL!=-1:
                content.append(reac[indexOfR+1:indexOfL])
        content.append(reac[indexOfR+1:])
    for i in range(1,len(content)):
        if content[i].isdigit():
            contentDic[str(content[i-1])]=int(content[i])
        else:
            contentDic[str(content[i-1])]=1  
    return contentDic

'''
    CaCO3 + HCl = CaCl2 + H2O + CO2
Ca    1    0        -1    0    0
C    1    0        0      0     -1
O    3    0        0     -1    -2
Cl    0    1        -2    0    0
     1    2      1        1        1
'''
def getSolution(element,matrix):
    sum=len(matrix[0])
    num=[0 for number in range(sum)]
    for i in range(sum):
        num[i]=Symbol('n'+str(i))
    #print num
    equation=[0 for i in range(len(element))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            equation[i]=equation[i]+num[j]*matrix[i][j]
    #print(equation)
    count=0
    solution=solve(equation,num)
    for elem in num:
        elemExisted=False
        for keys in solution:
            if elem==keys:
                elemExisted=True
        if not elemExisted:
            count+=1
            solution[elem]=elem
  #  print("Free variables %d"%(count))
  #  print(solution)
    for keys in solution:
        solution[keys]=str(solution[keys])
    solutionVector=[]
    for elem in num:
        solutionVector.append(solution[elem])
  #  print(solution)
 #   print(solutionVector)
    if count==1:
        solutionVector=simplifyTheSolution(solutionVector)
    else:
        print("infinate combinations")
    return solutionVector
'''           
n4/2  Cu  +  2*n4  HNO3   =  n4/2  Cu(NO3)2  +  n4  NO2  +  n4  H2O 
n4  MnO2  +  4*n4  HCl   =  n4  MnCl2  +  2*n4  H2O  +  n4  Cl2 
2*n4/3  Al  +  2*n4/3  NaOH   =  2*n4/3  NaAlO2  +  -2*n4/3  H2O  +  n4  H2 
'''
def simplifyTheSolution(solutionVector):
    p=[]    #numerator
    q=[]    #denominator
    solution=[]
    for elem in solutionVector:
        index=elem.find("/")
        if index==-1:
            q.append(1)
            indexOfX=elem.find("*")
            if indexOfX!=-1:
                p.append(int(elem[:indexOfX]))
            else:
                p.append(1)
        else:
            q.append(int(elem[index+1:]))
            indexOfX=elem.find("*")
            if indexOfX!=-1:
                p.append(int(elem[:indexOfX]))
            else:
                p.append(1)
    z=[]
  #  print(p)
  #  print(q)
    for elem in q:
        z.append(elem)
    z.sort(cmp=None, key=None, reverse=False)
    x=set()
    for elem in z:
        x.add(elem)
    z=[]
    for elem in x:
        z.append(elem)
  #  print 'After removing',
  #  print(z)
    needToBeRemoved=[]
    for elem in z:
        for elem2 in z:
            if elem2%elem==0 and elem!=1 and elem!=elem2:
                needToBeRemoved.append(elem)
    for elem in needToBeRemoved:
        z.remove(elem)
  #  print 'to count commonMulti',
  #  print z
    commonMul=1
    for elem in z:
        commonMul=commonMul*elem
    for i in range(len(q)):
        solution.append(str(commonMul*p[i]/q[i]))
    return solution
        
        
                    
            
        