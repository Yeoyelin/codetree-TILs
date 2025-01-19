hospital_list = [0, 0, 0, 0]

for _ in range(3):
    symptom, temperature = input().split()
    temperature = int(temperature)

    if symptom == 'Y' and temperature >= 37:
        hospital_list[0] += 1
    elif symptom == 'N' and temperature >= 37:
        hospital_list[1] += 1
    elif symptom == 'Y':
        hospital_list[2] += 1
    else:
        hospital_list[3] += 1

for i in range(0, 4 , 1):
    print("%d" %(hospital_list[i]), end = " ")
if hospital_list[0] >= 2:
    print("E", end = " ")
