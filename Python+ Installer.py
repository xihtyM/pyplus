import os, requests;

# GIT URL - DO NOT CHANGE

url = "https://raw.githubusercontent.com/xihtyM/python_scripts/main/Python%2B/src/CMD.py";
text = requests.get(url).text;
text = text.replace('\r',"");

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop');

# ALL PROMPTS

prompt = ["Would you like to update an installation [Y/N]? ","Desktop Shortcut [Y/N] - Not working: ","Installation directory: ","Path of Python+ folder: "];
ind = 0;
short = False;

def addFiles(path,s,a):
    print("Installing cmd.py");
    with open(os.path.join(path,"cmd.py"),"w") as cmd:
        cmd.write(text);
    if(a):
        with open(os.path.join(path,"vars/dir.txt"),"w") as directory:
            directory.write(path);
    if(s):
        with open(os.path.join(desktop,"lmfao"),"w") as shrt:
            shrt.write("i am bad at coding");

while(True):
    i = input(prompt[ind]);

    if(ind == 0):
        i = i.lower();
        if(i == "y"):
            ind = 3;
            continue;
    if(ind == 1 and isinstance(i,str)):
        i = i.lower();
        if(i == "y"):
            short = True;
            ind += 1;
            continue;
        if(i == "n"):
            ind += 1;
            continue;
        print("Error: Please use Y or N");
        continue;
    
    if(ind == 2 and os.path.exists(i)):
        i = i.replace("\\","/");
        if(i[len(i)-1] == "/"):
            i = i[0:len(i)-1];
        try:
            os.mkdir(os.path.join(i,"Python+"));
            os.mkdir(os.path.join(i,"Python+/src"));
            os.mkdir(os.path.join(i,"Python+/src/vars"));
            addFiles(i+"/Python+/src",short,True);
            ind+=1;
        except WindowsError as e:
            print("Error:",e);
            continue;
    if(ind == 3 and os.path.exists(i)):
        if(os.path.exists(os.path.join(i,"Python+/src"))):
            addFiles(i+"/Python+/src",False,False);
            break;
        if(os.path.exists(os.path.join(i,"src"))):
            addFiles(i+"src",False,False);
            break;
        print("Creating files");
        if(os.path.exists(os.path.join(i,"Python+"))):
            os.mkdir(os.path.join(i,"Python+/src"));
            os.mkdir(os.path.join(i,"Python+/src/vars"));
            addFiles(i+"/Python+/src",False,True);
        else:
            os.mkdir(os.path.join(i,"src"));
            os.mkdir(os.path.join(i,"src/vars"));
            addFiles(i+"/src",False,True);
    break;
