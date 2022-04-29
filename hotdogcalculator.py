#Olaide Bamisile
#4/12/2022
#Hotdog cookout calculator

people = int(input('how many people will be attending: '))

print(people)

hotdogs_per_people = int(input('how many hotodgs will be given: '))

hotdogs = people * hotdogs_per_people

print(hotdogs)

buns = hotdogs // 8
hotdog = hotdogs // 10

print( buns, "packages of hotdog buns" )
print( hotdog, "packages of hotdog" )

buns_leftover = hotdogs % 8
hotdog_leftover = hotdogs % 10

print(buns_leftover, "hotdog buns will be leftover")
print(hotdog_leftover, "hotdogs will be leftover")
