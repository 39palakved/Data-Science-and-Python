                                                                    
                                                                    # DATA PREPARATION PHASE TO MODEL THE DATA 

#1 HOW TO PARTITION DATA USING PYTHON

library(partition)
library(ggplot2)
set.seed(1234)
# create a 100 x 15 data set with 3 blocks
df <- simulate_block_data(
 # create 3 correlated blocks of 5 features each
 block_sizes = rep(5, 3),
 lower_corr = .4,
 upper_corr = .6,
 n = 100
)

#HOW TO BUILD RANDOM FOREST USING PYTHON 
# Steps to build Random Forest in python
'''1.  Import the required libraries
2.  Import and print the dataset 
3.  Select all rows and column 1 from dataset 
4.   Fit Random forest regressor to the dataset 
5.   Predicting a new result 
6.  Visualising the result'''

from sklearn.ensemble import RandomForestClassifier
y = train_data["Survived"]
features = ["Pclass", "Sex", "SibSp", "Parch","Fare","Age"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])
model = RandomForestClassifier(n_estimators=100, max_depth=5,
random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)