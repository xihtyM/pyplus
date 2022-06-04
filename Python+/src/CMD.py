import os, time, math;
from py_console import console
from tkinter import *;

# ALL PRE-DEFINED VARIABLES

b64 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-/";
directory = open(os.getcwd()+"\\vars\\dir.txt","r");
cmdSep = ">>";

def find_nth(text, find, c):
    start = text.find(find);
    while(start >= 0 and c > 1):
        start = text.find(find, start+len(find));
        c -= 1;
    return start+1;

def base64(i):
    if(isinstance(i,int)):
        endText = b64[i];
        return endText;
    else:
        console.error("Cannot be encrypted to base64.");
        return -1;

class KeyWords:
    multi_char_keywords = ["print","return","func","let","end","true","false","if","else"];
    seperator = "\n";
    whitespace = " ";

class Console:
    def __init__(self):
        self.directory = directory.read();
        while(True):
            i = input(self.directory+cmdSep+" ").lower();
            self.run(i);

    #COMPILER

    def compile(self,lc,path):
        path = path[0:path.find(".")]+".ppy+";
        try:
            with open(path,"w") as writeFile:
                writeFile.write(lc);
        except Exception as err:
            console.error("Error opening/writing to file.\n"+err);
            pass;
        console.success("Successfully compiled without errors!");
        
    #FORMATTER

    def formatter(self,code,path):
        SeperatedCode = [];
        seperations = code.count("\n")+1;
        fCode = "";
        prev = 0;

        for i in range(seperations):
            # BRANCHLESS WAY OF SAYING IF IT IS THE LAST ITERATION, MAKE IT THE FULL LENGTH OF THE STRING
            nth = (find_nth(code,KeyWords.seperator,i+1),len(code))[(seperations-i)*len(code) < len(code)+1];
            # REMOVE '\n' AND INDENTS
            c = code[prev:nth].replace("\n","");
            # REPLACES KEYWORDS WITH NUMBER ASSOCIATED WITH IT
            for x,v in enumerate(KeyWords.multi_char_keywords): c = c.replace(v,base64(x+2));
            tabs = "";
            for x,v in enumerate(c):
                if(v == " "):
                    tabs += v;
                    continue;
                break;
            tabs = tabs.replace("    ","\t").replace("\t","1");
            if(" " in tabs):
                console.error('Error: Unexpected indentation at line', str(i+1)+"\n"+'Got', tabs.count(" "), '(Expected: 4) spaces\nAt:',c.lstrip());
                return -1;
            c = tabs+c.lstrip();
            SeperatedCode.append(c);
            prev = nth;

        # FORMAT

        for i,line in enumerate(SeperatedCode):
            fCode += line.replace(" ","") + "0";

        self.compile(fCode,path);
        
    #CHANGE DIRECTORY
    
    def chdir(self):
        i = input(cmdSep+" ");
        if(os.path.exists(i)):
            with open(os.getcwd()+"\\vars\\dir.txt","w") as dir_:
                if(i[len(i)-1] == "\\" or i[len(i)-1] == "/"):
                    i = i[0:len(i)-1];
                dir_.write(i);
            self.directory = i;
        else:
            console.error("Error: Path was not found");
    
    #OPEN CODE

    def open(self):
        i = input(cmdSep+" ");
        if(os.path.exists(i)):
            with open(i,"r") as dir_:
                self.formatter(dir_.read(),i);
        else:
            i = self.directory+"\\"+i;
            if(os.path.exists(i)):
                with open(i,"r") as dir_:
                    self.formatter(dir_.read(),i);
            else:
                console.error("Error: Path was not found");

    #CLEAR

    def clear(self):
        print("Clearing...");
        os.system("cls");
        
    #READ INPUT

    def run(self,i):
        # Change default directory command
        if(i == "chdir"):
            try:
                self.chdir();
            except Exception as err:
                console.error("Error changing directory.\n"+err);
                pass;
        if(i == "py+ compile"):
            try:
                self.open();
            except Exception as err:
                console.error("Error opening compiler.\n"+err);
                pass;
        if(i == "clear"):
            try:
                self.clear();
            except Exception as err:
                console.error("Error clearing command line.\n"+err);
                pass;

Console();
