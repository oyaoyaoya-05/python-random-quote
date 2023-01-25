import numpy as np
import matplotlib.pyplot as plt

a = float(input('enter the value of rate of progration a :'))
n = int(input('enter number of divisions :'))
h = 1/n
x = []
name = 0
xpoints = np.arange(0,1,h)


########################## inital conditions ################################

def inital_cond1():

	for i in range(n):
		
		j = 0
		x.append(i*h)
	
			 	
		if x[i] >0 and x[i] <= 0.2:
	
			u[j][i] = 1	
				#print(u)
			ypoints.append(u[j][i])
		
		else:
			
			u[j][i] = 0
			ypoints.append(u[j][i])
				
	
	inital_cond1.y = ypoints
	
	return(u)

def inital_cond2():
	
	for i in range(n):
		
		j = 0
		x.append(i*h)
			
		if x[i] < 0.05:
	
			u[j][i] = 0
			ypoints.append(u[j][i])
		
		elif x[i] < 0.35: 
	
			u[j][i] = np.sin(4*np.pi*((x[i]-0.05)/0.3))
			#print(u[i][j],'1')
			ypoints.append(u[j][i])
	
		else:
			u[j][i] = 0
			ypoints.append(u[j][i])
		
	inital_cond2.y = ypoints
	
	return(u)
		
def inital_cond3():
	
	for i in range(n):
		
		j = 0
		x.append(i*h)
		#print(x[i][j])
	
	
		if x[i] < 0.05:
	
			u[j][i] = 0
			ypoints.append(u[j][i])
		
		elif x[i] < 0.35: 
	
			u[j][i] = np.sin(8*np.pi*((x[i]-0.05)/0.3))
			#print(u[i][j],'1')
			ypoints.append(u[j][i])
	
		else:
			u[j][i] = 0
			ypoints.append(u[j][i])
	
	inital_cond3.y = ypoints
		
	return(u)
		
def inital_cond4():
	
	for i in range(n):
		
		j = 0
		x.append(i*h)
		#print(x[i][j])
	
	
		if x[i] < 0.05:
	
			u[j][i] = 0
			ypoints.append(u[j][i])
		
		elif x[i] < 0.35: 
	
			u[j][i] = np.sin(12*np.pi*((x[i]-0.05)/0.3))
			#print(u[i][j],'1')
			ypoints.append(u[j][i])
	
		else:
			u[j][i] = 0
			ypoints.append(u[j][i])
	
	inital_cond4.y = ypoints
	
	return(u)

def inital_cond5():
	
	for i in range(n):
		
		j = 0
		x.append(i*h)
		#print(x[i][j])
	
	
		if x[i] < 0.05:
	
			u[j][i] = 0
			ypoints.append(u[j][i])
		
		elif x[i] < 0.35: 
	
			u[j][i] = np.exp(-50*((x[i]-0.2)**2/0.4**2))
			#print(u[i][j],'1')
			ypoints.append(u[j][i])
	
		else:
			u[j][i] = 0
			ypoints.append(u[j][i])
	
	inital_cond5.y = ypoints
	
	return(u)

#######################################################################################################################

####################################### schemes ##########################################################
def FTFS():

	delta_t = 0
	file = open('FTFS_cond{0:d}_{1:.2f}.csv'.format(condition,mu),'w')
	file.write('FTFS scheme'+'\n')
	file.close()
	
	for j in range(0,n-1):
		
		delta_t = delta_t + step
		if delta_t >0.35:
			print('here',delta_t)
			break
		
		file = open('FTFS_cond{0:d}_{1:.2f}.csv'.format(condition,mu),'a')
		
		file.write('\n'+'time :'+'\t'+ str(delta_t) + '\n')
		
		
		file.close()
		ypoints = []
		u[j][0] = 0
		u[j][n-1] = 0
		ypoints.append(u[j][n-1])
		ypoints.append(u[j][0])
		
		for i in range(1,n-1):
			
			if delta_t <0.35:
			
				u[j+1][i] = u[j][i] - mu*(u[j][i+1] - u[j][i])
				
				file = open('FTFS_cond{0:d}_{1:.2f}.csv'.format(condition,mu),'a')
				file.write(str(u[j+1][i]) + ' ')
				file.close()
				ypoints.append(u[j+1][i])
				

	FTFS.y = ypoints
	FTFS.u = u			
	return(u)
	

