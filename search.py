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
