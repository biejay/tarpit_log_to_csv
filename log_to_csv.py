from subprocess import Popen
import os
path=os.getcwd()+"/"
outputfile="tarpit.csv"
inputfile="tarpit.log"
with open(path+inputfile, "r+") as f:
     data = f.read().split("\n")
     outf=open(path+outputfile,"w")
     outf.write("datetime;ip;port;status;\n")
     for x in data:
         datetime=x[:x.find("INFO")-1]
         ip=x[x.find(" ('")+3:x.find("',")]
         port=x[x.find("', ")+3:x.find(") ")]
         if " disconnected" in x:
             status="disconnected"
         elif " connected" in x:
             status="connected"
         else:             
             continue
         outf.write(datetime+";"+ip+";"+port+";"+status+";\n")
     f.close()
     outf.close()
     print(inputfile+" >>> "+outputfile)
     print(str(len(data))+" Rows converted")
