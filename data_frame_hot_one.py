#Ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 

#lst = ['robot'] * 10
#lst += ['human'] * 10
#random.shuffle(lst)
#data = pd.DataFrame({'whoAmI': lst})
#return data

#Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?




import random           #Библиотека для рандомизации значений, тут нужна для создания DataFrame
import pandas as pd     #Библиотека для работы с DataFrame

with open('who_i_am.csv','w'):             #обнуляю оба файла перед новым запуском программы
    pass

with open('result_who_i_am.csv','w'):
    pass

def random_data_frame(): #Спрятал генератор DataFrame в функцию, чтобы не мешал)
    lst = ['robot'] * 10
    lst += ['human'] * 10
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI': lst})
    return data

data = random_data_frame()  #В этом блоке я загоняю все в csv файл - дальше работа будет вестись с ним
data.to_csv('who_i_am.csv')

# df = pd.read_csv('who_i_am.csv')   #Тут читаем,  что записали 

data_dict = dict(data)        #Тут я решил занести все знвчения Data Frame в множество, для словаря
st = set()
for i in data_dict['whoAmI']:
    st.add(i)

res_df = dict() #Создаем словарь из которого дальше следаем Data Frame вида Hot One
for i in st:
    res_df[i] = [bool(0)] * len(data['whoAmI'])
j = 0

for i in data['whoAmI']:          #Заполняем Hot One вид
    res_df[i][j] = bool(1)
    j += 1

res_df = pd.DataFrame(res_df)          #Резульнат ухадит в новую табличку)
res_df.to_csv('result_who_i_am.csv')