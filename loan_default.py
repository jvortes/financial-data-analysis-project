import pandas as pd

# Set display options to show non-exponential numbers
pd.set_option('display.float_format', lambda x: '{:.2f}'.format(x))
df = pd.read_csv("C:/Users/jvort/OneDrive/Documents/archive/loan.csv", header=0)

# Display the first few rows of the DataFrame
print(df.head())
# Calculate summary statistics
print(df.describe())

# total generated loan amount 2,260,668.00
# mean / average loan amount 15,047
# min / max: 500 / 40,000.00