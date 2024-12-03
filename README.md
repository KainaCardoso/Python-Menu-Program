# Python-Menu-Program

This Python script provides a simple command-line interface (CLI) to perform various operations, such as showing the local date and time, displaying the local IP address, connecting to a remote device, backing up files, and saving web pages.

**Features**

- Show Local Date and Time**: Displays the current date and time on the local computer.
- Show Local IP Address: Retrieves and displays the local IP address.
- Show Remote Home Directory**: Connects to a remote Linux device and lists the contents of the home directory.
- Backup Remote File**: Backs up a specified file on the remote device.
- Save Web Page**: Downloads and saves the content of a specified web page to the local desktop.

**Requirements**

- Python 3.x
- netmiko library (for SSH connections)
- requests library (for HTTP requests)

You can install the required libraries using pip:

pip install netmiko requests

**Usage**

1. Clone this repository to your local machine:

  use this command: git clone https://github.com/yourusername/Menu-Assignment-011.git

2. Navigate to the project directory:

  cd Menu-Assignment-011

3. Open the script in your preferred text editor and modify the REMOTE_DEVICE settings with your remote device details.

4. Run the script:
  python Menu_Assignment_011.py

5. Follow the on-screen menu to execute the desired option.


**Example Menu**

Menu:
1 - Show date and time (local computer)
2 - Show IP address (local computer)
3 - Show Remote home directory listing
4 - Backup remote file
5 - Save web page
Q - Quit
