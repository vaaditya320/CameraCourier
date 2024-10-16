# CameraCourier

**CameraCourier** is a simple yet powerful tool that allows you to capture photos using your webcam and send them via email directly from your Raspberry Pi or any Linux machine. This project utilizes Tkinter for the graphical user interface, OpenCV for image capture, and Python's built-in libraries for sending emails.

## Features

- Capture images using the webcam.
- Send captured images via email.
- User-friendly interface with touch support for Raspberry Pi.

## Requirements

- Python 3
- pip (Python package installer)

## Setup Instructions

Follow these steps to set up and run CameraCourier on your Raspberry Pi or Linux system:

### 1. Update and Upgrade Your System

Before starting, ensure your system is up-to-date. Open the terminal and run:

```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install pip
If pip is not installed by default, you can install it with the following command:
```bash
sudo apt install python3-pip -y
```
### 3. Clone the Repository
Clone this repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/CameraCourier.git
cd CameraCourier
```
### 4. Run the Install Script
Run the install.sh script to install all required dependencies:

```bash
chmod +x install.sh
./install.sh
```

#### 5. Create a .env File
Create a .env file in the project directory to store your email credentials. Use the following format:

```plaintext

SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
```
Note: Make sure to use an App Password instead of your regular Gmail password if you have 2-Step Verification enabled. App Passwords may contain spaces, so ensure you copy them exactly.

### 6. Run the Application
After completing the setup, you can run the CameraCourier application:

```bash
python3 main.py
```
## Usage
Click the "Open Camera" button to start the webcam and view the live feed.
Tap the "Capture Photo" button to take a picture.
After capturing, enter the email address to which you want to send the image.
Choose between "Retake" (to capture again) or "Send" (to email the photo).
## Contributing
If you want to contribute to this project, feel free to submit a pull request or create an issue for suggestions and improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

