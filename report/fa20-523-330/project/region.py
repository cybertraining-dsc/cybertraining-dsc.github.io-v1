#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:33:58 2020

@author: tobi
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt


olist_customers = pd.read_csv('dataset/olist_customers_dataset.csv')
olist_customers.head(5)

olist_orders = pd.read_csv('dataset/olist_orders_dataset.csv')
olist_orders.head(5)

olist_sellers = pd.read_csv('dataset/olist_sellers_dataset.csv')
olist_sellers.head(5)

olist_products = pd.read_csv('dataset/olist_products_dataset.csv')
olist_products.head(5)

olist_payments = pd.read_csv('dataset/olist_order_payments_dataset.csv')
olist_payments.head(5)

olist_reviews = pd.read_csv('dataset/olist_order_reviews_dataset.csv')
olist_reviews.head(5)

olist_items = pd.read_csv('dataset/olist_order_items_dataset.csv')
olist_items.head(5)

df = olist_customers
df = df.merge(olist_orders, on ='customer_id',how='left')
df = df.merge(olist_items, on ='order_id',how='left')
df = df.merge(olist_products,on ='product_id',how='left')
df.isna().sum()

plt.figure(98,figsize=(20,10))

sns.heatmap(df.isna(), cmap="viridis")

city_orders = pd.DataFrame(df.groupby(['customer_city'])['product_category_name'].count())
plt.figure(99)
plt.hist(df['customer_state'])
state_sales = pd.DataFrame(df.groupby(['customer_state'])['customer_state'].count())
plt.figure(97)

dfsp = df[df['customer_state']=='SP']
dfsp['product_category_name'] = dfsp['product_category_name'].astype(str)
plt.hist(dfsp['product_category_name'])
plt.figure(96)
products_SP = pd.DataFrame(dfsp.groupby(['product_category_name'])['product_category_name'].count()).astype(int)
products_SP = products_SP.rename(columns={'product_category_name':'product'})
products_SP.reset_index(level=0, inplace=True)
products_SP["product_category_name"] = products_SP["product_category_name"].astype(str)
plt.bar(products_SP["product_category_name"],products_SP["product"])
