# Databricks notebook source
print("dumit")

# COMMAND ----------

# MAGIC %md
# MAGIC 1. sumit
# MAGIC 2. sumit
# MAGIC 3. sumit
# MAGIC
# MAGIC * a
# MAGIC * b
# MAGIC * c
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %run /Includes/Setup

# COMMAND ----------

name

# COMMAND ----------

# MAGIC %fs ls /databricks-datasets

# COMMAND ----------

dbutils.help()

# COMMAND ----------

a=dbutils.fs.ls('databricks-datasets')

# COMMAND ----------

display(a)

# COMMAND ----------


