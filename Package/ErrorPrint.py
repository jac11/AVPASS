#!/usr/bin/env python
import os
import time    
R,W='\033[31m','\033[0m'                                                                   
class ErrorPrint:
    def __init__(self):
        self.CheckArgs()
        self.Error()
        self.Print()
    def CheckArgs(self,**kwargs):
        with open (self.args.exploit,'rt') as Check:
             Check = Check.read()
        if ('\\x' not in Check  and 'eax' not in Check ) and (self.args.load or self.args.decode ) :
            with open ('Package/Template/Banner.txt','r') as r :
                print(R+r.read()+W)   
            print("🚑️ argument Error      :--------------:  Look like raw data" )
            time.sleep(.20)
            print("💡️ Explain             :--------------:  shellcode '\\Xxx' can function with the '--load' option in a Python holder shellcode")
            exit()
        elif ('edi' and 'eax 'and 'push' in Check) and not (self.args.assembly)  :
            with open ('Package/Template/Banner.txt','r') as r :
                print(R+r.read()+W) 
            print("🚑️ argument Error    :--------------:  Payload File Look Like assembly code" )
            time.sleep(.20)
            print("💡️ Explain           :--------------:  with assembly Code with option --assembly or -A ")
            exit()
        elif ('edi' and 'eax 'and 'push' in Check and self.args.assembly) and not (self.args.load) :
            with open ('Package/Template/Banner.txt','r') as r :
                print(R+r.read()+W) 
            print("🚑️ argument Error    :--------------:  Payload File Look Like assembly code" )
            time.sleep(.20)
            print("💡️ Explain           :--------------:  with assembly Use option --load or -L to Hoald the shellcode ")
            exit()  
        elif ('\\x' not in Check  and 'eax' not in Check ) and (self.args.assembly or self.args.load or self.args.decode ) :
            with open ('Package/Template/Banner.txt','r') as r :
                print(R+r.read()+W)   
            print("🚑️ argument Error      :--------------:  look like raw Payload  " )
            time.sleep(.20)
            print("💡️ Explain             :--------------:  with raw data use -B -b or --P_base64 --Key_base64")
            exit()      
    def Error(self,**kwargs):
        with open ('Package/Template/Banner.txt','r') as r :
            print(R+r.read()+W)
        if "No such file or directory" in str(self.ErrorCommand):
            time.sleep(.20)
            print("⚠️  No such file or directory    :--------------:   " +str(self.ErrorCommand).split(':')[1].replace('/','',1) )
        else:
            time.sleep(.20)
            print('⚠️  argument Error   :--------------:   ' +str(self.ErrorCommand))    
    def INFO(self,**kwargs):
        with open ('Package/Template/Banner.txt','r') as r :
            print(R+r.read()+W)   
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
#        -E -B -b -A -L -D -O
#        -E -B -b -L -D -O
#        -E -B -b -L -O
#        -E -B -b -O
#        -E -O
#        -E -b -O
#        -E -B -O
