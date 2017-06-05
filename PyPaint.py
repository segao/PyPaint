# PyPaint
# Sharon Gao, 2017
from tkinter import *
import pyscreenshot as ImageGrab

# TOOLS
PENCIL, BRUSH, ERASER, LINE, RECTANGLE, OVAL = list(range(6))

class Paint:
    def __init__(self, canvas):
        self.canvas = canvas
        self._tool, self._color, self._width, self._fill, self._obj = None, None, None, None, None
        self.lastx, self.lasty = None, None
        self.canvas.bind('<Button-1>', self.click)
        self.canvas.bind('<B1-Motion>', self.draw)

    def draw(self, event):
        if self._tool is None or self._obj is None:
            return
        x, y = self.lastx, self.lasty
        if self._tool in (LINE, RECTANGLE, OVAL):
            self.canvas.coords(self._obj, (x, y, event.x, event.y))
        elif self._tool in (PENCIL, BRUSH, ERASER):
            if self.lastx is not None and self.lasty is not None:
                if self._tool == PENCIL:
                    self.canvas.create_line(self.lastx, self.lasty, event.x, event.y, fill = self._color)
                elif self._tool == BRUSH:
                    if self._width is None:
                        x1, y1 = (event.x - 5), (event.y - 5)
                        x2, y2 = (event.x + 5), (event.y + 5)
                    else:
                        x1, y1 = (event.x - self._width), (event.y - self._width)
                        x2, y2 = (event.x + self._width), (event.y + self._width)
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill = self._color, outline = self._color)
                elif self._tool == ERASER:
                    if self._width is None:
                        x1, y1 = (event.x - 15), (event.y - 15)
                        x2, y2 = (event.x + 15), (event.y + 15)
                    else:
                        x1, y1 = (event.x - self._width), (event.y - self._width)
                        x2, y2 = (event.x + self._width), (event.y + self._width)
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill = "#ffffff", outline = "#ffffff")
                self.lastx, self.lasty = event.x, event.y
                
    # Updates x and y coordinates
    # Anchors starting coordinates for shapes
    def click(self, event):
        if self._tool is None:
            return
        if self._color is None:
            self._color = '#000000'
        x, y = event.x, event.y
        if self._tool == LINE:
            self._obj = self.canvas.create_line((x, y, x, y), fill = self._color, width = self._width)
        elif self._tool == RECTANGLE:
            if self._fill == True:
                self._obj = self.canvas.create_rectangle((x, y, x, y), outline = self._color, fill = self._color, width = self._width)
            else:
                self._obj = self.canvas.create_rectangle((x, y, x, y), outline = self._color, width = self._width)
        elif self._tool == OVAL:
            if self._fill == True:
                self._obj = self.canvas.create_oval((x, y, x, y), outline = self._color, fill = self._color, width = self._width)
            else:
                self._obj = self.canvas.create_oval((x, y, x, y), outline = self._color, width = self._width)
        self.lastx, self.lasty = x, y
        
    # Value updaters
    def select_tool(self, tool):
        print('Tool', tool)
        self._tool = tool
    
    def select_color(self, color):
        print('Color', color)
        self._color = color
    
    def select_width(self, width):
        print('Width', width)
        self._width = width
    
    def select_fill(self, fill):
        print('Fill', fill)
        self._fill = fill

