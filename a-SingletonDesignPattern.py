# Ticketing System via Singleton PAttern
# The Singleton pattern is a creational design pattern that ensures 
# a class has only one instance and 
# provides a GLOBAL point of access to that instance 
# throughout the application. 


class TicketDispenser:
    _instance = None
    _ticket_count = 0

    # This gets called everytime the class gets instatiated
    def __new__(self):
        # Check if the class doesn't have an instance yet
        if self._instance is None:
            # Create a new instance if it doesn't exist
            self._instance = super().__new__(self)
        # Return the instance (either the existing or newly created one)
        return self._instance


    def get_ticket(self):
        self._ticket_count += 1
        return f"Ticket #{self._ticket_count}"

# Usage
ticket_machine1 = TicketDispenser()
ticket_machine2 = TicketDispenser()

print(ticket_machine1 is ticket_machine2)  # Output: True - Both variables point to the same instance

ticket1 = ticket_machine1.get_ticket()
ticket2 = ticket_machine2.get_ticket()

print(ticket1)  # Output: Ticket #1
print(ticket2)  # Output: Ticket #2
