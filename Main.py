
import pyimgur
from twilio.rest import Client


# Uploading image to imgur and receiving image link

client_id = input("Enter client id : ") # your client id
client_secret = input("Enter client secret : ") # your client secret
access_token = input("Enter access token : ") # your access token
refresh_token = input("Enter refresh token : ") # your refresh token

client = pyimgur.Imgur(client_id, client_secret, access_token, refresh_token)
image_path = input("Enter path of the image : ")
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
    from_="number_by_which_message_is_sent",
    body= image_link)


# Printing image link

print("Image Link: ", image_link)
print("Image Link has also been sent to you via message.")