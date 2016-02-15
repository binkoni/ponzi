import time
month = 0
people = [0]
money = 1000
while True:
    print("month:",  month)
    people.append([0] * (2 ** (month + 1)))
    people[0] += money * (2 ** (month + 1))
    for i in range(1, month):
        for j in range(0, 2 ** i):
            if people[i][j] == 0:
                people[0] -= 1000
                people[i][j] += 1000
            else:
                people[0] -= people[i][j]
                people[i][j] *= 2
    print(people)
    month += 1
    time.sleep(1)
    

