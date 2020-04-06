import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


df = pd.read_excel('Задача.xlsx')
columns = ['Person', 'Age', 'Driving experience', 'Loss', 'Salary level']
data = pd.DataFrame()
for col in zip(df.columns, columns):
    data[col[1]] = df[col[0]]
persons = list(data.pop('Person'))

scaler = StandardScaler()
X = scaler.fit_transform(data)
n_clusters = 3
km = KMeans(n_clusters=n_clusters)
data['Claster'] = km.fit_predict(X)

data['Persons'] = persons

dict_ = {
    0: {"Возраст, лет": data[data["Claster"] == 0]["Age"].median(),
        "Опыт вождения, лет": data[
            data["Claster"] == 0]["Driving experience"].median(),
        "Убыточность, %": data[data["Claster"] == 0]["Loss"].median(),
        "Уровень з/п, руб/год": data[
            data["Claster"] == 0]["Salary level"].median()},
    1: {"Возраст, лет": data[data["Claster"] == 1]["Age"].median(),
        "Опыт вождения, лет": data[
            data["Claster"] == 1]["Driving experience"].median(),
        "Убыточность, %": data[data["Claster"] == 1]["Loss"].median(),
        "Уровень з/п, руб/год": data[
            data["Claster"] == 1]["Salary level"].median()},
    2: {"Возраст, лет": data[data["Claster"] == 2]["Age"].median(),
        "Опыт вождения, лет": data[
            data["Claster"] == 2]["Driving experience"].median(),
        "Убыточность, %": data[data["Claster"] == 2]["Loss"].median(),
        "Уровень з/п, руб/год": data[
            data["Claster"] == 2]["Salary level"].median()}
    }
