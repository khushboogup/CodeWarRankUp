def generate_hashtag(s):
    text='#'+s.title().strip()
    text=''.join(text.split())
    if len(text)>140 or s=='':
        return False
    else:
        return text