from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def nations(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/databricks-datasets/tpch/delta-001/nation/")
