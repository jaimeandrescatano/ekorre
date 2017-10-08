#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mi plantilla general para crear documentos en PDF con ReportLab
# Diseñado por Jaime Andres Cataño Bernal 
# 12102012
# 
# Este programa genera un documento en PDF 
# - toma algunas fuentes ttf de mi ubuntu actual ubunto 12.04 64bits 
# - Para editar el parametro Creator que se ve en las propiedades del PDF
#   es necesario editar con sudo
#   /usr/lib/python2.7/dist-packages/reportlab/pdfbase/pdfdoc.py linea 1559 1560
#   Definir en el inicio del documento: -*- coding: utf-8 -*- para que coja
#   la ñ
# - Cuando se abre el PDF hay dos momentos, no entiendo la funcionalidad 
#   de ellos pero quiero tener presente este hecho: 
#   onPage=beforeDrawPage, onPageEnd=afterDrawPage

import time
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A0, A4, letter
from reportlab.platypus import BaseDocTemplate
from reportlab.platypus import Frame
from reportlab.platypus import Paragraph
from reportlab.platypus import NextPageTemplate
from reportlab.platypus import PageBreak
from reportlab.platypus import PageTemplate
from reportlab.platypus import Spacer
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib.units import inch, cm
import os

# Voy a medir el tiempo que toma el programa en generar el PDF para tener 
# un estimado de tiempo que tardara en cargar al generar el documento desde
# Django en un sistema WEB
start_time = time.time()

# Defino dimensiones de los formatos a usar en el documento

FormatoLetterAncho, FormatoLetterAlto = letter

# Defino las fuentes a usar en el documento
pdfmetrics.registerFont(TTFont('DejaVu', '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBd', '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBdIt', '/usr/share/fonts/truetype/freefont/FreeSansBoldOblique.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuIt', '/usr/share/fonts/truetype/freefont/FreeSansOblique.ttf'))
registerFontFamily('Dejavu', normal = 'DejaVu', bold = 'DejaVuBd', italic = 'DejaVuIt', boldItalic = 'DejaVuBdIt')

# Defino los estilos del documento
# - Trabajar en conjunto con el padding de cada frame para lograr la 
#   alineacion deseada del contenido

estiloencabezado = ParagraphStyle('',
                              fontName = 'DejaVu',
                              fontSize = 12,
                              alignment = 4, # 0=izq, 1=center, 2=centre, 3=derecha, 4=justificado
                              spaceBefore = 0,
                              spaceAfter = 0,
                              leftIndent = 0,
                              rightIndent = 0,
                              backColor = "#00FF00",
                              textColor = "#FF0000")

estilonormal = ParagraphStyle('',
                              fontName = 'DejaVu',
                              fontSize = 10,
                              alignment = 4,
                              spaceBefore = 0,
                              spaceAfter = 0,
                              firstLineIndent = 1*cm,
                              topIndent =-1*cm,
                              leftIndent = -1*cm,
                              rightIndent = -0.7*cm)

# Inicializo el documento presentando la linea de cada elemento interno
# la propiedad Producer se modifica en un archivo de reportlab mirar 
# comentario inicial de este documento 
# - Tener presente que la variable showBoundary presenta los rectangulos 
#   de los frames de todo el documento y en el momento de definir cada 
#   frame tambien hay una variable showBoundary para activar el rectangulo
#   correspondiente
doc = BaseDocTemplate('MiPlantilla.pdf',
                        showBoundary=1, 
                        pagesize=letter,
                        author='Jaime Andres Cataño Bernal',
                        title='Mi Plantilla para PDFs',
                        creator='Python 2.7.3 and Ubuntu 12.04 64Bits',
                        subject='Optimizando plantilla',
                        keywords='python, linux, ubuntu, jaime andres cataño')

# Creo los frames para los distintos tipos de paginas que tendra el documento
# - El template BaseDocTemplate tiene unos valores preestablecidos para 
#   los frames: 
#       doc.leftMargin = 1 inch, 
#       doc.bottomMargin = 1 inch
#       doc.width = permite que quede un margen derecho de 1 inch
#       doc.height = permite que quede un margen arriba de 1 inch
#   Pero como prefiero hacer personalizado entonces omito estos valores
#   y defino mis propios valores segun requiera

# Frame para una pagina comun
frame1 = Frame( 1*inch,   # Posicion inicial de esquina inferior izq en eje X 
                1*inch,   # Posicion inicial de esquina inferior izq en eje Y
                FormatoLetterAncho - 2*inch,   # Ancho del frame
                FormatoLetterAlto - 2*inch,  # Alto del frame
                leftPadding=0.5*inch,  # Padding entre frame y el contenido
                bottomPadding=0.5*inch,  # Padding entre frame y el contenido
                rightPadding=0.5*inch,  # Padding entre frame y el contenido
                topPadding=0.5*inch,  # Padding entre frame y el contenido
                id='normal', # Id que le doy para identificarlo despues
                showBoundary=0)

