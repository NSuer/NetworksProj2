def connect(args):
    if len(args) != 2:
        print("Error: Insufficient arguments for %connect command. Usage: %connect <address> <port>")
        return
    address, port = args
    print(f"Connecting to server at {address}:{port}")

def join(args):
    if len(args) != 0:
        print("Error: %join command does not require any arguments.")
        return
    print("Joining the message board")

def post(args):
    if len(args) < 2:
        print("Error: Insufficient arguments for %post command. Usage: %post <subject> <content>")
        return
    subject = args[0]
    message_content = ' '.join(args[1:])
    print(f"Posting message - Subject: {subject}, Content: {message_content}")

def users(args):
    if len(args) != 0:
        print("Error: %users command does not require any arguments.")
        return
    print("Retrieving list of users")

def leave(args):
    if len(args) != 0:
        print("Error: %leave command does not require any arguments.")
        return
    print("Leaving the group")

def message(args):
    if len(args) != 1:
        print("Error: %message command requires one argument - message ID.")
        return
    message_id = args[0]
    print(f"Retrieving message content for message ID: {message_id}")

def parse_command(command):
    parts = command.split()
    action = parts[0]
    args = parts[1:]

    match action:
        case '%connect':
            connect(args)
        case '%join':
            join(args)
        case '%post':
            post(args)
        case '%users':
            users(args)
        case '%leave':
            leave(args)
        case '%message':
            message(args)
        case '%exit':
            exit_client()
        case _:
            print("Unknown command")

def exit_client():
    print("Exiting the client program")
    exit()

command_num = 0
while True:
    command = input(f"mux-{command_num}:")
    if command and command[0] == '%':
        parse_command(command)
    else:
        pass
    command_num += 1