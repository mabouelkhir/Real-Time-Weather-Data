%pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType, LongType

# Create a SparkSession
spark = SparkSession.builder \
    .appName("KafkaToHiveORC") \
    .config("spark.sql.orc.impl", "native") \
    .enableHiveSupport() \
    .getOrCreate()

# Kafka details
kafka_server = "kafka-broker:29092"
topic = "weather_project"

# Define the schema to match your data
schema = StructType([
    StructField("weather_main", StringType()),
    StructField("weather_description", StringType()),
    StructField("temp", DoubleType()),
    StructField("temp_min", DoubleType()),
    StructField("temp_max", DoubleType()),
    StructField("pressure", IntegerType()),
    StructField("humidity", IntegerType()),
    StructField("visibility", IntegerType()),
    StructField("wind_speed", DoubleType()),
    StructField("dt", StringType()),
    StructField("country", StringType()),
    StructField("sunrise", StringType()),
    StructField("sunset", StringType()),
    StructField("timezone", IntegerType()),
    StructField("name", StringType())
])

# Read data from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_server) \
    .option("subscribe", topic) \
    .load() \
    .selectExpr("CAST(value AS STRING)") \
    .select(from_json("value", schema).alias("data")) \
    .select("data.*")

# Write data to a Hive table in ORC format
df.writeStream.outputMode("append").format("orc").option("path", "/user/hive/warehouse/weather_data").option("checkpointLocation", "/tmp/checkpoint").start().awaitTermination()
spark.stop()