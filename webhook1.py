#This code is below is just for sending message with the audio file 
'''
import requests
import Bro
webhook_url = 'https://discord.com/api/webhooks/1461244445058924619/tC4fUIBShpIMPWBEPOdUc6Z6D9ioNAC7mgUBfhLy_dWo70Nn8QlB36g3dv9WdZbprKX_'

data = {
    "content": "audio should be working "
}


response = requests.post(webhook_url, json=data)

'''


from dhooks import Webhook, File
import Bro

hook = Webhook("https://discord.com/api/webhooks/1461244445058924619/tC4fUIBShpIMPWBEPOdUc6Z6D9ioNAC7mgUBfhLy_dWo70Nn8QlB36g3dv9WdZbprKX_")



discord = File("/home/mrtightlight/.local/lib/Pyaudio/output.wav")
               
hook.send(file=discord)
#The break system is for when pip dose not install wright 
#pip install dhook --break-system-packages

