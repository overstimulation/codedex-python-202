poland_womens_epee_2023 = [
    {
        'name': 'Renata Knapik-Miazga',
        'age': 36,
        'height': 1.82,
        'handedness': 'Left-handed',
        'ranking': 60
    },
    {
        'name': 'Magdalena Pawłowska',
        'age': 31,
        'height': 1.78,
        'handedness': 'Left-handed',
        'ranking': 145
    },
    {
        'name': 'Martyna Swatowska-Wenglarczyk',
        'age': 30,
        'height': 1.72,
        'handedness': 'Left-handed',
        'ranking': 50
    },
    {
        'name': 'Ewa Trzebińska',
        'age': 35,
        'height': 1.76,
        'handedness': 'Right-handed',
        'ranking': 163
    }
]

print('Team members:')
for i in range(0, 4):
      print('- {}'.format(poland_womens_epee_2023[i]['name']))

poland_womens_epee_2023[3]['ranking'] = 160

average_age = sum(member['age'] for member in poland_womens_epee_2023) / len(poland_womens_epee_2023)
print(f'Average age: {int(average_age)}')

average_height = sum(member['height'] for member in poland_womens_epee_2023) / len(poland_womens_epee_2023)
print(f'Average height: {average_height}')

average_ranking = sum(member['ranking'] for member in poland_womens_epee_2023) / len(poland_womens_epee_2023)
print(f'Average ranking: {int(average_ranking)}')