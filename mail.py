import tkinter as tk
import smtplib

def send_email():
    sender_email = email_entry.get()
    sender_password = password_entry.get()
    recipient_email = recipient_entry.get()
    message = message_entry.get("1.0", "end")
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.sendmail(sender_email, recipient_email, message)
        status_label.config(text="Email sent successfully!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {e}", fg="red")
    
root = tk.Tk()
root.title("Mail Application")

# Sender's email address
email_label = tk.Label(root, text="Email address:")
email_label.pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack()

# Sender's email password
password_label = tk.Label(root, text="Email password:")
password_label.pack()
password_entry = tk.Entry(root, width=50, show="*")
password_entry.pack()

# Recipient's email address
recipient_label = tk.Label(root, text="Recipient address:")
recipient_label.pack()
recipient_entry = tk.Entry(root, width=50)
recipient_entry.pack()

# Email message
message_label = tk.Label(root, text="Message:")
message_label.pack()
message_entry = tk.Text(root, width=50, height=10)
message_entry.pack()

# Send button
send_button = tk.Button(root, text="Send", command=send_email)
send_button.pack()

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
