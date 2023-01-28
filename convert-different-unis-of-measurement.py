# this program converts different unis of measurement
a=int(input("input an integer number between 1 to 6 to convert different unis of measurement:\n 1.Meter to Centimeter \n 2.Centimeter to Meter \n 3.Inch to Centimeter \n 4.Centimeter to Inch\n 5.Inch to Feet\n 6.Feet to Inch\n  "))
if 1<=a<=6:
 x=float(input("input the lenght:  "))
if a==1:
 print(x,"Meter is equal to",(x*100),"Centimeter")    
elif a==2:
 print(x,"Centimeter is equal to",(x/100),"Meter")      
elif a==3:
 print(x,"Inch is equal to",(x*2.54),"Centimeter")      
elif a==4:
 print(x,"Centimeter is equal to",(x/2.54),"Inch")        
elif a==5:
 print(x,"Inch is equal to",(x*0.083333),"Feet")    
elif a==6:
 print(x,"Feet is equal to",(x/0.083333),"Inch")      
else:
 print("You intered wrong option.\n Please input an integer number between 1 to 6 next time.")
