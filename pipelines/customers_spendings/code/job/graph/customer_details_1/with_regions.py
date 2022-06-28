from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def with_regions(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in1.r_regionkey") == col("in0.n_regionkey")), "inner")\
        .select(*[col("in1.r_name").alias("region")], col("in0.*"))
