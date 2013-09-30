'''
Created on 2012-5-24

@author: shd101wyy
'''
import ChemicalEquationFunctions as func
class ChemicalEquation(object):
    '''
    classdocs
    '''
    def __init__(self,reactants=[],resultants=[]):
        '''
        Constructor
        '''
        self.reactants=reactants
        self.resultants=resultants
        self.element=[]
        self.reactantsNumber=len(reactants)
        self.resultantsNumber=len(resultants)
        
        def inputReactantsAndResultants():
            print("Please enter the " +
                        "number of reactants")
            self.reactantsNumber=int(raw_input())
            print("Please enter the number" +
                        "of resultants")
            self.resultantsNumber=int(raw_input())
            self.reactants=[0 for number in range(self.reactantsNumber)]
            self.resultants=[0 for number in range(self.resultantsNumber)];
            print("Please enter reactant")
            for i in range(self.reactantsNumber):
                self.reactants[i]=str(raw_input())
            print("Please enter resultant")
            for i in range(self.resultantsNumber):
                self.resultants[i]=str(raw_input())
            #print(self.reactants)
            #print(self.resultants)  
            
        def getElement():
            
            def deleteTheSameElementInArray():
            #   String elementFromArray;
            #  String elementFromArray2;
            #    print(self.element)
                elementSet=set()
                for elem in self.element:
                    elementSet.add(elem)
                self.element=[]
                for elem in elementSet:
                    self.element.append(elem)
                    
                        
            for i in range(self.reactantsNumber):
                if len(self.reactants[i])==1:
                    self.element.append(self.reactants[i])
                    continue
                for char in self.reactants[i]:
                    if char.isupper():
                        self.element.append(char)
                for j in range(len(self.reactants[i])-1):
                    if self.reactants[i][j+1].islower():
                        temp=self.reactants[i][j]+self.reactants[i][j+1]
                        self.element.remove(self.reactants[i][j])
                        self.element.append(temp)
 
            deleteTheSameElementInArray()   

        
        def makeEquation():
            self.matrix=[[0 for column in range(self.reactantsNumber+self.resultantsNumber)] for row in range(len(self.element))]
            for elem in self.element:
                for reac in self.reactants:
                    zkh=reac.find("(")
                    ykh=reac.find(")")
                    index=reac.find(elem)
                    if index==-1:
                        self.matrix[self.element.index(elem)][self.reactants.index(reac)]=0
                    else:
                        if zkh==-1:  #without ()
                            self.matrix[self.element.index(elem)][self.reactants.index(reac)]=func.countNumber(elem,reac)
                        else:        #with ()
                            content=func.getContent(reac)
                            co=0
                            for keys in content.keys():
                                if keys.find(elem)!=-1:
                                    co=co+func.countNumber(elem, keys)*content[keys]
                            self.matrix[self.element.index(elem)][self.reactants.index(reac)]=co
                

                for resul in self.resultants:
                    zkh=resul.find("(")
                    ykh=resul.find(")")
                    index=resul.find(elem)
                    if index==-1:
                        self.matrix[self.element.index(elem)][self.resultants.index(resul)+self.reactantsNumber]=0
                    else:
                        if zkh==-1:  #without ()
                            self.matrix[self.element.index(elem)][self.resultants.index(resul)+self.reactantsNumber]=-func.countNumber(elem,resul)
                        else:        #with ()
                            content=func.getContent(resul)
                            co=0
                            for keys in content.keys():
                                if keys.find(elem)!=-1:
                                    co=co+func.countNumber(elem, keys)*content[keys]
                            self.matrix[self.element.index(elem)][self.resultants.index(resul)+self.reactantsNumber]=-co
            
                       
        def getTheAnswer():
            self.solution=func.getSolution(self.element, self.matrix)
            
            
        
         
        def displayTheAnswer():
            count=1
            self.stringSolution=''
            for i in range(self.reactantsNumber):
                #print(self.solution[i]),
                self.stringSolution+=self.solution[i]
                #print(" "+self.reactants[i]+" "),
                self.stringSolution+=" "+self.reactants[i]+" "
                if count<self.reactantsNumber:
                    #print("+ "),
                    self.stringSolution+="+ "
                    count+=1
            #print(" = "),
            self.stringSolution+=" = "
            count=1;
            for i in range(self.resultantsNumber):
                #print(self.solution[i+self.reactantsNumber]),
                self.stringSolution+=self.solution[i+self.reactantsNumber]
                #print(" "+self.resultants[i]+" "),
                self.stringSolution+=" "+self.resultants[i]+" "
                if count<self.resultantsNumber:
                    #print("+ "),
                    self.stringSolution+="+ "
                    count+=1


        if self.resultants==[] or self.reactants==[]:
            inputReactantsAndResultants()


        getElement()
        makeEquation()
        getTheAnswer()
        displayTheAnswer()

    def getStringSolution(self):
        return self.stringSolution

# Normal Mode
'''
chem=ChemicalEquation()
print chem.getStringSolution()
'''

def Balance(input_str):
    index_of_eq = input_str.find("=")
    if index_of_eq==-1:
        print "Error"
        exit(0)
    reactants = input_str[0:index_of_eq]
    resultants = input_str[index_of_eq+1:]

    reactants = reactants.replace(" ","")
    resultants = resultants.replace(" ","")

    reactants = reactants.split("+")
    resultants = resultants.split("+")

    chem = ChemicalEquation(reactants, resultants)
    return chem.getStringSolution()
'''
This function above can be called directly

result = Balance('C+CO2=CO')

like that

'''




