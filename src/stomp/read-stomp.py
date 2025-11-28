import time
import stomp


# Define a custom listener class to handle incoming messages


class MyListener(stomp.ConnectionListener):
    print("Esperando mensajes....")
    def on_error(self, headers, message):
        print(f'Received an error: "{message}"')

    def on_message(self,  message):
        mensaje = message.body

        print(f'Received message: "{message}"')
        print(f'  mensaje: "{mensaje}"')

        # print(f'Headers: {headers}')


# Connection details
host = 'alma-gncon'  # Replace with your STOMP broker's host
port = 61613  # Replace with your STOMP broker's port
username = 'admin'  # Replace with your broker's username
password = 'admin'  # Replace with your broker's password
destination = '/topic/demo'  # Replace with the queue/topic you want to subscribe to

# Create a connection object
conn = stomp.Connection([(host, port)])

# Set the listener
conn.set_listener('', MyListener())

# Start the connection
# conn.start()

# Connect to the broker
conn.connect(username, password, wait=True)

# Subscribe to the destination
conn.subscribe(destination=destination, id=1, ack='auto')

print(f"Subscribed to {destination}. Waiting for messages...")

try:
    # Keep the connection alive to receive messages
    while True:
        time.sleep(1)


except KeyboardInterrupt:
    print("\nDisconnecting...")
finally:
    # Disconnect from the broker
    conn.disconnect()