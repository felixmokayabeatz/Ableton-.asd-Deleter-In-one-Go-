import os

def delete_files_with_extension(directory, extension):
    deleted_files = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(extension):
                file_path = os.path.join(root, filename)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    deleted_files += 1
                except Exception as e:
                    print(f"Failed to delete: {file_path} - {e}")

    print(f"Total {extension} files deleted: {deleted_files}")

def user_input():
    directory_path = input("Enter the directory path: ")
    extension_choice = input("Enter the file extension you want to delete (e.g., .zpa, .url, .asd): ")
    return directory_path, extension_choice

if __name__ == "__main__":
    print("WARNING: This script deletes files irreversibly. Use only if you fully understand its functionality.")
    proceed = input("If you understand and wish to proceed, type 'YES' in all caps: ")
    
    if proceed == "YES":
        directory, extension = user_input()
        delete_files_with_extension(directory, extension)
    else:
        print("Operation aborted. Please ensure you understand the functionality before using the script.")
