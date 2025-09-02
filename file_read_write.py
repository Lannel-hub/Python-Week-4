# File Read & Write Challenge
def modify_file():
    try:
        # Read original file
        with open('input.txt', 'r') as file:
            content = file.read()
        
        # Modify content (add line numbers)
        lines = content.split('\n')
        modified = '\n'.join(f"{i+1}: {line}" for i, line in enumerate(lines))
        
        # Write to new file
        with open('output.txt', 'w') as file:
            file.write(modified)
        
        print("File successfully processed!")
        
    except FileNotFoundError:
        print("Error: Input file not found")
    except PermissionError:
        print("Error: Permission denied")
    except Exception as e:
        print(f"Error: {e}")

# Run the program
modify_file()
