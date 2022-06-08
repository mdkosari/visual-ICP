import sys
sys.path.insert(0,'lib')
import dataio
import icp
import out


def ShowListFile(directory):
    
    li=dataio.ShowListFile(directory)
    

def GetFileName(directory='input/ready'):
    out.Message("\t\t .......... List Converted Your Files ...........")
    if not dataio.ShowListFile(directory):
        out.Error("\t\t\t\t\t\t[404] File Not Found In Folder('input/redy')")
        out.Error("\t\t\t\t\t\t[!!!] Pleas Create File By Convert Function")
        return False
    out.Message("\t\t...............................")
    out.Message("\t\t Input Source And Target Files Points")
    out.Warning("\t\t For Example => mk1mov.txt mk1fix.txt'")
    out.MessageBlank("\t\t\t\t Enter Your File")
    inp=input('\t\t\t\t\t')
    inp=inp.split(' ')
    return inp

def convertData(addressFile):
    dataio.ConvertData(addressFile)
    
def Start(addressDirect='input/ready'):
    inp = GetFileName(addressDirect)
    out.Message("\t\t[/] Starting Calculations...")
    icp.start(addressDirect+'/'+inp[0], addressDirect+'/'+inp[1])
