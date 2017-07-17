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
