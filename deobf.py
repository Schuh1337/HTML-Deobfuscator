import re, html, os

def deobfuscate(obfuscated):
    decode = html.unescape(obfuscated)
    decode = re.sub(r'<script>.*?</script>', '', decode, flags=re.DOTALL)
    decode = re.sub(r'<noscript>.*?</noscript>', '', decode, flags=re.DOTALL)
    return decode

obfuscated = ''' HERE '''  # <-- full obfuscated code here

deobf = deobfuscate(obfuscated)

path = 'deobf.html'
with open(path, 'w', encoding="utf-8") as file:
    file.write(deobf)
print(f"Deobfuscated code has been saved to {os.path.abspath(path)}")
input()
