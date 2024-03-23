# Message
    # Uses Unix Timestamp

'''
        // Message will be in following order 
        // Action
        // Group
        // Message ID
        // Sender
        // Post Date
        // Subject
        // Message
'''
class Message:
    def __init__(self, action, group, message_id, sender, post_date, subject, message):
        self.action = action
        self.group = group
        self.message_id = message_id
        self.sender = sender
        self.post_date = post_date
        self.subject = subject
        self.message = message

    def to_string(self):
        # this currently uses pipes as a delimiter, this may change
        # all based upon server implementation
        return f"{self.action}|{self.group}|{self.message_id}|{self.sender}|{self.post_date}|{self.subject}|{self.message}"



# Connection
# Error courtesy of chatgpt
import socket
import threading

class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._is_connected = False
        self._receive_thread = threading.Thread(target=self._receive_loop)
        self._receive_thread.daemon = True  # Daemonize the thread so it exits when the main thread exits
        self._receive_thread.start()

    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
            self._is_connected = True
            print("Connected to", (self.host, self.port))
        except ConnectionRefusedError:
            print("Connection refused. Make sure the server is running and the port is correct.")
            self.disconnect()

    def disconnect(self):
        if self._is_connected:
            self.socket.close()
            self._is_connected = False
            print("Disconnected from", (self.host, self.port))

    def send(self, data:Message):
        if self._is_connected:
            try:
                self.socket.sendall(data.to_string.encode())
            except BrokenPipeError:
                print("Connection closed by peer.")
                self.disconnect()

    def _receive_loop(self):
        while True:
            if self._is_connected:
                try:
                    data = self.socket.recv(1024)
                    if not data:
                        print("Connection closed by peer.")
                        self.disconnect()
                        break
                    print("Received:", data.decode())
                except ConnectionResetError:
                    print("Connection reset by peer.")
                    self.disconnect()
                    break