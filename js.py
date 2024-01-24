import os

def deobfuscate(obfuscated):
    decoded_code = ""
    for char in obfuscated:
        decoded_code += chr(ord(char) - 1)
    return decoded_code

obfuscated = """  HERE  """  # <-- full obfuscated code here

deobf = deobfuscate(obfuscated)

path = 'deobf.html'
with open(path, 'w', encoding="utf-8") as file:
    file.write(deobf)
print(f"Deobfuscated code has been saved to {os.path.abspath(path)}")
input()
