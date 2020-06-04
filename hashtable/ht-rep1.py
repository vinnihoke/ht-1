class Node:
    def __init__(self, key, value):
        # Setup nodes
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({repr(self.key)}, {repr(self.value)}'

MIN_CAPACITY = 8

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, node):
        node.next = self.head
        self.head = node

    def get(self, target):
        # Set the current to self.head
        current = self.head

        # While current is not None
        while current is not None:
            # If the current value matches target:
            if current.value == target:
                return current

            # Otherwise
            elif current.value == None:
                return None

            # Set current to the next value
            current = current.next

    def remove(self, target):
        # Set the current to the self.head
        current = self.head

        # If current value is target
        if current.value == target:
            # Weave around the value to be removed.
            self.head = self.head.next

            # Returned the removed value
            return current

        # Record the previous value as the previous self.head
        previous = current
        
        # Set the current as the removed values next value
        current = current.next

        # While current is not None
        while current is not None:
            # Check if the next value, which is now current, is the target value.
            if current.value == target:
                # Current is still the current head and hasn't been removed yet. Setting previous.next to current.next targets current for trash collection.
                previous.next = current.next

                # Return the removed value
                return current
            else:
                # advance the list and keep moving.
                previous = previous.next
                current = current.next

            # Nothing was found. Return None.
            return None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity

        # Create an empty list of None values the length of the capacity.
        self.storage = [None] * capacity

    def storage_capacity(self):
        return len(self.storage)

    def load_factor(self):
        # Start a count
        total = 0

        for i in range(len(self.storage)):
            # Check if there is a value at storage[i]
            if self.storage[i] != None:

                # Record the current head.
                current = self.storage[i].head

                while current.next is not None:
                    # increment the total.
                    total += 1

                    #  Move along the linked list.
                    current = current.next

                # There is only one item in the list.
                total += 1
        # Calculate load capacity by dividing the total by the len of storage capacity.
        return total / self.storage_capacity()


    def hash_algorithm(self, key):
        # using DJB2 Hash, 32-bit
        # Don't quite understand this bit.
        bytes_obj = str(key).encode("utf-8")
        djb2_val = 5381
        total_val = 0
        for char in bytes_obj:
            total_val += ((djb2_val << 5) + djb2_val) + char
            total_val &= 0xffffffff
        return total_val

    def hash_index(self, key):
        # This will return a value that will be used to add the object to a hopefully unique spot in the array. Otherwise they'll collide and be added to a linked list.
        return self.hash_algorithm(key) % self.capacity

    def put(self, key, value):
        # Create an index.
        index = self.hash_index(key)

        # Create a reference to the current node at index
        reference = self.storage[index]

        # Is something new?
        if reference != None:

            # Store a reference to the current value
            current = reference.head

            # Loop through the LL if current.next is not none.
            while current.next is not None:

                # If current key is the key:
                if current.key == key:

                    #Set the current value to the passed in value.
                    current.value = value
                # Advance down the list
                current = current.next

            # Current is now the final spot in the LL 
            if current.key == key:

                # Set the final node's value.
                current.value = value

            else:
                # This is the first element in the list. Create a LL.
                reference = LinkedList()

                # Add to head of LL
                reference.add_to_head(Node(key, value))

    def delete(self, key):

        # Create an index.
        index = self.hash_index(key)

        # Create a reference to the current node at index
        reference = self.storage[index]

        # If the key at head is a match for key
        if reference.head.key == key:

            # Remove the value and garbage collection does the rest.
            reference.head.value = None

        # This head.key is not a match
        else:
            # Set the current head to store it for further use.
            current = reference.head

            # While current.next != None loop the list
            while current.next is not None:
                # Check if the current key is the target
                if current.key == key:
                    # Set target value to None for garbage removal
                    current.value = None
                # increment the list
                current = current.next

            # Current value is the key.
            if current.key == key:

                # Remove the value to be collected by garbage pickup.
                current.value = None
            else:
                return "Key not found!"

    def get(self, key):
        
        # Create an index
        index = self.hash_index(key)

        # Create a reference to the current node at index
        reference = self.storage[index]

        # Is the reference None?
        if reference == None:

            # There is nothing at self.storage[index]
            return None

        # Something there, does it have a key?
        if reference.head.key == key:

            # This is what we are looking for, return the value
            return reference.head.value

        # Something there, but doesn't match key. Start looping
        else:

            # Create a reference for current
            current = reference.head

            while current.next is not None:

                # Check if the current.key is the key
                if current.key == key:

                    # We have a match!
                    return current.value

                # Continue to loop
                current = current.next

            # Is current is not the final node, is it the key?
            if current.key == key:
                
                # Yes it is, return value
                return current.value

            # there were no matches, return None.
            else:
                return None


    def resize(self, new_capacity):

        # Create a copy of the current storage.
        storage_copy = self.storage

        # Change the capacity to the incoming capacity.
        self.capacity = new_capacity

        # Create a new self.storage with the new capacity size.
        self.storage = [None] * self.capacity

        # Loop through everything in the previous storage and re-map it using the new capcity.
        for i in range(len(storage_copy)):

            # Exclude un-used values. Checking if something exists.
            if storage_copy[i] != None:

                # Create a reference to the current head.
                current = storage_copy[i].head

                #  If there is a current.next loop
                while current.next is not None:

                    # Add the value to the new resized storage
                    self.put(current.key, current.value)

                    # increment the current so it'll loop
                    current = current.next

                # There is no current.next, just add it in.
                self.put(current.key, current.value)

                




