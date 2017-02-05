
def hello():
    print 'Hello'
    print 'Fun'


def greet(lang):
	if lang == 'es':
	    return 'Hola'
	elif lang == 'fr':
		return 'Bonjour'
	else:
		return 'Hello'

hello()
print greet('en')
print greet('es')
print greet('fr')
