from tkinter import *
from math import*
from fractions import gcd
import re

def matrix(str1,str2,str3):
    print("")
    print("New Matrix:")
    x=[]
    y=[]
    z=[]
    newx=[]
    newx2=[]
    newLine2=[]
    newLine1=[]
    #### THE FOLLOWING CODE CONSISTS OF STRING MANIPULATION FOR THE INPUTED EQUATIONS.... YES ITS HIDEOUS....#####
    ### IT LOOKS FOR + or - SIGNS AND FINDS THE SINGLE OR DOUBLE DIGIT NUMBERS ####
    for i in range(len(str1)):
        str1+="hellooooo"
        if (re.findall('\d+', str1[i])) and (re.findall('\d+', str1[i-1])):
               if i!=0:
                    newstr=str1[i-1]+str1[i]
                    int1=int(newstr)
                    
                    if str1[i-1]=="-":
                      int1=int1-(2*int1)
                    x.append(int1)
               if i==0:
                  int1=int(str1[i])
                  if str1[i-2]=="-":
                            int1=int1-(2*int1)
                  x.append(int1)

                   
        elif (re.findall('\d+', str1[i])):
        
                int1=int(str1[i])
                if str1[i-1]=="-":
                            int1=int1-(2*int1)
                if (re.findall('\d+', str1[i+1])):
                    int1=int1
                else:
                   x.append(int1)
                
                
                
    for i in range(len(str2)):

        str2+="hellooooo"
        if (re.findall('\d+', str2[i])) and (re.findall('\d+', str2[i-1])):
               if i!=0:
                         newstr2=str2[i-1]+str2[i]
                         int2=int(newstr2)

                         if str2[i-2]=="-":
                            int2=int2-(2*int2)
                         y.append(int2)
               if i==0:
                  int2=int(str2[i])
                  if str2[i-1]=="-":
                       int2=int2-(2*int2)

                  y.append(int2)

                   
        elif (re.findall('\d+', str2[i])):
                
                int2=int(str2[i])
                if str2[i-1]=="-":
                            int2=int2-(2*int2)
                if (re.findall('\d+', str2[i+1])):
                    int2=int2
                else:
                    y.append(int2)

    for i in range(len(str3)):                  

        str3+="hellooooo"
        if (re.findall('\d+', str3[i])) and (re.findall('\d+', str3[i-1])):
               
               if i!=0:
                         newstr3=str3[i-1]+str3[i]
                         int3=int(newstr3)

                         if str3[i-2]=="-":
                            int3=int3-(2*int3)
                         z.append(int3)
               if i==0:
                  int3=int(str3[i])
                  if str3[i-1]=="-":
                            int3=int3-(2*int3)
                  z.append(int3)

        elif (re.findall('\d+', str3[i])):
                int3=int(str3[i])
                if str3[i-1]=="-":
                            int3=int3-(2*int3)
                if (re.findall('\d+', str3[i+1])):
                    int3=int3
                else:
                    z.append(int3)
       
    print(x)
    print(y)
    print(z)
    print("")
    #Math Starts Here

        #SecondTable
            
            #SecondRow
    newx.append(x[0]*y[0])
    newx.append(x[1]*y[0])
    newx.append(x[2]*y[0])
    newx.append(x[3]*y[0])
    
    
    y[0]=x[0]*y[0]
    y[1]=y[1]*x[0]
    y[2]=y[2]*x[0]
    y[3]=y[3]*x[0]
    
    line1i=newx[0]-y[0]
    line1ii=newx[1]-y[1]
    line1iii=newx[2]-y[2]
    line1iV=newx[3]-y[3]

           #ThirdRow
    newx2.append(x[0]*z[0])
    newx2.append(x[1]*z[0])
    newx2.append(x[2]*z[0])
    newx2.append(x[3]*z[0])
    
    z[0]=x[0]*z[0]
    z[1]=z[1]*x[0]
    z[2]=z[2]*x[0]
    z[3]=z[3]*x[0]
    
    line2i=newx2[0]-z[0]
    line2ii=newx2[1]-z[1]
    line2iii=newx2[2]-z[2]
    line2iV=newx2[3]-z[3]
    

        #ThirdTable
            #ThirdRow
    
    newLine1.append(line1ii*line2i)
    newLine1.append(line1ii*line2ii)
    newLine1.append(line1ii*line2iii)
    newLine1.append(line1ii*line2iV)

    newLine2.append(line2ii*line1i)
    newLine2.append(line2ii*line1ii)
    newLine2.append(line2ii*line1iii)
    newLine2.append(line2ii*line1iV)

    finalLine1=newLine2[0]-newLine1[0]
    finalLine2=newLine2[1]-newLine1[1]
    finalLine3=newLine2[2]-newLine1[2]

    finalLine4=newLine2[3]-newLine1[3]
    divider=gcd(finalLine3,finalLine4)
    if divider==0:
        divider=1
    finalLine3=finalLine3/divider
    finalLine4=finalLine4/divider

    if finalLine1==0 and finalLine2==0 and finalLine3==0 and finalLine4==0:
        xtest=(newLine2[3]/newLine2[1])
        ytest=(((newLine2[2])*-1)/newLine2[1])
        if ytest>0:
            
            newY="Y= " + str(xtest)+ "+" + str(ytest)+ "t"
        else:
            newY="Y= " + str(xtest)+ str(ytest)+ "t"        

        xtest2=xtest*x[1]*-1
        ytest2=ytest*x[1]*-1
        if ytest2>0:
            newY2=str(xtest2)+ "+" + str(ytest2)+ "t"
        else:
            newY2=str(ytest2)+ "t"

        newZ="Z= t"
        newZ2= int(x[2]*-1)
        tAdd=newZ2+ytest2
        intAdd=int(x[3])+int(xtest2)
        if intAdd==0:
            if tAdd>0:
                newX="X= " +str(tAdd)+"t"
            else:
               newX="X= "+ str(tAdd)+"t"
        else:
    
            if tAdd>0:
                newX="X= " + str(intAdd)+"+"+str(tAdd)+"t"
            else:
               newX="X= "+ str(intAdd)+str(tAdd)+"t"
            

        

        print("")
        print("Your planes intersect in a line with the equation")
        print(newX)
        print(newY)
        print(newZ)


#IF NO SOLUTION
    elif int(finalLine3)==0 and int(finalLine4)!=0:
            print("")
            print("Not all the planes intersect. No Solution.")

#Intersects at a point
    elif int(finalLine3)!=0 and int(finalLine4)!=0:

        pointZ=finalLine4/finalLine3
        pointY=(newLine2[3]-(pointZ*newLine2[2]))/newLine2[1]
        pointX=(x[3]-(x[1]*pointY)-(x[2]*pointZ))/x[0]
        finalX="X= " + str(pointX)
        finalY="Y= " + str(pointY)
        finalZ="Z= " + str(pointZ)
        print("")
        print("Your planes intersect at the point:")
        print(finalX)
        print(finalY)
        print(finalZ)

matrix("1x+2y+4z=19","3x-4y-4z=-1","1x+3y+1z=11")
matrix("1x-3y-2z=9","1x+11y+5z=-5","2x+8y+3z=4")
    

    

        
    
    

    
        
    
            
            