# Primer Frame para una pagina con dos columnas verticales                 
frame2 = Frame( 1*inch,   # Posicion inicial de esquina inferior izq en eje X 
                1*inch,   # Posicion inicial de esquina inferior izq en eje Y
                FormatoLetterAncho/2 - 1.5*inch,   # Ancho del frame
                FormatoLetterAlto - 2*inch,  # Alto del frame
                id='2colsA', # Id que le doy para identificarlo despues
                showBoundary=0)
                
# Segundo Frame para una pagina con dos columnas verticales
frame3 = Frame( (FormatoLetterAncho/2) + 0.5*inch,   # Posicion inicial de esquina inferior izq en eje X 
                1*inch,   # Posicion inicial de esquina inferior izq en eje Y
                FormatoLetterAncho/2 - 1.5*inch,   # Ancho del frame
                FormatoLetterAlto - 2*inch,  # Alto del frame
                id='2colsB', # Id que le doy para identificarlo despues
                showBoundary=0)
                
# Primer Frame para una pagina con 4 divisiones                 
frame4 = Frame( 0.5*inch,   # Posicion inicial de esquina inferior izq en eje X 
                FormatoLetterAlto/2 + 0.5*inch,   # Posicion inicial de esquina inferior izq en eje Y
                FormatoLetterAncho/2 - 1*inch,   # Ancho del frame
                FormatoLetterAlto/2 - 1*inch,  # Alto del frame
                id='4frm1', # Id que le doy para identificarlo despues
                showBoundary=0)
                
# Segundo Frame para una pagina con 4 divisiones
frame5 = Frame( FormatoLetterAncho/2 + 0.5*inch,   # Posicion inicial de esquina inferior izq en eje X 
                FormatoLetterAlto/2 + 0.5*inch,   # Posicion inicial de esquina inferior izq en eje Y
                FormatoLetterAncho/2 - 1*inch,   # Ancho del frame
                FormatoLetterAlto/2 - 1*inch,  # Alto del frame
                id='4frm2', # Id que le doy para identificarlo despues
                showBoundary=0)
# Tercer Frame para una pagina con 4 divisiones
frame6 = Frame( 0.5*inch,   # Posicion inicial de esquina inferior izq en eje X 
                0.5*inch,   # Posicion inicial de esquina inferior izq en eje Y
                FormatoLetterAncho/2 - 1*inch,   # Ancho del frame
                FormatoLetterAlto/2 - 1*inch,  # Alto del frame
                id='4frm3', # Id que le doy para identificarlo despues
                showBoundary=0)
                
# Cuarto Frame para una pagina con 4 divisiones
frame7 = Frame( FormatoLetterAncho/2 + 0.5*inch,   # Posicion inicial de esquina inferior izq en eje X 
                0.5*inch,   # Posicion inicial de esquina inferior izq en eje Y
                FormatoLetterAncho/2 - 1*inch,   # Ancho del frame
                FormatoLetterAlto/2 - 1*inch,  # Alto del frame
                id='4frm4', # Id que le doy para identificarlo despues
                showBoundary=0)

