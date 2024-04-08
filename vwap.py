import numpy as np
import pandas as pd
from pandas import DataFrame

# Set options to display all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 4)


def prepare_klines_data(klines):
    columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume',
               'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',
               'taker_buy_quote_asset_volume', 'ignore']

    df = pd.DataFrame(klines, columns=columns)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df.drop(columns=['close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',
                     'taker_buy_quote_asset_volume', 'ignore'], inplace=True)
    df = df.astype(float)

    return df


def prepare_kline_stream_data(kline, data: DataFrame):
    columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']

    kline_data_formatted = [
        kline['t'],
        float(kline['o']),
        float(kline['h']),
        float(kline['l']),
        float(kline['c']),
        float(kline['v'])
    ]

    new_df = pd.DataFrame([kline_data_formatted], columns=columns)
    new_df['timestamp'] = pd.to_datetime(new_df['timestamp'], unit='ms')
    new_df.set_index('timestamp', inplace=True)

    return pd.concat([data, new_df])


def vwap_zscore(data: DataFrame, pds):
    volume_close = data['volume'] * data['close']
    mean = volume_close.rolling(window=pds).sum() / data['volume'].rolling(window=pds).sum()
    close_mean = data['close'] - mean
    close_mean_pow = close_mean.pow(2)
    close_mean_pow_sma = close_mean_pow.rolling(window=pds).mean()
    vwapsd = np.sqrt(close_mean_pow_sma)
    return close_mean / vwapsd
