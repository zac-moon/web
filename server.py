import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = ''  
    port = 60951
    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    def error(eoc, url_request,client_address,html_content,client_socket):
        print('')
        print(f'ERROR OCCURED : {eoc}')
        print(f'URL Request : {url_request}')
        print(f'FROM : IP{client_address} SOCKET{client_socket}')
        print(f'CONTENT RETURNED :{html_content}')
        print('')

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print('=========================================')
            print(f"Connection established with {client_address}")

            url_request = client_socket.recv(1024).decode().strip()

            if not url_request:  
                print("Error: Empty URL Request")
                client_socket.sendall(b"<h1>400 Bad Request</h1>")
                eoc = '400 bad Request (URL Field Empty)'
                error(eoc, url_request,client_address,html_content,client_socket)
            else:
                print(f'URL Requested : {url_request}')
                html_content = read_html_content(url_request)

                client_socket.sendall(html_content.encode())
                print(f'Read source HTML from {url_request}')
                print(f'Source sent to client {client_address}')

            client_socket.close()
        except FileNotFoundError:
            print(f"Error: 404 URL Not Found: {url_request}")
            eoc = "404 Not Found"
            error(eoc, url_request,client_address,html_content,client_socket)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error occurred: {e}")
            eoc = e
            error(eoc, url_request,client_address,html_content,client_socket)

    server_socket.close()
    print("Server closed")


def read_html_content(url_request):
    split_path = []
    refsars = 'url_blank_'
    split_path += url_request.split('.')

    if len(split_path) == 2:
        refsars = url_request + "/index.html"
    elif len(split_path) == 3:
        refsars = f"{split_path[1]}.{split_path[2]}/{split_path[0]}/index.html"

    try:
        with open(refsars, "r") as sourcefile:
            return sourcefile.read()
    except FileNotFoundError:
        print(f"Error: 404 URL Not Found: {url_request}")
        return f"<h1>404 Not Found- {url_request}</h1>"
    except Exception as e:
        print(f"Error occurred: {e}")
        return f"<h1>Internal Server Error</h1><br><h3>Error : {e}</h3>"


if __name__ == "__main__":
    start_server()
