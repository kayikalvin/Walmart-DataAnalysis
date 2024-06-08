import pandas as pd
import os
from datetime import datetime

#get the working directory
current_directory = os.getcwd()

# Print the current working directory
print("Current working directory:", current_directory)

df = pd.read_csv(r"filepath")

# Add a new column named `time_of_day` to give insight of sales in the Morning, Afternoon and Evening. This will help answer the question on which part of the day most sales are made.

#Convert to String: Assuming your DataFrame is named df, convert the Time column to string:
df['hour'] = df['Time of Day'].str[:2].astype(int)

#Create New Column: Next, create a new column named time_of_day based on the hour values:
df['time_of_day'] = pd.cut(df['hour'], bins=[0, 12, 18, 24], labels=['Morning', 'Afternoon', 'Evening'])

#Clean Up: Finally, drop the temporary hour column if you don’t need it anymore:
df.drop(columns=['hour'], inplace=True)

#save to the cvs file
df.to_csv('WalmartSalesData.csv', index=False)

#Add a new column named `day_name` that contains the extracted days of the week on which the given transaction took place (Mon, Tue, Wed, Thur, Fri).
#This will help answer the question on which week of the day each branch is busiest.
#converting date column to datetime to avoid errors when using .dt
#The errors='coerce' parameter ensures that any invalid date values are converted to NaT (Not-a-Time) instead of raising an error.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df['day_name'] = df['Date'].dt.day_name()



df.to_csv('WalmartSalesData.csv', index=False)

# #Add a new column named `month_name` that contains the extracted months of the year on which the given transaction took place (Jan, Feb, Mar). Help determine which month of the year has the most sales and profit.
# #creating a column to hold the months data
 df['month'] = df['Date'].dt.month

  months = {
     1:'January',
     2:'February',
     3:'March',
     4:"April",
     5:"May",
     6:"June",
     7:"July",
     8:"August",
     9:"September",
     10:"october",
     11:"November",
     12:"December"
 }

# #the clumn was displayed in numbers so we create a dictionary to be mapped over to be exuated to the figures
df["Month"] = df["month"].map(months)

# delete tghe month column you dont need it anymore
df.drop(columns=['month'], inplace=True)

# #save the changes to the csv file
df.to_csv('WalmartSalesData.csv', index=False)#Convert the 'Date' column to the day of the week.
    
df['Day of Week'] = df['Date'].dt.day_name()

df

## Business Questions To Answer

### Generic Question

#1. How many unique cities does the data have?
unique_cities = df["City"].nunique()
print(unique_cities)

#2. In which city is each branch
# Group by branch and aggregate the cities into a list
branch_cities = df.groupby('Branch')['City'].unique()

# Create a new DataFrame to display the results
result_df = pd.DataFrame(branch_cities)
result_df.reset_index(inplace=True)  # Reset index for cleaner display

# Rename columns for clarity
result_df.columns = ['Branch', 'Cities']

# Print the result
print(result_df)

#
### Product

# 1. How many unique product lines does the data have?

unique_products = df['Product line'].nunique()
print(unique_products)

#2. What is the most common payment method?
import pandas as pd
df = pd.read_csv(r"filepath")

common = df.groupby("Payment")["Quantity"].sum()

result_df = pd.DataFrame(common)
result_df.reset_index(inplace=True)

# most_common_method = common.idxmax()
print(f"The most common payment method is: ({common})")

#3. What is the most selling product line?
most_sold =  df.groupby("Product line")["Quantity"].sum() 
result_df = pd.DataFrame(most_sold) 


print(f"The most common payment method is: ({most_sold})")

#4. What is the total revenue by month?
total_revenue =  df.groupby("Month")["Total"].sum() 
# result_df = pd.DataFrame(most_sold) 
total_revenue

#5. What is the city with the largest revenue?
total_cityrevenue =  df.groupby("City")["Total"].sum() 

sorted_df = df.sort_values(by='Total')

# max_value = df['Total'].max()
total_cityrevenue

#6. What product line had the largest revenue?

# Assuming total_cityrevenue is already calculated as shown in the question:
total_cityrevenue = df.groupby("Product line")["Total"].sum()

# Get the index of the maximum value in total_cityrevenue
max_index = total_cityrevenue.idxmax()

# Retrieve the product line corresponding to the maximum value
product_line_with_max_revenue = max_index
max_total_revenue = total_cityrevenue[max_index]

print("Product line with maximum total revenue:", product_line_with_max_revenue)
print("Maximum total revenue:", max_total_revenue)

# #7. Fetch each product line and add a column to those product line showing "Good", "Bad". Good if its greater than average sales
# #get the average of the total sales
 average_sales = df['Total'].mean()
