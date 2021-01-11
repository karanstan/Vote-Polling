#databse and matplotlib
import pandas as pd
import sqlite3
#import matplotlib.pyplot as plt
import seaborn as sns
con = sqlite3.connect('votebank.db')
df = pd.read_sql_query("SELECT * FROM VOTEBANK",con)
print(df.head(13))
#plt.bar(df['VOTE'],50)
print(sns.countplot(x="VOTE",data=df))
con.close()
