from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def by_custkey(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.c_custkey") == col("in1.o_custkey")), "inner")\
        .select(col("in0.c_custkey").alias("c_custkey"), col("in1.o_orderdate").alias("o_orderdate"), col("in1.o_totalprice").alias("o_totalprice"))
