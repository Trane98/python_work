import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix

heart_diseas_or_attack_df = pd.read_csv("C:\Program Files (x86)\python_work\python_work\AI_kursusgange\Lektion_4\HeartDiseaseHealthIndicatorsDataset\heart_disease_health_indicators_BRFSS2015.csv") # --> data path

'## Take a quick look at the data structure ##'
# Look at the top five rows
heart_diseas_or_attack_df.head()
# The info() method is useful to get a quick description of the data, in particular the total number of rows, each attribute’s type, and the number of non-null values:
heart_diseas_or_attack_df.info()
describe = heart_diseas_or_attack_df.describe()

# look at a histogram for another view of the data distribution
heart_diseas_or_attack_df.hist(bins=50, figsize=(12,6))
plt.show()
print(heart_diseas_or_attack_df['HeartDiseaseorAttack'].value_counts())

# look for correlations
corr_matrix = heart_diseas_or_attack_df.corr()
print(corr_matrix['HeartDiseaseorAttack'].sort_values(ascending=False))

attributes = ["BMI", "GenHlth", "MentHlth",
              "Smoker"]
scatter_matrix(heart_diseas_or_attack_df[attributes], figsize=(12, 8))
plt.show()

