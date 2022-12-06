# DATA PREPARATION
# 1. HOW TO ADD INDEX FIELD USING PYTHON

# importing pandas package
import pandas as pd
 
# making data frame from csv file
data = pd.read_csv("employees.csv")
 
# setting first name as index column
data.set_index("First Name", inplace = True)
 
# display
data.head()

# HOW TO IDENTIFY OUTLIERS USING PYTHON 

#Removed all the existing objects
rm(list = ls())
#Setting the working directory
setwd("D:/Ediwsor_Project - Bike_Rental_Count/")
getwd()

#Load the dataset

bike_data = read.csv("day.csv",header=TRUE)
### Missing Value Analysis ###
sum(is.na(bike_data))
summary(is.na(bike_data))
#From the above result, it is clear that the dataset contains NO
Missing Values.