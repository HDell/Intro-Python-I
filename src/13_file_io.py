"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'foo.txt')
with open(filename) as foo:
    contents = foo.read()
    print(contents)
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
filename = 'bar.txt'
with open(filename, 'w') as bar:
    bar.write("Line one. \nLine two. \nLine three.")
