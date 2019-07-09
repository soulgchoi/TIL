import webbrowser

urls = [
    'www.github.com',
    'www.google.com',
    'www.mail.google.com',
    'http://edu.ssafy.com/edu/main/index.do',
    'https://www.youtube.com/channel/UCyn-K7rZLXjGl7VXGweIlcA'
]

for url in urls:
    webbrowser.open(url)

