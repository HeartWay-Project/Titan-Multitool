from Config.Util import *
from Config.Config import *
from Config.Translates import *
from PIL import Image
import os

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

Title("Steganography")

Slow(steganography_banner)

def encode_message_in_image(image_path: str, message: str):
    image = Image.open(image_path)
    encoded_image = image.copy()
    width, height = image.size
    message += "END"
    message_bits = ''.join([format(ord(i), '08b') for i in message])
    
    index = 0
    for y in range(height):
        for x in range(width):
            if index < len(message_bits):
                pixel = list(image.getpixel((x, y)))
                for n in range(3):  # R, G, B
                    if index < len(message_bits):
                        pixel[n] = int(format(pixel[n], '08b')[:-1] + message_bits[index], 2)
                        index += 1
                encoded_image.putpixel((x, y), tuple(pixel))
            else:
                output_directory = "1-Output/Steganography/"
                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)
                
                original_filename = os.path.basename(image_path)
                output_filename = f"h{original_filename}"
                output_path = os.path.join(output_directory, output_filename)

                encoded_image.save(output_path)
                print(f"\n{BEFORE + current_time_hour() + AFTER}{INFO}{primary}{tr('MessageEncode')} {reset}{output_path}")
                Continue()
                Reset()

def decode_message_from_image(image_path: str) -> str:
    image = Image.open(image_path)
    width, height = image.size
    message_bits = []
    
    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))
            for n in range(3):  # R, G, B
                message_bits.append(format(pixel[n], '08b')[-1])
    
    message_bytes = [message_bits[i:i+8] for i in range(0, len(message_bits), 8)]
    message = ''.join([chr(int(''.join(byte), 2)) for byte in message_bytes])
    
    return message.split("END")[0]

def main():
    while True:
        print(f"\n{secondary}[{primary}1{secondary}] {primary}{tr('EncodeMessage')}")
        print(f"{secondary}[{primary}2{secondary}] {primary}{tr('DecodeMessage')}")
        choix = input(f"\n{INPUT} {primary}{tr('Chose')} -> {reset}")

        if choix == '1':
            image_path = input(f"\n{INPUT} {primary}{tr('PathImage')} -> {reset}")
            if not os.path.exists(image_path):
                print(f"{tr('ImageNotExist')}")
                Continue()
                Reset()
            
            message = input(f"\n{INPUT} {primary}{tr('MessageToEncode')} -> {reset}")
            encode_message_in_image(image_path, message)

        elif choix == '2':
            image_path = input(f"\n{INPUT} {primary}{tr('PathEncodedImage')} -> {reset}")
            if not os.path.exists(image_path):
                print(f"{tr('ImageNotExist')}")
                Continue()
                Reset()
            
            message = decode_message_from_image(image_path)
            print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} {primary}{tr('DecodedMessage')} : {reset}{message}\n")
            Continue()
            Reset()

        else:
            Continue()
            Reset()

if __name__ == "__main__":
    main()
