import os
import socket
import requests
from datetime import datetime
from netmiko import ConnectHandler

# The remote device settings in this case will be the virtual box
REMOTE_DEVICE = {
    'device_type': "linux",
    'host': "127.0.0.1",
    'port': "5679",
    'username': "kaina",  
    'password': "kaina",
}

def show_date_time():
    # Get the current local date and time
    current_time = datetime.now()
    print("Local Date and Time:", current_time)

def show_ip_address():
    # Get the local computer's hostname and IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("Local IP Address:", ip_address)
    
# Connect to the remote device and list the home directory
def show_remote_home_directory():
    try:
        connection = ConnectHandler(**REMOTE_DEVICE)  # Establish SSH connection
        output = connection.send_command('ls ~')  # Run command to list home directory
        print("Home Directory Listing:\n", output)  # Print the output
        connection.disconnect()  # Close the connection
    except Exception as e:
        print("Error connecting to remote device:", e)

def backup_remote_file():
    # Ask the user for the file path to back up
    remote_file_path = input("Enter the full path of the remote file to back up including file name: ")
    backup_file_path = remote_file_path + '.old'  # Create a new backup file name
    try:
        connection = ConnectHandler(**REMOTE_DEVICE)  # Establish SSH connection
        connection.send_command(f'cp {remote_file_path} {backup_file_path}')  # Copy the file
        print("Backup created:", backup_file_path)  # Confirm backup creation
        connection.disconnect()  # Close the connection
    except Exception as e:
        print("Error backing up the file:", e)

def save_web_page():
    # Ask the user for a URL to save the web page
    url = input("Enter the URL of the web page to save: ")
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    filename = os.path.join(desktop_path, url.split('/')[-1] or 'saved_web_page.txt')
    
    try:
        response = requests.get(url)  # Make a GET request to the URL
        if response.status_code == 200:  # Check if the request was successful
            with open(filename, 'w', encoding='utf-8') as file:  # Open the file for writing
                file.write(response.text)  # Write the web page content to the file
            print("Web page saved as:", filename)  # Confirm saving
        else:
            print("Failed to save the web page. Status code:", response.status_code)  # Handle failure
    except Exception as e:
        print("Error saving web page:", e)

def main():
    while True:
        # Display the menu options
        print("\nMenu:")
        print("1 - Show date and time (local computer)")
        print("2 - Show IP address (local computer)")
        print("3 - Show Remote home directory listing")
        print("4 - Backup remote file")
        print("5 - Save web page")
        print("Q - Quit")

        choice = input("Select an option: ").strip().upper()  # Get user choice

        # Call the appropriate function based on user choice
        if choice == '1':
            show_date_time()
        elif choice == '2':
            show_ip_address()
        elif choice == '3':
            show_remote_home_directory()
        elif choice == '4':
            backup_remote_file()
        elif choice == '5':
            save_web_page()
        elif choice == 'Q':
            print("Exiting the program.")
            break  # Exit the loop and end the program
        else:
            print("Invalid option. Please try again.")  # Handle invalid input

if __name__ == '__main__':
    main()  # Start the program
