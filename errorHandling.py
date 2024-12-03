def read_file_with_error_handling():
    try:
        # Prompt the user to enter the name of the file they want to read
        filename = input("Enter the filename: ")
        
        # Attempt to open the file in read mode
        with open(filename, 'r') as file:
            # Read the entire content of the file
            content = file.read()
        
        # Print the file's content to the console
        print("File content:")
        print(content)
    
    # Handle the case where the specified file does not exist
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    
# Call the function to test its functionality
read_file_with_error_handling()
