#!/usr/bin/env python

import os
import shutil
import string
import random
import fileinput

class RandomVar:
    def __init__(self):

        self.RandomVarCreate()
        self.RandomName()   

    def RandomVarCreate(self,**kwargs):

        LenStr = 14
        self.ListVar = []
        for _ in range(19):
            Var =''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for _ in range(LenStr))
            self.ListVar.append(Var)   
        if self.args.load:    
            with open (os.getcwd()+'/Package/Template/ShellCode.txt','rt') as ExploitRename:
                self.ExploitRename = ExploitRename.read().replace('ShellCode','_'+self.ListVar[15])
            with open (os.getcwd()+'/Package/Template/ShellCode.txt','wt') as FulNameShell :
                FulNameShellCode = FulNameShell.write(self.ExploitRename)      
    def RandomName(self,**kwargs): 

        CopyShellHolder = shutil.copy(os.getcwd()+'/Package/Template/TempPayload.txt',os.getcwd()+'/Package/Template/TempPayloadLoader.txt')
        FShellHplder = os.getcwd()+'/Package/Template/TempPayloadLoader.txt'
        for line in fileinput.FileInput(FShellHplder,inplace=1):
            if 'class' in line:
                line.replace('():','').replace('class ','')
                line = line.replace(line,'class '+'c'+self.ListVar[0]+' '+ '() :\n')
            elif '_1()' in line:
                line = line.replace(line,'   c'+self.ListVar[0]+'()') 
            elif '_2' in line:
                line = line.replace('_2','_'+self.ListVar[1])  
            elif '_3' in line :
               line = line.replace('_3','_'+self.ListVar[2])
            elif '_4' in line :
                line = line.replace('_4','_'+self.ListVar[3])  
            elif '_5' in line :
                line = line.replace('_5','_'+self.ListVar[4])   
            elif '_6' in line :
                line = line.replace('_6','_'+self.ListVar[5])     
            elif '_7' in line :
                line = line.replace('_7','_'+self.ListVar[6])   
            elif '_8' in line :
                line = line.replace('_8','_'+self.ListVar[7])   
            elif '_9' in line :
                line = line.replace('_9','_'+self.ListVar[8])       
            elif '_10' in line :
                line = line.replace('_10','_'+self.ListVar[9]) 
            elif '_11' in line :
                line = line.replace('_11','_'+self.ListVar[10]) 
            elif '_12' in line :
                line = line.replace('_12','_'+self.ListVar[11])
            elif '_13' in line :
                line = line.replace('_13','_'+self.ListVar[12]) 
            elif '_14' in line :
                line = line.replace('_14','_'+self.ListVar[13]) 
            elif '_15' in line :
                line = line.replace('_15','_'+self.ListVar[14]) 
            elif '_16' in line :
                line = line.replace('_16','_'+self.ListVar[15]) 
            print(line,end=''),  
        for line in fileinput.FileInput(FShellHplder,inplace=1):
            if '_16' in line :
                line = line.replace('_16','_'+self.ListVar[15]) 
            if '_17' in line :
                line = line.replace('_17','_'+self.ListVar[16])
            if '_18' in line :
                line = line.replace('_18','_'+self.ListVar[17])        
            print(line,end=''),
        for line in fileinput.FileInput(FShellHplder,inplace=1):
            if '_13' in line :
                line = line.replace('_13','_'+self.ListVar[12])
            if 'def __init__(self):' in line:
               line = line.replace('def __init__(self):','def __init__(self,'+'_'+self.ListVar[15]+'='+'_'+self.ListVar[15]+'):')       
            print(line,end=''),          
        Pattern = '_'+self.ListVar[15]+'  =   b""'    
        with open( os.getcwd()+'/Package/Template/TempPayloadLoader.txt','rt') as CopyShell:
            CopyShell = CopyShell.read().replace(Pattern,self.ExploitRename)
        with open( os.getcwd()+'/Package/Template/TempPayloadLoader.txt','wt') as ReCopyShell:
            ReCopyShell.write(CopyShell)
if __name__=='__main__':
    RandomVar()