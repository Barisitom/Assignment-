# I created an array and was pulling the data from the array
print( "\nA son sucessfully completed his secondary Education was asked by his father son where are you heading from now hence forte do want to further your learning to 'high school', 'still' and 'None' \n")
answer = input('answer please HIGH SCHOOL, SKILL,  NONE: ')

arr = ['Perfect, what course please? COMPUTER PROGRAMING, PUBLIC HEALTH and MEDICINE: ',
    'Nice son, what skill please? HAIR STYLIST, CATERER and BARBER: ',
    'then what do you want Games? FOOTBALL PLAYER, TENNIS PLAYER and GOLFER: ',
    'choose from the option displayed ' 
]
arr2  =['great you made a right choice','i love your choice', 'son perfect', 
        'choose from the option beside'

]
arr3  =['awesome choice son', 'good to go son', 'magnificent son', 
        'choose from the option beside'
]
arr4  =['awesome choice ', 'like it son', 'okay son', 'choose from the option beside']


if answer.lower() == 'high school':
    ans = input(arr[0])
    if ans.lower() == 'computer programing':
        print(arr2[0])
    elif ans.lower() == 'public health':
        print(arr2[1]) 
    elif ans.lower() == 'medicine':
        print(arr2[2])     
    else:
        print(arr2[3])
    
elif answer.lower() == 'skill':
    ans2 = input(arr[1])
    if ans2.lower() == 'hair stylist':
        print(arr3[0])
    elif ans2.lower() == 'caterer':
        print(arr3[1]) 
    elif ans2.lower() == 'barber':
        print(arr3[2]) 
    else:
        print(arr3[3])

elif answer.lower() == 'none': 
    ans3 = input(arr[2] )
    if ans3.lower() == 'football player':
        print(arr4[0])
    elif ans3.lower() == 'tennis player':
        print(arr4[1]) 
    elif ans3.lower() == 'golfer':
        print(arr4[2]) 
    else:
        print(arr4[3])

else:
    print(arr[3])
