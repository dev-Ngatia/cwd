import http.server
import socketserver

# Set the IP address and port
ip_address = "0.0.0.0"  # Use your local IP address
port = 8888

# Combine the IP address and port into a tuple
address = (ip_address, port)

# Define the handler to use for serving files (this uses the SimpleHTTPRequestHandler)
handler = http.server.SimpleHTTPRequestHandler

# Create the server with the specified address and handler
http_server = socketserver.TCPServer(address, handler)

# Print a message indicating that the server is running
print(f"Server is running at http://{ip_address}:{port}/")

# Start the server
http_server.serve_forever()
