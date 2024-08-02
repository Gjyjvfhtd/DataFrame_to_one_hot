#Ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 

#lst = ['robot'] * 10
#lst += ['human'] * 10
#random.shuffle(lst)
#data = pd.DataFrame({'whoAmI': lst})
#return data

#Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?




import random           #Библиотека для рандомизации значений, тут нужна для создания DataFrame
import pandas as pd     #Библиотека для работы с DataFrame

def random_data_frame(): #Спрятал генератор DataFrame в функцию, чтобы не мешал)
    lst = ['robot'] * 10
    lst += ['human'] * 10
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI': lst})
    return data

data = random_data_frame()  #В этом блоке я загоняю все в csv файл - дальше работа будет вестись с ним
data.to_csv('who_i_am.csv')