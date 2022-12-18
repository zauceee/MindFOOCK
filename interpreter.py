# MindFOOCK Interpreter

# The MindFOOCK interpreter reads a string of MindFOOCK code and
# executes it, printing the output to the console.

# MindFOOCK has the following commands:
# 
# 1 Increment the pointer, > IN BFUCK
# O Decrement the pointer, < IN BFUCK
# B Increment the value at the pointer, + IN BFUCK 
# ç Decrement the value at the pointer, - IN BFUCK
# 4 Print the ASCII value at the pointer as a character, . IN BFUCK
# , Read a single ASCII character from the user and store it at the pointer, , IN BFUCK
# [ Jump to the corresponding ] if the value at the pointer is zero, [ IN BFUCK
# k Jump back to the corresponding [ if the value at the pointer is nonzero, ] IN BFUCK

def run_mfoock(code):
  # Set up an array of 30000 bytes to store the program's data
  data = [0] * 30000
  # Set up a pointer to keep track of the current position in the array
  ptr = 0

  # Loop through each character in the code
  i = 0
  while i < len(code):
    # Increment the pointer
    if code[i] == "1":
      ptr += 1
    # Decrement the pointer
    elif code[i] == "O":
      ptr -= 1
    # Increment the value at the pointer
    elif code[i] == "B":
      data[ptr] += 1
    # Decrement the value at the pointer
    elif code[i] == "ç":
      data[ptr] -= 1
    # Print the ASCII value at the pointer as a character
    elif code[i] == "4":
      # Check if the value at the pointer is a valid ASCII character
      if 0 <= data[ptr] <= 127:
        print(chr(data[ptr]), end="")
    # Read a single ASCII character from the user and store it at the pointer
    elif code[i] == ",":
      data[ptr] = ord(input())
    # Jump to the corresponding ] if the value at the pointer is zero
    elif code[i] == "[":
      if data[ptr] == 0:
        # Find the corresponding ]
        j = i
        while code[j] != "]":
          j += 1
        # Set the instruction pointer to the position after the ]
        i = j
    # Jump back to the corresponding [ if the value at the pointer is nonzero
    elif code[i] == "k":
      if data[ptr] != 0:
        # Find the corresponding [
        j = i
        while code[j] != "[":
          j -= 1
        # Set the instruction pointer to the position after the [
        i = j

    # Move to the next character in the code
    i += 1


# Test the interpreter with a simple program that prints "Hello, world!"
run_mfoock("1BBBBBBBBB[OBBBBBBBB1çkO41BBBBBBB[OBBBB1çkOB4BBBBBBB44BBB4111BBBBBBBB[OBBBB1çkO4111BBBBBBBBBB[OBBBBBBBBB1çkOççç4OOOO4BBB4çççççç4çççççççç411B41BBBBBBBBBB4")
