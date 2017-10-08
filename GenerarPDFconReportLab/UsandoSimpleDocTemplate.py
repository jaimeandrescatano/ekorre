#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Generar un documento en PDF con ReportLab
# Este programa genera un documento en PDF con la plantilla 
# "SimpleDocTemplate" de platypus en donde la primer pagina puede ser
# diferente a las demas 
 
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.lib.pagesizes import A4, letter
from PIL import Image

PAGE_WIDTH, PAGE_HEIGHT = letter

capitulo = 'Cap %d' % 1
tema = 'Descripcion General del Edificio'
logo = Image.open('logo.png')
##logo = 'el logo de 40x40pixels'
arquitecto = 'Nombre del arquitecto'
empresa = 'nombre de la empresa'
proyecto = 'Descripcion del proyecto'
situacion = 'poblacion, municipio'
referencia = 'referencia interna'
 
l1 = (1*cm, PAGE_HEIGHT-2.3*cm, PAGE_WIDTH-1.5*cm, PAGE_HEIGHT-2.3*cm)
l2 = (1*cm, 1.5*cm, PAGE_WIDTH-1.5*cm, 1.5*cm)
lineas = [l1,l2]
 
estiloencabezado = ParagraphStyle('',
                              fontName = 'DejaVuBd',
                              fontSize = 10,
                              alignment = 0,
                              spaceBefore = 0,
                              spaceAfter = 0,
                              leftIndent = -1*cm,
                              rightIndent = -0.7*cm)
 
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
 
##plantillaBase = BaseDocTemplate(filename = fich_pdf,
##                            pagesize = A4,
##                            showBoundary=0,
##                            allowSplitting = 1,
##                            _pageBreakQuick = 1)
 
#importar una fuente TT
pdfmetrics.registerFont(TTFont('DejaVu', '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBd', '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBdIt', '/usr/share/fonts/truetype/freefont/FreeSansBoldOblique.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuIt', '/usr/share/fonts/truetype/freefont/FreeSansOblique.ttf'))
registerFontFamily('Dejavu', normal = 'DejaVu', bold = 'DejaVuBd', italic = 'DejaVuIt', boldItalic = 'DejaVuBdIt')
 
def PrimeraPagina(canvas, doc):
    canvas.saveState()
 
    # Lineas
    canvas.setStrokeColor('Grey')
    canvas.setLineWidth(0.01)
    canvas.lines(lineas)
 
    # Textos
    canvas.setFont('DejaVu',7)
    
    # Cabecera
    canvas.drawInlineImage(logo, 1*cm, PAGE_HEIGHT-2.*cm, width = 40, height = 40)
    canvas.drawString(2.5*cm, PAGE_HEIGHT-1.*cm, 'ARQUITECTO: ' + arquitecto)
    canvas.drawString(2.5*cm, PAGE_HEIGHT-1.5*cm, 'EMPRESA: ' + empresa)
 
    canvas.drawRightString(PAGE_WIDTH-1.7*cm, PAGE_HEIGHT-1*cm, 'PROYECTO: '+ proyecto)
    canvas.drawRightString(PAGE_WIDTH-1.7*cm, PAGE_HEIGHT-1.5*cm, 'SITUACION: ' + situacion)
    canvas.drawRightString(PAGE_WIDTH-1.7*cm, PAGE_HEIGHT-2.*cm, 'REFERENCIA: ' + referencia)
    
    # Pie
    canvas.drawCentredString(PAGE_WIDTH/2.0, 1.0 * cm, u'%s' % tema)
    canvas.drawRightString(PAGE_WIDTH - 1.7 * cm, 1.0 * cm, u'Pág. %d' % doc.page)
 
    canvas.restoreState()
 
def PaginasCentrales(canvas, doc):
    canvas.saveState()
 
    # Lineas
    canvas.setStrokeColor('Grey')
    canvas.setLineWidth(0.01)
    canvas.lines(lineas)
 
    # Textos
    canvas.setFont('DejaVu',7)
    
    # Cabecera
    canvas.drawInlineImage(logo, 1*cm, PAGE_HEIGHT-2.*cm, width = 40, height = 40)
    canvas.drawString(2.5*cm, PAGE_HEIGHT-1.*cm, 'ARQUITECTO: ' + arquitecto)
    canvas.drawString(2.5*cm, PAGE_HEIGHT-1.5*cm, 'EMPRESA: ' + empresa)
 
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-1.0*cm, capitulo)
 
    # Pie
    canvas.drawCentredString(PAGE_WIDTH/2.0, 1.0 * cm, u'%s' % tema)
    canvas.drawRightString(PAGE_WIDTH - 1.7 * cm, 1.0 * cm, u'Pág. %d' % doc.page)
 
    canvas.restoreState()
 
def go():
    doc = SimpleDocTemplate("GenerarPDFconReportLab.pdf")
    
    # Capitulo 1
    Titulo1 = u'CAPITULO 1: En una galaxia muy muy lejana...'
    T1 = Paragraph(Titulo1, estiloencabezado)
    textoT1 = u'Habia una vez un niño que se llamaba Luke Skywalker. '*20
    txtT1 = Paragraph(textoT1, estilonormal)
    
    # Capitulo 2
    Titulo2 = u'CAPITULO 2: La formación de las virutas de chocolate.'
    T2 = Paragraph(Titulo2, estiloencabezado)
    textoT2 = u'La preparacion del chocolate en barra por los artesanos.'*20
    txtT2 = Paragraph(textoT2, estilonormal)
    
    Story = [Spacer(1,cm)]
    Story.append(T1)
    Story.append(txtT1)
    Story.append(Spacer(1,1*cm))
    Story.append(T2)
    Story.append(txtT2)
    Story.append(Spacer(1,1*cm))
    Story.append(T1)
    Story.append(txtT1)
    Story.append(Spacer(1,1*cm))
    Story.append(T2)
    Story.append(txtT2)
    Story.append(Spacer(1,1*cm))
    Story.append(T1)
    Story.append(txtT1)
    Story.append(Spacer(1,1*cm))
    Story.append(T2)
    Story.append(txtT2)
    Story.append(Spacer(1,1*cm))
 
    doc.build(Story, 
                onFirstPage=PrimeraPagina, 
                onLaterPages=PaginasCentrales)
if __name__ == "__main__":
    go()
