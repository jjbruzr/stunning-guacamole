# to create a dictionary, you name it and then = empty curly braces
acronyms = {}


# to create a key value pair, name the dictionary, then the key then value
acronyms['LOL'] = 'Laught out loud'
acronyms['IDK'] = "I don't know"
acronyms['TBH'] = 'To be honest'
acronyms['BRT'] = 'Be right there'
acronyms['OMW'] = 'On my way!'

# update a key's value, it is the same as initially assigning the value
# acronym['TBH'] = 'you smell bad'


# print a particular key's value
# print(acronyms['LOL'])

# to delete a key from a dictionary you use the del keywork
del acronyms['BRT']


# print the entire dictionary
print(acronyms)