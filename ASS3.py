
# EXPLORATORY DATA ANALYSIS
HOW TO CONSTRUCT A BAR GRAPH WITH OVERLAY USING PYTHON

library(datasets)
# LOAD DATA ################################################
?mtcars
head(mtcars)
# BAR CHARTS ###############################################
barplot(mtcars$cyl) # Doesn't work
# Need a table with frequencies for each category
cylinders <- table(mtcars$cyl) # Create table
barplot(cylinders) # Bar chart
plot(cylinders) # Default X-Y plot (lines)
# CLEAN UP #################################################
# Clear environment
rm(list = ls()) # remove all the declared variables
# Clear packages
detach("package:datasets", unload = TRUE) # For base
# Clear plots
dev.off() # But only if there IS a plot
# Clear console
cat("\014") # ctrl+L

#2. HOW TO CONSTRUCT A HISTOGRAMS WITH OVERLAY USING PYTHON

# LOAD PACKAGES ############################################
library(datasets)
# LOAD DATA ################################################
?iris
head(iris)
# BASIC HISTOGRAMS #########################################
hist(iris$Sepal.Length)
hist(iris$Sepal.Width)
hist(iris$Petal.Length)
hist(iris$Petal.Width)
# HISTOGRAM BY GROUP #######################################
# Put graphs in 3 rows and 1 column
par(mfrow = c(3, 1))
# Histograms for each species using options
hist(iris$Petal.Width [iris$Species == "setosa"],
 xlim = c(0, 3), # Limit for x
 breaks = 9, # Bargraphs max count
 main = "Petal Width for Setosa",
 xlab = "",
 col = "red")
hist(iris$Petal.Width [iris$Species == "versicolor"],
 xlim = c(0, 3),
 breaks = 9,
 main = "Petal Width for Versicolor",
 xlab = "",
 col = "purple")
hist(iris$Petal.Width [iris$Species == "virginica"],
 xlim = c(0, 3),
 breaks = 9,
 main = "Petal Width for Virginica",

 xlab = "",
 col = "blue")
# Restore graphic parameter
par(mfrow=c(1, 1))
# CLEAN UP #################################################
# Clear packages
detach("package:datasets", unload = TRUE) # For base
# Clear plots
dev.off() # But only if there IS a plot
# Clear console
cat("\014") # ctrl+L
# Clear mind :)