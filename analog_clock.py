#Analog Clock in Python

import tkinter as TK
import datetime
import time
import math

def hands(root,canvas,second_hand):
	pass

def main():

	root = TK.Tk()
	canvas = TK.Canvas(root, height=300, width=300,bg="white")

	clock_border = canvas.create_oval(50,50,250,250)

	canvas.create_text(150+90*math.cos(math.pi/2-12*30/180*math.pi)
			,150-90*math.sin(math.pi/2-12*30/180*math.pi)
			,fill="darkblue",font="Times 12 bold"
			,text="12")
	canvas.create_text(150+90*math.cos(math.pi/2-1*30/180*math.pi)
		,150-90*math.sin(math.pi/2-1*30/180*math.pi)
		,fill="darkblue",font="Times 12 bold"
		,text="1")
	canvas.create_text(150+90*math.cos(math.pi/2-2*30/180*math.pi)
		,150-90*math.sin(math.pi/2-2*30/180*math.pi),fill="darkblue"
		,font="Times 12 bold"
	    ,text="2")
	canvas.create_text(150+90*math.cos(math.pi/2-3*30/180*math.pi)
		,150-90*math.sin(math.pi/2-3*30/180*math.pi),fill="darkblue"
		,font="Times 12 bold"
	    ,text="3")
	canvas.create_text(150+90*math.cos(math.pi/2-4*30/180*math.pi)
		,150-90*math.sin(math.pi/2-4*30/180*math.pi),fill="darkblue"
		,font="Times 12 bold"
       	,text="4")
	canvas.create_text(150+90*math.cos(math.pi/2-5*30/180*math.pi)
		,150-90*math.sin(math.pi/2-5*30/180*math.pi),fill="darkblue"
		,font="Times 12 bold"
        ,text="5")
	canvas.create_text(150+90*math.cos(math.pi/2-6*30/180*math.pi)
		,150-90*math.sin(math.pi/2-6*30/180*math.pi),fill="darkblue"
		,font="Times 12 bold"
        ,text="6")
	canvas.create_text(150+90*math.cos(math.pi/2-7*30/180*math.pi)
		,150-90*math.sin(math.pi/2-7*30/180*math.pi),fill="darkblue"
		,font="Times 12 bold"
        ,text="7")
	canvas.create_text(150+90*math.cos(math.pi/2-8*30/180*math.pi)
		,150-90*math.sin(math.pi/2-8*30/180*math.pi),fill="darkblue"
		,font="Times 12 bold"
        ,text="8")
	canvas.create_text(150+90*math.cos(math.pi/2-9*30/180*math.pi)
		,150-90*math.sin(math.pi/2-9*30/180*math.pi),fill="darkblue"
		,font="Times 12 bold"
        ,text="9")
	canvas.create_text(150+90*math.cos(math.pi/2-10*30/180*math.pi)
		,150-90*math.sin(math.pi/2-10*30/180*math.pi),fill="darkblue"
		,font="Times 12 bold"
        ,text="10")
	canvas.create_text(150+90*math.cos(math.pi/2-11*30/180*math.pi)
		,150-90*math.sin(math.pi/2-11*30/180*math.pi),fill="darkblue"
		,font="Times 12 bold"
	    ,text="11")
	canvas.pack()

	while(True):
		t=datetime.datetime.now()
		h=t.hour%12
		m=t.minute
		s=t.second

		second_hand = canvas.create_line(150,150,
			150+100*math.cos(math.pi/2-s*6/180*math.pi),
			150-100*math.sin(math.pi/2-s*6/180*math.pi))

		minute_hand = canvas.create_line(150,150,
			150+75*math.cos(math.pi/2-m*6/180*math.pi),
			150-75*math.sin(math.pi/2-m*6/180*math.pi))

		hour_hand = canvas.create_line(150,150,
			150+50*math.cos(math.pi/2-h*30/180*math.pi),
			150-50*math.sin(math.pi/2-h*30/180*math.pi))

		time.sleep(1)

		canvas.update()

		canvas.delete(second_hand)
		canvas.delete(minute_hand)
		canvas.delete(hour_hand)

	root.mainloop()

main()
