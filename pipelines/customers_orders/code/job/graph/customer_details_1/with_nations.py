from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def with_nations(spark: SparkSession, in0: DataFrame, in1: DataFrame, in2: DataFrame) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.c_custkey") == col("in1.c_custkey")), "inner")\
        .join(in2.alias("in2"), (col("in2.n_nationkey") == col("in1.c_nationkey")), "inner")\
        .select(*[col("in2.n_name").alias("nation"), col("in2.n_regionkey").alias("n_regionkey")], col("in0.*"))
