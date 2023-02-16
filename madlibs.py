"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

PEOPLES = [
    "Barack Obama",
    "Britney Spears",
    "Morgan Freeman",
    "Beyonce",
    "Your sister",
    "Brad Pitt",
    "Lady Gaga",
]


COLORS = [
    "Tie-dye",
    "Yellow",
    "Green",
    "Magenta",
    "Blood-orange",
    "Rainbow",
    "Sparkly-pink",
]

NOUNS = [
    "Beaker",
    "Lamp",
    "Coffee Mug",
    "Binder",
    "Computer Mouse",
    "Lunchbox",
    "Bookbag",
]

ADJECTIVES = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():

    player = request.args.get("person")

    return render_template("compliments.html", person=player)

@app.route("/game")
def show_madlib_form():
    response = request.args.get("response")
    if response == 'no':
        return render_template("goodbye.html")
    else:
        return render_template("game.html", adjectives=ADJECTIVES, nouns=NOUNS, colors=COLORS, peoples=PEOPLES)

@app.route("/madlibs")
def say_goodbye():
    adjective = request.args.get("adjective")
    noun = request.args.get("noun")
    color = request.args.get("color")
    person = request.args.get("people")

    return render_template("madlibs.html", noun = noun, adjective = adjective, color = color, person = person)



if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
