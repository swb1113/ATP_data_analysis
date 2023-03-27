import glob
import pandas as pd

# list all csv files only
csv_files = glob.glob('*.{}'.format('csv'))
df_csv_append = pd.DataFrame()
 
# append the CSV files
for file in csv_files:
    df = pd.read_csv(file)
    df_csv_append = df_csv_append.append(df, ignore_index=True)
 
df_csv_append.to_csv("top_100.csv", index=False)
