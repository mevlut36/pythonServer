# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer
import HTMLClass

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        html = HTMLClass.MyServer
        self.send_response(200)
        self.end_headers()
        html.start_html(self)
        html.start_head(self)
        self.wfile.write(bytes("<meta charset='utf-8'>", "utf-8"))
        html.link(self, "data:;base64,iVBORw0KGgo=", "icon")
        # html.link(self, "style.css", "stylesheet")
        html.bootstrap(self, None)
        html.end_head(self)
        # <body>
        self.wfile.write(bytes("<body>", "utf-8"))
        html.div(self, "d-flex", "wrapper")
        html.div(self, "d-flex", "wrapper")
        html.div(self, "bg-white", "sidebar-wrapper")
        html.div(self, "list-group list-group-flush", "")
        # Image Nav
        html.li(self, [html.img(self, "luffy.png"), "18 ans", "<i class='bi-file-person-fill'></i> Etudiant en BTS SIO : SISR", "mevlut36@gmail.com", "<i class='bi-phone'></i> 07 00 00 00 00", "<i class='bi-flag-fill'></i> <b>Langues:</b>", "<i class='bi-flag'></i> - Anglais", "<i class='bi-flag'></i> - Français", "<i class='bi-flag'></i> - Turc"], "navbar-nav bg-gradient-primary sidebar sidebar-dark accordion", "list-group-item")
        html.end_div(self)
        html.end_div(self)
        html.end_div(self)
        # Mid
        html.div(self, "container-fluid", "")
        html.h1(self, "Mevlut TUNCA", "mb-0", underline=True)
        html.br(self)
        html.div(self, "col-md-3", "")
        html.card_list(self, "<i class='bi-bookmark-check-fill'></i> Cursus Scolaire", ["BTS SIO : SISR", "Baccalaureat STI2D", "Brevet des collèges"]), html.br(self)
        html.card_list(self, "<i class='bi-bookmark-check-fill'></i> Cursus Professionnel", ["Stage de troisième", "Espace vert"]), html.br(self)
        html.card_list(self, "<i class='bi-bookmark-check-fill'></i> Compétences", ["Programmation web : HTML, CSS, PHP", "Programmation orientée objet : Python, Arduino / Processing"]), html.br(self)
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
