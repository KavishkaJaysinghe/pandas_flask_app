from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load CSV file once
df = pd.read_csv("data.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    search = request.form.get("search")
    filtered = df

    if search:
        filtered = df[df["Name"].str.contains(search, case=False)]

    return render_template("index.html", tables=[filtered.to_html(classes='data')], titles=filtered.columns.values)

if __name__ == "__main__":
    app.run(debug=True)
 
