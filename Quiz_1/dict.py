def make_dict (dictionary_file):
    dictionary = {}
    for i in dictionary_file:
        if len(i) <= 10:
            word_length = len(i)
        else:
            word_length = 10
        try:
            dictionary[word_length].append(i)
        except:
            dictionary[word_length] = [i]
    return dictionary

if __name__ == '__main__':

    d = {2: ['at', 'to', 'no'], 3: ['add', 'sun'], 10: ['Hello! How are you?']}
    dictionary = make_dict(['at', 'add', 'sun', 'to', 'no', 'Hello! How are you?'])
    print(dictionary)
    assert dictionary == d
    print('Everything works correctly!')