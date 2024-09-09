
#####################################
# Import Libraries 
#####################################
import statistics
from datetime import date
import os
import pandas as pd
#quandl provides the framework, API Key to NASDAQ data.
# To setup and access an account with free API. https://data.nasdaq.com/publishers/QDL
# Create an account.
# Copy the API Key  NOTE:  Do NOT share your API key. 
import quandl


# Set your Quandl API key
#see lines 9-12 for API key
quandl.ApiConfig.api_key = "my API Key"

# Fetch WTI crude oil data using the correct dataset from FRED
wti_data = quandl.get("FRED/DCOILWTICO")

# Fetch Brent crude oil data from FRED
brent_data = quandl.get("FRED/DCOILBRENTEU")

# Print the last few rows to check the data
print(wti_data.tail(365))

# Print the last few rows to check the data
print(brent_data.tail(365))



#Creating two folders WTI and Brent under code parent directory.

# Define the parent folder and subfolder names
parent_folder = 'code'
subfolder1 = 'WTI'
subfolder2 = 'Brent'
filename_WTI = 'wti_last_365_days.csv'
filename_Brent = 'Brent_last_365_days.csv'

# Create the full path
full_path_WTI = os.path.join(parent_folder, subfolder1, filename_WTI)
full_path_Brent = os.path.join(parent_folder, subfolder2, filename_Brent)

# Ensure the directories exist
os.makedirs(os.path.dirname(full_path_WTI), exist_ok=True)
os.makedirs(os.path.dirname(full_path_Brent), exist_ok=True)

print(f"CSV file saved to '{full_path_WTI}'")
print(f"CSV file saved to '{full_path_Brent}'")


# Extract the last 365 rows of the DataFrame  <---Brent
last_365_days_brent = wti_data.tail(365)

# Save the DataFrame to a CSV file
last_365_days_brent.to_csv('brent_last_365_days.csv', index=True)

# Extract the last 365 rows of the DataFrame for WTI and Brent
last_365_days_wti = wti_data.tail(365)
last_365_days_brent = brent_data.tail(365)

# Save the DataFrames to CSV files
last_365_days_wti.to_csv(full_path_WTI, index=True)
last_365_days_brent.to_csv(full_path_Brent, index=True)

print(f"Data saved to '{full_path_WTI}'")
print(f"Data saved to '{full_path_Brent}'")


# Convert the last 365 rows to a list of dictionaries
data_list_wti = last_365_days_wti.to_dict(orient='records')
data_list_brent = last_365_days_brent.to_dict(orient='records')

# Extract the start and end dates
start_date_wti = last_365_days_wti.index[0].strftime("%Y-%m-%d")
end_date_wti = last_365_days_wti.index[-1].strftime("%Y-%m-%d")
start_date_brent = last_365_days_brent.index[0].strftime("%Y-%m-%d")
end_date_brent = last_365_days_brent.index[-1].strftime("%Y-%m-%d")



#Start and End Data Comparison to make sure datasets for WTI and Brent Dates match
if start_date_wti== start_date_brent:
    print("WTI dates match Brent Crude Dates.")
else:
    print("WTI dates do not match Brent Crude Dates.")

if start_date_wti== start_date_brent:
# Print the dates for verification
    print(f"Start Date: {start_date_wti}")
    print(f"End Date: {end_date_wti}")

else:
    print("WTI dates do not match Brent Crude Dates.")


#####################################
# Statistical Data for WTI based on Closing Price
#####################################

#min_price_wti: float = min(wti_data)  
min_price_wti = last_365_days_wti['Value'].min()
#max_price_wti: float = max(wti_data)  
max_price_wti = last_365_days_wti['Value'].max()
mean_price_wti = last_365_days_wti['Value'].mean()


#####################################
# Statistical Data for Brent based on Closing Price
#####################################

#min_price_brent: float = min(brent_data)  
min_price_brent = last_365_days_brent['Value'].min()

#max_price_brent: float = max(brent_data)  
max_price_brent = last_365_days_brent['Value'].max()
#With pandas "Value" is recommended.  I was getting a null value in the numurator.
#Min and Max were displaying a value of 'Value'
mean_price_brent = last_365_days_brent['Value'].mean()

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Millennium Group: Delivering Professional Insights For The Financial Markets'

#####################################
# F-String Defined
#####################################
byline: str = f"""
----------------------------------------------------------------------------
Millennium Group: Delivering Professional Insights For The Financial Markets
----------------------------------------------------------------------------

Crude Oil Markets Statistical Examples-Spreading WTI and Brent:
Crude Oil Daily Close Statistics From:    {start_date_wti} to {end_date_wti}
Minimum Daily Close WTI:                 {min_price_wti}
Minimum Daily Close Brent:               {min_price_brent}

Maximum Daily Close WTI:                 {max_price_wti}
Maximum Daily Close Brent:               {max_price_brent}

Mean Closing Price WTI:                  {round(mean_price_wti, 2)}
Mean Closing Price Brent:                {round(mean_price_brent, 2)}

"""


#####################################
# Define a main() function for this module.
#####################################
def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())
#####################################
# Define get_byline() function for this module.
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#Future code enhancements:
#1.  When running the program.  Output to standard out shows WTI and Brent data are not in sync.
#    Print statement shows WTI start date is 05/09/2020.  Brent start date shows 05/11/2020.
#    A validated user imput statement setting start and end dates would solve that problem.
#    Catch/Try could be used to catch date formating errors.  <--Basically input validation.
#2.  Data Source was an issue.  I used pynance last year to get 'spy' data.  It's been depricated.
#    ChapGPT recommended yfinance.  I had DNS resolution problems.  I could ping yahoo.com, but fs.yahoo.com wasn't not reachable.
#    Even though it returned an IP Address.  Google Search showed known issue.
#3.  I settled on quantl after trying data vendors.  quantl pulls data from NASDAQ.  Data is dated.
#    Even Academic pricing is $300 per year.#zachlawrence_python.py
