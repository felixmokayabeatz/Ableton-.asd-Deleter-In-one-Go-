Ableton ASD File Deletion Script

This Python script facilitates the deletion of specific file types within a designated directory. Users can input the directory path and the file extension(s) to delete files.

Usage

1. Running the Script:
    - Ensure Python is installed on your system.
    - Open a terminal or command prompt.

2. Navigate to the Directory:
    - Use the `cd` command to move to the directory where the script ('AbletonAsd.py') is located, example 'cd C:\Users\YourName\Downloads'

3. Running the Script:
    - Execute the script by typing, in the terminal/Command prompt.
    ```
    python AbletonAsd.py
    ```
    Press Enter.

4. User Warning:
    - A warning message displays, cautioning users about the irreversible nature of file deletions.

5. Confirmation:
    - Type 'YES' in all caps to proceed if you understand the script's functionality.
    - If not, the script aborts to prevent accidental use by those unfamiliar with its operations.

6. Input Directory and File Extensions:
    - Enter the directory path where files are located when prompted.
    - Input the file extension(s) to delete (e.g., `.zpa, .url, .asd`) separated by commas.

7. Deletion Process:
    - The script traverses the specified directory, identifies files with the provided extension(s), and attempts to delete them.
    - Progress messages are displayed, indicating successful deletions or any encountered errors.

8. Caution and Verification:
    - Deletions are permanent. Ensure accuracy in the directory path and file extensions to prevent unintended data loss.
    - Always verify selected files before confirming the deletion process.

9. Completion:
    - Once the script completes, it displays the total number of files deleted with the specified extension(s).

Notes:
- Use this script only if you fully understand its functionality.
- Exercise extreme caution as file deletions are irreversible.
- Ensure accuracy in the selection of directory path and file extensions to avoid accidental removal of important files.
