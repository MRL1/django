distance = 100
allDistance = 100
for i in range(10):
    distance = distance / 2
    allDistance = allDistance + distance
print(distance)
print(allDistance)

Sn = 100.0
Hn = Sn / 2

for n in range(2,11):

    Hn /= 2
    Sn += 2 * Hn

print('Total of road is %f' % Sn)
print('The tenth is %f meter' % Hn)
