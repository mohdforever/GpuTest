#
# Simple and ugly GUI (graphical user interface) for GpuTest.
# (c)2013-2014 Geeks3D - http://www.geeks3d.com/gputest/
#
# Do no hesitate to improve this GUI if you have time ;)
#

import os
#from subprocess import call
import tkinter as tk


root = tk.Tk()
g_command_line = ""
allDemos = []
g_width=1280
g_height=720
resolution = tk.IntVar()
fullscreen = tk.IntVar()
submit_score = tk.IntVar()
screen_name = tk.StringVar()


class cDemo():
  def __init__(self, demo_name="", description="", demo_url="", demo_code=""):
      self.demo_name = demo_name;
      self.description = description;
      self.demo_url = demo_url;
      self.demo_code = demo_code;
     
  
def get_list(event):
  cs = listbox1.curselection()
  if cs:
    index = cs[0]
    seltext = listbox1.get(index)
    description = ""
    for demo in allDemos:
      if demo.demo_name == seltext:
        description = demo.description
    demo_descr.delete('1.0', 'end')
    demo_descr.insert(tk.END, description)


def open_demo_webpage():
  cs = listbox1.curselection()
  if cs:
    index = cs[0]
    seltext = listbox1.get(index)
    demo_url = ""
    for demo in allDemos:
      if demo.demo_name == seltext:
        demo_url = demo.demo_url
    #demo_url = "www.geeks3d.com"
    os.system("xdg-open http://" + demo_url)

  
def update_screen_resolution():
  global g_width
  global g_height
  
  if (resolution.get() == 1):
    g_width=800
    g_height=600
  elif (resolution.get() == 2):
    g_width=1024
    g_height=640
  elif (resolution.get() == 3):
    g_width=1280
    g_height=720
  elif (resolution.get() == 4):
    g_width=1920
    g_height=1080

def prepare_command_line():
  global g_command_line
  global allDemos
  global fullscreen
  global g_width
  global g_height
  global submit_score
  global screen_name

  
  update_screen_resolution()
  
  seltext = ""
  cs = listbox1.curselection()
  if cs:
    index = cs[0]
    seltext = listbox1.get(index)
  else:
    print ("\nPlease select a test (FurMark is the default test).")
    index = 0
    seltext = listbox1.get(index)
  
  demo_code = ""
  for demo in allDemos:
    if demo.demo_name == seltext:
      demo_code = demo.demo_code
  g_command_line = "./GpuTest /test='%s' /width=%d /height=%d /gpumon_terminal" % (demo_code, g_width, g_height)
  if (fullscreen.get() == 1):
    g_command_line += " /fullscreen"
    

def run_demo():
  prepare_command_line()
  os.system(g_command_line) 
  

def run_benchmark():
  global g_command_line
  prepare_command_line()
  g_command_line += " /benchmark  /print_score"
  
  if (submit_score.get() == 1):
    g_command_line += " /submit_gpudb"
    name = screen_name.get()
    if (name != ""):
      g_command_line += " /user_screen_name=\"%s\"" % (name)
  
  os.system(g_command_line)
  
class cDemo():
  def __init__(self, demo_name="", description="", demo_url="", demo_code=""):
      self.demo_name = demo_name;
      self.description = description;
      self.demo_url = demo_url;
      self.demo_code = demo_code;


demo = cDemo("FurMark (OpenGL 2.1/3.0)", "FurMark GPU burner (www.ozone3d.net/benchmarks/fur/)", "www.ozone3d.net/benchmarks/fur/", "fur")
allDemos.append(demo)
demo = cDemo("TessMark X8 (OpenGL 4.0)", "TessMark OpenGL 4 tessellation benchmark (www.ozone3d.net/benchmarks/tessmark/)", "www.ozone3d.net/benchmarks/tessmark/", "tess_x8")
allDemos.append(demo)
demo = cDemo("TessMark X16 (OpenGL 4.0)", "TessMark OpenGL 4 tessellation benchmark (www.ozone3d.net/benchmarks/tessmark/)", "www.ozone3d.net/benchmarks/tessmark/", "tess_x16")
allDemos.append(demo)
demo = cDemo("TessMark X32 (OpenGL 4.0)", "TessMark OpenGL 4 tessellation benchmark (www.ozone3d.net/benchmarks/tessmark/)", "www.ozone3d.net/benchmarks/tessmark/", "tess_x32")
allDemos.append(demo)
demo = cDemo("TessMark X64 (OpenGL 4.0)", "TessMark OpenGL 4 tessellation benchmark (www.ozone3d.net/benchmarks/tessmark/)", "www.ozone3d.net/benchmarks/tessmark/", "tess_x64")
allDemos.append(demo)
demo = cDemo("GiMark (OpenGL 3.3)", "GiMark OpenGL 3.3 geometry instancing benchmark", "www.geeks3d/gputest/", "gi")
allDemos.append(demo)
demo = cDemo("PixMark Julia FP64 (OpenGL 4.0)", "PixMark Julia FP64: double precision floating point test", "www.geeks3d/gputest/", "pixmark_julia_fp64")
allDemos.append(demo)
demo = cDemo("PixMark Julia FP32 (OpenGL 2.1/3.0)", "PixMark Julia FP32: simple precision floating point test", "www.geeks3d/gputest/", "pixmark_julia_fp32")
allDemos.append(demo)
demo = cDemo("PixMark Piano (OpenGL 2.1/3.0)", "PixMark Piano: heavy pixel shader test (credits in README.txt)", "www.geeks3d/gputest/", "pixmark_piano")
allDemos.append(demo)
demo = cDemo("PixMark Voloplosion (OpenGL 2.1/3.0)", "PixMark Volplosion: heavy pixel shader test (credits in README.txt)", "www.geeks3d/gputest/", "pixmark_volplosion")
allDemos.append(demo)
demo = cDemo("Plot3D (OpenGL 2.1/3.0)", "Plot3D: heavy wireframe mesh grid deformed by a vertex shader.", "www.geeks3d/gputest/", "plot3d")
allDemos.append(demo)
demo = cDemo("Triangle (OpenGL 2.1/3.0)", "Triangle: simple triangle.", "www.geeks3d/gputest/", "triangle")
allDemos.append(demo)

