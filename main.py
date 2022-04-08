from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def ana_sayfa():
  return render_template('anasayfa.html')

@app.route('/kategoriler')
def kategoriler():
  return render_template('kategoriler.html')
  
@app.route('/kayit')
def kategoriler():
  return render_template('kayit.html')

app.run(host='0.0.0.0', port=8080)
