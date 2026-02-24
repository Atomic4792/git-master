from json import dumps
from pandas import DataFrame, read_json
from io import StringIO 


def print_table(json_data: list) -> DataFrame:
    #TODO: put some pretty printing logic here
    #read_json and StringIO work together to create a DataFrame object
    #without too much hassle. Without them it would take a couple loops
    #and new funtions to achieve the same thing. READ THE DOCS
    json_table_dataframe= read_json(StringIO(dumps(json_data)))
    return json_table_dataframe[['id','email', 'username','roles']]