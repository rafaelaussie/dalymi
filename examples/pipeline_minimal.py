import logging

import pandas as pd
from dalymi import Pipeline
from dalymi.resources import PandasCSV


logging.basicConfig()
logging.getLogger('dalymi').setLevel(logging.INFO)


pl = Pipeline()


first_df = PandasCSV(name='first_df', loc='data/first_df.csv', columns=['a'])
second_df = PandasCSV(name='second_df', loc='data/second_df.csv', columns=['a', 'b'])


@pl.output(first_df)
def first(**context):
    return pd.DataFrame({'a': range(5)})


@pl.output(second_df)
@pl.input(first_df)
def second(first_df, **context):
    first_df['b'] = first_df['a']**2
    return first_df


if __name__ == '__main__':
    pl.cli()
