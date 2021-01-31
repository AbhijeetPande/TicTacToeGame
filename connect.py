from tkinter import *
from time import *

class MyFrame(Frame):
  def __init__(self):
    self._msg = -1
    Frame.__init__(self)
    def onObjectClick(event):                  
      print('Got object click', event.x, event.y)
      print(event.widget.find_closest(event.x, event.y))
      self._msg = int(''.join(map(str, event.widget.find_closest(event.x, event.y)))) - 6
      print(self._msg)
      print(type(self._msg))

    self.myCanvas = Canvas(width=300, height=300, bg="lightblue")
    self.myCanvas.grid()
    #we need: 
    #1 rectangle
    board = self.myCanvas.create_rectangle(90, 90, 210, 210, fill = "yellow3")
    #4 lines
    my_line_id_1 = self.myCanvas.create_line(130, 90 , 130, 210, fill = "black")
    my_line_id_2 = self.myCanvas.create_line(170, 90 , 170, 210, fill = "black")

    my_line_id_3 = self.myCanvas.create_line(90, 130 , 210, 130, fill = "black")
    my_line_id_4 = self.myCanvas.create_line(90, 170 , 210, 170, fill = "black")    

    #1 circle

    #9 squares - light up if mouse hovers over
    #buttonEnter1 = Button( width=38, height=38).place(x=91, y=91) 
    upper_square_1 = self.myCanvas.create_rectangle(91, 91, 129, 129, fill = "yellow3")
    upper_square_2 = self.myCanvas.create_rectangle(131, 91, 169, 129, fill = "yellow3")
    upper_square_3 = self.myCanvas.create_rectangle(171, 91, 209, 129, fill = "yellow3")

    middle_square_1 = self.myCanvas.create_rectangle(91, 131, 129, 169, fill = "yellow3")
    middle_square_2 = self.myCanvas.create_rectangle(131, 131, 169, 169, fill = "yellow3")
    middle_square_3 = self.myCanvas.create_rectangle(171, 131, 209, 169, fill = "yellow3")

    lower_square_1 = self.myCanvas.create_rectangle(91, 171, 129, 209, fill = "yellow3")
    lower_square_2 = self.myCanvas.create_rectangle(131, 171, 169, 209, fill = "yellow3")
    lower_square_3 = self.myCanvas.create_rectangle(171, 171, 209, 209, fill = "yellow3")


    
    click_1 = [100, 100, 120, 120]
    click_2 = [140, 100, 160, 120]
    click_3 = [180, 100, 200, 120]

    click_4 = [100, 140, 120, 160]
    click_5 = [140, 140, 160, 160]
    click_6 = [180, 140, 200, 160]
    
    click_7 = [100, 180, 120, 200]
    click_8 = [140, 180, 160, 200]
    click_9 = [180, 180, 200, 200]

    My_circle = self.myCanvas.create_oval(0, 0, 0, 0, width = 10)
    click_container = [click_1, click_2, click_3, click_4, click_5, click_6, click_7, click_8, click_9]
    My_iris_1 = self.myCanvas.create_oval(135, 135, 145, 145, fill = "blue")
    My_iris_2 = self.myCanvas.create_oval(195, 135, 205, 145, fill = "blue")

    self.myCanvas.tag_bind(upper_square_1, '<ButtonPress-1>', onObjectClick)
    self.myCanvas.tag_bind(upper_square_2, '<ButtonPress-1>', onObjectClick)
    self.myCanvas.tag_bind(upper_square_3, '<ButtonPress-1>', onObjectClick)

    self.myCanvas.tag_bind(middle_square_1, '<ButtonPress-1>', onObjectClick)
    self.myCanvas.tag_bind(middle_square_2, '<ButtonPress-1>', onObjectClick)
    self.myCanvas.tag_bind(middle_square_3, '<ButtonPress-1>', onObjectClick)

    self.myCanvas.tag_bind(lower_square_1, '<ButtonPress-1>', onObjectClick)
    self.myCanvas.tag_bind(lower_square_2, '<ButtonPress-1>', onObjectClick)
    self.myCanvas.tag_bind(lower_square_3, '<ButtonPress-1>', onObjectClick)
    
    while True:
      if self._msg != -1:
        print("I reached here")
        print(type(self._msg))
        print(self._msg)
        self.myCanvas.coords(My_circle, click_container[self._msg][0], click_container[self._msg][1], click_container[self._msg][2],click_container[self._msg][3])
        self.myCanvas.update()
      
      self.myCanvas.coords(My_iris_1, 137, 137, 142, 142)
      self.myCanvas.coords(My_iris_2, 197, 137, 202, 142)
      sleep(1)
      self.myCanvas.update()
      self.myCanvas.coords(My_iris_1, 135, 135, 145, 145)
      self.myCanvas.coords(My_iris_2, 195, 135, 205, 145)
      sleep(1)
      self.myCanvas.update()

frame02 = MyFrame()

frame02.mainloop()