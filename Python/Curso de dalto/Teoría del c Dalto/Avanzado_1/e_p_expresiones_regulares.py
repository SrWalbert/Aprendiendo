import re

# Encontrando un numero con formato CABA y ocultalo

numero_caba = "Hola pedro, mi numero es: +52 555 555 5555"
patron_caba = r"\+\d{1,3}\s\d{3}\s\d{3}\s\d{4}"

numero_caba_oculto = re.sub(patron_caba, " *Numero Oculto* ", numero_caba)
print(numero_caba_oculto)
