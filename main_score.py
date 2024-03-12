from flask import Flask, render_template, request

app = Flask(__name__)


def read_score():
    try:
        with open("scores.txt", "r") as file:
            score = int(file.read().strip())
        return score
    except Exception as e:
        return f"ERROR: {str(e)}"


@app.route('/')
def score_server():
    # Get the score directly from the file scores.txt
    score = read_score()

    if score is not None:
        # Display the score
        return render_template('score_template.html', score=score)
    else:
        # Display an error if score parameter is missing
        return render_template('error_template.html', error='Score parameter missing')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
