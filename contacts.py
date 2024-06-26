contacts = {
    'number': 4,
    'students':
        [
            {'name': "Jason Abruzzo", 'email':'jason.abruzzo@gmail.com'},
            {'name': "Harry Potter", 'email':'harry@examply.com'},
            {'name': 'Hermione Granger', 'email': 'hermione@example.com'},
            {'name': 'Ron Weasley', 'email': 'ron@example.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])