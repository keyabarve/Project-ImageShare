import webbrowser
import pyimgur
from twilio.rest import Client


# Part 1 : Uploading image to imgur and receiving image link

client_id = input("Enter client id : ") # your client id
client_secret = input("Enter client secret : ") # your client secret

client_imgur = pyimgur.Imgur(client_id, client_secret)
auth_url = client_imgur.authorization_url('pin')
webbrowser.open(auth_url)
pin = input("Enter the pin : ") # the pin you receive on your imgur account
client_imgur.exchange_pin(pin)

image_path = input("Enter path of the image : ") # path of the image which you want to upload
image = client_imgur.upload_image(image_path)
image_link = image.link


# Part 2 : Receiving image link as a message to preferred number


account_sid = "your_account_sid" # your account sid from twilio
auth_token  = "your_auth_token" # your auth token from twilio

client_twilio = Client(account_sid, auth_token)

message = client_twilio.messages.create(
    to= input ("Enter phone number at which you would like to receive the image link : ") # your phone number 
    from_="your_twilio_account_trial_number",
    body= image_link)


# Part 3 : Printing image link

print("Image Link: ", image_link)
print("Image Link has also been sent to you via message.")
