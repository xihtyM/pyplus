import os, time, math;
from tkinter import *;

# ALL PRE-DEFINED VARIABLES

directory = open(os.getcwd()+"\\vars\\dir.txt","r");
cmdSep = ">>";

class KeyWords:
    mutli_char_keywords = ["print","return","func","let","class","true","false"];
    operators = ["!=", "==", "+=","-="];
    single_char_keywords = [";","\n","\\","*",'"',"'",":",".","[","]","(",")","{","}"];
    whitespace = " ";
    keywords = mutli_char_keywords + single_char_keywords + operators;

class Console:
    def __init__(self):
        self.directory = directory.read();
        while(True):
            i = input(self.directory+cmdSep+" ");
            self.run(i);

    #LEXXER

    def lex(self,code):
        #LOOP THROUGH EVERY CHAR OF THE CODE
        LexxedCode = "";
        for i,char in enumerate(code):
            if(char != KeyWords.whitespace):
                LexxedCode += char;
            if(i+1 < len(code)):
                if(code[i+1] == KeyWords.whitespace or code[i+1] in KeyWords.keywords or LexxedCode in KeyWords.keywords):
                    if(LexxedCode != ""):
                        print(LexxedCode.replace('\n', '<newline>'));
                        LexxedCode = "";
        print(LexxedCode);
    #CHANGE DIRECTORY
    
    def chdir(self):
        i = input(">> ");
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
        i = input(">> ");
        if(os.path.exists(i)):
            with open(i,"r") as dir_:
                self.lex(dir_.read());
        else:
            print("Error 0: Path was not found");
    
    #READ INPUT
    
    def run(self,i):
        # Change default directory command
        if(i == "chdir"):
            self.chdir();
        if(i == "py+ compile"):
            self.open();

Console();
