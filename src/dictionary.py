class DICTIONARY:
    def __init__(self, name, url, cls_span):
        self.name = name
        self.url = url
        self.cls_span = cls_span

class CAMBRIDGE(DICTIONARY):
    def __init__(self):
        super().__init__("CAMBRIDGE", "https://dictionary.cambridge.org/dictionary/english/", "eg deg")

class MERRIAM_WEBSTER(DICTIONARY):
    def __init__(self):
        super().__init__("MERRIER_WESTER", "https://www.merriam-webster.com/dictionary/", "t has-aq")

class OXFORD(DICTIONARY):
    def __init__(self):
        super().__init__("OXFORD", "https://www.oxfordlearnersdictionaries.com/definition/english/", "x")
        
        
        
DICT_ENUM = {
    "CAMBRIDGE": CAMBRIDGE,
    "MERRIAM_WEBSTER": MERRIAM_WEBSTER,
    "OXFORD": OXFORD
}
        