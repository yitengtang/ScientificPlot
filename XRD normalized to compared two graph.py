import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np

# Function to remove commas from a string
def remove_comma(s):
    return float(s.replace(',', ''))

# Set the path to the text file
file_path = r'E:\XRD\2023\mki\yitang sample 05-15-2023.txt'

# Read the text file (assuming space or tab delimiter), skipping the first line ([Data]) and column names (Angle, PSD)
# Remove commas from the values using the remove_comma function
df = pd.read_csv(file_path, delim_whitespace=True, header=None, skiprows=161, skipinitialspace=True, converters={0: remove_comma, 1: remove_comma})

# Assuming the first column is x and the second column is y
x = df.iloc[:, 0]
y = df.iloc[:, 1]

# Normalize y to [0:1]
y = (y - np.min(y)) / (np.max(y) - np.min(y))

# Set the path to the second data file
second_file_path = r'E:\XRD\2023\3\03082023\02232023s1pbsnpl22-1140-1.csv'

# Read the second data file
df2 = pd.read_csv(second_file_path)

# Extract the x and y values from the second DataFrame
x2 = df2.iloc[:, 0]
y2 = df2.iloc[:, 1]

# Normalize y2 to [0:1]
y2 = (y2 - np.min(y2)) / (np.max(y2) - np.min(y2))

# Set a prominence threshold to ignore small peaks
prominence_threshold = 0.5

# Detect the peaks in the first data with a prominence threshold
peaks, _ = find_peaks(y, prominence=prominence_threshold)

# Create a figure with one subplot
fig, ax = plt.subplots(figsize=(10, 10), dpi=100)

# Plot the first data 
ax.plot(x, y, linewidth=3, label='PSLB 116')
ax.plot(x[peaks], y[peaks], 'ro', markersize=5)

# Annotate the peaks with their x and y values
for peak in peaks:
    ax.annotate(f'({x[peak]:.2f}, {y[peak]:.2f})', 
                 (x[peak], y[peak]), textcoords="offset points", 
                 xytext=(-10, 5), ha='center', fontsize=12, color='red')

# Add shorter vertical drop lines at specific x-axis values
drop_line_positions = [24.7, 29.8, 42.7]
drop_line_height = 1  # Customize the height of the drop lines to match the normalized data
for position in drop_line_positions:
    ax.plot([position, position], [0, drop_line_height], color='blue', linestyle='--', linewidth=1)

# Plot the second data 
ax.plot(x2, y2, linewidth=3, label='Geology department')

# Set the x-axis label
ax.set_xlabel('2θ', fontsize=16)

# Set the y-axis label
ax.set_ylabel('Normalized Counts', fontsize=16)

# Set the title
ax.set_title('PbSCl NPL', fontsize=16)

# Set the y-axis range starting from 0
plt.ylim(0, 1.2)
plt.xlim(20,51)

# Set the tick labels to be inside the plot
ax.tick_params(axis='both', direction='in', labelsize=16)

# Add a legend
ax.legend(fontsize=16)

# Show the plot
plt.show()

