import smtplib

my_email = "e.b.underwood@gmail.com"
password = "nvnm pbvq smfy xguq"

# Use 'with' to automatically open and close the connection safely
# Force Port 587 and set an explicit 10-second timeout
try:
    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=10) as connection:
        connection.ehlo()  # Identify yourself to the server
        connection.starttls()  # Secure the connection using TLS
        connection.ehlo()  # Re-identify yourself over the encrypted channel

        print("Logging in...")
        connection.login(user=my_email, password=password)

        print("Sending email...")
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,  # Corrected argument name from to_addr to to_addrs
            msg="Subject: Python Test\n\nHello",  # Added basic header structure
        )
        print("Email sent successfully!")

except TimeoutError:
    print("Connection timed out. Your internet router or ISP is blocking Port 587.")
except Exception as e:
    print(f"An error occurred: {e}")
