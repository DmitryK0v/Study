class TextProcessor(object):
    def __init__(self):
        self._puncktuation = '.,!?:;#@&'

    def __is_punctuation(self, char):
        return char in self._puncktuation

    def get_clean_string(self, text):
        cln_str = ''
        for char in text:
            if self.__is_punctuation(char):
                continue
            else:
                cln_str += char
        return cln_str


class TextLoader(object):
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_str(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print('Clean string is: {}'.format(self.__clean_string))
        return self.__clean_string


class DataInterface(object):
    def __init__(self):
        self.__text_loader = TextLoader()

    def process_text(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_str(text)
            clean = self.__text_loader.clean_string
            clean_texts.append(clean)
        return clean_texts

di = DataInterface()
textos = ['dfsdl,md4lwmoi.i&?!@#', 'So many, ...mana power!!!! AOAAA?']
di.process_text(textos)