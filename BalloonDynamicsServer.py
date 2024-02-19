import socket
import pickle
from BalloonDynamics import BalloonDynamics  # Assuming BalloonDynamics.py is in the same directory

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host and port
host = 'localhost'
port = 8888

# Bind socket to host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print(f"Server listening on {host}:{port}")

# Initialize BalloonDynamics instance
balloon_dynamics = BalloonDynamics()

while True:
    # Accept incoming connection
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive data from client (Unity)
    data = client_socket.recv(1024)
    print(data)
    
    if data:
        # Unpickle received data (assuming it's a tuple of score and delta_time)
        score, delta_time = pickle.loads(data)
        print(score, delta_time)

        # Update game dynamics
        balloon_dynamics.update(score, delta_time)

        # Send updated game dynamics back to client (Unity)
        dynamics_data = (balloon_dynamics.get_spawn_rate(), balloon_dynamics.get_speed(), balloon_dynamics.get_difficulty_level())
        client_socket.sendall(pickle.dumps(dynamics_data))

    # Close connection
    client_socket.close()
