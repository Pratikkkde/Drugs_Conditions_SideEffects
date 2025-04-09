import pandas as pd 
df = pd.read_csv("drugs.csv")
#Standardizing column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 2. Fill missing values
#- 'alcohol': Fill with assumption of 'No interaction'
df['alcohol'] = df['alcohol'].fillna("No interaction")

# - 'related_drugs': Leave missing as is
# - Other columns: Retain missing values for now

# 3. Cleaning string columns: strip whitespace
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip()

#Normalize key textual columns to lowercase
for col in ['drug_name', 'medical_condition', 'side_effects']:
    if col in df.columns:
        df[col] = df[col].str.lower()

#Converting 'rating' and 'no_of_reviews' to numeric
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['no_of_reviews'] = pd.to_numeric(df['no_of_reviews'], errors='coerce')

# 6. Parse 'activity' column (if it contains %)
def parse_activity(val):
    try:
        return float(val.replace('%', '').strip())
    except:
        return None

if 'activity' in df.columns:
    df['activity'] = df['activity'].apply(parse_activity)

#Removed the duplicates
df.drop_duplicates(inplace=True)

# 9. Saving cleaned data
df.to_csv("cleaned_drugs.csv", index=False)
print("Data cleaned and saved to 'cleaned!_drugs.csv'")

# Load the original cleaned dataset
df = pd.read_csv("cleaned!_drugs.csv")

#Converting 'alcohol' column to boolean: 'x' → 1, everything else → 0
#df['alcohol'] = df['alcohol'].apply(lambda x: 1 if str(x).strip().lower() == 'x' else 0)

#Filling empty strings and nulls in specific columns with 'Unknown'
#columns_to_fill_unknown = ['related_drugs', 'side_effects', 'generic_name', 'drug_classes']
#for col in columns_to_fill_unknown:
 #   df[col] = df[col].replace('', 'Unknown')         # empty string
  #  df[col] = df[col].fillna('Unknown')              # NaN

#Fill missing values in rating and no_of_reviews with 0
df['rating'] = df['rating'].fillna(0)
df['no_of_reviews'] = df['no_of_reviews'].fillna(0)

#Catch any other remaining empty strings across the DataFrame and fill with 'Unknown'
#df.replace('', 'Unknown', inplace=True)

# Saving the cleaned data
df.to_csv("final_cleaned_drugs.csv", index=False)

print(" Final cleaned data saved to 'final_cleaned_drugs.csv'")

#Managing missing values: Load the uploaded CSV file
df = pd.read_csv("cleaned_drugs.csv")  

#Replaced NaN values with "Unknown" in the specified columns
columns_to_replace = ['brand_names', 'drug_classes', 'generic_name', 'side_effects', 'related_drugs']
df[columns_to_replace] = df[columns_to_replace].fillna("Unknown")

#Saved the cleaned DataFrame to a new CSV file
df.to_csv("final_corrected_drugs.csv", index=False)

print("NaN values replaced and file saved as final_corrected_drugs.csv")