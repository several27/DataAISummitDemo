from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *
from prophecy.utils import *
from job.graph import *

def pipeline(spark: SparkSession) -> None:
    df_orders = orders(spark)
    df_orders_source = orders_source(spark)
    df_by_custkey = by_custkey(spark, df_orders, df_orders_source)
    df_sum_amounts = sum_amounts(spark, df_by_custkey)
    df_customer_details_1 = customer_details_1(spark, df_sum_amounts)
    orders_report(spark, df_customer_details_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.start(spark)
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
