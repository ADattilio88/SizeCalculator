#Annalisa Dattilio
#This program will allow the user to enter their size/measurements and be able to find their perfect size across online clothing stores domestically and internationally
mylist = list(("Nike", "Cotton On"))
for x in range(len(mylist)):
    print(mylist[x])

#how to show only the sizes for store user selects
user_store_selection = str(input("Please select a store from the list above: "))
#if user_store_selection == "nike":
    # print what
#elif user_store_selection == "cotton on":
    #print what
#else:
    #print("Please only select stores from the list.")

#NIKE(Women's Bottoms)
#https://www.nike.com/size-fit/womens-bottoms-alpha - Nike women's size chart


#Waist size in inches
    
Nike_waist_size_XXS_low = 21.25
Nike_waist_size_XXS_high = 23.5
Nike_waist_size_XS_low = 23.5
Nike_waist_size_XS_high = 26
Nike_waist_size_S_low = 26
Nike_waist_size_S_high = 29
Nike_waist_size_M_low = 29
Nike_waist_size_M_high = 31.5
Nike_waist_size_L_low = 31.5
Nike_waist_size_L_high = 34.5
Nike_waist_size_XL_low = 34.5
Nike_waist_size_XL_high = 38.5
Nike_waist_size__XXL_low = 38.5
Nike_waist_size__XXL_high = 42.5


#Hip size in inches

Nike_hip_size_XXS_low = 30.5
Nike_hip_size_XXS_high = 33
Nike_hip__size_XS_low = 33
Nike_hip__size_XS_high = 35.5
Nike_hip_size_S_low = 35.5
Nike_hip_size_S_high = 38.5
Nike_hip_size_M_low = 38.5
Nike_hip_size_M_high = 41
Nike_hip_size_L_low = 41
Nike_hip_size_L_high = 44
Nike_hip_size_XL_low = 44
Nike_hip_size_XL_high = 47
Nike_hip_size_XXL_low = 47
Nike_hip_size_XXL_high = 50

 
#Height in inches

Nike_height_XXS_low = 64
Nike_height_XXS_high = 68
Nike_height_XS_low = 64
Nike_height_XS_high = 68
Nike_height_S_low = 64
Nike_height_S_high = 68
Nike_height_M_low = 64
Nike_height_M_high = 68
Nike_height_L_low = 64
Nike_height_L_high = 68
Nike_height_XL_low = 64
Nike_height_XL_high = 68
Nike_height_XXL_low = 64
Nike_height_XXL_high = 68

user_waist_size = int(input("Enter waist size in centimeters: "))
print(user_waist_size / 2.54, end= " in. ") # the / operator is used to convert centimeters to inches through division
user_waist_size_in = user_waist_size / 2.54

user_hip_size = int(input("\nEnter hip size in centimeters: "))
print(user_hip_size * 0.393701, end= " in. ") # the * operator is used to convert centimeters to inches through multiplication
user_hip_size_in = user_hip_size * 0.393701

user_height = int(input("\nEnter height in centimeters: "))
print(user_height / 2.54, end= " in.")
user_height_in = user_height / 2.54


#waist size

if user_waist_size_in > 21.25 and user_waist_size_in < 23:
    print("\nYour waist fits size", "XXS", sep=": ")
if user_waist_size_in > 23.5 and user_waist_size_in < 26:
    print("\nYour waist fits size", "XS", sep=": ")
if user_waist_size_in > 26 and user_waist_size_in < 29:
    print("\nYour waist fits size", "S", sep=": ")
if user_waist_size_in > 29 and user_waist_size_in < 31.5:
    print("\nYour waist fits size", "M", sep=": ")
if user_waist_size_in > 31.5 and user_waist_size_in < 34.5:
    print("\nYour waist fits size", "L", sep=": ")
if user_waist_size_in > 34.5 and user_waist_size_in < 38.5:
    print("\nYour waist fits size", "XL", sep=": ")
if user_waist_size_in > 38.5 and user_waist_size_in < 42.5:
    print("\nYour waist fits size", "XXL", sep=": ")


#hip size
    
if user_hip_size_in > 30.5 and user_hip_size_in < 33:
    print("Your hips fit size", "XXS", sep=": ")
if user_hip_size_in > 33 and user_hip_size_in < 35.5:
    print("Your hips fit size", "XS", sep=": ")
if user_hip_size_in > 35.5 and user_hip_size_in < 38.5:
    print("Your hips fit size", "S", sep=": ")
if user_hip_size_in > 38.5 and user_hip_size_in < 41:
    print("Your hips fit size", "M", sep=": ")
if user_hip_size_in > 41 and user_hip_size_in < 44:
    print("Your hips fit size", "L", sep=":")
if user_hip_size_in > 44 and user_hip_size_in < 47:
    print("Your hips fit size", "XL", sep=": ")
