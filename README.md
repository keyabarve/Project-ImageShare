# Introduction
Project ImageShare is a tool which helps post an image from your computer to Imgur and sends you back the link of the posted image via a text message.
Follow the steps given below to use this tool.

Used the Imgur API to upload the image from your computer, using the path of the image. The program asks for the user's Imgur account information, to post the image on the user's account. The program outputs a link to the uploaded image.

Used Twilio's API to send a message containing the link to the image, to the phone number provided by the user.

# Inspiration
It is usually a hassle to share a particular image with a lot of people. Imgur is an image-hosting platform that allows you to upload an image and share it with many people using a simple link. This tool allows you to easily upload a desired image to your Imgur account and even sends you a text message with the link of the image, so you can share it quickly and easily with as many people as you want.

# Requirements
The following dependencies can be easily installed using the steps given below.
* pyimgur
* twilio

# Instructions for Usage
* **Installing the Requirements**
  * ```pip install pyimgur``` can be used to install pyimgur.
  * ```pip install twilio``` can be used to install twilio.
  
  **NOTE :** If the ```pip``` command doesn't work, try using ```pip3``` or ```sudo pip``` or ```sudo pip3``` instead.
  
* **Downloading the Program**
  * Open up Terminal on your computer.
  * Clone this repository using the ```git clone``` command as follows:
    git clone https://github.com/keyabarve/Project-ImageShare. Press Enter.
  * Type ```cd``` and enter the path of the repository. Press Enter.
* **Uploading the Image to Imgur and Receiving the Link**
  * In Terminal itself, type the command ```python3 Main.py```. Press Enter.
  * Type in your Client ID, Client Secret, the Pin that you receive, and finally the path of the image you wish to upload. Press Enter after you type in each detail.
  * Type in the phone number to which you wish to receive a text message (SMS) containing the link of your uploaded image. Press Enter.
  * You will receive the link of your image in Terminal, and the same link will be sent to your phone number.

# Contributions
* Keya Barve
* Mandeepika Saini
