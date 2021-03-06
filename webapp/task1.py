import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import dill as pickle

df = pd.read_csv('Данные для задачи.txt', sep=';')
print(df['VEHICLE_MAKE'])
df = df.drop(columns=["VEHICLE_MAKE", "VEHICLE_MODEL",
                      "CLIENT_REGISTRATION_REGION"])

policy_branch = {"Москва": 0, "Санкт-Петербург": 1}
gender_values = {"M": 1, "F": 0}
policy_intermediary = {"N": 910}
policy_clm_n = {"1S": 0.5, "1L": 1.5, "4+": 4, "n/d": 2}
policy_clm_glt_n = {"1S": 0.5, "1L": 1.5, "4+": 4, "n/d": 2}
policy_prv_clm_n = {"1S": 0.5, "1L": 1.5, "4+": 4, "N": 2}
policy_prv_clm_glt_n = {"1S": 0.5, "1L": 1.5, "4+": 4, "N": 2}
policy_years_ren = {"N": 3}

df1 = df.replace({'POLICY_BRANCH': policy_branch,
                  'INSURER_GENDER': gender_values,
                  'POLICY_INTERMEDIARY': policy_intermediary,
                  'POLICY_CLM_N': policy_clm_n,
                  'POLICY_CLM_GLT_N': policy_clm_glt_n,
                  'POLICY_PRV_CLM_GLT_N': policy_prv_clm_glt_n,
                  'POLICY_YEARS_RENEWED_N': policy_years_ren,
                  'POLICY_PRV_CLM_N': policy_prv_clm_n})

df1["POLICY_CLM_N"] = df1["POLICY_CLM_N"].astype('float64')
df1["POLICY_CLM_GLT_N"] = df1["POLICY_CLM_GLT_N"].astype('float64')
df1["POLICY_PRV_CLM_N"] = df1["POLICY_PRV_CLM_N"].astype('float64')
df1["POLICY_PRV_CLM_GLT_N"] = df1["POLICY_PRV_CLM_GLT_N"].astype('float64')
df1["POLICY_YEARS_RENEWED_N"] = df1["POLICY_YEARS_RENEWED_N"].astype('float64')
df1["POLICY_INTERMEDIARY"] = df1["POLICY_INTERMEDIARY"].astype('float64')

df_train = df1[df1.DATA_TYPE == 'TRAIN']
df_test = df1[df1.DATA_TYPE != 'TRAIN']

df_train = df_train.drop(['DATA_TYPE'], axis=1)
df_test = df_test.drop(['DATA_TYPE'], axis=1)

X_train = df_train.drop(['POLICY_IS_RENEWED'], axis=1)
y_train = df_train['POLICY_IS_RENEWED']
X_test = df_test.drop(['POLICY_IS_RENEWED'], axis=1)
y_test = df_test['POLICY_IS_RENEWED']

classifier = RandomForestRegressor()
classifier.fit(X_train, y_train)

df_test["POLICY_IS_RENEWED"] = np.array(
    [int(i.round()) for i in classifier.predict(X_test)])

final_df = df_test[['POLICY_ID', 'POLICY_IS_RENEWED']]

with open('final.csv', 'w') as f:
    f.write(final_df.to_csv(index=False, sep=';'))

with open('./model/model.pkl', 'wb') as file:
    pickle.dump(classifier, file)

model_columns = list(df_train.columns)
with open('./model/model_columns.pkl', 'wb') as file:
    pickle.dump(model_columns, file)
