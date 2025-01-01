# messages.py

class MessageStore:
    def __init__(self, max_messages=100):
        self.messages = []
        self.max_messages = max_messages

    def add_message(self, message):
        """Add a message to the store and keep only the last `max_messages`."""
        self.messages.append(message)
        # Keep only the last `max_messages` messages
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def get_messages(self):
        """Retrieve all stored messages."""
        return self.messages


# Create an instance of the store with a limit of 100 messages
message_store = MessageStore()
