#If First Number Is greater than Second Number The Result will be the Addition of (First + Second) else it will be (First - Second)

#Write the First Number
First_Number= int(input("Enter your First Number :"))

#Write the Second Number
Second_Number= int(input("Enter your Second Number :"))

if First_Number > Second_Number :
 print (First_Number + Second_Number)
 
elif First_Number == Second_Number :
    print ("Both No Is Same")
    
else:
     print(First_Number - Second_Number)
     
