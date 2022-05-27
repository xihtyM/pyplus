from tkinter import *;
from tkinter import messagebox;
from tkinter import filedialog;
import os,time,math;

class TextEditor:
    def __init__(self,root):
        self.menuhidden = False;
        self.root = root;
        self.root.title("Untitled");
        self.root.geometry("720x480");
        self.filename = "";
        self.title = StringVar();
        scrol_y = Scrollbar(self.root,orient=VERTICAL);
        self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("arial",15),fg="green",bg="black",state="normal",highlightcolor='white',relief=GROOVE);
        scrol_y.pack(side=RIGHT,fill=Y);
        scrol_y.config(command=self.txtarea.yview);
        self.txtarea.pack(fill=BOTH,expand=1);
        self.txtarea.config(insertbackground="green");
        self.menubar = Menu(self.root,font=("calibri",15,"bold"));
        self.root.config(menu=self.menubar);

        self.filemenu = Menu(self.menubar,font=("calibri",12),tearoff=0)
        self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
        self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
        self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
        self.filemenu.add_command(label="Save As",accelerator="Ctrl+Shift+S",command=self.saveasfile)
        self.filemenu.add_separator()
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        
        self.editmenu = Menu(self.menubar,font=("calibri",12),tearoff=0)
        self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
        self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
        self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
        self.editmenu.add_separator()
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        
        self.shortcuts();
    def settitle(self):
        if self.filename != "":
            self.root.title(self.filename)
        else:
            self.root.title("Untitled")
    def F11(self,*args):
        self.root.attributes("-fullscreen",not self.root.attributes("-fullscreen"));
    def newfile(self,*args):
        if self.filename == "":
            if self.txtarea.get("1.0") != "":
                self.saveasfile();
        self.txtarea.delete("1.0",END);
        self.filename = "";
        self.settitle();
    def openfile(self,*args):
        try:
            self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
            if self.filename != "":
                infile = open(self.filename,"r");
                self.txtarea.delete("1.0",END);
                for line in infile:
                    self.txtarea.insert(END,line);
                infile.close();
                self.settitle();
            else:
                return "break";
        except Exception as e:
            messagebox.showerror("Exception",e);
    
    def savefile(self,*args):
        try:
            if self.filename:
                data = self.txtarea.get("1.0",END);
                outfile = open(self.filename,"w");
                outfile.write(data);
                outfile.close();
                self.settitle();
            else:
                self.saveasfile();
        except Exception as e:
            messagebox.showerror("Exception",e);
    def altf4(self,*args):
        if self.filename == "":
            if self.txtarea.get("1.0") != "":
                self.saveasfile();
    def saveasfile(self,*args):
        try:
            untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")));
            if untitledfile == "":
                return 0;
            data = self.txtarea.get("1.0",END);
            outfile = open(untitledfile,"w");
            outfile.write(data);
            outfile.close();
            self.filename = untitledfile;
            self.settitle();
        except Exception as e:
            messagebox.showerror("Exception",e);
    def hidemenu(self,*args):
        self.menuhidden = not self.menuhidden;
        if self.menuhidden == False:
            root.config(menu=self.menubar);
        else:
            root.config(menu=Menu(root));
        return "break";
    def test(self,*args):
        print(*args);
    def cut(self,*args):
        self.txtarea.event_generate("<<Cut>>");
    def copy(self,*args):
        self.txtarea.event_generate("<<Copy>>");
    def paste(self,*args):
        self.txtarea.event_generate("<<Paste>>");
    def shortcuts(self):
        self.txtarea.bind("<F11>",self.F11);
        self.txtarea.bind("<Control-n>",self.newfile);
        self.txtarea.bind("<Control-o>",self.openfile);
        self.txtarea.bind("<Control-s>",self.savefile);
        self.txtarea.bind("<Key>",self.test);
        self.txtarea.bind("<Control-h>",self.hidemenu);
        self.txtarea.bind("<Alt-KeyPress-F4>",self.altf4);
        #self.txtarea.bind("<Control-BackSpace>",self.backspace);
root = Tk()

TextEditor(root)

root.mainloop()
