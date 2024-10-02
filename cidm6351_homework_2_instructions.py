# -*- coding: utf-8 -*-
"""Copy of CIDM6351 Homework 2 Instructions

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/125MdEYW-0TbRrY5aCQG6lUEFh7ucgxoI

Name: Amarachi Anthony
Course: BUSINESS DATA ETL (CIDM-6351-70)
Date: Sept 24th 2023

<h1  align="center">CIDM6351: Homework 2 Instructions. Importing and Cleaning Data</h1>

* Watch: Dr. Humpherys explains homework 2 video (5 mins) https://www.screencast.com/t/9tIllQJD8Hv  
* **Save a copy to your Google Drive and answer the questions on your copy**
* **Change the share to "Anyone with link" so the professor can view your code**
* **Submit the share link of your Colab Notebook to WTClass**
* This assignment is open notes/Internet/Datacamp but you can only consult with a CIS tutors or the professor.
- Students should complete this assignment **individually.** If you need help, contact a CIS tutor or the professor.
- Submit the URL to your Google Colab notebook to \\Wtclass\cidm6351\Week 6\Turn in Homework 2\

### Scenario: You are a data engineer for a large ice cream manufacturing company. Company stake holders want to know which ice cream flavors to diversity into. You need to gather and prepare some data on the favorite types of ice cream. You find some survey data on this topic. You will import the data, perform some cleaning tasks, and create a simple bar chart of the most popular ice cream flavors and the percentage of adults who like those flavors. ###
Original data comes from https://fox8.com/news/the-21-most-popular-ice-cream-flavors-in-america/

###Data Dictionary: ###  
Both data files have the following fields/columns.

Ice_Cream_Flavor : <str> The name of the ice cream.  
Like_It_Percentage : <str> The percetage of adults surveyed who like that particular ice cream flavor.  
Favorite_Percentage : <str> The percentage of adults surveyed who say that flavor is their favorite.

# Question 1 (30%): Importing data with Pandas
"""

# Run this cell
# Dr. Humpherys provides you the URLs to the data files you need.
ice_cream_part_one_url = 'https://raw.githubusercontent.com/sean-humpherys/randomfilestorage/main/ice_cream_part_one.csv'
ice_cream_part_two_url = 'https://raw.githubusercontent.com/sean-humpherys/randomfilestorage/main/ice_cream_part_two.json'

"""### Q1.1 (5%) Import the pandas library as pd"""

# --- put your answer below ---
import pandas as pd

"""### Q1.2  (5%) Load the data stored in ```ice_cream_part_one.csv``` into Pandas DataFrames. No need to print the data yet."""

# --- put your answer below ---
df_csv = pd.read_csv(ice_cream_part_one_url)

"""### Q1.3  (5%) Load the data stored in ```ice_cream_part_two.json``` into Pandas DataFrames. No need to print the data yet."""

# --- put your answer below ---
df_json = pd.read_json(ice_cream_part_two_url)



"""### 1.4  (5%) Print the information or head of both dataframes, respectively"""

# ---put your answer below--
# Print information about the DataFrame and first few rows (head) of the DataFrame
print(df_csv.head())
print(df_json.head())

"""### 1.5  (5%) Combine the two dataframes into one panda dataframe called "ice_cream". ###
If you need a hint, search on Google "combine two pandas dataframes", "join two pandas dataframes", or "concatenate pandas dataframe". Searching with the correct phrase is a useful data engineering technique.
"""

# ---put your answer below ---

ice_cream = pd.concat([df_csv, df_json], ignore_index=True)

"""### 1.6  (5%) Print the contents of the ice_cream dataframe. ###"""

# ---put your answer below ---
print("\nHead of ice_cream DataFrame:")
print(ice_cream)

"""# Question Two. (50%) Clean the data in preparation for data analysis. #

### Q2.1 (10%) Remove missing data. Notice the row on Jalapeno ice cream does not have like it percentage or favorite percentage. Remove any row with missing data.###
This was not taught yet in Datacamp. However, as a data engineer you will find yourself needing to learn how to do tasks not previously learned before. Consider searching Google for "pandas remove missing values" or "pandas remove blank rows".
"""

# --- put your answer below ---
ice_cream.dropna(inplace=True)
print(ice_cream)

