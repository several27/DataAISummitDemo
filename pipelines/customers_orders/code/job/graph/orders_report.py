from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def orders_report(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("error").saveAsTable("maciej.customer_spendings")
