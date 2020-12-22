import numpy as np
import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
data = pd.read_csv("C:\\Users\\King\\Documents\\GitHub\\Recommende_System-for_Educational_Guidance\\Dataannotations.csv",sep=",", header=None)
# information = pd.read_csv(r'C:\\Users\\King\\Desktop\\prohect0\\majors-information.csv',sep=",", header=None)
information = pd.read_excel(r'C:\Users\King\Documents\GitHub\Recommende_System-for_Educational_Guidance\majors-information.xlsx', header=None)
# test=[1,0,1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,0,92,85,80,90,80,90,170,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
test=[1,0,1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,92,85,80,90,80,90,170,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

col=[]
for i in range(0,len(test)):col.append(i)
df = pd.DataFrame([test], columns = col)

loaded_model = pickle.load(open("C:/Users/King/Desktop/prohect0/model_knn.sav", 'rb'))

distances, indices = loaded_model.kneighbors(df,  n_neighbors=25)
print(distances, indices)


Specialty_number=[]

for col_indices in range(len(indices)):
    for r_indices in range(len(indices[0])):
        print(indices[col_indices][r_indices],"----",data[1][indices[col_indices][r_indices]],"----",distances[col_indices][r_indices])
        Specialty_number.append(data[1][indices[col_indices][r_indices]])



list_information=[]
for row_Specialty_number in range(len(Specialty_number)):
    for row_information in range(len(information[3])):
        if information[3][row_information] == Specialty_number[row_Specialty_number]:
            list_information.append(information.loc[row_information])


#العلمي 	الادبي	تجاري 	صناعي	التكنولوجي


list_data=[]
    #العلمي
if test[28]==1:
    list_data=list_information.copy()
    #ادبي
elif test[29]==1:
    for row in range(len(list_information)):
        if test[29]==list_information[row][9]:
            list_data.append(list_information[row])
    #تجاري
elif  test[30]==1:
    for row in range(len(list_information)):
        if test[30]==list_information[row][10]:
            list_data.append(list_information[row])
    #صناعي
elif test[31]==1:
    for row in range(len(list_information)):
        if test[31]==list_information[row][11]:
            list_data.append(list_information[row])
    #التكنولوجي
elif test[32]==1:
    for row in range(len(list_information)):
        if test[32]==list_information[row][12]:
            list_data.append(list_information[row])

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(pd.DataFrame(list_data))
