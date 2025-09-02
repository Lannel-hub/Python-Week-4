# Error Handling Lab
def read_user_file():
    filename = input("Enter filename: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except PermissionError:
        print(f"Error: Cannot read '{filename}' - permission denied")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file")
    except Exception as e:
        print(f"Error reading file: {e}")

# Run the program
read_user_file()
