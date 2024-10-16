import cv2
import smtplib
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from email.message import EmailMessage
import tempfile
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email credentials from .env file
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

# Global variable for storing the captured image path
captured_image_path = None

# Initialize the Tkinter window
root = Tk()
root.title("Photo Capture and Email")
root.geometry("600x500")
root.configure(bg='#f0f8ff')  # Light blue background

# Label to show the captured image
image_label = Label(root, bg='#f0f8ff')
image_label.pack(pady=20)

# Email entry field
email_label = Label(root, text="Enter recipient's email:", font=("Arial", 12), bg='#f0f8ff')
email_entry = Entry(root, width=30, font=("Arial", 12))

# Function to reset the UI to the main screen (with Open Camera button)
def reset_to_main_screen():
    image_label.pack_forget()
    email_label.pack_forget()
    email_entry.pack_forget()
    retake_button.pack_forget()
    send_button.pack_forget()

    # Re-show the capture button
    capture_button.pack(pady=20)

# Function to open the camera and capture an image
def open_camera():
    global captured_image_path
    cap = cv2.VideoCapture(0)

    def show_frame():
        ret, frame = cap.read()
        if ret:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)
            video_label.after(10, show_frame)

    # Capture button functionality
    def capture_image():
        global captured_image_path
        ret, frame = cap.read()
        if ret:
            temp_dir = tempfile.gettempdir()
            captured_image_path = os.path.join(temp_dir, "captured_photo.jpg")
            cv2.imwrite(captured_image_path, frame)

            # Close the camera feed
            cap.release()
            camera_window.destroy()

            # Show the captured image in the Tkinter window
            img = Image.open(captured_image_path)
            img.thumbnail((250, 250))
            img_tk = ImageTk.PhotoImage(img)
            image_label.config(image=img_tk)
            image_label.image = img_tk  # Keep reference to avoid garbage collection

            # Show email prompt and buttons after capturing
            show_email_prompt()

    # Create a new Tkinter window for the camera feed
    camera_window = Toplevel(root)
    camera_window.title("Camera")
    camera_window.geometry("800x600")

    video_label = Label(camera_window)
    video_label.pack()

    # Add the capture button on the camera feed
    capture_button = Button(camera_window, text="Capture", font=("Arial", 14), command=capture_image, bg='#ff6347', fg='white')
    capture_button.pack(pady=20)

    show_frame()

# Show email prompt and retake/send buttons
def show_email_prompt():
    email_label.pack(pady=10)
    email_entry.pack(pady=5)

    retake_button.pack(pady=5)
    send_button.pack(pady=5)

# Function to handle retaking the image
def retake_photo():
    # Hide email and buttons and open camera again
    email_label.pack_forget()
    email_entry.pack_forget()
    retake_button.pack_forget()
    send_button.pack_forget()

    open_camera()

# Function to send the email with the captured photo
def send_email():
    recipient_email = email_entry.get()
    if not recipient_email:
        messagebox.showerror("Error", "Please enter an email address")
        return

    if not captured_image_path:
        messagebox.showerror("Error", "No image captured")
        return

    # Create email message
    msg = EmailMessage()
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg['Subject'] = "Captured Photo"
    msg.set_content("Here is the captured photo")

    # Attach the photo
    with open(captured_image_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(captured_image_path)
        msg.add_attachment(file_data, maintype='image', subtype='jpeg', filename=file_name)

    # Send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")

    # Reset to the main screen after sending the email or error
    reset_to_main_screen()

# Create buttons
capture_button = Button(root, text="Open Camera", font=("Arial", 14), command=open_camera, bg='#00bfff', fg='white')
capture_button.pack(pady=20)

retake_button = Button(root, text="Retake", font=("Arial", 14), command=retake_photo, bg='#ffa500', fg='white')
send_button = Button(root, text="Send", font=("Arial", 14), command=send_email, bg='#32cd32', fg='white')

root.mainloop()
