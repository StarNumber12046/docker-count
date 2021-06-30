import flask, time, datetime
timer = time.time()
    
#-
app = flask.Flask(__name__)


@app.route("/")
def index():
    try:
        timed = float(time.time() - timer)
        todestroy = str((timed - timer)).rindex(".") + 2
        print(round(timed, int(todestroy)))
    
        return "Time: " + str(round(timed, 2))
    except:
        return "Programma terminato con codice di errore 13. Errore: eccesso di cringe"


app.run(host="0.0.0.0", port=8080)
