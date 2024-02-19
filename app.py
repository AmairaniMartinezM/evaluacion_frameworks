import web

# Configuración de la aplicación
urls = (
    '/', 'Index',
    '/login', 'Login',
    '/bienvenida', 'Bienvenida'
)

# Inicialización de la aplicación web
app = web.application(urls, globals())
render = web.template.render('templates/')

# Modelo para la validación de usuario
class Usuario:
    @staticmethod
    def validar(username, password):
        return username == "usuario" and password == "1234"

# Controlador para la página de inicio
class Index:
    def GET(self):
        return render.index()

# Controlador para la página de login
class Login:
    def GET(self):
        return render.login()

    def POST(self):
        data = web.input()
        username = data.username
        password = data.password

        if Usuario.validar(username, password):
            web.setcookie('username', username)
            raise web.seeother('/bienvenida')
        else:
            return render.login_error()

# Controlador para la página de bienvenida
class Bienvenida:
    def GET(self):
        username = web.cookies().get('username')
        if username:
            return render.bienvenida(username)
        else:
            raise web.seeother('/login')

if __name__ == "__main__":
    app.run()