def FTCS():
	delta_t = 0
	file = open('FTCS_cond{0:d}_{1:.2f}.csv'.format(condition,mu),'w')
	file.write('FTCS scheme'+'\n')
	file.close()
	for j in range(0,n-1):
		
		delta_t = delta_t + step
		if delta_t >0.35:
			
			break
		
		file = open('FTCS_cond{0:d}_{1:.2f}.csv'.format(condition,mu),'a')
		file.write('\n'+'time:'+'\t'+ str(delta_t) + '\n')
		file.close()
		ypoints = []
		u[j][0] = 0
		u[j][n-1] = 0
		ypoints.append(u[j][n-1])
		ypoints.append(u[j][0])
		
		for i in range(1,n-1):
			
			if delta_t <0.35:
			
				u[j+1][i] = u[j][i] - (mu/2)*(u[j][i+1] - u[j][i-1])
				ypoints.append(u[j+1][i])
				file = open('FTCS_cond{0:d}_{1:.2f}.csv'.format(condition,mu),'a')
				file.write( str(u[j+1][i]) + ' ')
				file.close()
			
			
	
	FTCS.y = ypoints
	FTCS.u = u				
	return()
	
def FTBS():

	delta_t = 0
	file = open('FTBS_cond{0:d}_{1:.2f}.csv'.format(condition,mu),'w')
	file.write('FTBS scheme'+'\n')
	file.close()
	
	for j in range(0,n-1):
		
		delta_t = delta_t + step
		if delta_t >0.35:
			
			break
			
		file = open('FTBS_cond{0:d}_{1:.2f}.csv'.format(condition,mu)'a')
		file.write('\n'+'time:'+'\t'+ str(delta_t) + '\n')
		file.close()
		ypoints = []
		u[j][0] = 0
		ypoints.append(u[j][0])
		
		for i in range(1,n):
			
			if delta_t <0.35:
			
				u[j+1][i] = u[j][i] - mu*(u[j][i] - u[j][i-1])
				file = open('FTBS_cond{0:d}_{1:.2f}.csv'.format(condition,mu),'a')
				file.write( str(u[j+1][i]) + ' ')
				file.close()
				ypoints.append(u[j+1][i])
			
	FTBS.y = ypoints
	FTBS.u = u				
	return()
	
def LW():
	delta_t = 0
	file = open('LW_cond{0:d}_{1:.2f}.csv'.format(condition,mu),'w')
	file.write('LW scheme'+'\n')
	file.close()
	
	for j in range(0,n-1):
		
		delta_t = delta_t + step
		if delta_t >0.35:
			
			break
		
		file = open('LW_cond{0:d}_{1:.2f}.csv'.format(condition,mu)'a')
		file.write('\n'+'time:'+'\t'+ str(delta_t) + '\n')
		file.close()
		ypoints = []
		u[j][0] = 0
		u[j][n-1] = 0
		ypoints.append(u[j][n-1])
		ypoints.append(u[j][0])
		
		for i in range(1,n-1):
			
			if delta_t <0.35:
			
				u[j+1][i] = u[j][i] - (mu/2)*(u[j][i+1] - u[j][i-1]) + (mu**2/2)*(u[j][i+1] - 2*u[j][i] + u[j][i-1])
				file = open('LW_cond{0:d}_{1:.2f}.csv'.format(condition,mu),'a')
				file.write(str(u[j+1][i]) + ' ')
				file.close()
				ypoints.append(u[j+1][i])
			
		
	
	LW.y = ypoints		
	return()
		
def BW():

	delta_t = 0
	file = open('BW_cond{0:d}_{1:.2f}.csv'.format(condition,mu),'w')
	file.write('BW scheme'+'\n')
	file.close()
	
	for j in range(0,n-1):
		
		delta_t = delta_t + step
		if delta_t >0.35:
			
			break
			
		file = open('BW_cond{0:d}_{1:.2f}.csv'.format(condition,mu),'a')
		file.write('\n'+'time:'+'\t'+ str(delta_t) + '\n')
		file.close()
		ypoints = []
		u[j][0] = 0
		u[j][1] = 0
		u[j][n-1] = 0
		u[j][n-2] = 0
		ypoints.append(u[j][n-1])
		ypoints.append(u[j][n-2])
		ypoints.append(u[j][0])
		ypoints.append(u[j][1])
		
		for i in range(2,n-2):
			
			if delta_t <0.35:
			
				u[j+1][i] = u[j][i] - (mu*0.5)*(3*u[j][i] - 4*u[j][i-1] + u[j][i-2]) + (mu**2*0.5)*(u[j][i] - 2*u[j][i-1] + u[j][i-2])
				file = open('BW_cond{0:d}_{1:.2f}.csv'.format(condition,mu),'a')
				file.write(str(u[j+1][i]) + ' ')
				file.close()
				ypoints.append(u[j+1][i])
			
		
	

	BW.y = ypoints	
	BW.u = u		
			
	return()


