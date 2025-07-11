# technically speaking Series is a pre-defined class in pandas library
'''
    method in str class
    method in list class
    method in tuple class
    method in dict class
    method in dict class

    method in student class

    method in series class
        IMP points
        ----------
            1. import the class from package
            2. create an object to the class
            3. call a method by using object

    CREATING SERIES
    ---------------
        1. Empty Series
        2. By using list
        3. By using array 
        4. Accessing single column from DataFrame


    -- how to create empty list
        a = []
        print(a)
    
    --  how to create empty series
            1. import pandas
            2. 

    --> Inside pandas series is available
    --> how to check, by using dir() function
'''
# import pandas as pd
# print(dir(pd))


'''
['ArrowDtype', 'BooleanDtype', 'Categorical', 'CategoricalDtype', 'CategoricalIndex', 'DataFrame', 'DateOffset', 'DatetimeIndex', 'DatetimeTZDtype', 'ExcelFile', 'ExcelWriter', 'Flags', 'Float32Dtype', 'Float64Dtype', 'Grouper', 'HDFStore', 'Index', 'IndexSlice', 'Int16Dtype', 'Int32Dtype', 'Int64Dtype', 'Int8Dtype', 'Interval', 'IntervalDtype', 'IntervalIndex', 'MultiIndex', 'NA', 'NaT', 'NamedAgg', 'Period', 'PeriodDtype', 'PeriodIndex', 'RangeIndex', 'Series', 'SparseDtype', 'StringDtype', 'Timedelta', 'TimedeltaIndex', 'Timestamp', 'UInt16Dtype', 'UInt32Dtype', 'UInt64Dtype', 'UInt8Dtype', '__all__', '__builtins__', '__cached__', '__doc__', '__docformat__', '__file__', '__git_version__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_built_with_meson', '_config', '_is_numpy_dev', '_libs', '_pandas_datetime_CAPI', '_pandas_parser_CAPI', '_testing', '_typing', '_version_meson', 'annotations', 'api', 'array', 'arrays', 'bdate_range', 'compat', 'concat', 'core', 'crosstab', 'cut', 'date_range', 'describe_option', 'errors', 'eval', 'factorize', 'from_dummies', 'get_dummies', 'get_option', 'infer_freq', 'interval_range', 'io', 'isna', 'isnull', 'json_normalize', 'lreshape', 'melt', 'merge', 'merge_asof', 'merge_ordered', 'notna', 'notnull', 'offsets', 'option_context', 'options', 'pandas', 'period_range', 'pivot', 'pivot_table', 'plotting', 'qcut', 'read_clipboard', 'read_csv', 'read_excel', 'read_feather', 'read_fwf', 'read_gbq', 'read_hdf', 'read_html', 'read_json', 'read_orc', 'read_parquet', 'read_pickle', 'read_sas', 'read_spss', 'read_sql', 'read_sql_query', 'read_sql_table', 'read_stata', 'read_table', 'read_xml', 'reset_option', 'set_eng_float_format', 'set_option', 'show_versions', 'test', 'testing', 'timedelta_range', 'to_datetime', 'to_numeric', 'to_pickle', 'to_timedelta', 'tseries', 'unique', 'util', 'value_counts', 'wide_to_long']
'''

import pandas as pd
s = pd.Series()     
print(s)                # Series([], dtype: object)
print(type(s))          # <class 'pandas.core.series.Series'>

#  s                -->      name of the object
#  Series           -->      name of the class in pandas
#  pd               -->      Alias name
#  s=pd.Series()    -->      Object creation 
#  Constructor      -->      during object creation constructor execute 

print("-----------------------------------")


data = [1, 2, 3, 4] 
ser = pd.Series(data)
print(ser)


