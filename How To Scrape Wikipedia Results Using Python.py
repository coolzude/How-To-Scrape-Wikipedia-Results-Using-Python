import wikipedia


# Urge User
query = input('what is your question ? :')
query.replace('wikipedia', 'who is')


# initalize wikipedia
results = wikipedia.summary(query, sentences=2)
print('According To Wikipedia')
print(results)
