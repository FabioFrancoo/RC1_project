import socket
import random

# Function to handle client interaction
def handle_client(client_socket, address):
    # Define the number range
    min_number = 1
    max_number = 100
    random_number = random.randint(min_number, max_number)

    print(f"Nova conexão desde {address}.")
    
    # Ask for player's name
    client_socket.send("Nome? ".encode())
    player_name = client_socket.recv(1024).decode()

    print(f"O jogador '{player_name}' conectou-se a partir do endereço {address}")

    # Initialize attempts counter
    attempts = 0

    while True:
        # Receive guess from client
        client_socket.send(f"Descobre o número secreto entre {min_number} e {max_number}: ".encode())
        guess = int(client_socket.recv(1024).decode())
        attempts += 1

        # Check if the guess is correct
        if guess < random_number:
            client_socket.send("Maior!\n".encode())
        elif guess > random_number:
            client_socket.send("Menor!\n".encode())
        else:
            client_socket.send(f"Parabéns {player_name}, acertaste no número secreto em {attempts} tentativas!\n".encode())
            break

    client_socket.close()

def main():
    # Set up the server
    server_ip = '0.0.0.0'
    server_port = 8888
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)

    print("À espera de conexões...")

    while True:
        # Accept a new client connection
        client_socket, client_address = server.accept()
        address = client_address[0]
        handle_client(client_socket, address)

if __name__ == "__main__":
    main()
