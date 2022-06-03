import os, time, math;
from colorama import Fore;
from tkinter import *;

# ALL PRE-DEFINED VARIABLES

directory = open(os.getcwd()+"\\vars\\dir.txt","r");
cmdSep = ">>";

def find_nth(text, find, c):
    start = text.find(find);
    while(start >= 0 and c > 1):
        start = text.find(find, start+len(find));
        c -= 1;
    return start+1;

class KeyWords:
    mutli_char_keywords = ["print","return","func","let","class","true","false"];
    seperator = "\n";
    whitespace = " ";

class Console:
    def __init__(self):
        self.directory = directory.read();
        while(True):
            i = input(self.directory+cmdSep+" ");
            self.run(i);

    #COMPILER

    def compile(self,lc,path):
        path = path[0:path.find(".")]+".ppy+";
        with open(path,"w") as writeFile:
            writeFile.write(lc);
        print("Successfully compiled without errors!");
        
    #LEXXER

    def lex(self,code,path):
        SeperatedCode = [];
        seperations = code.count("\n")+1;
        LexxedCode = "";
        prev = 0;

        for i in range(seperations):
            # BRANCHLESS WAY OF SAYING IF IT IS THE LAST ITERATION, MAKE IT THE FULL LENGTH OF THE STRING
            nth = (find_nth(code,KeyWords.seperator,i+1),len(code))[(seperations-i)*len(code) < len(code)+1];
            # REMOVE '\n' AND INDENTS
            c = code[prev:nth].replace("\n","");
            tabs = "";
            for x,v in enumerate(c):
                if(v == " "):
                    tabs += v;
                    continue;
                break;
            tabs = tabs.replace("    ","\t").replace("\t","1");
            if(" " in tabs):
                print(f'{Fore.RED}Error: Expected indentation at line: ',str(i+1)+"\n"+c.lstrip());
                return -1;
            c = tabs+c.lstrip();
            SeperatedCode.append(c);
            prev = nth;

        # LEX

        for i,line in enumerate(SeperatedCode):
            c = line;
            #if(c in KeyWords.mutli_char_keywords):
            LexxedCode += c + "0";

        self.compile(LexxedCode,path);
        
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
            print("Error 0: Path was not found");
    
    #OPEN CODE

    def open(self):
        i = input(cmdSep+" ");
        if(os.path.exists(i)):
            with open(i,"r") as dir_:
                self.lex(dir_.read(),i);
        else:
            i = self.directory+"\\"+i;
            if(os.path.exists(i)):
                with open(i,"r") as dir_:
                    self.lex(dir_.read(),i);
            else:
                print("Error 0: Path was not found");

    #CLEAR

    def clear(self):
        print("Clearing...");
        os.system("cls");
        
    #READ INPUT

    def run(self,i):
        # Change default directory command
        if(i == "chdir"):
            self.chdir();
        if(i == "py+ compile"):
            self.open();
        if(i == "clear"):
            self.clear();

Console();
