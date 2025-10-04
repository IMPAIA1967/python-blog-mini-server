from flask import Flask, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/<path:any_path>', methods=['GET'])
def contacts(any_path=None):
    try:
        with open('contacts.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        return Response(html_content, mimetype='text/html; charset=utf-8')
    except FileNotFoundError:
        return Response('<h1>Ошибка: файл contacts.html не найден</h1>',
                       status=404, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)