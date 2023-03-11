### Join the Orders and Customers project tables

import pandas as pd

customers = pd.read_csv('projectdata_customers.csv')
orders = pd.read_csv('projectdata_orders.csv')

merge = pd.merge(customers,orders, on='CustomerID', how='inner')

merge.to_csv('projectdata_merge.csv',index=False)









