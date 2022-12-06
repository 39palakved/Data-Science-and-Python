


                                                                                #LOGISTIC REGRESSION MODELLING


# HOW TO PERFORM LOGISTIC REGRESSION USING PYTHON

# import the class
from sklearn.linear_model import LogisticRegression
# instantiate the model (using the default parameters)
logreg = LogisticRegression()
# fit the model with data
logreg.fit(X_train,y_train)
#
y_pred=logreg.predict(X_test)

#HOW TO PERFORM  POISSON REGRSSION USING PYTHON   

input <- warpbreaks
print(head(input))
output <-glm(formula = breaks ~ wool + tension,
data = warpbreaks, family = poisson)
print(summary(output))
output_result <-glm(formula = breaks ~ wool + tension,
data = warpbreaks, family =
poisson)
output_result