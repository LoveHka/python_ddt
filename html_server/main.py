from bottle import route, run, request

@route("/")
def home():
    return """
    <form action="/name" method="post">
    <input name="username">
    <input name="password">
    <input type="submit">
    </form>
    """

@route("/name", method="POST")
def name():
    a = int(request.forms.get("username"))
    b = int(request.forms.get("password"))
    return f"""
    Я получил имя <b>{a + b}</b>
    <a href="/" > Перейти назад </a>
"""

run(host="0.0.0.0", port=80)

