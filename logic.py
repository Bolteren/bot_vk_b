import amath
import botConfiguration as bConf
import re
import search


class DecisionMaking():
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
        if checs_text_commparis != 'False':
            params = re.findall('\d{1,}', self.text)
            if checs_text_commparis == 'lit':
                self.responce = amath.correction(params[0], params[1])
            elif checs_text_commparis == 'grad':
                self.responce = amath.correction(params[1], params[0])
            else:
                pass
        elif False:
            pass
        else:
            pass


        return self.responce


    def pr(self):
        print(search.comparison_degrees(self.text))


def main():
    a = DecisionMaking("5 градусов 10 литров")
    a.clean_text()
    print(a.get_responce())


if __name__ == "__main__":
    main()