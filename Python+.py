import time as t, os;

__startTime__ = -99999999;

class Main():
    def find_nth(haystack, needle, n):
        start = haystack.find(needle);
        while(start >= 0 and n > 1):
            start = haystack.find(needle, start+len(needle));
            n -= 1;
        return start+1;
    def compile_(txt):
        
        if(len(txt)<1): return 0;
        
        endtxt=[];

        #MAKE READABLE
        
        for i,v in enumerate(txt):
            seperators = v.count(";");
            val = v;
            if(v.count==0): continue;
            previousValue = 0;
            for x in range(seperators):
                f = Main.find_nth(val,";",x+1);
                endtxt.append(val[previousValue:f]);
                if(f+1<len(val)): #IF IT ISN'T THE FINAL ; OF A LINE
                    if(val[f]==" "):
                        previousValue = f+1;
                        continue;
                previousValue = f;
        
        #COMPILE

        for i,v in enumerate(endtxt):

            #PRINT
            if(v[0:6] == "print("):
                endParanthesis = v.find(")");
                printedText = v[6:endParanthesis];
                if printedText.isdigit() == True: print(int(printedText)); continue;
                if isinstance(printedText,float) == True: print(float(printedText)); continue;
                if printedText[0]+printedText[len(printedText)-1] == "''" or printedText[0]+printedText[len(printedText)-1] == '""':
                    printedText = printedText[1:len(printedText)-1];
                else:
                    if(printedText.find(",") == -1): printedText = Vars.variables[printedText][0]; print(printedText); continue;
                    preInt = 0;
                    allVars = [];
                    for ind,va in enumerate(printedText):
                        if(va == ","):
                            allVars.append(printedText[preInt:ind]);
                            preInt = ind+1;
                        if(ind+1==len(printedText)):
                            allVars.append(printedText[preInt:len(printedText)]);
                    printedText = "";
                    for ind,va in enumerate(allVars):
                        if(ind==0):
                            if(allVars[ind].isdigit()): printedText += str(allVars[ind]); continue;
                            if(allVars[ind][0]+allVars[ind][len(allVars[ind])-1] == '""' or allVars[ind][0]+allVars[ind][len(allVars[ind])-1] == "''"):
                                printedText += str(allVars[ind][1:len(allVars[ind])-1]);
                                continue;
                            printedText += str(Vars.variables[allVars[ind]][0]);
                            continue;
                        if(allVars[ind].isdigit()): printedText += " "+str(allVars[ind]); continue;
                        if(allVars[ind][0]+allVars[ind][len(allVars[ind])-1] == '""' or allVars[ind][0]+allVars[ind][len(allVars[ind])-1] == "''"):
                            printedText += " "+str(allVars[ind][1:len(allVars[ind])-1]);
                            continue;
                        printedText += " "+str(Vars.variables[allVars[ind]][0]);
                print(printedText);
                continue;


            #VARIABLES


            #INTEGER VARIABLE
            
            if(v[0:3] == "int"):
                if(v[3] != " "): raise ValueError("Method "+v+" was not found.");
                if(v.find("==") != -1): raise ValueError("Inappropriate value (in "+v+")");
                endOfValue = Main.find_nth(v," ",2);
                NewVariable = v[4:endOfValue-1];
                NewValue = v[v.find("=")+2:len(v)-1];
                try:
                    NewValue = int(eval(NewValue));
                except ValueError:
                    raise ValueError("Inoperable type at "+v+" (Expected int, got "+type(NewValue));
                if(NewVariable in Vars.variables):
                    if(Vars.variables[NewVariable][1] == "const"):
                        raise ValueError("Cannot edit a constant. At "+v);
                Vars.variables[NewVariable] = NewValue,"int";
                continue;

            #CONSTANT VARIABLE
            
            if(v[0:5] == "const"):

                #CONST STRING
                
                if(v[5:9] == " str"):
                    if(v[9] != " "): raise ValueError("Method "+v+" was not found.");
                    if(v.find("==") != -1): raise ValueError("Inappropriate value (in "+v+")");
                    endOfValue = Main.find_nth(v," ",3);
                    NewVariable = v[10:endOfValue-1];
                    NewValue = v[v.find("=")+2:len(v)-1];
                    if(NewValue[0]+NewValue[len(NewValue)-1] != '""' and NewValue[0]+NewValue[len(NewValue)-1] != "''"):
                        raise ValueError("Inoperable type at "+v+" (Expected str, got "+type(NewValue));
                    NewValue = NewValue[1:len(NewValue)-1];
                    
                    if(NewVariable in Vars.variables):
                        raise ValueError("Cannot edit a constant.");
                    else:
                        Vars.variables[NewVariable] = NewValue,"const";
                    continue;

                #CONST INT

                if(v[5:9] == " int"):
                    if(v[9] != " "): raise ValueError("Method "+v+" was not found.");
                    if(v.find("==") != -1): raise ValueError("Inappropriate value (in "+v+")");
                    endOfValue = Main.find_nth(v," ",3);
                    NewVariable = v[10:endOfValue-1];
                    NewValue = v[v.find("=")+2:len(v)-1];
                    try:
                        NewValue = int(eval(NewValue));
                    except ValueError:
                        raise ValueError("Inoperable type at "+v+" (Expected int, got "+type(NewValue));
                    
                    if(NewVariable in Vars.variables):
                        raise ValueError("Cannot edit a constant.");
                    else:
                        Vars.variables[NewVariable] = NewValue,"const";
                    continue;

                #CONST DOUBLE

                if(v[0:6] == "double"):
                    if(v[6] != " "): raise ValueError("Method "+v+" was not found.");
                    if(v.find("==") != -1): raise ValueError("Inappropriate value (in "+v+")");
                    endOfValue = Main.find_nth(v," ",2);
                    NewVariable = v[7:endOfValue-1];
                    NewValue = v[v.find("=")+2:len(v)-1];
                    try:
                        NewValue = float(eval(NewValue));
                    except ValueError:
                        raise ValueError("Inoperable type at "+v+" (Expected double, got "+type(NewValue));
                    if(NewVariable in Vars.variables):
                        raise ValueError("Cannot edit a constant.");
                    else:
                        Vars.variables[NewVariable] = NewValue,"const";
                    continue;
                
            #DOUBLE VARIABLE
            
            if(v[0:6] == "double"):
                if(v[6] != " "): raise ValueError("Method "+v+" was not found.");
                if(v.find("==") != -1): raise ValueError("Inappropriate value (in "+v+")");
                endOfValue = Main.find_nth(v," ",2);
                NewVariable = v[7:endOfValue-1];
                NewValue = v[v.find("=")+2:len(v)-1];
                try:
                    NewValue = float(eval(NewValue));
                except ValueError:
                    raise ValueError("Inoperable type at "+v+" (Expected double, got "+type(NewValue));
                if(NewVariable in Vars.variables):
                    if(Vars.variables[NewVariable][1] == "const"):
                        raise ValueError("Cannot edit a constant. At "+v);
                Vars.variables[NewVariable] = NewValue,"double";
                continue;
            
            #STRING VARIABLE
            
            if(v[0:3] == "str"):
                if(v[3] != " "): raise ValueError("Method "+v+" was not found.");
                if(v.find("==") != -1): raise ValueError("Inappropriate value (in "+v+")");
                endOfValue = Main.find_nth(v," ",2);
                NewVariable = v[4:endOfValue-1];
                NewValue = v[v.find("=")+2:len(v)-1];
                if(NewValue[0]+NewValue[len(NewValue)-1] != '""' and NewValue[0]+NewValue[len(NewValue)-1] != "''"):
                    raise ValueError("Inoperable type at "+v+" (Expected str, got "+type(NewValue));
                if(NewVariable in Vars.variables):
                    if(Vars.variables[NewVariable][1] == "const"):
                        raise ValueError("Cannot edit a constant. At "+v);
                NewValue = NewValue[1:len(NewValue)-1];
                Vars.variables[NewVariable] = NewValue,"str";
                continue;


            #COMMENTS + WHITESPACE

            
            if(v[0:2] == "//"):
                continue;
            if(v == ""):
                continue;

            #IF THE METHOD IS NOT FOUND, RAISE AN ERROR
            
            raise ValueError("Method "+v+" was not found.");
        
    def main():
        global __startTime__;
        path = input("Path: ");
        __startTime__ = t.time(); #START CLOCK
        if(os.path.exists(path) != True): print("Path does not exist"); return -1; #PATH EXISTS
        if(5>len(path)): print("Too small"); return -1; #PATH EXTENSION IS TOO SMALL
        if(path[len(path)-4:len(path)] != ".py+"): print("Incompatible file type (use .py+)"); return -1; #INCORRECT PATH EXTENSION
        
        with open(path) as file:
            txt = file.readlines();
        Compile = Main.compile_(txt);
        
        if(Compile == 0): return 0;
        
        return 1;

class Vars():
    variables = {};

Vars.variables["%pi%"] = 3.141592653589793, "const";

mClass = Main.main();
__endTime__ = t.time(); #END CLOCK
print("Process finished in",round(__endTime__-__startTime__,7),"seconds with exit code",mClass);
