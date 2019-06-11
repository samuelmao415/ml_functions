#change directory
import os
cwd = os.getcwd()
os.chdir("/home/udi/foo")

#change display settings
pd.set_option('max_colwidth', 200)
pd.options.display.max_rows = 999

#read csv
prolog_rules = pd.read_csv('prolog_rules_error_analysis.csv', sep="\t")
combined_set.to_csv('prolog_rules_error_analysis.csv', sep='\t', index = False)

#read txt
data = pd.read_csv('theyes_email.txt', sep=" ", header=None)
data.columns = ["email_provided"]

#regex sub in a dataframe
toy.alltext=toy.alltext.apply(lambda x: re.sub("(\d+\%)+([a-z]+)|([a-z]+)+(\d+\%)", "\\2  \\2\\1  \\3  \\3\\4",x))

#join dataframes
item_color_id = final_item_color_table_merged.merge(item_table_result, on = 'item_id', how = 'inner')

#pandas groupby and count
prolog_rules.groupby(['outfit_id']).size().sort_values(ascending=False)

#pandas select rows with multiple conditions
missing_Apparel_Outerwear  = bad_data_df.loc[(bad_data_df.prolog_rulesA =='A') &( bad_data_df.prolog_rulesO =='O' )][['outfit_id','prolog_rules_combined']]

#merge multiple dataframes
data_frames = [single_Apparel, multiple_bags, Apparel_missing_type_in_JSON,dresses,duplicate_dresses,dress_overlaps_with_top_and_bottom,missing_Apparel]
df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['outfit_id','prolog_rules_combined'],how='outer'), data_frames)

#fill na for a dataframe
condition_dress = (appended_dict_unlist_df['attributes.meta_type'] == 'dress') & (appended_dict_unlist_df['attributes.type'].isna()==True)
condition_else = (appended_dict_unlist_df['attributes.meta_type'] != 'dress') & (appended_dict_unlist_df['attributes.type'].isna()==True)
appended_dict_unlist_df.loc[condition_dress,'attributes.type'] = appended_dict_unlist_df.loc[condition_dress,'attributes.type'].fillna('dress')
appended_dict_unlist_df.loc[condition_else,'attributes.type'] = appended_dict_unlist_df.loc[condition_else,'attributes.type'].fillna('not_available')
