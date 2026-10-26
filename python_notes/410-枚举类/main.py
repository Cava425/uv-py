from enum import Enum


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr'))


for name, member in Month.__members__.items():
    print(f'{name}: {member} : {member.value}')

print('=' * 50)

print(Month.Jan == 'Jan')