from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def month_cleanup(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn(
          "month",
          when((col("month") == lit(1)), lit("January"))\
            .when((col("month") == lit(2)), lit("February"))\
            .when((col("month") == lit(3)), lit("March"))\
            .when((col("month") == lit(4)), lit("April"))\
            .when((col("month") == lit(5)), lit("May"))\
            .when((col("month") == lit(6)), lit("June"))\
            .when((col("month") == lit(7)), lit("July"))\
            .when((col("month") == lit(8)), lit("August"))\
            .when((col("month") == lit(9)), lit("September"))\
            .when((col("month") == lit(10)), lit("October"))\
            .when((col("month") == lit(11)), lit("November"))\
            .when((col("month") == lit(12)), lit("December"))\
            .otherwise(lit("Unknown"))
        )\
        .drop("n_regionkey")\
        .withColumn("amounts", concat(lit("\uFFE1"), format_number(col("amounts"), 2)))
