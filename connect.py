from tkinter import *
from time import *

def onObjectClick(event):                  
    print('Got object click', event.x, event.y)
    print(event.widget.find_closest(event.x, event.y))


class MyFrame(Frame):
  def __init__(self):
    Frame.__init__(self)

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

    #9 crosses
    #9 circles
    # my_rect_id = self.myCanvas.create_rectangle(100, 100, 200, 200, fill = "yellow3")
    # my_s_rect_id = self.myCanvas.create_rectangle(120, 120, 220, 220, fill = "yellow")
    # my_line_id_o = self.myCanvas.create_line(120, 120 , 200, 120, fill = "yellow")
    # my_line_id_s = self.myCanvas.create_line(120, 120, 120, 200, fill = "yellow")
    # my_line_id_t = self.myCanvas.create_line(100, 100, 120, 120, fill = "yellow")
    # my_edge_1 = self.myCanvas.create_line(100, 200, 120, 200, fill = "yellow3")
    # my_edge_2 = self.myCanvas.create_line(120, 200, 120, 220, fill = "yellow")
    # my_edge_3 = self.myCanvas.create_line(200, 100, 200, 120, fill = "yellow3")
    # my_edge_4 = self.myCanvas.create_line(200, 120, 220, 120, fill = "yellow")

    # My_eye_1 = self.myCanvas.create_oval(130, 130, 150, 150, fill = "white")
    # My_eye_2 = self.myCanvas.create_oval(190, 130, 210, 150, fill = "white")

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