import flask
from flask import request, jsonify
from inBot import scraper

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    if request:
        content = request.json
        tasks = content['tasks']
        with open('usernames.txt', 'a+') as filehandler:
            for task in tasks:
                username = task['text']
                filehandler.write(username+'\n')
        with open('usernames.txt', 'r+') as filehandler:
            names = filehandler.read()
            names = names.split('\n')
            if len(names) > 3:
                filehandler.truncate(0)
                scraper(names)
        return {"response": "success"}
    else:
        return jsonify({"error": "No username found"})


if __name__ == "__main__":
    app.run(threaded=True)
