import re


def comparison_degrees(text):
    txt1 = re.search('лит\w{0,}\s\d{1,}\sгра\w{0,}\s\d{1,}', text)
    txt2 = re.search('гра\w{0,}\s\d{1,}\sлит\w{0,}\s\d{1,}', text)
    txt3 = re.search('\d{1,}\sлит\w{0,}\s\d{1,}\sгра\w{0,}', text)
    txt4 = re.search('\d{1,}\sгра\w{0,}\s\d{1,}\sлит\w{0,}', text)
    if txt1 or txt3:
        return 'lit'
    elif txt2 or txt4:
        return 'grad'
    else:
        return 'False'


def check_harting(text):#как-то это надо переписать. Не красиво(((
    txt1 = re.search('мощ\w{0,}\s\d{1,}\sтем\w{0,}\s\d{1,}\sобъ\w{0,}\s\d{1,}', text)
    txt2 = re.search('\d{1,}\sмощ\w{0,}\s\d{1,}\sтем\w{0,}\s\d{1,}\sобъ\w{0,}', text)
    txt3 = re.search('мощ\w{0,}\s\d{1,}\sобъ\w{0,}\s\d{1,}\sтем\w{0,}\s\d{1,}', text)
    txt4 = re.search('\d{1,}\sмощ\w{0,}\s\d{1,}\sобъ\w{0,}\s\d{1,}\sтем\w{0,}', text)
    txt5 = re.search('тем\w{0,}\s\d{1,}\sмощ\w{0,}\s\d{1,}\sобъ\w{0,}\s\d{1,}', text)
    txt6 = re.search('\d{1,}\sтем\w{0,}\s\d{1,}\sмощ\w{0,}\s\d{1,}\sобъ\w{0,}', text)
    txt7 = re.search('тем\w{0,}\s\d{1,}\sобъ\w{0,}\s\d{1,}\sмощ\w{0,}\s\d{1,}', text)
    txt8 = re.search('\d{1,}\sтем\w{0,}\s\d{1,}\sобъ\w{0,}\s\d{1,}\sмощ\w{0,}', text)
    txt9 = re.search('объ\w{0,}\s\d{1,}\sтем\w{0,}\s\d{1,}\sмощ\w{0,}\s\d{1,}', text)
    txt10 = re.search('\d{1,}\sобъ\w{0,}\s\d{1,}\sтем\w{0,}\s\d{1,}\sмощ\w{0,}', text)
    txt11 = re.search('мощ\w{0,}\s\d{1,}\sобъ\w{0,}\s\d{1,}\sтем\w{0,}\s\d{1,}', text)
    txt12 = re.search('\d{1,}\sмощ\w{0,}\s\d{1,}\sобъ\w{0,}\s\d{1,}\sтем\w{0,}', text)
    if txt1 or txt2:
        out = 'MTO'
    elif txt3 or txt4:
        out = 'MOT'
    elif txt5 or txt6:
        out = 'TMO'
    elif txt7 or txt8:
        out = 'TOM'
    elif txt9 or txt10:
        out = 'OTM'
    elif txt11 or txt12:
        out = 'OMT'
    else:
        out = 'False'
    return out