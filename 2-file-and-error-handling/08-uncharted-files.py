sent_message = 'Hey there! This is a secret message.'
unsent_message = 'This message has been unsent.'

with open('sent_message.txt', 'w') as file:
  file.write(sent_message)

with open('sent_message.txt', 'r+') as file:
  original_message = file.read()
  file.seek(0)
  file.truncate(len(unsent_message))
  file.write(unsent_message)
  print(f'Original message: {original_message}')
  print(f'Unsent message: {unsent_message}')