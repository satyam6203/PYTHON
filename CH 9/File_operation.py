# Open the file in read mode
with open("file.txt", "r") as f:
    lines = f.readlines()

# 1. Number of lines
num_lines = len(lines)

# Combine all lines into one string
text = " ".join(lines)

# Convert to lowercase and split into words
words = text.lower().split()

# 2. Number of unique words
unique_words = set(words)

# 3. Dictionary of word occurrences
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1
    
# Output
print("Number of lines:", num_lines)
print("Number of unique words:", len(unique_words))
print("Word occurrences:")
print(word_count)
