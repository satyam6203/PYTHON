import re

# 1. Take input from user to append
data = input("Enter the content to append:\n")

# 2. Append data to the existing file
with open("python_ex.py", "a") as f:
    f.write("\n" + data)

print("\nData appended successfully.\n")

# 3. Reopen the file and read its content
with open("python_ex.py", "r") as f:
    content = f.read()

print("File content before removing comments:\n")
print(content)

# 4. Remove single-line comments using regex
# This removes everything starting with # till end of line
clean_content = re.sub(r"#.*", "", content)

print("\nFile content after removing single-line comments:\n")
print(clean_content)
