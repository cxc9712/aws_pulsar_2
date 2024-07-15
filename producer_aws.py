##Producer1
import pulsar
import csv

import boto3
from io import StringIO
import pandas as pd
# Initialize the Pulsar client
client = pulsar.Client('pulsar://localhost:6650')

# Create a producer on a specific topic
producer = client.create_producer('my-topic')


s3 = boto3.resource('s3')
bucket_name = 'cirweatherapr14'
file_name = 'CIR_weather1.csv'

obj = s3.Object(bucket_name, file_name)
data = obj.get()['Body'].read()

data_string = data.decode('utf-8')
data_file = StringIO(data_string)

df = pd.read_csv(data_file)

# Read data from a CSV file and send it to the Pulsar topic
for index, row in df.iterrows():
    message = row.to_json()
    producer.send(message.encode('utf-8'))
# Close the producer and the client
# producer.close()
client.close()