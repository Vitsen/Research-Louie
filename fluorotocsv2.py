import Tkinter
from tkFileDialog import askopenfilename, asksaveasfilename
import tkMessageBox

class GUI(Tkinter.Frame):

  def __init__(self, root):
    Tkinter.Frame.__init__(self, root)
    
    # define buttons
    Tkinter.Button(self, text='Select input files',command=self.askopenfilename).pack()
    Tkinter.Button(self, text='Output file name:',command=self.asksaveasfilename).pack()
    Tkinter.Button(self, text='Create CSV',command=self.createCSV).pack()
    Tkinter.Button(self, text='Close',command=self.close_window).pack()

    self.file_input = options = {}
    options['filetypes'] = [('all files', '.*'),('text files', '.txt')]
    options['defaultextension'] = '.txt'

    self.file_output = options2 = {}
    options2['filetypes'] = [('comma-separated values', '.csv'),('all files', '.*')]
    options2['defaultextension'] = '.csv'

  def askopenfilename(self):
    files = askopenfilename(multiple=True, **self.file_input)
    files = self.tk.splitlist(files)
    self.input1 = files
    
  def asksaveasfilename(self):
    filename = asksaveasfilename(**self.file_output)
    self.output1 = filename

  def close_window(self): 
    return root.destroy()

  def createCSV(self):
    numfiles = len(self.input1)
    files = [None]*numfiles
    #Takes the data from input files
    for i in range(numfiles):
      with open(self.input1[i],'r') as f:
        files[i] = f.readlines()    
    files = zip(*files)    
    with open(self.output1,'w') as g:
      g.write("Wavelength")
      for i in range(numfiles):
        g.write(","+str((self.input1[i]).rsplit("/")[-1]))
      for i in range(1,len(files)/3):
        g.write("\n")
        g.write(files[i][0].split()[0])
        for j in range(numfiles):
          g.write(","+files[i][j].split()[1])
    tkMessageBox.showinfo('Confirmation','Your CSV has been made!')      

root = Tkinter.Tk()
root.title("Fluorometer Data to CSV Converter")
test = GUI(root).pack()
root.mainloop()
