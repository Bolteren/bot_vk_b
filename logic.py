import amath
import botConfiguration as bConf
import re
import search


class DecisionMaking:
    def __init__(self, text):
        self.botPhrases = bConf.bot_phrases_config()
        self.userPhrases = bConf.users_phrases_config()
        self.text = text.lower()
        self.responce = ""

    def clean_text(self):
        text_list = self.text.split()
        fin_list = [word for word in text_list if word not in self.userPhrases['removable']]
        self.text = ' '.join(fin_list)

    def get_responce(self):
        checs_text_commparis = search.comparison_degrees(self.text)
        checs_text_harting = search.check_harting(self.text)

        if checs_text_commparis != 'False':
            params = re.findall('\d{1,}', self.text)
            if checs_text_commparis == 'lit':
                self.responce = amath.correction(params[0], params[1])
            elif checs_text_commparis == 'grad':
                self.responce = amath.correction(params[1], params[0])
            else:
                pass
        elif checs_text_harting != 'False':#расчет с разным расположеием значений (переделать!)
            params = re.findall('\d{1,}', self.text)
            if checs_text_harting == 'MTO':
                self.responce = amath.rate_harting(params[2], params[1], params[0])
            elif checs_text_harting == 'MOT':
                self.responce = amath.rate_harting(params[1], params[2], params[0])
            elif checs_text_harting == 'TMO':
                self.responce = amath.rate_harting(params[2], params[0], params[1])
            elif checs_text_harting == 'TOM':
                self.responce = amath.rate_harting(params[1], params[0], params[2])
            elif checs_text_harting == 'OTM':
                self.responce = amath.rate_harting(params[0], params[1], params[2])
            elif checs_text_harting == 'OMT':
                self.responce = amath.rate_harting((params[0], params[2], params[1]))
            pass
        else:
            pass


        return self.responce


    def pr(self):
        print(search.comparison_degrees(self.text))


def main():
    a = DecisionMaking("мощность 5 температура 10 объем 10")
    a.clean_text()
    print(a.get_responce())


if __name__ == "__main__":
    main()