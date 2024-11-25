try:
    with open('/.file.text', 'r') as file:
        print(file.read()) 

except FileNotFoundError:
    print("Error: The file 'file.text' was not found.")
except IOError:
    print("Error: Unable to read the file 'file.text'. It may be in use or you may not have permission.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Append to the 'write' file
with open("write", "a") as write:
    write.write("I love python")

# Write to the new file
with open("new.file", "w") as newFile:
    newFile.write("This is week 4 assignment")

    import os
print("Current Working Directory:", os.getcwd())

print("Files in the current directory:", os.listdir())





 




