import os
print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())

try:
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col
    from pyspark.ml.feature import StringIndexer, VectorAssembler
    from pyspark.ml.classification import DecisionTreeClassifier
    from pyspark.ml.evaluation import MulticlassClassificationEvaluator
    
    print("Successfully imported PySpark modules")

    spark = SparkSession.builder.appName("SparkAI").getOrCreate()
    print("Successfully created SparkSession")

    if not os.path.exists("iris.csv"):
        print("Error: iris.csv file not found!")
    else:
        data = spark.read.csv("iris.csv", header=True, inferSchema=True)
        data.show(5)

except Exception as e:
    print("Error occurred:", str(e))

   

indexer = StringIndexer(inputCol="species", outputCol="label")
data = indexer.fit(data).transform(data)

assembler = VectorAssembler(inputCols=["sepal_length", "sepal_width", "petal_length", "petal_width"], outputCol="features")
final_data = assembler.transform(data).select("features", "label")

train_data, test_data = final_data.randomSplit([0.8, 0.2], seed=42)


dt = DecisionTreeClassifier(labelCol="label", featuresCol="features")
model = dt.fit(train_data)
predictions = model.transform(test_data)
evaluator = MulticlassClassificationEvaluator(labelCol="label", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print(f"Test Accuracy: {accuracy:.2f}")

# Save the model using the correct syntax
model.write().overwrite().save("decision_tree_model")
from pyspark.ml.classification import DecisionTreeClassificationModel

loaded_model = DecisionTreeClassificationModel.load("decision_tree_model")


import tensorflow as tf
from pyspark.ml.linalg import Vectors

# Convert Spark DataFrame to Pandas for deep learning model input
df_pandas = final_data.toPandas()
X = tf.convert_to_tensor(df_pandas["features"].apply(lambda x: list(x)).tolist())
y = tf.convert_to_tensor(df_pandas["label"].values)



from pyspark.sql.types import StructType, StructField, FloatType

schema = StructType([
    StructField("sepal_length", FloatType(), True),
    StructField("sepal_width", FloatType(), True),
    StructField("petal_length", FloatType(), True),
    StructField("petal_width", FloatType(), True)
])

# Create streaming_data directory if it doesn't exist
if not os.path.exists("streaming_data"):
    os.makedirs("streaming_data")
    print("Created streaming_data directory")

# Set up streaming data source
stream_data = spark.readStream.schema(schema).csv("streaming_data")

# Transform streaming data to create features column
stream_data_with_features = assembler.transform(stream_data)

# Make predictions on the transformed streaming data
predictions = model.transform(stream_data_with_features)

# Start the streaming query and store it in a variable
query = predictions.writeStream.outputMode("append").format("console").start()
print("Streaming query started. Add CSV files to streaming_data directory to process them.")

# Wait for the streaming to finish
query.awaitTermination()