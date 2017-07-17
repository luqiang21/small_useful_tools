'''
Sometimes, we need to train on data that has some categorical variables
when we are training, there are no problems, we can convert categorical variables
into dummy values.
But when you are predicting, same technique of converting might not give you the
same number of dummy values because you may have a very small testing data set
which you don't have the same number of possible values for the categorical variables.
Then different feature number will give you error when you want to predict using
the trained model.

We can first store the unique values for each categorical variable, then when we
want to predict, we can convert the categorical variables using the stored values.
'''

import pandas as pd
df = read_csv('data.csv')
unique_categorical_values_dic = {}
if is_train:
    # if training, write unique values for each categorical field to train.csv
    unique_categorical_values_dic[categories[0]] = list(df[categories[0]][~df[categories[0]].isnull()].unique())

    train_unique_categorical_values_df = pd.Series(df[categories[0]].unique())
    for category in categories[1:]:
        unique_categorical_values_dic[category] = list(df[category][~df[category].isnull()].unique())

        series = pd.Series(df[category].unique())
        train_unique_categorical_values_df = pd.concat([train_unique_categorical_values_df, series], axis=1)

    train_unique_categorical_values_df.columns = categories
    train_unique_categorical_values_df.to_csv('../data/train.csv')
    print '\nUnique values for each categorical fields written to train.csv'
else:
    # if test, read unique values for each categorical fields from train.csv
    train_unique_categorical_values_df = pd.read_csv('../data/train.csv')
    for category in categories:
        unique_categorical_values_dic[category] = list(train_unique_categorical_values_df
            [category][~train_unique_categorical_values_df[category].isnull()].unique())
    print '\nRead unique values for each categorical fields from train.csv'



'''preprocess categorical variables'''

for category in categories:
    if unique_categorical_values_dic[category]:
        category_values = unique_categorical_values_dic[category]
        df_temp[category] = pd.Categorical(df[category], category_values, ordered=False)

## df_temp is the dataframe having dummy variables. And it is the same for training and testing.
