from enum import Enum


# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr'))
class Month(Enum):
    JAN = 'Jan'
    FEB = 'Feb'
    MAR = 'Mar'
    APR = 'Apr'


for name, member in Month.__members__.items():
    print(f'{name}: {member} : {member.value}')

print('=' * 50)

print(Month.JAN == Month('Jan'))

print(Month.JAN)
print(Month.JAN.name)
print(Month.JAN.value)