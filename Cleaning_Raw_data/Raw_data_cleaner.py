class Clean_raw_data:
    def __init__(self):
        pass

    def clean_data(self, Raw_data):
        Zomato_dataframe = Raw_data.drop(['url', 'phone', 'dish_liked'], axis=1)
        Zomato_dataframe.drop_duplicates(inplace=True)
        Zomato_dataframe.dropna(how='any', inplace=True)

        Zomato_dataframe=Zomato_dataframe.rename(columns={'approx_cost(for two people)': 'cost', 'listed_in(city)': 'type',
                                         'listed_in(type)': 'city'})

        Zomato_dataframe['cost']=((Zomato_dataframe['cost'].astype(str)).apply(lambda X:X.replace(',','.'))).astype(float)

        Zomato_dataframe = Zomato_dataframe.loc[Zomato_dataframe.rate !='NEW']
        Zomato_dataframe = Zomato_dataframe.loc[Zomato_dataframe.rate !='-'].reset_index(drop=True)
        replace_slash=lambda X:(X.replace('/5',''))
        Zomato_dataframe.rate = Zomato_dataframe.rate.apply(replace_slash).str.strip().astype(float)
        Zomato_dataframe.name = Zomato_dataframe.name.apply(lambda X:X.title())
        Zomato_dataframe['online_order'] = Zomato_dataframe['online_order'].replace({'Yes':True,'No':False})
        Zomato_dataframe['book_table'] = Zomato_dataframe['book_table'].replace({'Yes': True, 'No': False})
        return Zomato_dataframe