root.title("Geeks3D GpuTest GUI 0.7.0")
root.resizable(False,False)

# create the listbox (note that size is in characters)
listbox1 = tk.Listbox(root, width=45, height=5, selectmode='single')
listbox1.grid(row=0, column=0)

# create a vertical scrollbar to the right of the listbox
yscroll = tk.Scrollbar(command=listbox1.yview, orient=tk.VERTICAL)
yscroll.grid(row=0, column=1, sticky=tk.N+tk.S)
listbox1.configure(yscrollcommand=yscroll.set)


demo_descr = tk.Text(root,  height=3, width=35, bg='white',wrap='word')
demo_descr.grid(row=1, column=0)

fullscreen_checkbox = tk.Checkbutton(root, text = 'Fullscreen', variable = fullscreen)
fullscreen_checkbox.grid(row=2, column=0, sticky=tk.W)
fullscreen_checkbox.deselect()

R_800x600 = tk.Radiobutton(root, text="800x600", variable=resolution, value=1)
R_800x600.grid(row=3, column=0, sticky=tk.W)
R1 = tk.Radiobutton(root, text="1024x640", variable=resolution, value=2)
R1.grid(row=4, column=0, sticky=tk.W)
R2 = tk.Radiobutton(root, text="1280x720", variable=resolution, value=3)
R2.grid(row=5, column=0, sticky=tk.W)
R3 = tk.Radiobutton(root, text="1920x1080", variable=resolution, value=4)
R3.grid(row=6, column=0, sticky=tk.W)

R1.select()

button1 = tk.Button(root, text='Run stress test', command=run_demo, width=30, height=2)
button1.grid(row=10, column=0, sticky=tk.W)

button2 = tk.Button(root, text='Run benchmark', command=run_benchmark, width=30, height=2)
button2.grid(row=11, column=0, sticky=tk.W)

label_separator = tk.Label(root,text='==========================')
label_separator.grid(row=12, column=0, sticky=tk.W)

submit_checkbox = tk.Checkbutton(root, text = 'Submit score to GPU database', variable = submit_score)
submit_checkbox.grid(row=13, column=0, sticky=tk.W)
submit_checkbox.deselect()

label_screen_name = tk.Label(root,text='Screen name (optional):')
label_screen_name.grid(row=14, column=0, sticky=tk.W)
entry1 = tk.Entry(root, text='', textvariable = screen_name)
entry1.grid(row=15, column=0, sticky=tk.W)

label_separator = tk.Label(root,text='==========================')
label_separator.grid(row=16, column=0, sticky=tk.W)

button3 = tk.Button(root, text='Selected demo webpage', command=open_demo_webpage)
button3.grid(row=17, column=0, sticky=tk.W)

enter1 = tk.Entry(root, width=45, bg='grey')
enter1.insert(0, '.:: (C)2013-2014 Geeks3D (www.geeks3d.com)::.')
enter1.grid(row=18, column=0)


for demo in allDemos:
  listbox1.insert(tk.END, demo.demo_name)
# Force the selection of the first demo otherwise prepare_command_line() will fail.
listbox1.activate(0)
listbox1.select_set(0, 0)

demo = allDemos[0]  
demo_descr.insert(tk.END, demo.description)

# left mouse click on a list item to display selection
listbox1.bind('<ButtonRelease-1>', get_list)

root.mainloop()

