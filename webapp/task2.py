import pandas as pd

df = pd.read_excel('выборка.xlsx', index_col=None)

persons1 = sorted(list(df["Участник 1"].values))
persons2 = sorted(list(df["Участник 2"].values))
all_persons = persons1 + persons2

all_persons = [i.split() for i in all_persons]

male = []
female = []
for i in all_persons:
    if i[2][-1] != 'а' and [i, all_persons.count(i)] not in male:
        male.append([i, all_persons.count(i)])
    else:
        if i[2][-1] == 'а' and[i, all_persons.count(i)] not in female:
            female.append([i, all_persons.count(i)])
male = sorted(male)
female = sorted(female)

possibly_relatives = []
for i in male:
    for j in female:
        if i[0][0] + 'а' in j[0][0]:
            possibly_relatives.append(
                [' '.join(i[0]), ' '.join(j[0]), i[1]+j[1]])

filtered_female = []
for i in range(1, len(female)):
    if ' '.join(female[i-1][0]) not in [j[1] for j in possibly_relatives]:
        filtered_female.append(female[i-1])


filtered_male = []
for i in range(1, len(male)):
    if ' '.join(male[i-1][0]) not in [j[0] for j in possibly_relatives]:
        filtered_male.append(male[i-1])


possibly_relatives = [i for i in possibly_relatives if i[2] >= 3]

filtered_female = [
    [' '.join(i[0]), i[1]] for i in filtered_female if i[1] >= 2]

filtered_male = [
    [' '.join(i[0]), i[1]] for i in filtered_male if i[1] >= 2]
