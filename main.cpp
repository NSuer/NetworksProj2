// Server for chat board using univast sockets 
#include <sys/socket.h>
#include <iostream>
#include <cstring>
#include <netinet/in.h>
#include <unistd.h>
#include <thread>

// max_clients is the maximum number of clients that can connect to the server
int max_clients = 64;
// client_threads is an array of threads that will handle each client
thread client_threads[max_clients];
// client_sockets is an array of sockets that will be used to communicate with each client
int client_sockets[max_clients];
// client_count is the number of clients that are currently connected to the server
int client_count = 0;
// SavedMessages is a 2D array that will store the messages that have been sent to the server
string SavedMessages[5][2];
// message_count is the number of messages that have been sent to the server
int message_count = 0;
// current_usernames is an array of strings that will store the usernames of the clients that are currently connected to the server
string current_usernames[64];

using namespace std;

int main() {
    // Create a socket
    int server_socket = socket(AF_INET, SOCK_STREAM, 0);
    // Check if the socket was created successfully
    if (server_socket == -1) {
        cout << "Error creating socket" << endl;
        return 1;
    }
    // Print a message to the console on successful creation of the server socket
    cout << "Server socket created" << endl;

    // Bind the socket to an IP address and port
    sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(54000);
    server_address.sin_addr.s_addr = INADDR_ANY;
    int bind_result = bind(server_socket, (sockaddr*)&server_address, sizeof(server_address));

    // Check if the socket was bound successfully
    if (bind_result == -1) {
        cout << "Error binding socket" << endl;
        return 1;
    }
    
    while (true) {
        // Listen for incoming connections
        listen(server_socket, SOMAXCONN);

        // Accept a new connection

        // if the maximum number of clients have connected to the server, print a message to the console
        if (client_count == max_clients) {
            cout << "Max clients reached" << endl;
        } else { // otherwise, accept the new connection
            // Accept the new connection
            client_sockets[client_count] = accept(server_socket, NULL, NULL);
            // Check if the connection was accepted successfully
            if (client_sockets[client_count] == -1) {
                cout << "Error accepting socket" << endl;
                return 1;
            }
            // make a new thread to handle the new client
            client_threads[client_count] = thread(handle_client, client_sockets[client_count]);
            // detach the thread so that it can run independently
            client_threads[client_count].detach();
            // increment the client count
            client_count++;
        }
    }
    return 0;
}

int handle_client(int client_socket) {\
    string action;
    string group;
    string message_id;
    string sender;
    string post_date;
    string subject;
    string message;

    char buffer[4096]; // buffer to store the message
    memset(buffer, 0, 4096); // clear the buffer
    while (client_socket) {
        int bytes_recieved = recv(client_socket, buffer, 4096, 0); // receive the message from the client

        // Check if the message was received successfully
        if (bytes_recieved == -1) {
            cout << "Error in recv()" << endl;
            return 1;
        }
        // Check if the client has disconnected
        if (bytes_recieved == 0) {
            cout << "Client disconnected" << endl;
            return 1;
        }

        // Message will be in following order 
        // Action
        // Group
        // Message ID
        // Sender
        // Post Date
        // Subject
        // Message

        // parse message by { and } and store in array
        string message = string(buffer, 0, bytes_recieved); // convert the buffer to a string
        vector<string> parsedMessage; // vector to store the parsed message
        size_t start = message.find('{'); // find the first '{' in the message
        size_t end; // variable to store the position of the '}'
        while (start != string::npos) { // while there are still '{'s in the message
            end = message.find('}', start); // find the next '}'
            if (end == string::npos) { // if there is no '}' after the '{'
                cout << "Invalid message format" << endl; // print an error message
                return 1;
            }
            string substring = message.substr(start + 1, end - start - 1); // extract the substring between the '{' and '}'
            parsedMessage.push_back(substring); // add the substring to the vector
            start = message.find('{', end); // find the next '{'
        }

        // Switch case on the action
        action = parsedMessage[0];
        group = parsedMessage[1];
        message_id = parsedMessage[2];
        sender = parsedMessage[3];
        post_date = parsedMessage[4];
        subject = parsedMessage[5];
        message = parsedMessage[6];

        switch (action) {
            case "POST": // Post a message to the group

                break;
            case "CREATE_USER": // Create a new user

                break;
            case "GET": // Get a message from the group

                break;
            default:
                cout << "Invalid action" << endl;
                return 1;
        }
    }
    return 0;
}
