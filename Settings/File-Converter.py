import os
from Config.Util import *
from Config.Config import *
from PIL import Image
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from pdf2docx import Converter
from docx import Document

OUTPUT_DIR = "1-Output/Converter"

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def convert_image(input_file, output_format):
    img = Image.open(input_file)
    
    if img.mode == 'RGBA' and output_format.lower() in ['jpg', 'jpeg']:
        img = img.convert('RGB')
    
    if output_format.lower() == 'jpg':
        output_format = 'jpeg'
    
    output_file = os.path.join(OUTPUT_DIR, os.path.splitext(os.path.basename(input_file))[0] + f".{output_format.lower()}")
    
    if output_format == 'jpeg':
        img.save(output_file, format=output_format.upper(), quality=100, optimize=True)
    elif output_format == 'ico':
        img.save(output_file, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
    else:
        img.save(output_file, format=output_format.upper())
    
    return output_file

def convert_video(input_file, output_format):
    clip = VideoFileClip(input_file)
    output_file = os.path.join(OUTPUT_DIR, os.path.splitext(os.path.basename(input_file))[0] + f".{output_format.lower()}")
    
    clip.write_videofile(output_file, bitrate="5000k", codec="libx264", audio_codec="aac")
    
    return output_file

def convert_audio(input_file, output_format):
    audio = AudioSegment.from_file(input_file)
    output_file = os.path.join(OUTPUT_DIR, os.path.splitext(os.path.basename(input_file))[0] + f".{output_format.lower()}")
    
    audio.export(output_file, format=output_format, bitrate="320k", parameters=["-q:a", "0"])
    
    return output_file

def convert_pdf_to_docx(input_file):
    output_file = os.path.join(OUTPUT_DIR, os.path.splitext(os.path.basename(input_file))[0] + ".docx")
    cv = Converter(input_file)
    cv.convert(output_file)
    cv.close()
    return output_file

def convert_docx_to_pdf(input_file):
    output_file = os.path.join(OUTPUT_DIR, os.path.splitext(os.path.basename(input_file))[0] + ".pdf")
    doc = Document(input_file)
    doc.save(output_file)
    return output_file

def convert_file(input_file, output_format):
    ext = input_file.split('.')[-1].lower()
    
    if ext in ['jpg', 'png', 'jpeg', 'gif', 'bmp']:
        return convert_image(input_file, output_format)
    elif ext in ['mp4', 'avi', 'mov', 'mkv']:
        return convert_video(input_file, output_format)
    elif ext in ['mp3', 'wav', 'aac']:
        return convert_audio(input_file, output_format)
    elif ext == 'pdf' and output_format.lower() == 'docx':
        return convert_pdf_to_docx(input_file)
    elif ext == 'docx' and output_format.lower() == 'pdf':
        return convert_docx_to_pdf(input_file)
    else:
        raise ValueError("Conversion non prise en charge pour ce type de fichier.")

def get_conversion_options(ext):
    options = {
        'image': ['jpeg', 'png', 'gif', 'bmp', 'ico'],
        'video': ['mp4', 'avi', 'mov', 'mkv'],
        'audio': ['mp3', 'wav', 'aac'],
        'pdf': ['docx'],
        'docx': ['pdf']
    }
    
    if ext in ['jpg', 'png', 'jpeg', 'gif', 'bmp']:
        return options['image']
    elif ext in ['mp4', 'avi', 'mov', 'mkv']:
        return options['video']
    elif ext in ['mp3', 'wav', 'aac']:
        return options['audio']
    elif ext == 'pdf':
        return options['pdf']
    elif ext == 'docx':
        return options['docx']
    else:
        return []

if __name__ == "__main__":
    ensure_output_dir()
    
    input_file = input(f"\n{INPUT} Enter the path of the file to convert -> {reset}")
    ext = input_file.split('.')[-1].lower()
    
    available_options = get_conversion_options(ext)
    
    if not available_options:
        print(f"\n{ERROR} No conversion option available for file with extension .{ext}")
    else:
        print(f"\n{INFO} Conversion options available:")
        for i, option in enumerate(available_options, 1):
            print(f"{secondary}[{primary}{i}{secondary}] {primary}{option}")
        
        choice = int(input(f"\n{INPUT} Enter the conversion option number -> {reset}"))
        
        if 1 <= choice <= len(available_options):
            output_format = available_options[choice - 1]
            try:
                output_file = convert_file(input_file, output_format)
                print(f"\n{INFO} File converted successfully: {reset}{output_file}")
                Continue()
                Reset()
            except Exception as e:
                print(f"Erreur: {e}")
        else:
            print(f"\n{ERROR} Invalid Option.")
            Continue()
            Reset()