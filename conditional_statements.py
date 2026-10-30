#  = int(input("enter score : "))

# if  == 50:
#     print("🏏")
# if  == 100:
#     print("⛑️")
# if  == 150:
#     print("💪")
# if  == 200:
#     print("🤸‍♂️")
# elif  < 50:
#     print()
# elif  > 50 nd  < 100:
#     print()
# elif  >100 nd  < 150:
#     print()
# elif  > 150 nd  < 200:
#     print()            

# if  >= 50:
#     print("🏏")
    
#     if  > 50 nd  < 100:
#      print()
     
# elif  >= 100:
#     print("⛑️")
      
#     if  > 100 nd  < 150:
#         print()
        
# elif  >= 150:
#     print("💪")
    
#     if  > 150 nd  < 200:
#         print()
        
# elif  >= 200:
#     print("🤸‍♂️")
#     print()

# print()
     
     
player_score = int(input("Enter player score : "))

if player_score > 200:
    print("🤸‍♂️")

elif player_score >= 150:
    print("💪")

elif player_score >= 100:
    print("⛑️")

elif player_score >= 50:
    print("🏏")

else:
    print("No achievement")

print(player_score)

#-----------------------------------------------------

player_score = int(input("Enter player score : "))


if player_score >= 50:   
    if player_score >= 100:
        if player_score >= 150:
            if player_score >= 200:
                print("🤸‍♂️")
            else:
                print("💪")
        else:
            print("⛑️")
    else:
        print("🏏")
        
print(player_score)