def FR():
	
	delta_t = 0
	file = open('FR_cond{0:d}_{1:.2f}.csv'format(condition,mu),'w')
	file.write('FR scheme'+'\n')
	file.close()
	
	for j in range(0,n-1):
		
		delta_t = delta_t + step
		if delta_t >0.35:
			
			break
			
		file = open('FR_cond{0:d}_{1:.2f}.csv'format(condition,mu),'a')
		file.write('\n'+'time :'+'\t'+ str(delta_t) + '\n')
		file.close()
		ypoints = []
		u[j][0] = 0
		u[j][1] = 0
		u[j][n-1] = 0
		u[j][n-2] = 0
		ypoints.append(u[j][n-1])
		ypoints.append(u[j][n-2])
		ypoints.append(u[j][0])
		ypoints.append(u[j][1])
		
		for i in range(2,n-2):
			
			if delta_t <0.35:
				u_lw = u[j][i] - (mu*0.5)*(u[j][i+1] - u[j][i-1]) + (mu**2*0.5)*(u[j][i+1] - 2*u[j][i] + u[j][i-1])
				
				u_bw = u[j][i] - (mu/2)*(3*u[j][i] - 4*u[j][i-1] + u[j][i-2]) + (mu**2/2)*(u[j][i] - 2*u[j][i-1] + u[j][i-2])
				
				u[j+1][i] = 0.5*(u_lw + u_bw)
				file = open('FR_cond{0:d}_{1:.2f}.csv'format(condition,mu),'a')
				file.write(str(u[j+1][i]) + ' ')
				file.close()
				ypoints.append(u[j+1][i])
			
			
	
	FR.y = ypoints			
	return()

#########################################################################
while True:
	
	print('select inital condition')
	condition = int(input('enter number from 1 to 5 :'))
	
	mu = (input('enter the CFL number : '))
	if len(mu)<1:break
	mu = float(mu)
	u = [[0]*n for i in range(n)]
	step = mu * h/(a)
	if condition == 1:
		ypoints = []
		inital_cond1()
		plt.figure(name)
		plt.ylim([-1.5,1.5])
		plt.title('inital')
		plt.plot(xpoints,inital_cond1.y)
		plt.savefig("{0:d}_{1:.2f}.png".format(condition,mu))
	
	if condition == 2:
		ypoints = []
		inital_cond2()
		plt.figure(name)
		plt.ylim([-1.5,1.5])
		plt.title('inital')
		plt.plot(xpoints,inital_cond2.y)
		plt.savefig("{0:d}_{1:.2f}.png".format(condition,mu))

	if condition == 3:
		ypoints = []
		inital_cond3()
		plt.figure(name)
		plt.ylim([-1.5,1.5])
		plt.title('inital')
		plt.plot(xpoints,inital_cond3.y)
		plt.savefig("{0:d}_{1:.2f}.png".format(condition,mu))	

	if condition == 4:
		ypoints = []
		inital_cond4()
		plt.figure(name)
		plt.ylim([-1.5,1.5])
		plt.title('inital')
		plt.plot(xpoints,inital_cond4.y)
		plt.savefig("{0:d}_{1:.2f}.png".format(condition,mu))

	if condition == 5:
		ypoints = []
		inital_cond5()
		plt.figure(name)
		plt.ylim([-1.5,1.5])
		plt.title('inital')
		plt.plot(xpoints,inital_cond5.y)
		plt.savefig("{0:d}_{1:.2f}.png".format(condition,mu))
	
	FTFS()
	FTCS()
	FTBS()
	LW()
	BW()
	FR()

	plt.figure(name+1)
	plt.ylim([-1.5,1.5])
	plt.title('FTBS')
	plt.plot(xpoints,FTBS.y)
	plt.savefig("FTBS_cond{0:d}_{1:.2f}.png".format(condition,mu))

	plt.figure(name+2)
	plt.ylim([-1.5,1.5])
	plt.title('FTCS')
	plt.plot(xpoints,FTCS.y)
	plt.savefig("FTCS_cond{0:d}_{1:.2f}.png".format(condition,mu))

	plt.figure(name+3)
	plt.ylim([-1.5,1.5])
	plt.title('LW')
	plt.plot(xpoints,LW.y)
	plt.savefig("LW_cond{0:d}_{1:.2f}.png".format(condition,mu))

	plt.figure(name+4)
	plt.ylim([-1.5,1.5])
	plt.title('BW')
	plt.plot(xpoints,BW.y)
	plt.savefig("BW_cond{0:d}_{1:.2f}.png".format(condition,mu))

	plt.figure(name+5)
	plt.ylim([-1.5,1.5])
	plt.title('FR')
	plt.plot(xpoints,FR.y)
	plt.savefig("FR_cond{0:d}_{1:.2f}.png".format(condition,mu))
	
	plt.figure(name+6)
	plt.ylim([-1.5,1.5])
	plt.title('FTFS')
	plt.plot(xpoints,FTBS.y)
	plt.savefig("FTFS_cond{0:d}_{1:.2f}.png".format(condition,mu))
	
	name = name+7






