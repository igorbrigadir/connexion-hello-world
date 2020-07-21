import connexion
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


def hello():
    return "Hello world."


app = connexion.App(__name__, specification_dir=".")
app.add_api("api.yaml")

limiter = Limiter(
    app.app,
    key_func=get_remote_address,
    default_limits=["10000 per day", "1000 per hour", "200 per minute", "1 per second"],
)

app.run(port=9876)
