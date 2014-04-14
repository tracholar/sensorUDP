import socket
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from math import sqrt
import time
import thread

address = (socket.gethostbyname(socket.gethostname()),9999)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

print address[0],'listen at port',address[1]

fig, ax = plt.subplots()
X = np.arange(0,1,0.001)
Y1 = np.zeros(len(X))
Y2 = np.zeros(len(X))
Y3 = np.zeros(len(X))
Y4 = np.zeros(len(X))
line1,line2,line3,line4, = ax.plot(X,Y1,'r',X,Y2,'g',X,Y3,'b',X,Y4,'k')
plt.ylim(-20,20)
N = len(X)

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
			if int(float(tmp[i]))== 82 and i<len(tmp)-3:
				#y = sqrt(float(tmp[i+1])*float(tmp[i+1])+float(tmp[i+2])*float(tmp[i+2])+float(tmp[i+3])*float(tmp[i+3]))
				y = float(tmp[i+1])
				Y1[0:N-1] = Y1[1:N]
				Y2[0:N-1] = Y2[1:N]
				Y3[0:N-1] = Y3[1:N]
				Y4[0:N-1] = Y4[1:N]
				Y1[-1] = float(tmp[i+1])
				Y2[-1] = float(tmp[i+2])
				Y3[-1] = float(tmp[i+3])
				Y4[-1] = sqrt(Y1[-1]**2+Y2[-1]**2+Y3[-1]**2)
				#print y
				#time.sleep(1)
				#print float(tmp[i+1]),float(tmp[i+2]),float(tmp[i+3])
		
		
		#print Y1,Y2,Y3


thread.start_new_thread(timer,())


def animate(i):
	
	line1.set_ydata(Y1)
	line2.set_ydata(Y2)
	line3.set_ydata(Y3)
	line4.set_ydata(Y4)
	return line1,line2,line3,line4,
def init():
	mY = np.ma.array(X, mask = True)
	line1.set_ydata(mY)
	line2.set_ydata(mY)
	line3.set_ydata(mY)
	line4.set_ydata(mY)
	return line1,line2,line3,line4,

ani = animation.FuncAnimation(fig, animate, init_func=init,
	interval=20, blit=True)
plt.show()

s.close()

