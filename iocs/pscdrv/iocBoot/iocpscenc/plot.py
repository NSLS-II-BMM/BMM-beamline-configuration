import pylab
import matplotlib.pyplot as plt 
import datetime
import os
import sys

#file_path = sys.argv[1][8:].split(',')[0]
file_path = sys.argv[1]

if os.path.isfile(file_path):
	data = pylab.loadtxt(file_path, dtype=int)
else:
	print file_path + ': no such file'
	sys.exit(0) 

date = []
i = 0
for (c1,c2) in zip(data[:,0], data[:,1]):
	sec = datetime.datetime.fromtimestamp(c1)
	try:
	        nsec = sec.replace(microsecond=int(c2//1000.0))
	except:
		print "nsec failed at " + str(c2)
        date.append(nsec)
plt.plot(date, data[:,2], '-', drawstyle='steps')

plt.show()
