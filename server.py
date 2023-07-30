import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the server to a specific address and port
    host = ''  # Listen on all available interfaces
    port = 12345  # Choose a suitable port number
    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        try:
            # Wait for a client to connect
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")

            # Receive the URL request from the client
            url_request = client_socket.recv(1024).decode().strip()

            # Process the URL request and read the HTML content from the file
            html_content = read_html_content(url_request)

            # Send the HTML content to the client
            client_socket.sendall(html_content.encode())

            # Close the connection with the client
            client_socket.close()
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error occurred: {e}")

    server_socket.close()
    print("Server closed")


def read_html_content(url_request):
    split_path = []
    split_path +=url_request.split('.')
    if len(split_path) == 1:
        refsars = 'errors/'+split_path[0]+'.html'
    elif split_path[1]=="errors":
        refsars = 'errors/'+split_path[0]+'.html'
    elif len(split_path) == 2:
        print('Sraight Domain')
        refsars = url_request + "/index.html"
    elif len(split_path) == 3:
        print("Subdomain")
        refsars = url_request[1]+'.'+url_request[2]+'/'+url_request[0]+'/index.html'

    try:
        with open(refsars, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: 404 URL Not Found: {url_request}")
        return "<h1>404 Not Found</h1>"
    except Exception as e:
        print(f"Error occurred: {e}")
        return "<h1>Internal Server Error</h1>"


if __name__ == "__main__":
    start_server()