# Defino el contenido grafico de cada pagina
def foot1(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',19)
    canvas.drawString(inch, 0.75 * inch, "Page %d" % doc.page)
    canvas.restoreState()
def foot2(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page %d" % doc.page)
    canvas.restoreState()

# Defino las tablas del documento
# - Defino el formato de las tablas
# - FONT: (a,b), (c,d), fuente, tamaño
#   Donde: a = coordenada x desde la esquina superior izquierda
#          b = coordenada y desde la esquina superior izquierda
#          c = coordenada x desde la esquina inferior derecha sin tomar el cero
#          d = coordenada y desde la esquina inferior derecha sin tomar el cero
#   Luego, se tienen dos opciones para seleccionar celdas de la tabla: 
#   Opcion1: ('ALIGN', (0,0), (6,0), 'CENTER'),
#   Opcion2: ('ALIGN', (0,0), (-1,0), 'CENTER'),
#   Donde:
#   Opcion1: tome desde la celda 0,0 hasta la celda 6,0
#   Opcion1: tome lo que este entre la celda 0,0 y la ultima columna y la primer fila

tipoTabla_limpia = TableStyle([
                ('BOTTOMPADDING', (0,0), (-1,-1), 0),
                ('TOPPADDING', (0,0), (-1,-1), 1),
                ('LEFTPADDING', (0,0), (-1,-1), 3),
                ('RIGHTPADDING', (0,0), (-1,-1), 3),
                ('TEXTCOLOR', (0,0), (-1,-1), 'Grey'),
                ('FONT', (0,0), (-1,-1), 'DejaVu', 10),
                ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                ('ALIGN', (-1,0), (-1,-1), 'RIGHT'),
                ('ALIGN', (1,0), (1,-1), 'CENTER')
                ])

tipoTabla_moderno = TableStyle([
                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                ('BOTTOMPADDING', (0,0), (-1,-1), 0),
                ('TOPPADDING', (0,0), (-1,-1), 1),
                ('LEFTPADDING', (0,0), (-1,-1), 3),
                ('RIGHTPADDING', (0,0), (-1,-1), 3),
                ('FONT', (0,0), (-1,-1), 'DejaVu', 8),
                ('GRID', (0,0), (-1,-1), 0.01*cm, 'Black'),
                ('FONT', (1,1), (-2,-4), 'DejaVu', 15),
                ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                ('ALIGN', (0,0), (0,-1), 'RIGHT'),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('SPAN',(0,0),(6,0)),
                ('ALIGN', (0,0), (-1,0), 'CENTER'),
                ('FONT', (0,0), (6,0), 'DejaVuBd', 20),
                ])

# - Contenido de la tabla 1
Mitabla1Contenido=[['Mi Tabla 1','01','02','03','04','05','06'],
                    ['10','11','12','13','14','15','16'],
                    ['20','21','22','23','24','25','26'],
                    ['30','31','32','33','34','35','36'],
                    ['40','41','42','43','44','45','46'],
                    ['50','51','52','53','54','55','56']]
        
# - Creo las tablas con el contenido y el formato
Mitabla1=Table(Mitabla1Contenido, style=tipoTabla_moderno)

# Defino el arreglo que contendra el contenido del documento 
# - En este punto tener presente que se indica el formato de la siguiente
#   pagina, en el caso de las paginas que usan varios frames solo se llama
#   el primer frame, despues en doc.addPageTemplates se adicionan los demas
#   marcos no entiendo porque lo definieron de esa forma pero funciona
#   correctamente
# - Usar tags tipo html para dar formato al texto como:
#   <font color=#0000FF>texto en azul </font>
#   hace que el tiempo de generacion del documento se multiplique alrededor
#   de 5 veces. 
# - Si quisiera un formato diferente para las paginas pares e impares probar
#   algo como esto: 
#       Elements.append(NextPageTemplate(['pageLeft', 'pageRight']))
                             
Elements=[]
Elements.append(NextPageTemplate('normal'))
Elements.append(Paragraph("Usando marco normal, "*500, estiloencabezado))

Elements.append(NextPageTemplate('2colsA'))
Elements.append(PageBreak())
Elements.append(Paragraph("Usando marco 2colsA,  "*500, estilonormal))

Elements.append(NextPageTemplate('normal'))
Elements.append(PageBreak())
Elements.append(Paragraph("Usando por 2 vez el marco normal. "*20, estilonormal))

Elements.append(NextPageTemplate('normal'))
Elements.append(PageBreak())
Elements.append(Paragraph("Despues de este parrafo debe haber un espacio de 3cm. "*20, estilonormal))
Elements.append(Spacer(1,3*cm))
Elements.append(Paragraph("Antes de este parrafo debe haber un espacio de 3cm. "*20, estilonormal))

Elements.append(NextPageTemplate('4frm1'))
Elements.append(PageBreak())
Elements.append(Paragraph("Usando 4frm1. "*500, estilonormal))

Elements.append(NextPageTemplate('normal'))
Elements.append(PageBreak())
Elements.append(Mitabla1)

# Le doy formato a cada pagina segun se requiera en este caso el parametro
# es el id de cada pagina el que permite realizar la edicion
doc.addPageTemplates([PageTemplate(id='normal',frames=frame1,onPage=foot1,onPageEnd=foot2, pagesize=letter),                     
                      PageTemplate(id='2colsA',frames=[frame2,frame3],onPage=foot2, pagesize=A4),
                      PageTemplate(id='4frm1',frames=[frame4,frame5,frame6,frame7],onPage=foot2, pagesize=letter),
                      ])

#Construyo el documento
doc.build(Elements)

# Presento el tiempo que ha tardado en ejecutarse el programa
tiempodeejecucion=(time.time() - start_time)
print "Tiempo de ejecucion: ", tiempodeejecucion, "segundos"

# Abro el archivo creado en el visor de pdf obviamente no mido este tiempo
# al no ser relevante en el sistema web 
os.system("evince MiPlantilla.pdf")


