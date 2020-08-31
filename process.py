with open("input.txt", "rt") as file:
    text = file.read()
    text = text.replace('\\,a', 'ą')
    text = text.replace('\\\'a', 'ą')
    text = text.replace('\\,e', 'ę')
    text = text.replace('\\\'o', 'ó')
    text = text.replace('\\.z', 'ż')
    text = text.replace('\\\'c', 'ć')
    text = text.replace('\\\'n', 'ń')
    text = text.replace('\\\'s', 'ś')
    text = text.replace('\\|', 'ł')

    with open("output.txt", "wt") as output:
        output.write(text)