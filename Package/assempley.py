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
         pass                
      def CreateFile(self,**kwargs) :
          with open (self.argr.exploit,'rt') as FileAssepley:
                FileAssepley =FileAssepley.read()
                self.file1 = str(FileNameObject+".obj")
                self.file2 = str(FileNameObject+".dump")
                self.file3 = str(FileNameObject+"_shellcode")
                self.file4 = str(FileNameObject+".Linker")                         
      def LINKER_ASSEMBLY(self,**kwargs):
             subprocess.call(['ld','-n','-o','{}'.format(self.file4),'{}'.format(self.file1)],stderr=PIPE)
             with open(self.file2,'w')as file:                 
                stdout =  subprocess.call(['objdump','-d','{}'.format(self.file1)], stdout=file,stderr=PIPE)                   
      def replace(self,**kwargs):
              with open(self.file2,"r") as file:
                        read = file.read()  
              findall= str(re.findall(":....................\D",read))   
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
              with open(self.file3,'w')as file: 
                     file.write(Header) 
              with open (self.file3,'r')as test:
                      self.test= test.read()
if __name__=="__main__": 
       ShellDump()
        

