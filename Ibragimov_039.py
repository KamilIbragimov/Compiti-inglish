from flask import Flask, request, render_template
import json
app = Flask(__name__)

def read_flashcards(id: int):
    with open("flashcards.json","r") as f:
        flashcards=json.load(f)
    print(flashcards)



@app.route("/flashcards/<id>", methods=['GET', 'POST'])
def get_flashcard_by_id(id):
        
    
          
       return render_template ("Flashcards.html", flashcard=flashcard)
def prompt_for_id() -> int:
    




if __name__ == "__main__":
    app.run(debug=True, port=6989)
       

