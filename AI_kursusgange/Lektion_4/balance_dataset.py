import pandas as pd

def balance_data(dataset, rows_in_each_class):
    '''
    param dataset:
        The pandas dataframe we want to select the number of rows from
    :param rows_in_each_class:
        Variable for choosing how many rows of each class you want
    :return:
        type: pd dataframe
            with the selected number of rows in each class
    '''

    # Select rows with HeartDiseaseAttack = 1
    rows_with_value_1 = dataset[dataset['HeartDiseaseorAttack'] == 1].sample(n=rows_in_each_class, random_state=42)

    # Select rows with HeartDiseaseAttack = 0
    rows_with_value_0 = dataset[dataset['HeartDiseaseorAttack'] == 0].sample(n=rows_in_each_class, random_state=42)

    # Combine the selected rows
    selected_rows = pd.concat([rows_with_value_1, rows_with_value_0])

    return selected_rows