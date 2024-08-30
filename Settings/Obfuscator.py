from Config.Util import *
from Config.Config import *
import os
import marshal

def obfuscate_code(source_code, chunk_size=100):
    compiled_code = compile(source_code, '<string>', 'exec')
    serialized_code = marshal.dumps(compiled_code)
    chunks = [serialized_code[i:i+chunk_size] for i in range(0, len(serialized_code), chunk_size)]
    chunks_as_strings = [chunk.decode('latin1') for chunk in chunks]
    
    class_name = "Titan"
    obfuscated_class = f"class {class_name}:\n"
    for i, chunk in enumerate(chunks_as_strings):
        obfuscated_class += f"    part{i} = {repr(chunk)}\n"
    
    obfuscated_code = obfuscated_class + "\nimport marshal\n"
    parts_join = ', '.join([f'{class_name}.part{i}.encode("latin1")' for i in range(len(chunks))])
    obfuscated_code += f"exec(marshal.loads(b''.join([{parts_join}])))\n"

    return obfuscated_code

def main():
    source_file = input(f"\n{INPUT} Path of the file to obfuscate -> {reset}")

    with open(source_file, 'r', encoding='utf-8') as f:
        source_code = f.read()

    obfuscated_code = obfuscate_code(source_code)

    output_dir = "1-Output/Obfuscator"
    os.makedirs(output_dir, exist_ok=True)

    base_name = os.path.basename(source_file)
    obfuscated_file_name = f"obf_{base_name}"
    obfuscated_file_path = os.path.join(output_dir, obfuscated_file_name)

    with open(obfuscated_file_path, 'w', encoding='utf-8') as f:
        f.write(obfuscated_code)

    print(f"\n{INFO} File successfully obfuscated in: {reset}{obfuscated_file_path}")
    Continue()
    Reset()

if __name__ == "__main__":
    main()
