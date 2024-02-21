#!/usr/bin/env python
import os
import time                                                                          
class ErrorPrint:
    def __init__(self):
        self.Error()
        self.Print()
    def Error(self,**kwargs):
        with open ('Package/Template/rr.txt','r') as r :
            print(r.read())
        if "No such file or directory" in str(self.ErrorCommand):
            print("⚠️  No such file or directory : "+str(self.ErrorCommand).split(':')[1].replace('/','',1) )
    def INFO(self,**kwargs):
        with open ('Package/Template/rr.txt','r') as r :
            print(r.read())   
        if self.args.exploit:
            time.sleep(.20)
            print("🏗️  ReadPayload      :--------------:  "+self.args.exploit)  
        if self.args.P_base64:
            time.sleep(.20)
            print('🥣️ Encode_Paylaod   :--------------:  base64')
        if self.args.Key_base64 :
            time.sleep(.20)
            print('🎁️ Encode_Key       :--------------:  base64') 
        if self.args.load:
            time.sleep(.20)
            print("🧲️ Load HOladr      :--------------:  PythonCode")
        if self.args.decode:
            time.sleep(.20)
            print("🐚️ ENCode_ShellCode :--------------:  XOR_ENCode")
        if self.args.assembly:
            time.sleep(.20)
            print("🎰️ Read assembly    :--------------:  "+self.args.exploit.split('/')[-1])
        if self.args.output:    
            time.sleep(.20)
            print('🐞️ File OutPut      :--------------:  '+'file://'+os.getcwd()+"/"+'StoreCode'+'/')  
        ListFileDelete = [ 'Package/Template/FileNameObject.dump',
                           'Package/Template/FileNameObjectShellCode',
                           'Package/Template/FileObjectDump.asm',
                           'Package/Template/ShellCode.txt',
                           'Package/Template/TempPayloadLoader.txt',
                         ]
        for File in ListFileDelete :
            if  os.path.exists(File):
                os.remove(File)
   
if __name__=='__main__':
   ErrorPrint() 
