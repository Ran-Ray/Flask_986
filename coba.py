from flask import Flask
import random

app = Flask(__name__)

fakta = ["Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.",
         "Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja",
         "Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten",
         "Salah satu cara untuk memerangi ketergantungan teknologi adalah dengan mencari kegiatan yang membawa kesenangan dan meningkatkan suasana hati"]

@app.route("/")
def home():
    return "<h1>Wacky Wandom Fwact</h1><a href='wandom_fwact'>click to get some fwact</a><h2>Password Generator</h2><a href='password_gen'>click to generate a random password</a>"

@app.route("/wandom_fwact")
def hello_world():
    return f"<h1>Hello, People!</h1><p>Hewwo!!!!!</p><h2>Some facts :</h2><p>{random.choice(fakta)}</p>"

@app.route("/password_gen")
def passw_gen():
    elements = "1234567890qwertyuiopasdfghjklzxcvbnm+-/*!&$#?=@<>"
    password = ""

    for i in range(10):
        password += random.choice(elements)

    return f"<h1>Hello!</h1><h2>Here's your randomly generated password :</h2><p>{password}</p>"

app.run(debug=True)