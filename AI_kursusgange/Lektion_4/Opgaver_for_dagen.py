import pandas as pd #Importere pandas
import matplotlib.pyplot as plt #Importere plots funktioner

df = pd.read_csv("C:\Program Files (x86)\python_work\python_work\AI_kursusgange\Lektion_4\HeartDiseaseHealthIndicatorsDataset\heart_disease_health_indicators_BRFSS2015.csv")#Fil lokation

print(df.head()) #Printer de første 5 rækker

df.info() #Viser information om dokumentet

#Klargøring til at få vidst forskellige værdier
description = df.describe()

df.describe()

print(description) #Printer en masse forskellige værdier med min og max samt kvartiler og gennemsnit


df.hist(figsize=(20, 15), bins=20)
plt.show()



heart_disease_distribution = df['HeartDiseaseorAttack'].value_counts()

# Vis resultatet
print(heart_disease_distribution)