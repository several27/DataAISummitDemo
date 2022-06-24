from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *

def customer_details_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df_nations = nations(spark)
    df_regions = regions(spark)
    df_customers_nations = customers_nations(spark)
    df_with_nations = with_nations(spark, in0, df_customers_nations, df_nations)
    df_with_regions = with_regions(spark, df_with_nations, df_regions)
    df_month_cleanup = month_cleanup(spark, df_with_regions)

    return df_month_cleanup
