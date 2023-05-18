from collections import defaultdict

class LanaguageLibrarian:
    
    LANGUAGE_LIBRARY = defaultdict(dict)

    LANGUAGE_LIBRARY['articles_conjunctions_prepositions']['en'] = ('of', 'and', 'but', 'or', 'for', 'yet', 'so', 'a', 'an', 'the')
    
    
    
    {'articles, conjunctions and prepositions' : {
                        'en': ('of', 'and', 'but', 'or', 'for', 'yet', 'so', 'a', 'an', 'the'),
                        'fr': ('le', 'la', 'les', 'et', 'ou', 'mais', 'donc', 'or', 'ni', 'car', 
                               'parce que', 'à', 'de', 'en', 'dans', 'par', 'avec', 'sans', 'sur', 'sous',
                                'entre', 'devant', 'derrière', 'près de', 'loin de', 'pour', 'chez',
                                'depuis', 'jusqu\'à', 'envers'),
                        'de': ('der', 'die', 'das', 'und', 'oder', 'aber', 'denn', 'doch', 'weil', 'da',
                               'in', 'an', 'auf', 'vor', 'mit', 'nach', 'seit', 'von', 'zu', 'bis', 'aus',
                               'bei', 'zu', 'an', 'vor', 'auf', 'ab'),
                        'nl': ('de', 'het', 'een', 'en', 'of', 'maar', 'dat', 'in', 'op', 'met', 'naar', 'van',
                               'uit', 'te', 'bij', 'tot', 'voor', 'door', 'om', 'als', 'dan'),
                        'es': ('el', 'la', 'los', 'las',
                               'y', 'e', 'o', 'u', 'pero', 'sino', 'y', 'ni', 'que', 'cuando', 'mientras',
                               'hasta', 'después', 'antes', 'desde', 'por', 'para', 'entre', 'con', 'en',
                               'a', 'ante', 'bajo', 'cabe', 'contra', 'de', 'desde', 'durante', 'en', 'entre','hacia', 'hasta', 'mediante', 'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras'),
                        'it': ('il', 'lo', 'la', 'i', 'gli', 'le',
                               'e', 'o', 'ma', 'però', 'anche', 'ne', 'che', 'quando', 'mentre', 'fino', 'dopo','prima', 'da', 'di', 'con', 'in', 'su', 'per', 'tra', 'fra', 'a', 'ad', 'al', 'dal','del', 'nel', 'col', 'sul', 'di', 'dai', 'dei', 'nel', 'sul', 'al', 'dal', 'dal', 'nel', 'sul', 'col', 'per', 'tra', 'fra', 'conforme', 'secondo', 'senza', 'come'),
                        'pt': ('o', 'a', 'os', 'as', 'e', 'ou', 'mas', 'porém', 'todavia', 'contudo', 'que'
                               'quando', 'enquanto', 'até', 'depois', 'antes', 'desde', 'por', 'para', 'entre',
                               'com', 'em', 'a', 'ante','após', 'de', 'desde', 'durante', 'em', 'entre', 'para', 
                               'por', 'segundo','sem', 'sob', 'sobre', 'atrás', 'através', 'conforme', 'exceto', 
                               'exceto', 'como'),
                        'no': (),
                        'sv': (),
                        'da': (),
                        'fi': ()
                        },
                        'job titles': {

                        },
                        'common nouns': {

                        }
    }
    def __init__(self):
        pass

    def get_dictionary(self):
        pass