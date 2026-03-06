from bottle import route, run, request

@route("/")
def home():
    return """
    <form action="/name" method="post">
    <b>Ваше имя:</b>
    <div><input name="username"></div>
    <div><input name="password"></div>
    <div><input type="submit"></div>
    </form>
    """

run(host="0.0.0.0", port=80)
