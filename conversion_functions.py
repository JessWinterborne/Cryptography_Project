# -*- coding: utf-8 -*-
# Conversion functions developed in Lecture 2 of Week 10

def char_to_byte(char): 
    """
    Returns the 8 bit binary representation (padded with 
    leading zeros with necessary) of ord(char), i.e. of 
    the order of the input character char. 
    """
    byte_string = bin(ord(char))[2:]     # The order of char as a binary string 
    num_zeros = 8 - len(byte_string)     # The number of zeros needed to pad out byte_string
    for i in range(num_zeros):           # Now pad out byte_string with num_zeros many zeros
        byte_string = '0' + byte_string  # to obtain the 8-bit binary representation
    return byte_string  

def convert_to_integer(text,verbose=False): 
    """
    Returns an integer that encodes the input string text. 
    Each character of text is encoded as a binary string of 
    8 bits. These strings are concatenated with a leading 1
    and the resulting binary string is converted into the 
    returned integer.
    """
    bin_string = '1'
    for letter in text: 
        bin_string = bin_string + char_to_byte(letter)
    if verbose: 
        print("The binary representation of this message is:")
        print(bin_string)
    return int(bin_string,2)

def convert_to_text(number): 
    """ 
    Returns a string that is the decoding of the input integer number.
    This is done by converting number to a binary string, removing the 
    leading character '1', slicing out each 8 bit substring consecutively,
    converting each such string to the character it encodes and concatenating
    these characters to obtain the decoded string.    
    """
    # Remove '0b1' from the string
    bin_string = bin(number)[3:]    
    text = ''                           
    length = len(bin_string)
    for i in range(0,length,8):  
        # Pick out binary strings, 8 bits at a time
        byte_string = bin_string[i:i+8]   
        # Convert byte_string to a character before 
        # appending it to text 
        text = text + chr(int(byte_string,2))  
    return text