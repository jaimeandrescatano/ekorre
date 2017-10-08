# Generar documento en PDF usando Latex
# Es necesario que latex este instalado en el sistema, en este caso tengo
# instalado TeXworks 0.5r952 (Debian) en ubuntu 12.04 64bits
# 
# Para generar el documento usar el siguiente comando: 
# python GenerarDocEnLatex.py -c "Mi Titulo" -t "Jaime Andres" -n Me

import subprocess
import argparse
import shlex
import os

content=r'''\documentclass{article}
\begin{document}
\textbf{\huge %(school)s \\}
\vspace{1cm}
\textbf{\Large %(title)s \\}
\end{document}
'''

parser=argparse.ArgumentParser()
parser.add_argument('-c', '--course')
parser.add_argument('-t', '--title')
parser.add_argument('-n', '--name',) 
parser.add_argument('-s', '--school', default='Te falto el titulo cabezon!')

args=parser.parse_args()
content%args.__dict__

with open('cover.tex','w') as f:
    f.write(content%args.__dict__)

proc=subprocess.Popen(shlex.split('pdflatex cover.tex'))
proc.communicate()


os.unlink('cover.tex')
os.unlink('cover.log')
