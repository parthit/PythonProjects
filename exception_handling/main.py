#
# try:
#     file = open(file='a_file.txt', mode='r')
#     a_dictionary = {'key': 'value'}
#     # print(a_dictionary['key123'])
# except FileNotFoundError:
#     file = open(file='a_file.txt', mode='w')
#     file.write('This should be written but wont be')
# except KeyError as error_message:
#     print(f'That key does not exist: {error_message}')
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print('File was closed.')

height = float(input("Enter height"))
weight = float(input("Enter weigth"))

if height > 3:
    raise ValueError("This can't be a real height for a normal human")

bmi = weight / height ** 2
print(bmi)