# #add a column
df['Good or Bad'] = ('')
# #saving changed to the dataset so that they can be seen
df.to_csv('WalmartSalesData.csv', index=False)
# #populating the column
 pl =df['Product line']
 def p (pl):
     if pl > average_sales:
         return 'Good'
     else: 
         return 'Bad'
    
    




 df['Good or Bad'] = df['Product line'].apply(p)

print(df.dtypes)

#8. Which branch sold more products than average product sold?
# get the average of the total sales



#9. What is the most common product line by gender?

#10. What product line had the largest VAT?

#11. What is the average rating of each product line?



import pandas as pd
from datetime import datetime

pd.set_option('display.max_columns', None)

df = pd.read_csv(r'filepath')
df.head()

df.isnull().sum()

df.info()

df['Date'] = pd.to_datetime(df['Date'])
df.dtypes

datetime_dim= pd.DataFrame(columns = ['date_id', 'day', 'month', 'year','weekday'])


datetime_dim['date_id'] = df['Date']
datetime_dim['day'] = df['Date'].dt.day
datetime_dim['month'] = df['Date'].dt.month
datetime_dim['year'] = df['Date'].dt.year
datetime_dim['weekday'] = df['Date'].dt.weekday

days = {
    1:'Monday',
    2:'Tuesday',
    3:'Wednesday',
    4:'Thursday',
    5:'Friday',
    6:'Saturday',
    7:'Sunday'
}
datetime_dim['weekday'] = datetime_dim['weekday'].map(days)

datetime_dim

gender_dim = pd.DataFrame(columns = ['gender_id','gender'])

gender_dim['gender'] = df['Gender']
gender_dim['gender_id'] = gender_dim['gender'].index
gender_dim.set_index('gender_id',inplace =True)

gender_dim = gender_dim.drop_duplicates('gender')


gender_dim

product_dim['product_line'] = product_dim['product_line'].astype(str)

customer_dim = pd.DataFrame(columns = ['customer_type_id','customer_type'])
customer_dim['customer_type'] = df['Customer type']
customer_dim['customer_type_id'] = customer_dim['customer_type'].index
# customer_dim = customer_dim.drop_duplicates('customer_type')
# customer_dim = customer_dim.reset_index(drop=True)
customer_dim['customer_type_id'] = customer_dim['customer_type'].index




branch_dim = pd.DataFrame(columns= ['branch_id','branch','city'])

branch_dim['branch'] = df['Branch']
branch_dim['branch_id'] = branch_dim['branch'].index
branch_dim['city'] = df['City']
# branch_dim = branch_dim.drop_duplicates('branch')
# branch_dim = branch_dim.reset_index(drop=True)
branch_dim['branch_id'] = branch_dim['branch'].index


product_dim = pd.DataFrame(columns =['product_id','product_line'])
product_dim['product_line'] = df['Product line']
product_dim['product_id'] = product_dim['product_line'].index


product_dim


time_dim = pd.DataFrame(columns= ['time_id','time','time_of_day'])
time_dim['time'] = df['Time']
time_dim['time_id'] = time_dim['time'].index
time_dim['time_of_day'] = df['time_of_day']


payment_dim = pd.DataFrame(columns=['payment_id','payment'])
payment_dim['payment'] = df['Payment']
payment_dim['payment_id'] = payment_dim['payment'].index
# payment_dim = payment_dim.drop_duplicates('payment')
# payment_dim = payment_dim.reset_index(drop=True)
payment_dim['payment_id'] = payment_dim['payment'].index

payment_dim



branch_dim['branch_id'] = branch_dim['branch'].index


gender_dim

datetime_dim

df.head(1)

fact_table = pd.DataFrame(columns= ['invoice_id','unit_price','quantity','VAT','total','cogs','gross_margin_percentage','gross_income','ratings','date_id','time_id','payment_id','branch_id','customer_type_id','gender_id','product_line_id'])

fact_table['invoice_id'] = df['Invoice ID']
fact_table['unit_price'] = df['Unit price']
fact_table['gross_income'] = df['gross income']
fact_table['VAT'] = df['Tax 5%']
fact_table['total'] =df['Total']
fact_table['cogs'] = df['cogs']
fact_table['gross_margin_percentage'] = df['gross margin percentage']
fact_table['quantity'] = df ['Quantity']
fact_table['ratings'] = df['Rating']
fact_table['date_id'] = datetime_dim['date_id'] 
fact_table['time_id'] = time_dim['time_id'] 
fact_table['payment_id'] = payment_dim['payment_id'] 
fact_table['branch_id'] = branch_dim['branch_id']
fact_table['customer_type_id'] = customer_dim['customer_type_id'] 
fact_table['gender_id'] = df['Gender']
fact_table['product_line_id'] = product_dim['product_id'] 



fact_table

customer_dim







df




