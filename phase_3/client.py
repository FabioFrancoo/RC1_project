import socket

def main():
    server_ip = input("Endereço IP do servidor: ")
    server_port = 8888

    # Connect to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    # Receive the prompt asking for name from the server
    prompt = client.recv(1024).decode()
    print(prompt, end="")  # Print the prompt (without an extra newline)

    # Send the player's name
    player_name = input()
    client.send(player_name.encode())

    while True:
        # Receive the number guess prompt from the server
        print(client.recv(1024).decode(), end="")

        # Send guess to the server
        guess = input("Número? ")
        client.send(guess.encode())

        # Receive hint or winning message
        message = client.recv(1024).decode()
        print(message)

        if "Parabéns" in message:
            break

    client.close()

if __name__ == "__main__":
    main()
