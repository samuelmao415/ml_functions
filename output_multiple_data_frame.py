import pandas as pd

def python_return_multipledf_from_single_df(df = 'TPR_USGAAPContractImportTemplate_Tririga_20190822_Impairment - ReSIFT.xlsx'):
    df = pd.ExcelFile(df, skiprows=0)
    tab_names = df.sheet_names
    df_names = list(map(lambda x: str(x)+'_df', tab_names))
    dfs = {}
    for ind, val in enumerate(df_names):
            #df_name = str(x) + '_df'
        dfs[val] = pd.read_excel(df,sheet_name = tab_names[ind])
    return(dfs)


res = python_return_multipledf_from_single_df()
res.keys()

res['LeaseNonLeaseComponent_df']
