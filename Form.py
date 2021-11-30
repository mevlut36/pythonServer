# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer
import HTMLClass

hostName = "localhost"
serverPort = 8081


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        html = HTMLClass.MyServer
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
                  [html.label(self, "name", "Votre nom:"), html.input(self, "text", "name", "form-control", "name", "Votre nom"),
                   html.label(self, "mail", "Votre E-Mail:"), html.input(self, "text", "mail", "form-control", "mail", "Votre E-mail"),
                   html.label(self, "password", "Votre Mot de passe:"), html.input(self, "password", "password", "form-control", "password", "Votre Mot de passe"),
                   html.div(self, "form-check", ""), html.checkbox(self, "checkbox", "remember"), html.label(self, "remember", "Se rappeler de moi"), html.end_div(self),
                   html.a(self, "Update", "form-control btn btn-primary", "index.py", "button")])
        html.end_form(self)
        html.end_div(self)
        html.end_div(self)
        html.end_div(self)
        self.wfile.write(bytes("</body></html>", "utf-8"))

        # </body>


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server start http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stop")
