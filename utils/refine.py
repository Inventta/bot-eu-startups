import pandas as pd
from constants import CATEGORIES, CONCATENATED_FILE, FINAL_FILE_LABI

# Read the concatenated.xlsx file
df_concatenated = pd.read_excel(CONCATENATED_FILE)

# Get the list corresponding to column 15 of the table
column_15_list = df_concatenated.iloc[:, 14].tolist()

segments = []
for item in column_15_list:
    words = str(item).lower().strip().split(", ")
    new_words = []
    for word in words:
        new_words.extend(word.split(" "))
    segments.append(new_words)

if(len(column_15_list) != len(segments)):
    print("Error: The length of the segments list is not equal to the length of the segments list.")
    exit(1)

categorized_segments = []

for segment in segments:
    found_category = False
    for word in segment:
        for category, keywords in CATEGORIES.items():
            if any(keyword in word for keyword in keywords):
                categorized_segments.append(category)
                found_category = True
                break
        if found_category:
            break 
    if not found_category:
        categorized_segments.append("other")

if(len(categorized_segments) != len(segments)):
    print("Error: The length of the categorized segments list is not equal to the length of the segments list.")
    exit(1)

# Create a new column in the dataframe for the categorized segments
df_concatenated['Categorized Segment'] = categorized_segments

# Save the updated dataframe to a new excel file
df_concatenated.to_excel(FINAL_FILE_LABI, index=False)

