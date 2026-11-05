
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "turismo_sjr_2026"

lugares = [
    {
        "nombre": "Paisajes rurales",
        "tipo": "Natural",
        "imagen": "paisaje.jpg",
        "descripcion": "Conoce los paisajes y comunidades rurales de San José del Rincón.",
        "horario": "8:00 a 17:00 horas",
        "ubicacion": "San José del Rincón, Estado de México"
    },
    {
        "nombre": "Bosques y naturaleza",
        "tipo": "Natural",
        "imagen": "bosque.jpg",
        "descripcion": "Disfruta de la vegetación y los espacios naturales de la región.",
        "horario": "8:00 a 17:00 horas",
        "ubicacion": "Zona rural de San José del Rincón"
    },
    {
        "nombre": "Vida en el campo",
        "tipo": "Cultural",
        "imagen": "milpa.jpg",
        "descripcion": "Conoce las actividades agrícolas y las tradiciones campesinas.",
        "horario": "9:00 a 16:00 horas",
        "ubicacion": "Comunidades rurales"
    },
    {
        "nombre": "Tradiciones y cultura",
        "tipo": "Cultural",
        "imagen": "iglesia.jpg",
        "descripcion": "Descubre las costumbres y expresiones culturales de la comunidad.",
        "horario": "Consultar con la comunidad",
        "ubicacion": "San José del Rincón"
    },
    {
        "nombre": "Gastronomía regional",
        "tipo": "Gastronomía",
        "imagen": "gastronomia.jpg",
        "descripcion": "Conoce los alimentos y platillos tradicionales de la región.",
        "horario": "Consultar disponibilidad",
        "ubicacion": "Comunidades del municipio"
    }
]

rutas = [
    {
        "nombre": "Ruta de la naturaleza",
        "descripcion": "Recorrido por paisajes, bosques y espacios naturales.",
        "duracion": "3 horas",
        "tipo": "Natural"
    },
    {
        "nombre": "Ruta cultural",
        "descripcion": "Conoce las tradiciones, costumbres y espacios comunitarios.",
        "duracion": "2 horas",
        "tipo": "Cultural"
    },
    {
        "nombre": "Ruta gastronómica",
        "descripcion": "Descubre los sabores y alimentos tradicionales.",
        "duracion": "2 horas",
        "tipo": "Gastronómica"
    }
]


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/lugares")
def ver_lugares():
    tipo = request.args.get("tipo", "")
    resultado = lugares

    if tipo:
        resultado = [l for l in lugares if l["tipo"] == tipo]

    return render_template("lugares.html", lugares=resultado)


@app.route("/rutas")
def ver_rutas():
    return render_template("rutas.html", rutas=rutas)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        correo = request.form["correo"]
        contraseña = request.form["contraseña"]

        if correo == "admin@gmail.com" and contraseña == "12345":
            session["admin"] = True
            return redirect(url_for("inicio"))
        else:
            error = "Correo o contraseña incorrectos."

    return render_template("login.html", error=error)


@app.route("/cerrar")
def cerrar():
    session.pop("admin", None)
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)
