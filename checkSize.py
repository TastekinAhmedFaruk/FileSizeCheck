import os
import datetime
import logging
import smtplib
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Timestamp created
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Special path of log file
log_dir = r"Folder Path"
log_file = os.path.join(log_dir, f'app_log_{timestamp}.txt')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#Get Os Info
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

def get_folder_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    logging.info(total_size / (1024 * 1024 ) )
    return total_size / (1024 * 1024 )  # MB size

# Check Path
def main():
    logging.info("Start Program")
    folder_path = "Source Path"
    max_size_mb = 20000
    folder_size = get_folder_size(folder_path)
    logging.info(f"Check source folder: {folder_path}")
    if folder_size >= max_size_mb:
        subject = hostname + " Folder Size Exceeded!"
        body = ip_address + " " + folder_path + " The folder has reached a certain size."
        to_email = "target@blabla.com"
        send_email(subject, body, to_email)

def send_email(subject, body, to_email):
    # Email configuration
    smtp_server = 'smtp.blabla.com'
    smtp_port = 587
    smtp_user = 'sender@blabla.com'
    smtp_password = 'pass'
    logging.info("Mail information success.")

    # Email created
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    logging.info("Mail created.")

    # Connect to SMTP server and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(smtp_user, to_email, msg.as_string())
    logging.info("Mail send.")
    server.quit()
    
if __name__ == "__main__":
    main()
    logging.info("End Program")