"""### Q2.2 (10%) Capitalize all the ice cream flavor names. Each word should start with a capital letter, e.g. "rocky road" should become "Rocky Road". Print the contents of the Ice_Cream_Flavors column to show you were successful.###
This was not taught in Datacamp. However, as a data engineer you will find yourself needing to learn how to do tasks not previously learned before. Consider searching Google for "how to capitalize first letter in a word in pandas dataframe" or "capitalize first letter of each word in pandas".
"""

# --- put your answer below ---
# Print the column names to determine the correct column name for ice cream flavors
print("Column names:")
print(ice_cream.columns)

# Capitalize ice cream flavor names using the correct column name  'Ice_Cream_Flavor'
ice_cream['Ice_Cream_Flavor'] = ice_cream['Ice_Cream_Flavor'].apply(lambda x: x.title())

# Print the modified "Ice_Cream_Flavors" column
print("\nIce Cream Flavors after capitalization:")
print(ice_cream['Ice_Cream_Flavor'])

"""### Q2.3 (10%) Remove the % character from the values in "Like_It_Percentage" and "Favorite_Percentage". And, print the contents of the dataframe to show you were successful.###
For example, the value 35% becomes just 35. We don't need the % character. We just want the integers. Consider searching Google for "how to remove the last character from pandas column".
"""

# --- put your answer below ---

# Remove the '%' character from 'Like_It_Percentage' and 'Favorite_Percentage'
ice_cream['Like_It_Percentage'] = ice_cream['Like_It_Percentage'].str.replace('%', '')
ice_cream['Favorite_Percentage'] = ice_cream['Favorite_Percentage'].str.replace('%', '')

# Print the DataFrame to show the modifications
print("Ice Cream DataFrame after removing '%':")
print(ice_cream)

"""### Q2.4 (10%) List the data so we know the most favorite to least faavorite ice cream flavors. Sort the data based by the highest liked percentage to the lowest liked percentage. If there is a tie, secondarily sort by those who say the ice cream is their favorite. Print the sorted dataframe.###"""

# --- put your answer below ---
# Convert the columns to numeric to sort proper
ice_cream['Like_It_Percentage'] = pd.to_numeric(ice_cream['Like_It_Percentage'])
ice_cream['Favorite_Percentage'] = pd.to_numeric(ice_cream['Favorite_Percentage'])

# Sort the DataFrame based on liked percentage and favorite percentage
sorted_ice_cream = ice_cream.sort_values(by=['Like_It_Percentage', 'Favorite_Percentage'], ascending=[False, False])

# Print the sorted DataFrame
print("Sorted Ice Cream DataFrame:")
print(sorted_ice_cream)

"""### Q2.5 (10%) Filter out any ice cream flavors with a like it percentage less than 20%, keep those with a value of 20% and above. Store the new dataset in a dataframe called "top_ice_creams". Print the new dataframe.##"""

# --- put your answer below ---

# Filter out ice cream flavors with a like it percentage less than 20%
top_ice_creams = ice_cream[ice_cream['Like_It_Percentage'] >= 20]

# Print the new DataFrame
print("Top Ice Creams (Like It Percentage >= 20%):")
print(top_ice_creams)

"""# Question Three (20%) #
###Create a simple bar graph of the top 20 ice cream flavors. Put the ice cream flavors on the x-axis and the like it percentage on the y-axis. Show the bar graph.###
Consider searching Google with "pandas bar chart" or "pandas plot".

"""

# -- put your answer below ---

# Take the top 20 ice cream flavors

import matplotlib.pyplot as plt

# Take the top 20 ice cream flavors
top_20_ice_creams = top_ice_creams.head(20)

# Create a bar graph
plt.figure(figsize=(12, 8))
plt.barh(top_20_ice_creams['Ice_Cream_Flavor'], top_20_ice_creams['Like_It_Percentage'], color='skyblue')
plt.xlabel('Like It Percentage')
plt.ylabel('Ice Cream Flavor')
plt.title('Top 20 Ice Cream Flavors by Like It Percentage')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest percentage at the top
plt.show()

"""### The End. Congrats on importing and cleaning data, with a simple data visualization at the end. ###
If you need help, reach out to the CIS tutors or the professor.
"""