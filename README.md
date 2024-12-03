# Python_Week_4_Assignment
# File Read & Write Challenge with Error Handling

This project demonstrates fundamental file handling and error management concepts in Python through two functions: **modifying file content** and **reading files with error handling**. These examples are practical, beginner-friendly, and useful for understanding how to manage file-related operations robustly.

---

## Features

1. **File Read & Write Operation:**
   - Reads content from a file.
   - Modifies the content (e.g., converts text to uppercase).
   - Writes the modified content to a new file.

2. **Error Handling:**
   - Prompts the user for a filename and gracefully handles cases where:
     - The file does not exist.
     - The file cannot be read due to permission or other issues.

---

## Functions

### 1. `modify_file_content()`

#### **Description**
This function reads content from an input file, modifies it (e.g., converts text to uppercase), and writes the modified content to an output file.

#### **How It Works**
1. Reads the content of the input file.
2. Modifies the content (e.g., converts text to uppercase).
3. Writes the modified content to the output file.

#### **Usage**
1. Call the function with the names of the input and output files:
   ```python
   modify_file_content('input.txt', 'output.txt')

   
6. The program will prompt you to enter:
- **Input filename**: The name of the file to read from.
- **Output filename**: The name of the file to write the modified content to.
7. The program will process the input file, modify the content (convert it to uppercase), and write it to the output file. If any errors occur, a descriptive error message will be shown.
