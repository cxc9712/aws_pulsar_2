##Producer1

import csv
import pulsar
# Initialize the Pulsar client
client = pulsar.Client('pulsar://localhost:6650')

# Create a producer on a specific topic
producer = client.create_producer('my-topic')

# Read data from a CSV file and send it to the Pulsar topic
with open('cir_sample.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        message = ','.join(row)
        producer.send(message.encode('utf-8'))

# Close the producer and the client
# producer.close()
client.close()