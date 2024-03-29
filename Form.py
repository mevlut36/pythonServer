# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer
import HTMLClass

hostName = "localhost"
serverPort = 8081


class MyServer(BaseHTTPRequestHandler):
    def _set_response(self, data='', method='GET'):
        html = HTMLClass.MyServer
        if method == 'POST':
            data = data.decode()
        self.send_response(200)
        self.end_headers()
        html.start_html(self)
        html.start_head(self)
        self.wfile.write(bytes("<title>Form</title>", "utf-8"))
        self.wfile.write(bytes("<meta charset='utf-8'>", "utf-8"))
        html.link(self, "data:;base64,iVBORw0KGgo=", "icon")
        html.bootstrap(self)
        html.end_head(self)
        # <body>
        self.wfile.write(bytes("<body>", "utf-8"))
        html.div(self, "d-flex", "wrapper")
        html.div(self, "container-fluid", "")
        html.div(self, "col-md-3", "")
        html.h4(self, "Connexion", "", True)
        html.form(self, "POST", "", "form-control",
                  [html.label(self, "name", "Votre nom:", True),
                   html.input(self, "text", "name", "form-control", "name", "Votre nom", True),
                   html.label(self, "mail", "Votre E-Mail:", True),
                   html.input(self, "email", "mail", "form-control", "mail", "Votre E-mail", True),
                   html.label(self, "password", "Votre Mot de passe:", True),
                   html.input(self, "password", "password", "form-control", "password", "Votre Mot de passe", True),
                   html.div(self, "form-check", "", True), html.checkbox(self, "checkbox", "remember", True),
                   html.label(self, "remember", "Se rappeler de moi", True), html.end_div(self, True),
                   html.button(self, "submit", "form-control btn btn-primary", "Update", True),
                   html.decode_data(self, data, "name"),
                   HTMLClass.crypt_pwd(data, 'password'),
                   ])
        html.end_form(self)
        html.end_div(self)
        html.end_div(self)
        html.end_div(self)
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_GET(self):
        self._set_response('')

    # </body>

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self._set_response(post_data, 'POST')


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server start http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stop")
