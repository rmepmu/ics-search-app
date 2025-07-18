from flask import Flask, request, render_template

app = Flask(__name__)

with open("ics_text.txt", encoding="utf-8") as f:
    content = f.read()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    keyword = request.args.get('keyword', '').strip().lower()
    if not keyword:
        return render_template("result.html", keyword=keyword, results=[])
    
    results = [line.strip() for line in content.split('\n') if keyword in line.lower()]
    return render_template("result.html", keyword=keyword, results=results)

if __name__ == '__main__':
    app.run(debug=True)
