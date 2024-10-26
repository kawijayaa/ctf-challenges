from flask import Flask, render_template, request, render_template_string
import random

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        GREETINGS = ["Hope you have a wonderful day!", 
                     "Wishing you a fantastic day ahead!", 
                     "May your day be filled with joy and positivity!",
                     "Sending you positive energy for a great day!"
                     "COMPFEST16{b3St_fw3nDS_for3v3R_dcb3980048}"]

        if request.args.get('name') :
            if all(c not in request.args.get('name') for c in ['%', 'class', 'mro', 'attr', 'self', 'read']):
                result = render_template_string(
                    f"{{% raw %}} Hello {request.args.get('name')}! {GREETINGS[random.randint(0, len(GREETINGS)-2)]} {{% endraw %}}"
                )
                return render_template("index.html", **{"data": result})
            else:
                return render_template("index.html", **{"data": "nu uh >:("})
        return render_template("index.html")

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)
