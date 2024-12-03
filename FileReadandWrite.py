def modify_file_content(input_file, output_file):
    try: 
        # Read the content of the input file
        with open(input_file, 'r') as file:                        # Open the input file in read mode
            content = file.read()                                  # Read the entire content of the file
        
        # Modify the content 
        modified_content = content.upper()                         # Convert the content to uppercase
        
        # Write the modified content to the output file
        with open(output_file, 'w') as file:                       # Open the output file in write mode
            file.write(modified_content)                           # Write the modified content to the file
        
        # Success message indicating the output file creation
        print(f"Modified content written to {output_file}")
    
    # Handle the case where the input file does not exist
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    
# Call the function with the input and output filenames
modify_file_content('input.txt', 'output.txt')



