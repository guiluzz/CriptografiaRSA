from flask import Flask, render_template, jsonify, request
from markupsafe import escape
import rsa

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['post'])
def resultado():
    chave_publica, chave_privada = rsa.newkeys(512)

    inputCriptografar = request.form.get('criptografar')
    inputDescriptar = request.form.get('descriptar')

    texto = inputCriptografar

    texto_encriptografar = rsa.encrypt(texto.encode(), chave_publica)

    texto_descriptografar = rsa.decrypt(
        texto_encriptografar, chave_privada).decode()

    resultado = [
        {
            'criptografar': inputCriptografar
        },
        {
            'criptografado': texto_encriptografar
        },
        {
            'descriptografado': texto_descriptografar
        }
    ]

    print("Texto para ser criptografado: ", texto)
    print("Texto criptografado", texto_encriptografar)
    print("Texto descriptografado: ", texto_descriptografar)
    return render_template('resultado.html', resultado=resultado)


app.run(debug=True)
