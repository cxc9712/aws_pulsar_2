import pulsar

# Initialize the Pulsar client
client = pulsar.Client('pulsar://localhost:6650')

# Create a consumer on the same topic
consumer = client.subscribe('my-topic', subscription_name='my-subscription')

while True:
    msg = consumer.receive()
    try:
        # Print the message content
        print("Received message: '%s'" % msg.data().decode('utf-8'))
        # Acknowledge the message
        consumer.acknowledge(msg)
    except:
        # Negative acknowledgment on failure
        consumer.negative_acknowledge(msg)

# Close the consumer and the client (never reached in this example)
# consumer.close()
client.close()