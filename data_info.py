def data_info(x):
    print(x.head())
    print("types are:",x.dtypes)
    print("*"*30)
    print("null values:",x.isnull().sum())
    print("*"*30)
    print("shape is:",x.shape)
