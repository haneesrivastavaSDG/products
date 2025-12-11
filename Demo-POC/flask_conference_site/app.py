from flask import Flask, render_template, request
from data import sessions

app = Flask(__name__)

@app.route('/')
def index():
    query = request.args.get('q', '').lower()
    
    if query:
        filtered_sessions = [
            s for s in sessions
            if query in s['title'].lower() or 
               query in s['speaker'].lower() or 
               query in s['category'].lower()
        ]
    else:
        filtered_sessions = sessions

    return render_template('index.html', sessions=filtered_sessions, query=query)

if __name__ == '__main__':
    app.run(debug=True)
