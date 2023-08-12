# import rsa

# chave_publica, chave_privada = rsa.newkeys(512)

# texto = "filemon"

# texto_encriptografar = rsa.encrypt(texto.encode(), chave_publica)

# texto_descriptografar = rsa.decrypt(
#     texto_encriptografar, chave_privada).decode()

# print("Texto para ser criptografado: ", texto)
# print("Texto criptografado", texto_encriptografar)
# print("Texto descriptografado: ", texto_descriptografar)


# #
# inputCriptografar = request.form.get('criptografar')
#     inputDescriptar = request.form.get('descriptar')

#     texto = inputCriptografar

#     chave_publica, chave_privada = rsa.newkeys(512)

#     texto_encriptografar = rsa.encrypt(texto.encode(), chave_publica)

#     texto_descriptografar = rsa.decrypt(
#         texto_encriptografar, chave_privada).decode()

#     resultado = [
#         {
#             'criptografar': inputCriptografar
#         },
#         {
#             'criptografado': texto_encriptografar
#         },
#         {
#             'descriptografado': texto_descriptografar
#         }
#     ]

#     print("Texto para ser criptografado: ", texto)
#     print("Texto criptografado", texto_encriptografar)
#     print("Texto descriptografado: ", texto_descriptografar)

#     return render_template('index.html', resultado=resultado)
