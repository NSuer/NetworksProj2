from . import terminal
from . import connection

command_num = 0
while True:
    command = input(f"mux-{command_num}:")
    if not command:
        continue
    if command[0] == '%':
        terminal.parse_command(command)
    else:
        # TODO TODOSW
        # This is where we should have the message be sent
        # this function should:
            # take data from cli
            # determine what it is doing
            # format it correctly as a message
            # pass the message off to connection
            # AWAIT (not actually, this needs to be a separate solution) a response
            # TODO AWAIT is super bad, we need multiple text areas for our GUI
        pass
    command_num += 1