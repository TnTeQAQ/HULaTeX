from flask import Blueprint, request, jsonify
from random import choice
import pdflatex

# with open('test.tex', 'rb') as f:
#     pdfl = pdflatex.PDFLaTeX.from_binarystring(f.read(), 'my_file')
# pdf, log, cp = pdfl.create_pdf()
#
# with open('test.pdf', 'wb+') as f:
#     f.write(pdf)
#     f.close()

backend = Blueprint('backend', __name__)