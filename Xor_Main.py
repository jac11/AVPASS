#!/usr/bin/env python

import argparse
import sys
from Package.ErrorPrint import ErrorPrint
class Main_Proecess:
 
    def __init__(self):

        self._arg_Parse()
        self._Call_Code()

    def _Call_Code(self):
        try:
            ErrorPrint.CheckArgs(self,args=self._arg_Parse)
            if self.args.exploit and not self.args.assembly:

                from Package.MSF_GET import _MSF_Call
                _MSF_Call._Features(self,args1=self._arg_Parse)

                if self.args.load:
                    from Package.RandomVar import RandomVar
                    RandomVar.RandomVarCreate(self)  
                    RandomVar.RandomName(self,argsN=self._arg_Parse) 

                from Package.MSF_GET import Xor_class
                Xor_class.Gen_Key(self,args1=self._arg_Parse)
                Xor_class.Xor_Process(self,args1=self._arg_Parse)
                Xor_class.Fainal_Stage(self,args1=self._arg_Parse)
              

            elif self.args.assembly and self.args.exploit:

                from Package.assembly import ShellDump
                ShellDump.CreateFile(self,args=self._arg_Parse)
                ShellDump.LINKER_ASSEMBLY(self,args=self._arg_Parse)
                ShellDump.ReplaceText(self,args=self._arg_Parse)

                from Package.MSF_GET import _MSF_Call
                _MSF_Call._Features(self,args1=self._arg_Parse)

                if self.args.load:
                   from Package.RandomVar import RandomVar
                   RandomVar.RandomVarCreate(self)  
                   RandomVar.RandomName(self,argsN=self._arg_Parse)  

                from Package.MSF_GET import Xor_class
                Xor_class.Gen_Key(self,args1=self._arg_Parse)
                Xor_class.Xor_Process(self,args1=self._arg_Parse)
                Xor_class.Fainal_Stage(self,args1=self._arg_Parse)
            ErrorPrint.INFO(self,args=self._arg_Parse)
        except Exception as ErrorCommand:
            self.ErrorCommand  = ErrorCommand        
            ErrorPrint.Error(self,args=self.ErrorCommand)         
      
    def _arg_Parse(self):

        parser = argparse.ArgumentParser(description="Usage: [OPtion] [arguments] [ -w ] [arguments]")       
        parser.add_argument("-E","--exploit"    , action=None ,required=True,help ="Specify the Payload to be encrypted") 
        parser.add_argument("-B","--Key_base64" , action='store_true' ,default=False,help ="Use base64 encoding key value for encryption")  
        parser.add_argument("-b","--P_base64"   , action='store_true' ,default=False,help ="Use base64 encoding for the Payload Before decryption")      
        parser.add_argument("-O","--output"     ,action=None          ,required=True,help ="Specify the output file for the encrypted Payload") 
        parser.add_argument("-L","--load"       , action='store_true' ,required=False,help ="Specify the output file for the encrypted Payload")
        parser.add_argument('-A',"--assembly"   , action='store_true' ,help ="  file has assembly code  ")
        parser.add_argument('-D',"--decode"   , action='store_true' ,help ="  file has assembly code  ")

        self.args = parser.parse_args()       

        if len(sys.argv)!=1 :
            pass
        else:
            parser.print_help()         
            exit()    
if __name__=='__main__':
    Main_Proecess()