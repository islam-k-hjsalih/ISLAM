import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('C:/Users/hp/dataMix.csv', na_values='?')
print(" The first 5 rows of the dataset are:")

print(df.head())



columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
           'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

colNum = ['age',  'cp', 'trestbps', 'chol',  'thalach',  'oldpeak',  'ca', ]

colcat = ['sex',  'fbs', 'restecg', 'exang', 'slope', 'thal', 'num']

"""
Relabeled values in attribute 'sex'
%    From: 0                       To: female              
%    From: 1                       To: male                
%
%
% Relabeled values in attribute 'chest_pain'
%    From: 1                       To: typ_angina          
%    From: 4                       To: asympt              
%    From: 3                       To: non_anginal         
%    From: 2                       To: atyp_angina         
%
%
% Relabeled values in attribute 'fbs'
%    From: 1                       To: t                   
%    From: 0                       To: f                   
%
%
% Relabeled values in attribute 'restecg'
%    From: 2                       To: left_vent_hyper     
%    From: 0                       To: normal              
%    From: 1                       To: st_t_wave_abnormality
%
%
% Relabeled values in attribute 'exang'
%    From: 0                       To: no                  
%    From: 1                       To: yes                 
%
%
% Relabeled values in attribute 'slope'
%    From: 3                       To: down                
%    From: 2                       To: flat                
%    From: 1                       To: up                  
%
%
% Relabeled values in attribute 'thal'
%    From: 6                       To: fixed_defect        
%    From: 3                       To: normal              
%    From: 7                       To: reversable_defect   
%
%
% Relabeled values in attribute 'num'
%    From: '0'                     To: '<50'               
%    From: '1'                     To: '>50_1'             
%    From: '2'                     To: '>50_2'             
%    From: '3'                     To: '>50_3'             
%    From: '4'                     To: '>50_4'             


"""

print("The null data in the dataset:")
for col in columns:

    print("The null data in " + col + " column: " + str(df[col].isnull().sum()))
print("____________________________________________________________________--")



print("The duplicated rows in the dataset:")
print(str(df.duplicated().sum()))


duplicate_rows = df[df.duplicated(keep=False)]

print("the duplicated rows are:")
print(duplicate_rows)

print("____________________________________________________________________--")

print("Distribution tables for categorical variables:")
descriptive_stats = df.describe().T

print(descriptive_stats)

print("____________________________________________________________________--")

print("Value counts for categorical variables:")

#categorical_columns = df.select_dtypes(include='object').columns.tolist()


for col in colcat:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts())

    print("the statistics of numerical columns are:")

    for col in colNum:
        print(f"{col} mean values: {df[col].mean():.2f}")
        print(f"{col} median values: {df[col].median():.2f}")
        print(f"{col} standard deviation values: {df[col].std():.2f}")
        print(f"{col} min values: {df[col].min():.2f}")
        print(f"{col} max values: {df[col].max():.2f}")
        print("--_--_--")


print("____________________________________________________________________--")

print("Value counts for categorical variables:")


for col in colNum:
    print(f"{col} mean values: {df[col].mean():.2f}")
    print(f"{col} median values: {df[col].median():.2f}")
    print(f"{col} standard deviation values: {df[col].std():.2f}")
    print(f"{col} min values: {df[col].min():.2f}")
    print(f"{col} max values: {df[col].max():.2f}")
    print("--_--_--")

print("____________________________________________________________________--")
print("Value counts for categorical variables:")

# categorical_columns = df.select_dtypes(include='object').columns.tolist()

for col in colcat:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts())

sns.heatmap(df.isnull(), cbar=False, cmap='YlGnBu')
plt.title("Missing Values")
plt.show()


sns.set(style="whitegrid")
plt.figure(figsize=(16, 20))


plt.subplot(3, 2, 1)
sns.histplot(df['age'], bins=20, kde=True, color='skyblue')
plt.title("Histogram of Age")


plt.subplot(3, 2, 2)
sns.boxplot(x='num', y='thalach', data=df)
plt.title("Heart Rate (thalach) vs Heart Disease Level")


plt.subplot(3, 2, 3)
sns.countplot(x='num', hue='num', data=df, palette='Set2', legend=False)
plt.title("Heart Disease Class Distribution")


plt.subplot(3, 2, 4)
sns.boxplot(x='exang', y='oldpeak', data=df)
plt.title("Oldpeak vs Exercise-Induced Angina (exang)")


plt.subplot(3, 2, 5)
sns.scatterplot(x='age', y='trestbps', hue='num', data=df, palette='coolwarm')
plt.title("Age vs Resting Blood Pressure by Disease Level")


plt.tight_layout()
plt.show()
