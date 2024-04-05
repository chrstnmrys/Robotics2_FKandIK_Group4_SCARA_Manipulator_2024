from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import ImageTk, Image
import tkinter as tk
import numpy as np
import math
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import spatialmath
from spatialmath import SE3
import matplotlib
matplotlib.use('TkAgg')




cal = tk.Tk()
cal.resizable(False,False)
cal.geometry("800x700")
cal.title("")
pc = tk.PhotoImage(file="//home//bitsin/Documents//ROB2_3202//e.png")
blabel=tk.Label(cal,image=pc)
blabel.place(x=0,y=0, relwidth=1,relheight=1)
font = ('Times',35,'bold')
fonts = ('Times',25,'bold','italic')
fonty = ('Times',15,'bold')
fontf = ('Times',10,)

def reset():
	a1_E.delete(0, END)
	a2_E.delete(0, END)
	a3_E.delete(0, END)
	a4_E.delete(0, END)
	a5_E.delete(0, END)

	T1_E.delete(0, END)
	T2_E.delete(0, END)
	d3_E.delete(0, END)

	X_E.delete(0, END)
	Y_E.delete(0, END)
	Z_E.delete(0, END)

		

def f_k():
	# link lengths in cm
	a1 = float(a1_E.get())/100
	a2 = float(a2_E.get())/100
	a3 = float(a3_E.get())/100
	a4 = float(a4_E.get())/100
	a5 = float(a5_E.get())/100

	# joint variables: is cm if f, is degrees if theta
	T1 = float(T1_E.get())/100
	T2 = float(T2_E.get())/100
	d3 = float(d3_E.get())/100

	# degree to radian
	T1 = (T1/180.0)*np.pi
	T2 = (T2/180.0)*np.pi

	# Parametric Table (theta, alpha, r, d)
	PT = [[(0.0/180.0)*np.pi + T1,(0.0/180.0)*np.pi,a2,a1],
	      [(0.0/180.0)*np.pi + T2,(180.0/180.0)*np.pi,a4,a3],
	      [(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,0,a5+d3]]

	# HTM formulae
	i = 0
	H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
	        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
	        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
	        [0,0,0,1]]

	i = 1
	H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
	        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
	        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
	        [0,0,0,1]]
	
	i = 2
	H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
	        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
	        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
	        [0,0,0,1]]

	H0_1 = np.matrix(np.around(H0_1,3))
	H1_2 = np.matrix(np.around(H1_2,3))
	H2_3 = np.matrix(np.around(H2_3,3))

	H0_2 = np.dot(H0_1,H1_2)
	H0_3 = np.dot(H0_2,H2_3)

	X0_3 = H0_3[0,3]
	X_E.delete(0,END)
	X_E.insert(0,np.around(X0_3*100,3))

	Y0_3 = H0_3[1,3]
	Y_E.delete(0,END)
	Y_E.insert(0,np.around(Y0_3*100,3))

	Z0_3 = H0_3[2,3]
	Z_E.delete(0,END)
	Z_E.insert(0,np.around(Z0_3*100,3))

	#Create links
	# [robot_variable]=DHRobot([RevoluteDH(d,r,alpha,offset)])
	SCARA_Manipulator = DHRobot([
		RevoluteDH(a1,a2,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
		PrismaticDH(0,a2,0,0,qlim=[0,0]),
		RevoluteDH(a3,a4,(180.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
		PrismaticDH(0,a4,0,0,qlim=[0,0]),
		PrismaticDH(0,0,(0.0/180.0)*np.pi,a5+d3,qlim=[0,(30/100)])
	    ], name="SCARA_Manipulator")

	#plot joints
	q1 = np.array([T1,0,T2,0,d3])

	#plot scale
	x1 = -0.5
	x2 = 0.5
	y1 = -0.5
	y2 = 0.5
	z1 = 0.0
	z2 = 0.5

	HTM = LabelFrame(cal,text="H0_1")
	HTM.place(relx=0.2,rely=0.72,anchor='n')
	H1 = Label(HTM,text=H0_1,font=('Times,15'))
	H1.grid(row=0,column=0)

	HTM1= LabelFrame(cal,text="H1_2")
	HTM1.place(relx=0.5,rely=0.72,anchor='n')
	H2 = Label(HTM1,text=H1_2,font=('Times,15'))
	H2.grid(row=0,column=0)

	HTM2= LabelFrame(cal,text="H2_3")
	HTM2.place(relx=0.8,rely=0.72,anchor='n')
	H3 = Label(HTM2,text=H2_3,font=('Times,15'))
	H3.grid(row=0,column=0)
	

	#Plot command
	SCARA_Manipulator.plot(q1,limits=[x1,x2,y1,y2,z1,z2],block=True)

def i_k():
	#Inverse Kinematics Using Graphical Method

	#Link lengths in cm
	a1 = float(a1_E.get())
	a2 = float(a2_E.get())
	a3 = float(a3_E.get())
	a4 = float(a4_E.get())
	a5 = float(a5_E.get())
	
	#Position Vector in cm
	xe = float(X_E.get())
	ye = float(Y_E.get())
	ze = float(Z_E.get())

	# To solve for Theta 1 or Th1
	phi2 = np.arctan(ye/xe) #1
	r1 = np.around(np.sqrt(ye**2 + xe**2)) #2
	phi1 = np.arccos((a4**2 - r1**2 - a2**2)/(-2 * r1 * a2)) #3
	if (phi1 > phi2):
		Th1 = (phi1 - phi2) 
	else:
		Th1 = (phi2 - phi1)

	# To solve fot Theta 2 or Th2
	phi3 = np.arccos((r1**2 - a2**2 - a4**2)/(-2 * r1 * a2)) #5
	Th2 = np.pi - phi3 #6

	# To solve for D3
	D3 = a1 + a3 - a5 - ze #7

	T1_E.delete(0,END)
	T1_E.insert(0,np.around(Th1*180/np.pi,3))

	T2_E.delete(0,END)
	T2_E.insert(0,np.around(Th2*180/np.pi,3))

	d3_E.delete(0,END)
	d3_E.insert(0,np.around(D3,3))

	#Create links
	# [robot_variable]=DHRobot([RevoluteDH(d,r,alpha,offset)])
	SCARA_Manipulator = DHRobot([
		RevoluteDH(0,a2/100,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
		PrismaticDH(0,a2/100,0,0,qlim=[0,0]),
		RevoluteDH(0,a4/100,(180.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
		PrismaticDH(0,a4/100,0,0,qlim=[0,0]),
		PrismaticDH(a5/100,0,(0.0/180.0)*np.pi,qlim=[0,30/100])
		], name="SCARA_Manipulator")

	#plot joints
	q1 = np.array([Th1,0,Th2,0,D3/100])

	#plot scale
	x1 = -0.5
	x2 = 0.5
	y1 = -0.5
	y2 = 0.5
	z1 = 0.0
	z2 = 0.5

	#Plot command
	SCARA_Manipulator.plot(q1,limits=[x1,x2,y1,y2,z1,z2],block=True)
	
## Title and Sub
tl = Label(text= "SCARA MANIPULATOR", font = font,bg = "darkgray")
tl.place(relx=0.5,rely=0.05,anchor='n')
stl = Label(text="Forward and Inverse Kinematics Calculator", font= fonts ,bg="darkgray")
stl.place(relx=0.5,rely=0.11,anchor='n')

# Link Lengths
ll = Label(text= "Link Lengths",font=('Times',20,'italic'),bg="darkgray")
ll.place(relx=0.5,rely=0.6,anchor='n')

LL = LabelFrame(cal)
LL.place(relx=0.5,rely=0.31,anchor='n')

a1 = Label(LL,text=("a1 = "),font=fonty)
a1_E = Entry(LL,width=6,font=fonty)
cm1 = Label(LL,text=("cm"),font=fonty)
a1.grid(row=0,column=0)
a1_E.grid(row=0,column=1)
cm1.grid(row=0,column=2)

a2 = Label(LL,text=("a2 = "),font=fonty)
a2_E = Entry(LL,width=6,font=fonty)
cm2 = Label(LL,text=("cm"),font=fonty)
a2.grid(row=1,column=0)
a2_E.grid(row=1,column=1)
cm2.grid(row=1,column=2)

a3 = Label(LL,text=("a3 = "),font=fonty)
a3_E = Entry(LL,width=6,font=fonty)
cm3 = Label(LL,text=("cm"),font=fonty)
a3.grid(row=2,column=0)
a3_E.grid(row=2,column=1)
cm3.grid(row=2,column=2)

a4 = Label(LL,text=("a4 = "),font=fonty)
a4_E = Entry(LL,width=6,font=fonty)
cm4 = Label(LL,text=("cm"),font=fonty)
a4.grid(row=3,column=0)
a4_E.grid(row=3,column=1)
cm4.grid(row=3,column=2)

a5 = Label(LL,text=("a5 = "),font=fonty)
a5_E = Entry(LL,width=6,font=fonty)
cm5 = Label(LL,text=("cm"),font=fonty)
a5.grid(row=4,column=0)
a5_E.grid(row=4,column=1)
cm5.grid(row=4,column=2)


# Joint Variables
jv = Label(text= "Joint Variables",font=('Times',20,'italic'),bg="darkgray")
jv.place(relx=0.2,rely=0.6,anchor='n')

JV = LabelFrame(cal)
JV.place(relx=0.2,rely=0.31,anchor='n')

T1 = Label(JV,text=("T1 = "),font=fonty)
T1_E = Entry(JV,width=6,font=fonty)
cm6 = Label(JV,text=("deg"),font=fonty)
T1.grid(row=0,column=0)
T1_E.grid(row=0,column=1)
cm6.grid(row=0,column=2)


T2 = Label(JV,text=("T2 = "),font=fonty)
T2_E = Entry(JV,width=6,font=fonty)
cm7 = Label(JV,text=("deg"),font=fonty)
T2.grid(row=1,column=0)
T2_E.grid(row=1,column=1)
cm7.grid(row=1,column=2)

d3 = Label(JV,text=("d3 = "),font=fonty)
d3_E = Entry(JV,width=6,font=fonty)
cm8 = Label(JV,text=("cm"),font=fonty)
d3.grid(row=2,column=0)
d3_E.grid(row=2,column=1)
cm8.grid(row=2,column=2)


# Position Vectors
pv = Label(text= "Position Vectors",font=('Times',20,'italic'),bg="darkgray")
pv.place(relx=0.8,rely=0.6,anchor='n')

PV = LabelFrame(cal)
PV.place(relx=0.8,rely=0.31,anchor='n')

X = Label(PV,text=("X = "),font=fonty)
X_E = Entry(PV,width=6,font=fonty)
cm9 = Label(PV,text=("deg"),font=fonty)
X.grid(row=0,column=0)
X_E.grid(row=0,column=1)
cm9.grid(row=0,column=2)

Y = Label(PV,text=("Y = "),font=fonty)
Y_E = Entry(PV,width=6,font=fonty)
cma = Label(PV,text=("deg"),font=fonty)
Y.grid(row=1,column=0)
Y_E.grid(row=1,column=1)
cma.grid(row=1,column=2)

Z = Label(PV,text=("Z = "),font=fonty)
Z_E = Entry(PV,width=6,font=fonty)
cmb = Label(PV,text=("deg"),font=fonty)
Z.grid(row=2,column=0)
Z_E.grid(row=2,column=1)
cmb.grid(row=2,column=2)

# Buttons
RST = LabelFrame(cal)
RST.place(relx=0.5,rely=0.6,anchor='n')
Rst = Button(RST,text="RESET",font=fonty,width = 20,command=reset )
Rst.grid(row=0,column=0)

FK = LabelFrame(cal)
FK.place(relx=0.2,rely=0.6,anchor='n')
Fk = Button(FK,text="FORWARD",font=fonty,width = 20,command=f_k)
Fk.grid(row=0,column=0)

IK = LabelFrame(cal)
IK.place(relx=0.8,rely=0.6,anchor='n')
Ik = Button(IK,text="INVERSE",font=fonty,width = 20,command=i_k)
Ik.grid(row=0,column=0)

def s_m():
	global sm
	sm = tk.Toplevel()
	sm.title("Scara Manipulator")
	sm.geometry("500x500")
	Sm = LabelFrame(sm)
	Sm.place(relx=0.5,rely=0.15,anchor='n')
	Sm1 = Label(Sm,bd=1,relief="solid",text="SCARA (Selective Compliance Assembly Robot Arm) \nManipulators are an essential advancement in the \nworld of robotics, distinguished by their distinctive \ndesign and varied functionality. \nSCARA robots were developed in the 1980s and \nhave since become vital components in a variety \nof industrial and production environments, providing \naccurate control and economical operation. \nSCARA Manipulators are versatile beyond only their \nmechanical design. These robots, which have advanced \ncontrol systems and programming interfaces, may \neasily be integrated into automated production \nlines and synced with other equipment, \nincreasing productivity and efficiency. ",font =('Times',15),justify=CENTER)
	Sm1.grid(row=0,column=0)

def d_f():
	global dof
	D_f = tk.Toplevel()
	D_f.title("SCARA Degrees of Freedom")
	D_f.geometry("800x450")
	dof = tk.PhotoImage(file="//home//bitsin/Documents//ROB2_3202//dof.png")
	dof_label=tk.Label(D_f,image=dof).pack(padx=20,pady=20)
	dof_label.place(x=0,y=0, relwidth=1,relheight=1)

def k_d():
	global kd
	K_d = tk.Toplevel()
	K_d.title("Kinematics Diagram & DH Frames Assignment of SCARA Manipulator")
	K_d.geometry("800x450")
	kd = tk.PhotoImage(file="//home//bitsin/Documents//ROB2_3202//kd.png")
	kd_label=tk.Label(K_d,image=kd).pack(padx=20,pady=20)
	kd_label.place(x=0,y=0, relwidth=1,relheight=1)

def p_t():
	global pt
	P_t = tk.Toplevel()
	P_t.title("SCARA Manipulator Parametric Table")
	P_t.geometry("800x400")
	pt = tk.PhotoImage(file="//home//bitsin/Documents//ROB2_3202//pt.png")
	pt_label=tk.Label(P_t,image=pt).pack(padx=20,pady=20)
	pt_label.place(x=0,y=0, relwidth=1,relheight=1)

UTL = LabelFrame(cal)
UTL.place(relx=0.5, rely=0.956,anchor='n')

SM = Button(UTL,text="SCARA Manipulator",font=fontf,width = 25,command=s_m)
SM.grid(row=0,column=0)
DF = Button(UTL,text="SCARA DOF",font=fontf,width = 25,command=d_f)
DF.grid(row=0,column=1)
DH = Button(UTL,text="DH Frames",font=fontf,width = 25,command=k_d)
DH.grid(row=0,column=2)
PT = Button(UTL,text="Parametric Table",font=fontf,width = 25,command=p_t)
PT.grid(row=0,column=3)

BX = Label(text="Homogeneous Transformation Matrix",font=fonty)
BX.place(relx=0.5, rely=0.67,anchor='n')
	
	




cal.mainloop()
