def file_handling():
  
    filename = input("Please enter the filename: ")

    try:
        # open and read the file
        with open(filename, 'r') as file:
            content = file.read()  
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        # Handling the error if the file is not found
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Unable to read the file '{filename}'.")
    finally:
        print("Thank you for trying to access the file.")