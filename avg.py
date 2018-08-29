'''
Sampling Frequency of ~330 Hz
'''
import csv
import mmap
import os

## Defining averaging
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
## 'test.txt' is a placeholder file for data in time intervals
try:
	os.remove("test.txt")
except OSError: 
	pass
## Variable initialization
ti = []
f0 = []
f1 = []
f2 = []
f5 = []
f6 = []
f7 = []
######################################################################
## Deleting the last line of data since data may have been interrupted 
lines = file('data.txt', 'r').readlines() 
# del lines[-1]
file('test.txt','wx+').writelines(lines)
######################################################################

## fill the variables to average
with open("test.txt","r") as f:
    rows = csv.reader(f, delimiter=',')
    for row in rows:      
        ti.append(float(row[0]))
        f0.append(float(row[1]))
        f1.append(float(row[2]))
        f2.append(float(row[3]))
        f5.append(float(row[4]))
        f6.append(float(row[5]))
        f7.append(float(row[6]))
N=len(ti)

#print f0
#print mean(f0)
#print '%05.3f' % mean(f0)
avgt = str(mean(ti))
avgf0 = '%05.3f' % mean(f0)
avgf1 = '%05.3f' % mean(f1)
avgf2 = '%05.3f' % mean(f2)
avgf5 = '%05.3f' % mean(f5)
avgf6 = '%05.3f' % mean(f6)
avgf7 = '%05.3f' % mean(f7)

with open("memmap.txt", "wb") as a:
	a.write("%s\n" % avgf0)
	a.write("%s\n" % avgf1)
	a.write("%s\n" % avgf2)
	a.write("%s\n" % avgf5)
	a.write("%s\n" % avgf6)
	a.write("%s\n" % avgf7)
	a.write("%s" % avgt)
with open("memmap.txt", "r+b") as a:
    ## memory map the file
    mm = mmap.mmap(a.fileno(),0)
    mm[:5] = avgf0
    mm[6:11] = avgf1
    mm[12:17] = avgf2
    mm[18:23] = avgf5
    mm[24:29] = avgf6
    mm[30:35] = avgf7
    mm[36:] = avgt
    mm.close
	

with open("average.txt", "a+") as f:
    f.write("%s," % avgt)
    f.write("%s," % avgf0)
    f.write("%s," % avgf1)
    f.write("%s," % avgf2)
    f.write("%s," % avgf5)
    f.write("%s," % avgf6)
    f.write("%s\n" % avgf7)
