from tkinter import *
from time import *
# Function returns which shape to print
def get_shape(currentShape):
  if currentShape == "x":
    currentShape = "o"
  elif currentShape == "o":
    currentShape = "x"
  return currentShape 

def check_victory(frame) :
  return False

def print_menu(frame) :
  return False

def print_game(frame) :
  # Create the canvas. A rectangle with four borders.
  frame.myCanvas = Canvas(width=300, height=300, bg="lightblue")
  frame.myCanvas.grid()

  # Create the rectangle
  board = frame.myCanvas.create_rectangle(90, 90, 210, 210, fill = "yellow3") 

  # Create 9 squares for the tic tac toe playing grid
  # Each square lights up if mouse hovers over it
  #buttonEnter1 = Button( width=38, height=38).place(x=91, y=91) 
  frame.upper_square_1 = frame.myCanvas.create_rectangle(91, 91, 129, 129, fill = "yellow3")
  frame.upper_square_2 = frame.myCanvas.create_rectangle(131, 91, 169, 129, fill = "yellow3")
  frame.upper_square_3 = frame.myCanvas.create_rectangle(171, 91, 209, 129, fill = "yellow3")

  frame.middle_square_1 = frame.myCanvas.create_rectangle(91, 131, 129, 169, fill = "yellow3")
  frame.middle_square_2 = frame.myCanvas.create_rectangle(131, 131, 169, 169, fill = "yellow3")
  frame.middle_square_3 = frame.myCanvas.create_rectangle(171, 131, 209, 169, fill = "yellow3")

  frame.lower_square_1 = frame.myCanvas.create_rectangle(91, 171, 129, 209, fill = "yellow3")
  frame.lower_square_2 = frame.myCanvas.create_rectangle(131, 171, 169, 209, fill = "yellow3")
  frame.lower_square_3 = frame.myCanvas.create_rectangle(171, 171, 209, 209, fill = "yellow3")

def bind_event(frame, click_function) :
  
  # Bind clicking of any square to function call for 'onObjectClick'
  frame.myCanvas.tag_bind(frame.upper_square_1, '<ButtonPress-1>', click_function)
  frame.myCanvas.tag_bind(frame.upper_square_2, '<ButtonPress-1>', click_function)
  frame.myCanvas.tag_bind(frame.upper_square_3, '<ButtonPress-1>', click_function)

  frame.myCanvas.tag_bind(frame.middle_square_1, '<ButtonPress-1>', click_function)
  frame.myCanvas.tag_bind(frame.middle_square_2, '<ButtonPress-1>', click_function)
  frame.myCanvas.tag_bind(frame.middle_square_3, '<ButtonPress-1>', click_function)

  frame.myCanvas.tag_bind(frame.lower_square_1, '<ButtonPress-1>', click_function)
  frame.myCanvas.tag_bind(frame.lower_square_2, '<ButtonPress-1>', click_function)
  frame.myCanvas.tag_bind(frame.lower_square_3, '<ButtonPress-1>', click_function)

# Function to print either 'x' or 'o' inside the square that was clicked.
def print_object(frame) :
  # Define the parameters for the circle or cross that needs to be drawn
  square_1 = [100, 100, 120, 120]
  square_2 = [140, 100, 160, 120]
  square_3 = [180, 100, 200, 120]

  square_4 = [100, 140, 120, 160]
  square_5 = [140, 140, 160, 160]
  square_6 = [180, 140, 200, 160]
  
  square_7 = [100, 180, 120, 200]
  square_8 = [140, 180, 160, 200]
  square_9 = [180, 180, 200, 200]

  click_container = [square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8, square_9]

  if frame._turn == "x" :
    frame.myCanvas.create_line(click_container[frame.square_id][0], 
                               click_container[frame.square_id][1], 
                               click_container[frame.square_id][2],
                               click_container[frame.square_id][3], 
                               fill = "black",
                               width = 10 )
    frame.myCanvas.create_line(click_container[frame.square_id][2], 
                               click_container[frame.square_id][1], 
                               click_container[frame.square_id][0],
                               click_container[frame.square_id][3], 
                              fill = "black",
                              width = 10 )
  elif frame._turn == "o" :
    frame.myCanvas.create_oval(click_container[frame.square_id][0],
                               click_container[frame.square_id][1], 
                               click_container[frame.square_id][2],
                               click_container[frame.square_id][3], 
                               width = 10)

class MyFrame(Frame):
  def __init__(self):
    self.square_id = -1
    self._history_o = []
    self._history_x = []
    self._turn = "o"
    Frame.__init__(self)

    print_game(self)
    
    # Function that will get called when a square is clicked
    def onObjectClick(event):                  
      print('Got object click', event.x, event.y)
      print(event.widget.find_closest(event.x, event.y))
      self.square_id = int(''.join(map(str, event.widget.find_closest(event.x, event.y)))) - 2
      self._history_o.append(self.square_id)
      print(self.square_id)
      print(type(self.square_id))
      self._turn = get_shape(self._turn)
      print_object(self)
      check_victory(self)

    bind_event(self, onObjectClick)


frame02 = MyFrame()

frame02.mainloop()