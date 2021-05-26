from pyspark.sql import SparkSession

sparkSession = SparkSession
				.builder
				.appName("spark-read-and-write")
				.getOrCreate()

data = [('First', 1), ('Second', 2), ('Third', 3), ('Fourth', 4), ('Fifth', 5)]

df = sparkSession.createDataFrame(data)
df.show()
