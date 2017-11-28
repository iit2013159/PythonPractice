import string
for i in string.ascii_lowercase:
    if(i in ('a','e','i','o','u')):
        print("Vowel")
    else:
        print("Consonant")