'''
Md. Riadul Islam
20151006010
'''

import Queue
##Single Line Comment Chack
from _ast import AST, Num
from heapq import heappush

mainLoc=Queue.PriorityQueue()
mainData={}

print ""

def linePrint():
    line=""
    for i in range(70):
        line+="_"
    return line+"\n"

def SingleLineCommentChack(data):
    while ((data.find("//")) != -1):
        beg=data.find("//")
        end=data.find("\n",beg)+1
        sub=data[beg:end]
        data=data.replace(sub,"")
    return data
##Multi Line Comment Chack
def MultilineCommentChack(data):
    while ((data.find("/*")) != -1):
        beg = data.find("/*")
        end = data.find("*/", beg)+2
        sub = data[beg:end]
        data = data.replace(sub, "")
    return data

##Keyword Chack
def KeywordChack(data):
    key=open("Keywords.cpp","r")
    keywords="\n_____________\nKeyword\n-------------\n"
    keyword=key.read().split()
    #data=data.split()
    for i in range(len(data)):
        for j in range(len(keyword)):
            if(data[i:i+len(keyword[j])]==keyword[j]):
                keywords=keywords+keyword[j]+"\n"
                mainLoc.put(i)
                mainData[i] = `i` + "    \t" + keyword[j] + " \t\t\tKeywords\t\t\t"+keyword[j]+"\n" + linePrint()
                break;
    return keywords

##Header File Chack
def HeaderFileChack(data):
    header="\n_____________\nHeader File\n-------------\n"
    loc=0
    beg=end=0
    while ((data.find("<")) != -1 and data.find(">", beg) !=-1):
        beg = data.find("<")
        end = data.find(">", beg)+1
        sub = data[beg:end]
        data = data.replace(sub, "")
        header = header+sub[1:len(sub)-1]+"\n"
        mainLoc.put(beg+1+loc)
        mainData[beg+1+loc] = `beg+1+loc` + "\t" + sub[1:len(sub)-1] + "\t\tHeader File\t\t\t-\n" + linePrint()
        loc += len(sub)

    return header

##Variable Chack
def VariableChack(data):
    key = open("DataType.cpp", "r")
    variable = "\n_____________\nVariable\n-------------\n"
    dataType= key.read().split("\n")
    #data=data.split()
    chack=0
    temp=""
    i=0
    while i < len(data):
        for j in range(len(dataType)):

            if (data[i:i+len(dataType[j])] == dataType[j]):
                i=i+len(dataType[j])+1
                while True:
                    if data[i]=="=":
                        variable=variable+" -> "+dataType[j]+"\n"
                        mainData[chack] = `chack` + "\t\t" + temp + "\t\t\tId\t\t\t" + dataType[j] + "\n" + linePrint()
                        if(data.find(",",i) !=-1 and data.find(";\n",i) !=-1):
                           t1=data.find(",",i)
                           t2 = data.find(";\n", i)
                           if t1>t2:
                               i=t2
                               chack = 0
                               temp = ""
                               break
                           elif t2>t1:
                               i=t1
                        chack = 0
                        temp = ""

                    elif data[i]==",":
                        variable=variable+" -> "+dataType[j]+"\n"
                        mainData[chack] = `chack` + "\t\t" + temp + "\t\t\tId\t\t\t" + dataType[j] + "\n" + linePrint()
                        chack = 0
                        temp = ""
                    elif data[i]==";" or  data[i]==")":
                        variable =variable+ "->" + dataType[j] + "\n"
                        i=i+1
                        break
                    elif data[i]=="(":
                        variable =variable+ "() -> " + dataType[j] + "\n"
                        temp+=" ()"
                        break
                    elif data[i]=="\n" :
                        variable =variable+ " -> " + dataType[j] + "\n"
                        break
                    else:
                        if chack==0:
                            mainLoc.put(i)
                            chack=i
                        variable =variable+ data[i]
                        temp+=data[i]
                    i =i+1
                mainData[chack] = `chack` + "\t\t" + temp + "\t\t\tId\t\t\t" + dataType[j] + "\n" + linePrint()
                chack = 0
                temp = ""
                break
        i=i+1
    return variable

##Special Symbol Chack
def SpecialCharactersChack(data):
    specialFile=open("Ascii.cpp","r")
    special="\n_____________\nSpecial Symbol\n-------------\n"
    specialValue=specialFile.read().split("\n")
    for i in range(len(data)):
        for j in range(len(specialValue)):
            if(data[i]==specialValue[j][0]):
                special=special+specialValue[j]+"\n"
                mainLoc.put(i)
                mainData[i] = `i`+"\t\t"+data[i]+"\t\tSpecial Symbol\t\t"+specialValue[j][2:]+"\n"+linePrint()
                break;
    return special

##Number Chack
def NumberChack(data):
    numberFile=open("Number.cpp","r")
    number="\n_____________\nNumber Value\n-------------\n"
    numberValue=numberFile.read().split("\n")
    chack=0
    i=0
    temp=""
    count=0
    while i < len(data) :
        for j in range(len(numberValue)):
            if (data[i] == numberValue[j]):
                if chack == 0 :
                    chack = int(i)


                temp+= data[i]
                break
            count+=1
        if chack !=0 and count ==len(numberValue) :
            if temp.find(".") != -1 and temp.find("f") != -1:
               number = number + temp +" -> Float" "\n"
               mainLoc.put(chack)
               mainData[chack] = `chack` + "\t\t" + temp + "\t\t\tNumber\t\t\tFloat\n" + linePrint()
            elif temp.find(".") != -1 :
                number = number + temp + " -> Double" "\n"
                mainLoc.put(chack)
                mainData[chack] = `chack` + "\t\t" + temp + "\t\t\tNumber\t\t\tDouble\n" + linePrint()

            elif temp.find("f") == -1:
                number = number + temp + " -> Int" "\n"
                mainLoc.put(chack)
                mainData[chack] = `chack` + "\t\t" + temp + "\t\t\tNumber\t\t\tInt\n" + linePrint()
            temp=""
            chack=0
        count = 0
        i+=1

    return number

##Outputs
def Outputs():
    newData="\n\nOutputes\n"+linePrint()+"Location\tLexemes\t\tToken Name\t\tAttribute Value\n"+linePrint()
    while not mainLoc.empty():
        newData+=("\t" + mainData[mainLoc.get()])
    return newData

fileRead=open("fileRead.cpp","r")
fileWrite=open("fileWrite.cpp","w")
data=fileRead.read()
data=SingleLineCommentChack(data) ##Single Line Comment Chack
data=MultilineCommentChack(data)  ##Multi Line Comment Chack
data=data+KeywordChack(data)+HeaderFileChack(data)+VariableChack(data)+SpecialCharactersChack(data)+NumberChack(data)+Outputs()
           ##Keyword Chack   ##Header File Chack    ##Variable Chack   ##special Chack    ## Number Cahck   ## Outputs
fileWrite.write(data)


