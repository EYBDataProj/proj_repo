# Databricks notebook source
import pandas as pd

# COMMAND ----------

test_df = pd.read_csv('data/all_fuels_data.csv')
test_df.head()

# COMMAND ----------

# test_df.plot.bar(y='volume')

# COMMAND ----------

test_df['close'].max()

