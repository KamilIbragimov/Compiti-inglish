from flask import Flask, request, render_template
import json
app = Flask(__name__)

with open("flashcards.json") as f:
    flashcards=json.load(f)


@app.route("/flashcards/<id>", methods=['GET', 'POST'])
def gg(id):
    
          
       
         
        
        

        return render_template ("Flashcards.html", flashcard=flashcards)
    


if __name__ == "__main__":
    app.run(debug=True, port=6989)
       

