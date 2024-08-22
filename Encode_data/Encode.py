class Data_Encoader:
    def encode_data(self,Zomato_Cleaned_data):
        for column in Zomato_Cleaned_data.columns[~Zomato_Cleaned_data.columns.isin(['rate','cost','votes'])]:
            Zomato_Cleaned_data[column] = Zomato_Cleaned_data[column].factorize()[0]
        return Zomato_Cleaned_data
