from bottle import Bottle, run, static_file, TEMPLATE_PATH
from app.controllers import auth
from app.controllers import planos

# Caminho dos templates
TEMPLATE_PATH.insert(0, "app/views")

app = Bottle()

# LOGIN
app.route('/', method='GET')(auth.login_page)
app.route('/login', method='GET')(auth.login_page)
app.route('/login', method='POST')(auth.login)

# DASHBOARD
app.route('/dashboard', method='GET')(auth.dashboard)

# CRUD PLANOS
app.route('/planos', method='GET')(planos.listar_planos)
app.route('/planos/novo', method='GET')(planos.criar_plano_form)
app.route('/planos', method='POST')(planos.criar_plano)

# STATIC FILES
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='app/static')

run(app, host='localhost', port=8080, debug=True, reloader=True)
