import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser


class MyServer(BaseHTTPRequestHandler):

    def start_html(self):
        """ Start html, tag : <html> """
        return self.wfile.write(bytes("<html>", "utf-8"))

    def end_html(self):
        """ End html, tag : </html> """
        return self.wfile.write(bytes("</html>", "utf-8"))

    def start_head(self):
        """ Start head, tag : <head> """
        return self.wfile.write(bytes("<head>", "utf-8"))

    def end_head(self):
        """ End head, tag : </head> """
        return self.wfile.write(bytes("</head>", "utf-8"))

    def title(self, title):
        """ Set title of website, tag : <title></title> """
        return self.wfile.write(bytes("<title> {0} </title>".format(title), "utf-8"))

    def bootstrap(self):
        """ Default Bootstrap, tag : <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css'> """
        return self.wfile.write(bytes("<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css' rel='stylesheet'>", "utf-8")) & self.wfile.write(bytes("<link href='https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.0/font/bootstrap-icons.css' rel='stylesheet'>", "utf-8"))

    def link(self, data, rel):
        """ Set link tag : <link rel='' href=''> """
        return self.wfile.write(bytes("<link rel='" + rel + "' href='" + data + "' >", 'UTF-8'))

    def a(self, text, classe, link, role):
        """ Add text, class, link, tag : <a href="link"></a> """
        return self.wfile.write(bytes("<a href='{0}' class='{1}' role='{2}'> {3} </a>".format(link, classe, role, text), "utf-8"))

    def button(self, type, classe, text):
        """ Set Button (self, class, text, button-name, tag : <button class='' type='' name=''></button> """
        return self.wfile.write(bytes("<button class='{0}' type='{1}'> {2} </button>".format(classe, type, text), "utf-8"))

    def parag(self, text, classe, underline=False, bold=False):
        """ Set paragraph (self, text, class, underline=True|False, bold=True|False, tag : <p></p> """
        if underline & bold:
            return self.wfile.write(bytes("<p class='{0}'><u><b> {1} </b></u></p>".format(classe, text), "utf-8"))
        elif underline:
            return self.wfile.write(bytes("<p class='{0}'><u> {1} </u></p>".format(classe, text), "utf-8"))
        elif bold:
            return self.wfile.write(bytes("<p class='{0}'><b> {1} </b></p>".format(classe, text), "utf-8"))
        elif not underline & bold:
            return self.wfile.write(bytes("<p class='{0}'> {1} </p>".format(classe, text), "utf-8"))

    def h1(self, text, classe, underline=False):
        """ Set h1 title (self, text, class, underline=True|False, tag : <h1></h1> """
        if underline:
            return self.wfile.write(bytes("<h1 class='{0}'><u> {1} </u></h1>".format(classe, text), "utf-8"))
        elif not underline:
            return self.wfile.write(bytes("<h1> {0} </h1>".format(text), "utf-8"))

    def h2(self, text, classe, underline=False):
        """ Set h2 title (self, text, class, underline=True|False, tag : <h2></h2> """
        if underline:
            return self.wfile.write(bytes("<h2 class='{0}'> {1} </h2>".format(classe, text), "utf-8"))
        elif not underline:
            return self.wfile.write(bytes("<h2 class='{0}'><u> {1} </u></h2>".format(classe, text), "utf-8"))

    def h3(self, text, classe, underline=False):
        """ Set h3 title (self, text, class, underline=True|False, tag : <h3></h3> """
        if underline:
            return self.wfile.write(bytes("<h3 class='{0}'><u> {1} </u></h3>".format(classe, text), "utf-8"))
        elif not underline:
            return self.wfile.write(bytes("<h3 class='{0}'> {1} </h3>".format(classe, text), "utf-8"))

    def h4(self, text, classe, underline=False):
        """ Set h4 title (self, text, class, underline=True|False, tag : <h4></h4> """
        if underline:
            return self.wfile.write(bytes("<h4 class='{0}'><u> {1} </u></h4>".format(classe, text), "utf-8"))
        elif not underline:
            return self.wfile.write(bytes("<h4 class='{0}'> {1} </h4>".format(classe, text), "utf-8"))

    def h5(self, text, classe, underline=False):
        """ Set h5 title (self, text, class, underline=True|False, tag : <h5></h5> """
        if underline:
            return self.wfile.write(bytes("<h5 class='{0}'><u> {1} </u></h5>".format(classe, text), "utf-8"))
        elif not underline:
            return self.wfile.write(bytes("<h5 class='{0}'> {1} </h5>".format(classe, text), "utf-8"))

    def h6(self, text, classe, underline=False):
        """ Set h6 title (self, text, class, underline=True|False, tag : <h6></h6> """
        if underline:
            return self.wfile.write(bytes("<h6 class='{0}'> {1} </h6>".format(classe, text), "utf-8"))
        elif not underline:
            return self.wfile.write(bytes("<h6 class='{0}'> {1} </h6>".format(classe, text), "utf-8"))

    def label(self, for_method, texte):
        return self.wfile.write(bytes("<label for='{0}'>{1}</label>".format(for_method, texte), "utf-8"))

    def b(self, text, classe):
        """ Add text in bold (self, text, class, tag : <b></b> """
        return self.wfile.write(bytes("<b class='{0}'> {1} </b>".format(classe, text), "utf-8"))

    def br(self):
        """ Set br (self, text, tag : <br> """
        return self.wfile.write(bytes("<br>", "utf-8"))

    def li(self, text, class_ul, class_li):
        """ Set a list with <ul> <li></li>*n </ul> (self, text, class_ul, class_li, tag : <ul> <li></li> </ul>"""
        li = bytes("<ul class='{0}'>".format(class_ul), "utf-8")
        for i in text:
            li += (bytes("<li class='{0}'>{1}</li>".format(class_li, i), "utf-8"))
        li += (bytes("</ul>", "utf-8"))
        return self.wfile.write(li)

    def form(self, method, action, classe, argss=None):
        """ Set form in-dev... (self, text, class, underline=True|False, tag : <form method='GET or POST'></form> """
        if argss is None:
            argss = []
        if method == "post":
            return self.wfile.write(bytes("<form method='post' action='{0}' class='{1}'> {2}".format(action, classe, argss), "utf-8"))
        elif method == "get":
            return self.wfile.write(bytes("<form method='get' action='{0}' class='{1}'> {2}".format(action, classe, argss), "utf-8"))

    def end_form(self):
        return self.wfile.write(bytes("</form>", "utf-8"))

    def img(self, images):
        """ Add image in-dev...(self, src, tag : <img src='path'> """
        img = open(images, "rb")
        encoded_img = base64.b64encode(img.read())
        decoded_img = encoded_img.decode()
        return "<img src='data:image/png;base64," + decoded_img + "' class='rounded-circle' style='width: 15rem;' />"

    def input(self, type, name, classe, id, placeholder):
        """ Add input (self, name, class, id, placeholder='', tag : <input name='' id='' placeholder='' class=''></input> """
        return self.wfile.write(bytes("<input type='{0}' class='{1}' name='{2}' id='{3}' placeholder='{4}' autocomplete='off'>".format(type, classe, name, id, placeholder), "utf-8"))

    def hr(self, classe):
        """ Set hr (self, class, tag : <hr class=''> """
        return self.wfile.write(bytes("<hr class='{0}'>".format(classe), "utf-8"))

    def div(self, classe, id):
        """ Add div (self, class, id, tag : <div class='' id=''> """
        return self.wfile.write(bytes("<div class='{0}' id='{1}'>".format(classe, id), "utf-8"))

    def end_div(self):
        """ End div (self, tag : </div> """
        return self.wfile.write(bytes("</div>", "utf-8"))

    def card_div(self, title, texte):
        """ Add div (self, class, id, tag : <div class='card'><div class='card-header py-3 bg-primary'><h6 class='m-0 font-weight-bold text-white'></h6></div><div class='card-body py-3'></div> """
        return self.wfile.write(bytes(
            "<div class='card'><div class='card-header py-3 bg-primary'><h6 class='m-0 font-weight-bold text-white'>{0}</h6></div><div class='card-body py-3'>{1}</div>".format(
                title, texte), "utf-8"))

    def card_list(self, title, texte):
        """ Add card div (self, class, id, tag :  <div class='card'><div class='card-header py-3 bg-primary'><h6 class='m-0 font-weight-bold text-white'></h6></div><div class='card-body py-3'></div></div>"""
        li = "<ul>"
        for i in texte:
            li += "<li>" + i + "</li>"
        li += "</ul>"
        response = bytes(
            "<div class='card'><div class='card-header py-3 bg-primary'><h6 class='m-0 font-weight-bold text-white'>" + title + "</h6></div><div class='card-body py-3'>" +
            li + "</div></div>", "utf-8")
        return self.wfile.write(response)
