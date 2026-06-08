from flask import Flask, render_template, request

from password_utils import (
    analyze_password,
    generate_password
)

from database import (
    init_db,
    check_reuse,
    save_password
)

app = Flask(__name__)

init_db()


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        password = request.form["password"]

        score, strength, entropy, suggestions = \
            analyze_password(password)

        reused = check_reuse(password)

        if not reused:
            save_password(password)

        result = {
            "score": score,
            "strength": strength,
            "entropy": entropy,
            "suggestions": suggestions,
            "generated": generate_password(),
            "reused": reused
        }

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
