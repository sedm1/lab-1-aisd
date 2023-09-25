results_of_the_polls = [set() for _ in range(8)]
person = set()
for student in open('students.txt', encoding='utf-8'):
    student = student.split()
    person.add(' '.join(student[:2]))
    for i in range(8):
        if student[i + 2] == 'да':
            results_of_the_polls[i].add(' '.join(student[:2]))

questions_list = open('questions.txt', encoding='utf-8').readlines()
for question_number in range(8):
    answer = input(questions_list[question_number])
    if answer.lower() == 'да':
        person = person & results_of_the_polls[question_number]
    else:
        person = person - results_of_the_polls[question_number]

    if len(person) == 1:
        print('Вы загадали ', *person, '.', sep='')
        break
    if len(person) == 0:
        print('Я не знаю такого студента!')
        break