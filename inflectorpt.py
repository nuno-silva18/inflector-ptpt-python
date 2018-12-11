rules = {
    # (<singular>, <plural>)
    ('ão', 'ões'),
    ('ês', 'eses'),
    ('l', 'is'),
    ('m', 'ns'),
    ('r', 'es'),
    ('s', 'es'),
    ('z', 'es')
}

exceptions = {
    ('cão', 'cães'),
    ('campus', 'campi'),
    ('cidadão', 'cidadãos'),
    ('fax', 'fax'),
    ('lápis', 'lápis'),
    ('mão', 'mãos'),
    ('qualquer', 'quaisquer'),
    ('tórax', 'tórax')
}

def singularize(word):
    for exception in exceptions:
        if exception[1] == word:
            return exception[0]
    for rule in rules:
        word_term = word[(len(word) - len(rule[1])):]
        if rule[1] == word_term:
            if rule[1] != 'es':
                word = word[:(len(word) - len(rule[1]))] + rule[0]
                return word
            else:
                return word[:(len(word) - len(rule[1]))]
    if word[-1] == 's':
        return word[:-1]
    return word

def pluralize(word):
    for exception in exceptions:
        if exception[0] == word:
            return exception[1]
    for rule in rules:
        word_term = word[(len(word) - len(rule[0])):]
        if rule[0] == word_term:
            if rule[1] != 'es':
                word = word[:(len(word) - len(rule[0]))] + rule[1]
                return word
            else:
                return word + rule[1]
    if word[-1] != 's':
        return word + 's'
    return word