if user_hip_size_in > 47 and user_hip_size_in < 50:
    print("Your hips fit size", "XXL", sep=": ")

#height
if user_height < 64 or user_height > 68:
    print("-If your height is below 5ft. 4in. know the pant legs will be slightly longer and may be baggy.\n-If your height is above 5ft. 8 in. know the pants will fit above the ankle")

#SPRINT 2


#COTTON ON(Women's Bottoms)
#https://cottonon.com/us/size-guide.html?gclid=Cj0KCQiA7bucBhCeARIsAIOwr--1ciZ5xW1MV06odv9bOfZkwd0VsflsiPgMhUOBfi0B5G0FwPpOWpcaAjuzEALw_wcB

#waist size
Cottonon_waist_size_xxxs_low = 21.6
Cottonon_waist_size_xxxs_high = 23.6
Cottonon_waist_size_xxs_low = 23.6
Cottonon_waist_size_xxs_high = 25.6
Cottonon_waist_size_xs_low = 25.6
Cottonon_waist_size_xs_high = 27.6
Cottonon_waist_size_s_low = 27.6
Cottonon_waist_size_s_high = 29.6
Cottonon_waist_size_m_low = 29.6
Cottonon_waist_size_m_high = 31.6
Cottonon_waist_size_l_low = 31.6
Cottonon_waist_size_l_high = 33.6
Cottonon_waist_size_xl_low = 33.6

#hip size
Cottonon_hip_size_xxxs_low = 31.6
Cottonon_hip_size_xxxs_high = 33.6
Cottonon_hip_size_xxs_low = 33.6
Cottonon_hip_size_xxs_high = 35.6
Cottonon_hip_size_xs_low = 35.6
Cotton_hip_size_xs_high = 37.6
Cottonon_hip_size_s_low = 37.6
Cottonon_hip_size_s_high = 39.6
Cottonon_hip_size_m_low = 39.6
Cottonon_hip_size_m_high = 41.6
Cottonon_hip_size_l_low = 41.6
Cottonon_hip_size_l_high = 43.6
Cottonon_hip_size_xl_low = 43.6

#WAIST SIZE
if user_waist_size_in > 21.6 and user_waist_size_in < 23.6:
    print("\nYour waist fits size", "0", sep=": ")
if user_waist_size_in > 23.6 and user_waist_size_in < 25.6:
    print("\nYour waist fits size", "2", sep=": ")
if user_waist_size_in > 25.6 and user_waist_size_in < 27.6:
    print("\nYour waist fits size", "4", sep=": ")
if user_waist_size_in > 27.6 and user_waist_size_in < 29.6:
    print("\nYour waist fits size", "6", sep=": ")
if user_waist_size_in > 29.6 and user_waist_size_in < 31.6:
    print("\nYour waist fits size", "8", sep=": ")
if user_waist_size_in > 31.6 and user_waist_size_in < 33.6:
    print("\nYour waist fits size", "10", sep=": ")
if user_waist_size_in > 33.6 and user_waist_size_in < 33.7:
    print("\nYour waist fits size", "12", sep=": ")

#HIP SIZE
if user_hip_size_in > 31.6 and user_hip_size_in < 33.6:
    print("\nYour hips fit size", "0", sep=": ")
if user_hip_size_in > 33.6 and user_hip_size_in < 35.6:
    print("\nYour hips fit size", "2", sep=": ")
if user_hip_size_in > 35.6 and user_hip_size_in < 37.6:
    print("\nYour hips fit size", "4", sep=": ")
if user_hip_size_in > 37.6 and user_hip_size_in < 39.6:
    print("\nYour hips fit size", "6", sep=": ")
if user_hip_size_in > 39.6 and user_hip_size_in < 41.6:
    print("\nYour hips fit size", "8", sep=": ")
if user_hip_size_in > 41.6 and user_hip_size_in < 43.6:
    print("\nYour hips fit size", "10", sep=": ")
if user_hip_size_in > 43.6 and user_hip_size_in < 43.7:
    print("\nYour hips fit size", "12", sep=": ")

user_waist_size != user_hip_size

    
#store does not carry your size. would you like to try a dufferent store? select y to continue or n to quit
answer = input("Would you like to continue? Enter yes or no: ")
#if answer == "yes":
    #what here (i want to prompt to run the program again)
#elif answer == "no":
    #what here (if no i want the program to stop and end there)
#else:
    #print("Please enter yes or no.")

#if(Nike_waist_size > 23.5 or Nike < 30
#if out of range, print store does not carry size


#additional websites used for assistance:
#https://www.w3schools.com/python/default.asp
#https://www.folkstalk.com/tech/how-to-ask-a-yes-or-no-question-on-python-with-code-examples/
