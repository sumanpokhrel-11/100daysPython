#example 1
# import random
# student_name = ['john', 'sam', 'hari', 'floki']
# student_score = {name:random.randint(30,101) for name in student_name}
# print(student_score)
# passed_student  ={name:score for name, score in student_score.items() if score>=60}
# print(passed_student)

#exercise 1
sentence = 'What is the Airspeed Velocity of an Unladen Swollow?'

length_word = {word:len(word) for word in sentence.split()}
print(length_word)


#exercise 2

weather_c = {
    'Monday' : 12,
    'Tuesday' : 14,
    'Wednesday' : 15,
    'Thursday' : 14,
    'Friday' : 21,
    'Saturday' : 22,
    'Sunday' : 24
}

weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items() }
print(weather_f)