import numpy as np
import os
import shutil

srcdir = "c:/test"
if os.path.exists("c:/test/output"):
   shutil.rmtree("c:/test/output")    #ɾ���ǿ��ļ���
srcfiles = os.listdir(srcdir)
output = "c:/test/output"
os.mkdir(output)

for srcfile in srcfiles:
    print srcfile
    os.chdir(srcdir)
    a = np.fromfile(srcfile,dtype="int16")
    a.shape= 4320,2160
    b =  np.transpose(a)
    os.chdir(output )
    b.tofile(srcfile)    
print "�������"
