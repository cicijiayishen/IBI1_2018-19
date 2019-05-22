# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:16:08 2019

@author: cici
Practical 14: Logistic Regression
"""

##########################Imprt Excel data in Python########################
import pandas as pd
df=pd.read_excel('C:/Users/sissy/Desktop/test Git/IBI1_2018-19/Practical14/Final_Fluview_Practical_dataset.xlsx')
df.info()
df.head(5)
#########################Data preparation###################################
df_regress=df[['Virus Strain',
               'Age',
               'Gender',
               'Hospitalized?',
               'Swine Contact?',
               'Attended Agricultural Event?']]
df_regress.head(5)
df_regress[df_regress.isna().any(axis=1)]
df_regress=df_regress.dropna()
df_regress[df_regress.isna().any(axis=1)]
for column in df_regress:
    print(column,df_regress[column].unique())
df_regress['Virus Strain']=df_regress['Virus Strain'].map({'Influenza A H3N2v':1,'Influenza A H1N1v':0,'Influenza A H1N2v':0,'Influenza A H7N2':0})
df_regress['Age']=df_regress['Age'].map({'<18 Years':0,'>=18 Years':1})
df_regress['Gender']=df_regress['Gender'].map({'Male':0,'male':0,'Female':1,'female':1})
df_regress['Hospitalized?']=df_regress['Hospitalized?'].map({'No':0,'no':0,'Yes':1,'yes':1})
df_regress['Swine Contact?']=df_regress['Swine Contact?'].map({'No':0,'no':0,'Yes':1,'yes':1})
df_regress['Attended Agricultural Event?']=df_regress['Attended Agricultural Event?'].map({'No':0,'no':0,'Yes':1,'yes':1})
df_regress.head(5)
########################Logistic regression##################################
import statsmodels.api as sm
import statsmodels.formula.api as smf
endog=df_regress['Virus Strain']
exog=sm.add_constant(df_regress[['Age','Gender','Hospitalized?','Swine Contact?','Attended Agricultural Event?']])
logit=smf.Logit(endog,exog)
result=logit.fit()
result.summary()
#odds ratios
import numpy as np
print('Odds ratios:')
print(np.exp(result.params))