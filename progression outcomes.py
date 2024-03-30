# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20234063
# Date:14th December 2023


progression_list=[]
Progress=0
Module_trailer=0
Module_retriever=0
Exclude=0
Total=0

from graphics import *

def rect(point1,point2,color):
    rect=Rectangle(point1,point2)
    rect.setFill(color)
    rect.draw(win)

def message(point1,message_name,size=13,color="#778899"):
    message=Text(point1,message_name)
    message.setStyle("bold")
    message.setFace("arial")
    message.setTextColor(color)
    message.setSize(size)
    message.draw(win)

def multipleOutcome():
    while True:
        print("\nWould you like to enter another set of data?")
        choice=str(input("Enter 'y' for yes or 'q' to quit and view results:")).lower()
        
        if choice=="q":
            return "q"
        elif choice=="y":
            return "y"    
        else :
            print("\n*___Invalid input.Please try again!___*\n")

def progression_outcome(p, d, f):
    
    if p == 120 :
        return "Progress"
    elif p == 100:
        return "Progress (module trailer)"
    elif f>= 80:
        return "Exclude"
    elif f<80:
        return "Module retriever"

def graph():
    
    rect(Point(55, 360 - 10*Progress), Point(145, 360), "light green")
    rect(Point(155, 360 - 10*Module_trailer), Point(245, 360),"#778899")
    rect(Point(255, 360 - 10*Module_retriever),Point(345, 360),"#50c878")
    rect(Point(355, 360 - 10*Exclude),Point(445, 360), "#ffd1dc")
    
    message(Point(100,380),"Progress")
    message(Point(200,380),"Trailer")
    message(Point(300,380),"Retriever")
    message(Point(395,380),"Excluded")

    message(Point(100, 360 -10* Progress - 20),Progress)
    message(Point(200, 360 - 10* Module_trailer-20),Module_trailer)
    message(Point(300, 360 - 10*Module_retriever-20),Module_retriever)
    message(Point(400, 360 - 10*Exclude-20),Exclude)
    
    message(Point(160,20), "Histogram Results",17,"#343434")
    message(Point(190,405),"Outcomes in total",15)
    message(Point(70,405),Total,15) 
    aLine=Line(Point(30,360),Point(470,360))
    aLine.draw(win)

def text(file_name,progression_list):
    with open (file_name,'w') as f:
        for data in progression_list:
            f.write(f'{data[0]} - {data[1]}, {data[2]}, {data[3]}\n')
        
def read(file_name):
    with open (file_name,'r') as f:
        lines=f.readlines()
        for line in lines:
            print(line.strip())

def textFile():
    
    print("\nPart 2:")
    for data in progression_list:
        print(f'{data[0]} - {data[1]}, {data[2]}, {data[3]}')
        
    text('progress.txt',progression_list)
    
    print("\nPart 3:")
    readed_programme=read('progress.txt')
    

while True:
    try:
        valid_range=[0, 20, 40, 60, 80,100,120]
        p=int(input("\nEnter the PASS credit: "))
        if p not in valid_range:
            print("Out of range")
            continue
        d=int(input("Enter the DEFER credit: "))
        if d not in valid_range:
            print("Out of range")
            continue
        f=int(input("Enter the FAIL credit: "))
        if f not in valid_range:
            print("Out of range")
            continue
        
        if (p+d+f) !=120:
            print("Total incorrect")
            continue

        outcome = progression_outcome(p, d, f)
        print(outcome)
        if outcome=='Progress':
            Progress+=1
        elif outcome=='Progress (module trailer)':
            Module_trailer+=1
        elif outcome=='Exclude':
            Exclude+=1
        elif outcome=='Module retriever':
            Module_retriever+=1

        Total=Progress+Module_trailer+Exclude+Module_retriever

        progression_store=(outcome,p,d,f)
        progress_list_store=progression_list.append(progression_store)

        choice=multipleOutcome()
        
        if choice=="q":
            win=GraphWin("Histogram",500,450)
            graph()
            win.getMouse() 
            
            textFile()
                            
            break
        
        elif choice=="y":
            continue
        
    except ValueError:
        print("Integer required")

