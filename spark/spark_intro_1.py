from pyspark.sql import SparkSession  
# Imports the SparkSession class, which is the entry point to working with DataFrames, SQL, and the structured APIs in PySpark.
# SparkSession replaces older contexts like SQLContext and HiveContext, providing a unified interface.
spark = (
    SparkSession.builder            # Starts the builder pattern used to configure the SparkSession.
        .appName("Spark-Learn")     # Sets the name of the Spark application (useful for monitoring in the Spark UI).
        .getOrCreate()              # Creates a new SparkSession or retrieves an existing one if already running.
)
# This SparkSession object (`spark`) is used to:
#   - Create DataFrames from RDDs, CSV, JSON, Parquet, databases, etc.
#   - Run SQL queries using spark.sql(...)
#   - Access the Spark cluster's resources for distributed computation.
#   - Configure runtime settings and manage the Spark application's lifecycle.
