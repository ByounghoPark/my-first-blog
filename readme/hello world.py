print("Hellw, Django girls!")

if 3 < 2:
    print("it works!")
else:
    print("oh my God!")

name = 'sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'sonja':
    print('Hey sonja')
else:
    print('Who are you?')

def hi(name):
    print('Hi ' + name + '!')

hi('Park')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Park']

for name in girls:
    hi(name)

for i in range(1, 6):
    print(i)