class Tool:
    def __init__(self, whiteboard, parent=None):
        # TOOL ICONS
        self.pencil = PhotoImage(file = "Images/pencil_tool.gif")
        self.brush = PhotoImage(file = "Images/brush_tool.gif")
        self.eraser = PhotoImage(file = "Images/eraser_tool.gif")
        self.line = PhotoImage(file = "Images/line_tool.gif")
        self.rectangle = PhotoImage(file = "Images/shape_tool.gif")
        self.oval = PhotoImage(file = "Images/oval_tool.gif")
        
        # COLOR ICONS
        self.black = PhotoImage(file = "Images/black.gif") #000000
        self.gray = PhotoImage(file = "Images/gray.gif") #808080
        self.white = PhotoImage(file = "Images/white.gif") #ffffff 
        self.red = PhotoImage(file = "Images/red.gif") #ff0000
        self.yellow = PhotoImage(file = "Images/yellow.gif") #ffff00
        self.green = PhotoImage(file = "Images/green.gif") #00ff00
        self.cyan = PhotoImage(file = "Images/cyan.gif") #00ffff
        self.blue = PhotoImage(file = "Images/blue.gif") #0000ff
        self.magenta = PhotoImage(file = "Images/magenta.gif") #ff00ff
        self.brown = PhotoImage(file = "Images/brown.gif") #883d00
        
        # BRUSH WIDTH ICONS
        self.one = PhotoImage(file = "Images/1.gif")
        self.two = PhotoImage(file = "Images/2.gif")
        self.three = PhotoImage(file = "Images/3.gif")
        self.four = PhotoImage(file = "Images/4.gif")
        self.five = PhotoImage(file = "Images/5.gif")
        self.six = PhotoImage(file = "Images/6.gif")
        
        # SHAPE FILL ICONS
        self.stroke = PhotoImage(file = "Images/stroke.gif")
        self.fill = PhotoImage(file = "Images/fill.gif")
        
        # FILE MANAGEMENT ICONS
        self.save = PhotoImage(file = "Images/save.gif")
        self.clear = PhotoImage(file = "Images/clear.gif")
        
        TOOLS = [
            (self.pencil, PENCIL),
            (self.brush, BRUSH),
            (self.eraser, ERASER),
            (self.line, LINE),
            (self.rectangle, RECTANGLE),
            (self.oval, OVAL)
        ]
        
        COLORS = [
            (self.black, '#000000'),
            (self.gray, '#808080'),
            (self.white, '#FFFFFF'),
            (self.red, '#FF0000'),
            (self.yellow, '#FFFF00'),
            (self.green, '#00FF00'),
            (self.cyan, '#00FFFF'),
            (self.blue, '#0000FF'),
            (self.magenta, '#FF00FF'),
            (self.brown, '#883d00')
        ]
        
        WIDTH = [
            (self.one, 1),
            (self.two, 3),
            (self.three, 5),
            (self.four, 10),
            (self.five, 20),
            (self.six, 30)
        ]
        
        FILL = [
            (self.stroke, False),
            (self.fill, True)
        ]
        
        self.whiteboard = whiteboard
        frame1 = Frame(parent)
        frame2 = Frame(parent)
        self._curr_tool = None
        self._curr_color = None
        self._curr_width = None
        self._curr_fill = None
        
        # Create and place icons
        for img, name in TOOLS:
            lbl = Label(frame1, relief='raised', image = img)
            lbl._tool = name
            lbl.bind('<Button-1>', self.update_tool)
            lbl.pack(padx = 6, pady = 3)
        spacer = Label(frame1, image = self.white)
        spacer.pack(padx = 6, pady = 3)
        for img, name in COLORS:
            lbl = Label(frame1, relief='raised', image = img)
            lbl._color = name
            lbl.bind('<Button-1>', self.update_color)
            lbl.pack(padx = 6, pady = 3)
        spacer = Label(frame1, image = self.white)
        spacer.pack(padx = 6, pady = 3)
        lbl = Label(frame1, relief = 'raised', image = self.save)
        #lbl.bind('<Button-1>', self.save_image)
        lbl.pack(padx = 6, pady = 3)
        frame1.pack(side = 'left', fill = 'y', expand = True, pady = 6)
        
        for img, value in WIDTH:
            lbl = Label(frame2, relief='raised', image = img)
            lbl._width = value
            lbl.bind('<Button-1>', self.update_width)
            lbl.pack(padx = 6, pady = 3)
        spacer = Label(frame2, image = self.white)
        spacer.pack(padx = 6, pady = 3)
        for img, value in FILL:
            lbl = Label(frame2, relief='raised', image = img)
            lbl._fill = value
            lbl.bind('<Button-1>', self.update_fill)
            lbl.pack(padx = 6, pady = 3)
        spacer = Label(frame2, image = self.white)
        spacer.pack(padx = 6, pady = 3)
        spacer = Label(frame2, image = self.white)
        spacer.pack(padx = 6, pady = 3)
        spacer = Label(frame2, image = self.white)
        spacer.pack(padx = 6, pady = 3)
        spacer = Label(frame2, image = self.white)
        spacer.pack(padx = 6, pady = 3)
        spacer = Label(frame2, image = self.white)
        spacer.pack(padx = 6, pady = 3)
        spacer = Label(frame2, image = self.white)
        spacer.pack(padx = 6, pady = 3)
        lbl = Label(frame2, relief = 'raised', image = self.clear)
        lbl.bind('<Button-1>', self.clear_canvas)
        lbl.pack(padx = 6, pady = 3)
        lbl = Label(frame2, relief = 'raised', image = self.save)
        lbl.bind('<Button-1>', self.popup)
        lbl.pack()
        frame2.pack(side='left', fill = 'y', expand = True, pady = 6)
        
    # Update current value and depress selected icon
    def update_tool(self, event):
        lbl = event.widget
        if self._curr_tool:
            self._curr_tool['relief'] = 'raised'
        lbl['relief'] = 'sunken'
        self._curr_tool = lbl
        self.whiteboard.select_tool(lbl._tool)
    
    def update_color(self, event):
        lbl = event.widget
        if self._curr_color:
            self._curr_color['relief'] = 'raised'
        lbl['relief'] = 'sunken'
        self._curr_color = lbl
        self.whiteboard.select_color(lbl._color)
    
    def update_width(self, event):
        lbl = event.widget
        if self._curr_width:
            self._curr_width['relief'] = 'raised'
        lbl['relief'] = 'sunken'
        self._curr_width = lbl
        self.whiteboard.select_width(lbl._width)
    
    def update_fill(self, event):
        lbl = event.widget
        if self._curr_fill:
            self._curr_fill['relief'] = 'raised'
        lbl['relief'] = 'sunken'
        self._curr_fill = lbl
        self.whiteboard.select_fill(lbl._fill)
    
    def popup(self, event):
        w = PopupWindow(root)
        root.wait_window(w.top)
        x = root.winfo_x()
        y = root.winfo_y()
        im = ImageGrab.grab(bbox = (x + 91, y + 31, x + 891, y + 653))
        if w.name is None:
            return
        file_name = w.name + w.type
        im.save(file_name)
        im.show()
        
    # Clear canvas
    def clear_canvas(self, event):
        canvas.delete("all")

# Class for popup window to save image
class PopupWindow:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        Label(top, text="File Name: ").grid(row = 1, padx = 10, pady = 5)
        self.e = Entry(top)
        self.e.grid(row = 1, column = 2, padx = 10, pady = 5)
        b = Button(top, text="Save Image", command=self.ok)
        b.grid(row = 2, column = 2, pady = 5)
        
        self.file_type = StringVar(top)
        self.file_type.set(".png")
        self.option = OptionMenu(top, self.file_type, ".png", ".jpeg", ".bmp")
        self.option.grid(row = 1, column = 3, padx = 10, pady = 5)
        
        self.name = None
        

    def ok(self):
        self.name = self.e.get() 
        self.type = self.file_type.get()
        self.top.destroy()


root = Tk()
root.geometry("900x640+0+0")
root.resizable(width = False, height = False)
root.title("PyPaint")
canvas = Canvas(highlightbackground='black', width = 800, height = 600)
whiteboard = Paint(canvas)
tool = Tool(whiteboard)
w = PopupWindow(root)
canvas.pack(fill = 'both', expand = True, padx=6, pady=6)
root.mainloop()
