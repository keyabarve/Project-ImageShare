import webbrowser
import pyimgur
from twilio.rest import Client


# Uploading image to imgur and receiving image link

client_id = input("Enter client id : ") # your client id
client_secret = input("Enter client secret : ") # your client secret

client = pyimgur.Imgur(client_id, client_secret)
auth_url = client.authorization_url('pin')
webbrowser.open(auth_url)
pin = input("Enter the pin : ") # the pin you receive on your imgur account
client.exchange_pin(pin)

image_path = input("Enter path of the image : ") # path of the image which you want to upload
image = client.upload_image(image_path)
image_link = image.link


# Receiving image link as a message to preferred number

# Your Account SID from twilio.com/console
account_sid = "your_account_sid"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to= input ("Enter phone number at which you would like to receive the image link : ") # your phone number 
    from_="your_twilio_account_trial_number",
    body= image_link)


Printing image link

print("Image Link: ", image_link)
print("Image Link has also been sent to you via message.")