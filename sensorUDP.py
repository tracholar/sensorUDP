import socket
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from math import sqrt
import time
import thread

address = ('192.168.199.217',9999)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

print address[0],'listen at port',address[1]

fig, ax = plt.subplots()
X = np.arange(0,1,0.01)
Y1 = np.zeros(len(X))
Y2 = np.zeros(len(X))
Y3 = np.zeros(len(X))
line1,line2,line3, = ax.plot(X,Y1,'r',X,Y2,'g',X,Y3,'b')
plt.ylim(-30,30)


def timer():
	while True:
		data, addr = s.recvfrom(2048)
		if not data:
			print "client has exist"
			return line1,line2,line3,
		
		#print data
		tmp = data.split(',')
		#print tmp
		#print sqrt(float(tmp[2])*float(tmp[2])+float(tmp[3])*float(tmp[3])+float(tmp[4])*float(tmp[4]))
		
		for i in range(0,len(tmp)):
			if int(float(tmp[i]))== 3 and i<len(tmp)-3:
				#y = sqrt(float(tmp[i+1])*float(tmp[i+1])+float(tmp[i+2])*float(tmp[i+2])+float(tmp[i+3])*float(tmp[i+3]))
				y = float(tmp[i+1])
				Y1[0:99] = Y1[1:100]
				Y2[0:99] = Y2[1:100]
				Y3[0:99] = Y3[1:100]
				Y1[-1] = float(tmp[i+1])
				Y2[-1] = float(tmp[i+2])
				Y3[-1] = float(tmp[i+3])
				print float(tmp[i+1]),float(tmp[i+2]),float(tmp[i+3])
		
		
		#print Y1,Y2,Y3


thread.start_new_thread(timer,())


def animate(i):
	
	line1.set_ydata(Y1)
	line2.set_ydata(Y2)
	line3.set_ydata(Y3)
	return line1,line2,line3,
def init():
	line1.set_ydata(Y1)
	line2.set_ydata(Y2)
	line3.set_ydata(Y3)
	return line1,line2,line3,

ani = animation.FuncAnimation(fig, animate, init_func=init,
	interval=50, blit=True)
plt.show()

while True:
	data, addr = s.recvfrom(2048)
	if not data:
		print "client has exist"
		break
	
	#tmp = data.split(',')
	print data
	#print sqrt(float(tmp[2])*float(tmp[2])+float(tmp[3])*float(tmp[3])+float(tmp[4])*float(tmp[4]))
	

	#y = sqrt(float(tmp[2])*float(tmp[2])+float(tmp[3])*float(tmp[3])+float(tmp[4])*float(tmp[4]))
	
	#Y[0:len(Y)-2] = Y[1:len(Y)-1]
	#Y[-1] = y
	#print y
	#line.set_xdata(X)
	#line.set_ydata(Y)
	#draw()
	#time.sleep(5)
s.close()

