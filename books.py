##########################################--CODE EXPLANATION--##########################################
#                                                                                                      #
# The code below does the following:                                                                   #
#   1) Sets up pandas and Flask to use for the webpage                                                 #
#   2) Sets the main path for the webpage '/' to be able to have GET and POST requests using Flask     #
#   3) Gets the csv file uploaded by the user and stores it in this directory                          #
#   4) Stores the 'Title' and 'Author' columns from the csv file as a pandas DataFrame                 #
#   5) Creates a list of books where each book is a list with its title and author as the elements     #
#                                                                                                      #
##########################################--------------------##########################################

import os
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Gives the Root url for the webpage to the 'fome()' function and allows for 'GET' and 'POST' requests.
@app.route('/', methods=['GET', 'POST'])
def home():
    # Creates the list that holds each book's name nad author and initializes it with temporary data
    books = [['NO BOOKS', 'NO AUTHERS']]

    # If there is a 'POST' request and there is a file given in that request:
    #   Create a variable 'uploaded_file' that holds the name of the csv file uploaded by the user and is the name in the index.html file
    #   Creates a directory path from the current directory and the uploaded file name
    #   Saves the csv file to that directory
    #   Opens the csv file (provided by the user) to be read:
    #       Creates a pandas DataFrame from the csv file and stores the columns for the title and author
    #       Then creates a list of books, where each book is a list with index=0 as the title and index=1 as the author
    if request.method == 'POST':
        if request.files:
            uploaded_file = request.files['filename']
            filepath = os.path.join(app.config['FILE_UPLOADS'], uploaded_file.filename)
            uploaded_file.save(filepath)

            with open(filepath) as file:
                df = pd.DataFrame(pd.read_csv(file))
                titles = df.get('Title')
                authers = df.get('Author')
                books = [list(x) for x in zip(titles, authers)]
                
    # Displays the index.html code and sends in the books that the user provided (or the template if the user has not submitted a csv yet).
    return render_template('index.html', books=books)

# Gets CWD to use for storing csv
app.config['FILE_UPLOADS'] = os.getcwd()
    

if __name__ == '__main__':
   app.run()