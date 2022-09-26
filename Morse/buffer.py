class Buffer:
    def __init__(self):
        """
        Initiates a buffer:
        A string with a custom append function that keeps it below a max length
        """
        self.value = ""
        self.max = 18

    def apnd(self, new_value):
        """
        apnd - function to add new values to the buffer, automatically clearing old values
        if the string becomes too long
        INPUTS:
        new_value - a single digit to be appended to 
        """
        # Append new value
        self.value += new_value
        # If string too long, remove digits from the start
        strLen = len(self.value)
        if strLen > self.max:
            self.value = self.value[(strLen-7):strLen]