#!/usr/bin/env python3

import re
import os
import time 
import sys
import shutil
import subprocess  
import argparse
import pathlib
from subprocess import  PIPE

class ShellDump:
        def __init__(self):      
            self.CreateFile()  
            self.LINKER_ASSEMBLY()
            self.ReplaceText()           
        def CreateFile(self,**kwargs) :
            self.FileAssepley = shutil.copy(os.getcwd()+'/Package/Template/assempley.asm',os.getcwd()+'/Package/Template/FileObjectDump.asm')
            FileDictionary = {  'File1': "FileNameObject.obj",
                                'File2': "FileNameObject.dump",
                                'File3': "FileNameObject_Shellcode",
                                'File4': "FileNameObject.Linker"    
                            }                
            for NameKey , NameValue in FileDictionary.items():
                with open(os.getcwd()+'/Package/Template/'+NameValue,'w') as NameKey :
                    continue  
            self.File1 = os.getcwd()+'/Package/Template/'+FileDictionary['File1'] 
            self.File2 = os.getcwd()+'/Package/Template/'+FileDictionary['File2'] 
            self.File3 = os.getcwd()+'/Package/Template/'+FileDictionary['File3'] 
            self.File4 = os.getcwd()+'/Package/Template/'+FileDictionary['File4']              
        def LINKER_ASSEMBLY(self,**kwargs):
            try:
                code = subprocess.call(['nasm','-f','elf32',"{}".format(self.FileAssepley),'-o','{}'.format(self.File1)],stderr=PIPE)
            except Exception :    
                code = subprocess.call(['nasm','-f','elf64',"{}".format(self.FileAssepley),'-o','{}'.format(self.File1)],stderr=PIPE) 
            subprocess.call(['ld','-n','-o','{}'.format(self.File4),'{}'.format(self.File1)],stderr=PIPE)
            with open(self.File2,'w')as file:                 
                stdout =  subprocess.call(['objdump','-d','{}'.format(self.File1)], stdout=file,stderr=PIPE)                   
        def ReplaceText(self,**kwargs):
                with open(self.File2,"r") as file:
                        read = file.read()  
                findall= "".join(str(re.findall(":....................\D",read))) 
                Header = findall.replace(":","")
                Header = Header.replace("   ",'')
                Header = Header.replace("\\s","") 
                Header = Header.replace("\\t","")
                Header = Header.replace(",","")
                Header = Header.replace("' '","") 
                Header = Header.replace(" ","")
                Header = Header.replace("[","")
                Header = Header.replace("]","")
                Header = Header.replace("'","")            
                Header= "".join("\\x%s"%Header[i:i+2] for i in range(0, len(Header), 2))
                Header= "".join('\n"%s"'%Header[i:i+56] for i in range(0, len(Header),56))   
                with open(self.File3,'w')as file: 
                     file.write(Header) 
                with open (self.File3,'r')as test:
                      self.test= test.read()
if __name__=="__main__": 
       ShellDump()
        

