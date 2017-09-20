import pandas as pd


def equal_operator(ds1, ds2):
    """
    Enter your code here
    """
    ds3 = ds1 == ds2
    ds3.tolist()
    return ds3

def greater_than_operator(ds1, ds2):
    """
    Enter your code here
    """
    ds3 = ds1 > ds2
    ds3.tolist()
    return ds3

def less_than_operator(ds1, ds2):
    """
    Enter your code here
    """
    ds3 = ds1 < ds2
    ds3.tolist()
    return ds3
