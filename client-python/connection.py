# Message
    # Uses Unix Timestamp

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

# Connection

# Actions