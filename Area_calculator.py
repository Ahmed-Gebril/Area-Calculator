## This program calculates the area of either a  cicle, a square or rectangle and also able to find the formula for a desired geometric shape
#by searching for its value inside a dictionary. if the value is not found, the user can add the associated formula for the
#geometric shape

#the program uses radiobutton to specifiy the desired shape.


from tkinter import *
from tkinter import messagebox
import math
from math import sqrt


class Userinterface:

    def __init__(self):
        """
        constructor:creates windows both topframe and bottomframe, labels
        and scales the window.

        """
        self.__mainwindow = Tk() ## Tkinter class that we have imported. A blank window.


        #changing the flower shape into a geometric one
        #also creating a dropdown menu.


        # Create two frames. The upper  for the Radiobuttons to include the shape choices
        # the other another for the regular Button widgets.
        self.__mainwindow.wm_title('Area calculator and formula finder')
        topframe = Frame(self.__mainwindow)
        topframe.grid(row=0,column=0)
        self.__bottomFrame = Frame(self.__mainwindow)
        self.__bottomFrame.grid(row=6,column=0)
        title = Label(topframe,text='Choose the geometric shape')

      #making a good-looking sclaing window.
        w = Scale(self.__mainwindow, from_=0, to=42)
        w.grid(row=1,column=1)
        w = Scale(self.__mainwindow, from_=0, to=200, orient=HORIZONTAL)
        w.grid(row=1,column=6)

        ## Five radio buttons that have the Five options and with their gridings.

        self.v=IntVar()
        self.v.set(1)

        self.rb1 = Radiobutton(topframe, text='Triangle', variable=self.v, value=5,command=self.triangle)
        self.rb2 = Radiobutton(topframe, text='Circle', variable=self.v,value=2,command=self.circle)
        self.rb3 = Radiobutton(topframe, text='Rectangle',value=3, variable=self.v,command=self.rectangle)
        self.rb4 = Radiobutton(topframe, text='Square', value=4,variable=self.v,command=self.square)
        self.rb5=Radiobutton(topframe, text='Find The formula', value=6,variable=self.v,command=self.finder)
        title.grid(row=0, column=0)
        self.rb1.grid(row=2, column=3)
        self.rb2.grid(row=3, column=3)
        self.rb3.grid(row=4, column=3)
        self.rb4.grid(row=5, column=3)
        self.rb5.grid(row=6,column=3)

    def circle(self): ## making a method for a circle area calculation

            self.restart()         ## caling the function restart.
            self.__radius = Entry(self.__bottomFrame, text='Radius')
            def calc():

              if   float(self.__radius.get())>0 :
                Area = (math.pi) *float(self.__radius.get())**2

                Area = Label(self.__bottomFrame, text=('Area=',round(Area,2) ),fg='blue')
                Area.grid(row=8, column=5)

              else: #if the value inter

               messagebox.showwarning("Error", "Please enter a positive number")

            self.__radius.grid(row=7,column=6)
            radius = Label(self.__bottomFrame,text='Enter the value of the radius')
            radius.grid(row=7, column=5)
            calculate=Button(self.__bottomFrame,text='Calculate',fg='red',command=calc)



            calculate.grid(row=7, column=7)



    def rectangle(self):




        self.restart()

        def calc():

         if float(self.width.get()) and float(self.length.get())>0:
            Area=(float(self.width.get()))*(float(self.length.get()))
            Area=Label(self.__bottomFrame,text=('Area=',round(Area,2)),fg='blue')
            Area.grid(row=8,column=5)

         else:
             messagebox.showwarning("Error", "Please enter a positive number")

        self.width = Entry(self.__bottomFrame)
        self.length = Entry(self.__bottomFrame)
        calculate = Button(self.__bottomFrame, text='Calculate', fg='red',command=calc)
        calculate.grid(row=6, column=7)

        self.width.grid(row=6, column=6)
        width=Label(self.__bottomFrame,text='width')
        length = Label(self.__bottomFrame, text='length')
        width.grid(row=6,column=5)
        length.grid(row=7,column=5)
        self.length.grid(row=7,column=6)


    def square(self): #method for the square
        self.restart()
        def calc():

         if float(self.length.get())>0:
            Area=float(self.length.get())**2
            Area=Label(self.__bottomFrame,text=('Area=',round(Area,2)),fg='blue')
            Area.grid(row=8,column=5)
         else:
             messagebox.showwarning("Error", "Please enter a positive number")

        self.length=Entry(self.__bottomFrame)
        calculate = Button(self.__bottomFrame, text='Calculate', fg='red',command=calc)
        length = Label(self.__bottomFrame, text='length')
        calculate.grid(row=6, column=7)
        self.length.grid(row=6, column=5)

        length.grid(row=6, column=4)


    def triangle(self): #method for the triangle
        self.restart()
        def calc():

         if float(a.get()) and float(b.get()) > 0 and float(c.get()) > 0:

            s=(float(a.get())+float(b.get())+float(c.get()) /2)
            Area=sqrt(s * (s - float(a.get())) * (s - float(b.get())) * (s - float(c.get())))


            Area=Label(self.__bottomFrame,text=('Area=',round(Area,1)),fg='blue')
            Area.grid(row=8,column=5)

         else:
             messagebox.showwarning("Error", "Please enter a positive number")



        a = Entry(self.__bottomFrame)
        b = Entry(self.__bottomFrame)
        c = Entry(self.__bottomFrame)
        calculate = Button(self.__bottomFrame, text='Calculate', fg='red',command=calc)
        calculate.grid(row=6, column=7)

        a.grid(row=6, column=6)
        firstside=Label(self.__bottomFrame,text='first side')
        secondside= Label(self.__bottomFrame, text='second side')
        thirdside =Label(self.__bottomFrame, text='third side')
        firstside.grid(row=6,column=5)
        secondside.grid(row=7,column=5)
        thirdside.grid(row=8,column=5)
        b.grid(row=7,column=6)
        c.grid(row=8, column=6)


    def finder(self): #the finder method
       self.restart()


       def adding(): #the function is responsible for adding new shape to
           #the dictionary if the shape is not found.

           newshape = Entry(self.__bottomFrame)
           x = newshape.get()
           Area_Formals[newshape.get()] = x
           messagebox.showinfo("Success", 'Area Added!')

       def finding(): #the function is responsible for finding the formula for the desired shape
           if choice.get() in Area_Formals:
               formula = Area_Formals[choice.get()]
               formula1=Label(self.__bottomFrame,text=('Area=',formula),fg='blue')
               formula1.grid(row=7,column=5)
           else:

               messagebox.showwarning("Error", 'Area not found, continue to add formula!')
               self.restart()
               newshape = Entry(self.__bottomFrame)
               newshapelabel = Label(self.__bottomFrame, text='Enter the name of the shape')
               shapeformulalabel=Label(self.__bottomFrame,text='Enter its formula')
               shapeformula=Entry(self.__bottomFrame)
               shapeformula.grid(row=7,column=5)
               shapeformulalabel.grid(row=7,column=4)
               newshape.grid(row=6, column=5)
               newshapelabel.grid(row=6, column=4)
               Add=Button(self.__bottomFrame,text='Add formula',command=adding)
               Add.grid(row=6, column=6)

       ## The dictionary includes values for shapes with its values.
       Area_Formals={'square':	'side*side', 'rectangle':	'length × width', 'parallelogram':	'base × height','triangle':	'base × height / 2', 'regular n-polygon':'(1/4) × n × side2 × cot(pi/n)','Ttapezoid':	'height × (base1 + base2) / 2','circle':	'pi × radius^2',
                 'ellipse':    'pi × radius1 × radius2','cube':'6 × side2','sphere'	: '4 × pi × radius^2','cylinder':	'perimeter of circle × height',
                 'Cone':    'pi × radius × side'}

       choice = Entry(self.__bottomFrame)

       choicelabel = Label(self.__bottomFrame, text='Enter the name of the shape')


       choice.grid(row=6,column=5)
       choicelabel.grid(row=6,column=4)
       find=Button(self.__bottomFrame,text='Find the formula',command=finding,fg='red')
       find.grid(row=6,column=6)
       choicelabel = choicelabel.lower()



    def start(self):


      self.__mainwindow.mainloop()

    def restart(self):  #restart method is called everytime a new radiobutton is clicked to guarantee that the widgets in
        # the bottomframe will not be overwriten. And therefore we won't have unlimited number of widgets.

        for widget in self.__bottomFrame.winfo_children():
            widget.destroy()

def main():


    ui = Userinterface()
    ui.start()   #start method is always called to keep the mainwindow.


main()

