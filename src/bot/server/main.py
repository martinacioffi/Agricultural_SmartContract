from flask import Flask, render_template
from src.bot.server.views import home_blueprint, pacman_blueprint

app = Flask(__name__, template_folder='../server/templates')
app.register_blueprint(home_blueprint)
app.register_blueprint(pacman_blueprint)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
