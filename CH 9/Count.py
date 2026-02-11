# Open the file in read mode
with open("file.txt", "r") as f:
    content = f.read()

# Split the content into words
words = content.split()

# Count the number of words
word_count = len(words)

# Display the result
print("Number of words in the file:", word_count)
