import wx
import wx.xrc
import struct
import serial
import time
import binascii
from xmodem import XMODEM

RET_SUCCESS     = '0'
RET_IVLD_SIZE   = '1'
RET_IVLD_ADDR   = '2'
RET_IVLD_CMD    = '3'
RET_NO_PRIV     = '4'
RET_IVLD_PARAM  = '5'
RET_READ_LOCK   = '6'
RET_WRITE_LOCK  = '7' 
RET_RESET       = '8'


class W7500_ISP_CMD(object):
    def __init__(self, comP, baud, parent, timeoutValue):
        self.ser = serial.Serial(comP, baud, timeout = timeoutValue)
        self.parent = parent

    def serialClose(self):
        self.ser.close()
    def __del__(self):
        self.serialClose()
        
    def negoComP(self):
        recv = ""
        #while True:
        for cnt in range(0,10):
            if recv == 0x00:
                continue
            elif recv == 'U':
                return 0;
            else:
                self.ser.write('U')
                recv = self.ser.read()
                for c in recv:
                    str = "Recv : {0:x}".format(ord(c))
                    print str
                    self.parent.m_statusBar_W7500_Status.SetStatusText(str)
                    #print "Recv : %04X" % ord(c)

                #time.sleep(0.2)
                print self.ser.readline()
                
        return -1
        
    def writeCmd(self,cmd,resp="0",paramLine=1,loopCnt=3):
        cmd = cmd + '\r'
        resp = resp + '\r\n'
        
        message = "Send Command : " + cmd
        print message
        #print "Send Command : %s" % cmd
        #self.parent.m_statusBar_W7500_Status.SetStatusText(message)

        self.ser.write(cmd)
        tempData =""
        
        for i in range(loopCnt):
            respData = self.ser.readline()
            if(i == paramLine -1):
                tempData = respData
            
            message = "Resp : " + respData
            print message
            #self.parent.m_statusBar_W7500_Status.SetStatusText(message)
            #print "Resp : %s" % respData,

            #if(respData[:1] == resp[:1]):
            if(respData == resp):
                break

        print("")
        return tempData

    def Dump(self,filename, addr,size,loopCnt=3, progressDialog=-1):
        cmd = "DUMP" + " " + addr + " " + size + '\r' 
        resp_val = []
        
        print "Send Command : %s" % cmd
        self.ser.write(cmd)
        
        f = open(filename,"wb")
        
        for i in range(loopCnt+1):
            respData = self.ser.readline()
            binary = binascii.a2b_hex(respData[9:17])
            progressDialog.Update(i)
            f.write(binary)

        f.close()
        
        respData = self.ser.readline()
        print respData
        
        return 0 

    
    def getc(self,size,timeout=1):
        return self.ser.read(size)
    def putc(self,data,timeout=1):
        return self.ser.write(data)
    
    def Xmodem_init(self):
        self.xmodem = XMODEM(self.getc,self.putc)
    def Xmodem_Send(self,start_addr,size,file_path,CallBack):
        cmd = "XPRG " + start_addr + " " + size + "\r"
        self.ser.write(cmd)
        stream = open(file_path,'rb')
        print "Start Send Binary using XMODEM"
        self.xmodem.send(stream,16,60,0,CallBack)
        stream.close()
 
        print self.ser.readall()
        print "End XMODEM"



if __name__ == "__main__":

    binary = []
    string = '00000000:01112233'
    
    #binary.append(binascii.a2b_hex(string[9:17]))
    print string[9:11]
    print string[11:13]
    print string[13:15]
    
    for cnt in range(len(binary)):
        print cnt
        print binary[cnt]
    
    contents = struct.unpack('<I',binary)[0]
    num = "%08X" % contents
    
    print num


#     
#     isp = W7500_ISP_CMD('COM12', 115200, 0.2)
#     isp.negoComP()
#     isp.writeCmd("","3")
#     #resp = isp.writeCmd("LOCK PROG 00000000 00000000")
#     #isp.Dump('dump.bin','00000000', '00020000', 32768)
#     
#     f = open('test.txt',"wb")
# 
#     #resp = isp.writeCmd("DUMP 00000000 00000004")
#     cmd = "DUMP 00000000 00000004" + "\r"
#     print "Send Command : %s" % cmd
# 
#     isp.ser.write(cmd)
# 
#     resp = isp.ser.readline()
#     print resp
# 
# #     binary = binascii.a2b_hex("00000000")
# #     f.write(binary)
#     f.close()
