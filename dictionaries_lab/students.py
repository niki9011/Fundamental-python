text = input()
course_program = {}

while ":" in text:

    name, id, course = text.split(":")
    if course not in course_program.keys():
        course_program[course] = {}

    course_program[course][id] = name

    text = input()

    text = text.replace("_", " ")

for id in course_program[text]:
    print(f"{course_program[text][id]} - {id}")
