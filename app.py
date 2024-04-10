from flask import Flask, render_template, request
import requests
from PIL import Image
import random
import os

app = Flask(__name__)

def generate_puzzle(image_path, rows, cols):
    # Open the image
    image = Image.open(image_path)
    width, height = image.size

    # Calculate the size of each piece
    piece_width = width // cols
    piece_height = height // rows

    # Create a list to hold the pieces
    piece_paths = []

    for row in range(rows):
        for col in range(cols):
            left = col * piece_width
            upper = row * piece_height
            right = (col + 1) * piece_width
            lower = (row + 1) * piece_height
            piece = image.crop((left, upper, right, lower))
            piece_path = os.path.join('static', 'images', f'piece_{row}_{col}.jpg')
            piece.save(piece_path)
            piece_paths.append(f'images/piece_{row}_{col}.jpg') 

    # Return the list of file paths
    print(piece_paths)
    random.shuffle(piece_paths)
    return piece_paths

    # Save the shuffled image
    output_path = os.path.join('static', 'images', 'shuffled_puzzle.jpg')
    shuffled_image.save(output_path)

    return output_path

@app.route('/ai_image', methods=['POST'])
def ai_image():
    # Extract text from input box
    text = request.form['text']

    # import requests

    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": "Bearer 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"}
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content
    image_bytes = query({
        "inputs": text,
    })

    # save image
    image_path = "static/images/ai_image.jpg"
    image_path_os = 'static/images/ai_image.jpg'#os.path.join('static', 'images', 'ai_image.jpg')
    with open(image_path, 'wb') as f:
        f.write(image_bytes)

    # send back to home but with the new image rather than the puzzle
    # shuffled_image_path = generate_puzzle(image_path, 4, 4)  # 4x4 puzzle
    shuffled_image_path = generate_puzzle(image_path_os, 4, 4)
    piece_paths = ["static/"+i for i in shuffled_image_path]
    return render_template('index.html', original_image=image_path, piece_paths=piece_paths)



    # You can access the image with PIL.Image for example
    # import io
    # from PIL import Image
    # image = Image.open(io.BytesIO(image_bytes))


@app.route('/')
def home():
    # if the method is get, we just use the camera image:
    # if request.method == 'GET':
    original_image_path = 'static/images/puzzle.jpg'
    shuffled_image_path = generate_puzzle(original_image_path, 4, 4)  # 4x4 puzzle
    piece_paths = ["static/"+i for i in shuffled_image_path]
    return render_template('index.html', original_image=original_image_path, piece_paths=piece_paths)
    # if the method is post, we generate an image from the input and use that image:
    # if request.method == 'POST':
        

if __name__ == '__main__':
    app.run(debug=True)













    
#    for piece in pieces:
#     piece.addEventListener('click', function() {
#         // get the position of the clicked piece
#         var position = pieces.indexOf(piece);

#         // get the position of the empty piece
#         var emptyPosition = pieces.indexOf(null);

#         // check if the clicked piece is next to the empty piece
#         if (isAdjacent(position, emptyPosition)) {
#             // swap the clicked piece with the empty piece
#             pieces[emptyPosition] = piece;
#             pieces[position] = null;

#             // update the puzzle
#             updatePuzzle();
#         }
#     });


# want to be able to move every piece using javascript.  
# Need to create a function that will check if the clicked piece is next to the empty piece.
# If it is, swap the two pieces and update the puzzle.

# create a function that will update the puzzle by rearranging the pieces on the board.

# check if the clicked piece is next to the empty piece. 
# This function will take two arguments: the position of the clicked piece and the position of the empty piece. 
# It will return true if the clicked piece is next to the empty piece, and false otherwise.


# function isAdjacent(position, emptyPosition) {

#     // get the row and column of the clicked piece
#     var row = Math.floor(position / cols);
#     var col = position % cols;

#     // get the row and column of the empty piece
#     var emptyRow = Math.floor(emptyPosition / cols);
#     var emptyCol = emptyPosition % cols;

#     // check if the clicked piece is next to the empty piece
#     if ((row === emptyRow && Math.abs(col - emptyCol) === 1) || (col === emptyCol && Math.abs(row - emptyRow) === 1)) {
#         return true;
#     } else {
#         return false;

# function updatePuzzle() {
#     // clear the board
#     board.innerHTML = '';

#     // add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);

#/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);


    
#    for piece in pieces:
#     piece.addEventListener('click', function() {
#         // get the position of the clicked piece
#         var position = pieces.indexOf(piece);

#         // get the position of the empty piece
#         var emptyPosition = pieces.indexOf(null);

#         // check if the clicked piece is next to the empty piece
#         if (isAdjacent(position, emptyPosition)) {
#             // swap the clicked piece with the empty piece
#             pieces[emptyPosition] = piece;
#             pieces[position] = null;

#             // update the puzzle
#             updatePuzzle();
#         }
#     });


# want to be able to move every piece using javascript.  
# Need to create a function that will check if the clicked piece is next to the empty piece.
# If it is, swap the two pieces and update the puzzle.

# create a function that will update the puzzle by rearranging the pieces on the board.

# check if the clicked piece is next to the empty piece. 
# This function will take two arguments: the position of the clicked piece and the position of the empty piece. 
# It will return true if the clicked piece is next to the empty piece, and false otherwise.


# function isAdjacent(position, emptyPosition) {

#     // get the row and column of the clicked piece
#     var row = Math.floor(position / cols);
#     var col = position % cols;

#     // get the row and column of the empty piece
#     var emptyRow = Math.floor(emptyPosition / cols);
#     var emptyCol = emptyPosition % cols;

#     // check if the clicked piece is next to the empty piece
#     if ((row === emptyRow && Math.abs(col - emptyCol) === 1) || (col === emptyCol && Math.abs(row - emptyRow) === 1)) {
#         return true;
#     } else {
#         return false;

# function updatePuzzle() {
#     // clear the board
#     board.innerHTML = '';

#     // add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);

#/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
    
#    for piece in pieces:
#     piece.addEventListener('click', function() {
#         // get the position of the clicked piece
#         var position = pieces.indexOf(piece);

#         // get the position of the empty piece
#         var emptyPosition = pieces.indexOf(null);

#         // check if the clicked piece is next to the empty piece
#         if (isAdjacent(position, emptyPosition)) {
#             // swap the clicked piece with the empty piece
#             pieces[emptyPosition] = piece;
#             pieces[position] = null;

#             // update the puzzle
#             updatePuzzle();
#         }
#     });


# want to be able to move every piece using javascript.  
# Need to create a function that will check if the clicked piece is next to the empty piece.
# If it is, swap the two pieces and update the puzzle.

# create a function that will update the puzzle by rearranging the pieces on the board.

# check if the clicked piece is next to the empty piece. 
# This function will take two arguments: the position of the clicked piece and the position of the empty piece. 
# It will return true if the clicked piece is next to the empty piece, and false otherwise.


# function isAdjacent(position, emptyPosition) {

#     // get the row and column of the clicked piece
#     var row = Math.floor(position / cols);
#     var col = position % cols;

#     // get the row and column of the empty piece
#     var emptyRow = Math.floor(emptyPosition / cols);
#     var emptyCol = emptyPosition % cols;

#     // check if the clicked piece is next to the empty piece
#     if ((row === emptyRow && Math.abs(col - emptyCol) === 1) || (col === emptyCol && Math.abs(row - emptyRow) === 1)) {
#         return true;
#     } else {
#         return false;

# function updatePuzzle() {
#     // clear the board
#     board.innerHTML = '';

#     // add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);

#/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
    
#    for piece in pieces:
#     piece.addEventListener('click', function() {
#         // get the position of the clicked piece
#         var position = pieces.indexOf(piece);

#         // get the position of the empty piece
#         var emptyPosition = pieces.indexOf(null);

#         // check if the clicked piece is next to the empty piece
#         if (isAdjacent(position, emptyPosition)) {
#             // swap the clicked piece with the empty piece
#             pieces[emptyPosition] = piece;
#             pieces[position] = null;

#             // update the puzzle
#             updatePuzzle();
#         }
#     });


# want to be able to move every piece using javascript.  
# Need to create a function that will check if the clicked piece is next to the empty piece.
# If it is, swap the two pieces and update the puzzle.

# create a function that will update the puzzle by rearranging the pieces on the board.

# check if the clicked piece is next to the empty piece. 
# This function will take two arguments: the position of the clicked piece and the position of the empty piece. 
# It will return true if the clicked piece is next to the empty piece, and false otherwise.


# function isAdjacent(position, emptyPosition) {

#     // get the row and column of the clicked piece
#     var row = Math.floor(position / cols);
#     var col = position % cols;

#     // get the row and column of the empty piece
#     var emptyRow = Math.floor(emptyPosition / cols);
#     var emptyCol = emptyPosition % cols;

#     // check if the clicked piece is next to the empty piece
#     if ((row === emptyRow && Math.abs(col - emptyCol) === 1) || (col === emptyCol && Math.abs(row - emptyRow) === 1)) {
#         return true;
#     } else {
#         return false;

# function updatePuzzle() {
#     // clear the board
#     board.innerHTML = '';

#     // add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);

#/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
    
#    for piece in pieces:
#     piece.addEventListener('click', function() {
#         // get the position of the clicked piece
#         var position = pieces.indexOf(piece);

#         // get the position of the empty piece
#         var emptyPosition = pieces.indexOf(null);

#         // check if the clicked piece is next to the empty piece
#         if (isAdjacent(position, emptyPosition)) {
#             // swap the clicked piece with the empty piece
#             pieces[emptyPosition] = piece;
#             pieces[position] = null;

#             // update the puzzle
#             updatePuzzle();
#         }
#     });


# want to be able to move every piece using javascript.  
# Need to create a function that will check if the clicked piece is next to the empty piece.
# If it is, swap the two pieces and update the puzzle.

# create a function that will update the puzzle by rearranging the pieces on the board.

# check if the clicked piece is next to the empty piece. 
# This function will take two arguments: the position of the clicked piece and the position of the empty piece. 
# It will return true if the clicked piece is next to the empty piece, and false otherwise.


# function isAdjacent(position, emptyPosition) {

#     // get the row and column of the clicked piece
#     var row = Math.floor(position / cols);
#     var col = position % cols;

#     // get the row and column of the empty piece
#     var emptyRow = Math.floor(emptyPosition / cols);
#     var emptyCol = emptyPosition % cols;

#     // check if the clicked piece is next to the empty piece
#     if ((row === emptyRow && Math.abs(col - emptyCol) === 1) || (col === emptyCol && Math.abs(row - emptyRow) === 1)) {
#         return true;
#     } else {
#         return false;

# function updatePuzzle() {
#     // clear the board
#     board.innerHTML = '';

#     // add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);

#/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
    
#    for piece in pieces:
#     piece.addEventListener('click', function() {
#         // get the position of the clicked piece
#         var position = pieces.indexOf(piece);

#         // get the position of the empty piece
#         var emptyPosition = pieces.indexOf(null);

#         // check if the clicked piece is next to the empty piece
#         if (isAdjacent(position, emptyPosition)) {
#             // swap the clicked piece with the empty piece
#             pieces[emptyPosition] = piece;
#             pieces[position] = null;

#             // update the puzzle
#             updatePuzzle();
#         }
#     });


# want to be able to move every piece using javascript.  
# Need to create a function that will check if the clicked piece is next to the empty piece.
# If it is, swap the two pieces and update the puzzle.

# create a function that will update the puzzle by rearranging the pieces on the board.

# check if the clicked piece is next to the empty piece. 
# This function will take two arguments: the position of the clicked piece and the position of the empty piece. 
# It will return true if the clicked piece is next to the empty piece, and false otherwise.


# function isAdjacent(position, emptyPosition) {

#     // get the row and column of the clicked piece
#     var row = Math.floor(position / cols);
#     var col = position % cols;

#     // get the row and column of the empty piece
#     var emptyRow = Math.floor(emptyPosition / cols);
#     var emptyCol = emptyPosition % cols;

#     // check if the clicked piece is next to the empty piece
#     if ((row === emptyRow && Math.abs(col - emptyCol) === 1) || (col === emptyCol && Math.abs(row - emptyRow) === 1)) {
#         return true;
#     } else {
#         return false;

# function updatePuzzle() {
#     // clear the board
#     board.innerHTML = '';

#     // add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);

#/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });

    
#    for piece in pieces:
#     piece.addEventListener('click', function() {
#         // get the position of the clicked piece
#         var position = pieces.indexOf(piece);

#         // get the position of the empty piece
#         var emptyPosition = pieces.indexOf(null);

#         // check if the clicked piece is next to the empty piece
#         if (isAdjacent(position, emptyPosition)) {
#             // swap the clicked piece with the empty piece
#             pieces[emptyPosition] = piece;
#             pieces[position] = null;

#             // update the puzzle
#             updatePuzzle();
#         }
#     });


# want to be able to move every piece using javascript.  
# Need to create a function that will check if the clicked piece is next to the empty piece.
# If it is, swap the two pieces and update the puzzle.

# create a function that will update the puzzle by rearranging the pieces on the board.

# check if the clicked piece is next to the empty piece. 
# This function will take two arguments: the position of the clicked piece and the position of the empty piece. 
# It will return true if the clicked piece is next to the empty piece, and false otherwise.


# function isAdjacent(position, emptyPosition) {

#     // get the row and column of the clicked piece
#     var row = Math.floor(position / cols);
#     var col = position % cols;

#     // get the row and column of the empty piece
#     var emptyRow = Math.floor(emptyPosition / cols);
#     var emptyCol = emptyPosition % cols;

#     // check if the clicked piece is next to the empty piece
#     if ((row === emptyRow && Math.abs(col - emptyCol) === 1) || (col === emptyCol && Math.abs(row - emptyRow) === 1)) {
#         return true;
#     } else {
#         return false;

# function updatePuzzle() {
#     // clear the board
#     board.innerHTML = '';

#     // add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);

#/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
    
#    for piece in pieces:
#     piece.addEventListener('click', function() {
#         // get the position of the clicked piece
#         var position = pieces.indexOf(piece);

#         // get the position of the empty piece
#         var emptyPosition = pieces.indexOf(null);

#         // check if the clicked piece is next to the empty piece
#         if (isAdjacent(position, emptyPosition)) {
#             // swap the clicked piece with the empty piece
#             pieces[emptyPosition] = piece;
#             pieces[position] = null;

#             // update the puzzle
#             updatePuzzle();
#         }
#     });


# want to be able to move every piece using javascript.  
# Need to create a function that will check if the clicked piece is next to the empty piece.
# If it is, swap the two pieces and update the puzzle.

# create a function that will update the puzzle by rearranging the pieces on the board.

# check if the clicked piece is next to the empty piece. 
# This function will take two arguments: the position of the clicked piece and the position of the empty piece. 
# It will return true if the clicked piece is next to the empty piece, and false otherwise.


# function isAdjacent(position, emptyPosition) {

#     // get the row and column of the clicked piece
#     var row = Math.floor(position / cols);
#     var col = position % cols;

#     // get the row and column of the empty piece
#     var emptyRow = Math.floor(emptyPosition / cols);
#     var emptyCol = emptyPosition % cols;

#     // check if the clicked piece is next to the empty piece
#     if ((row === emptyRow && Math.abs(col - emptyCol) === 1) || (col === emptyCol && Math.abs(row - emptyRow) === 1)) {
#         return true;
#     } else {
#         return false;

# function updatePuzzle() {
#     // clear the board
#     board.innerHTML = '';

#     // add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);

#/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
    
#    for piece in pieces:
#     piece.addEventListener('click', function() {
#         // get the position of the clicked piece
#         var position = pieces.indexOf(piece);

#         // get the position of the empty piece
#         var emptyPosition = pieces.indexOf(null);

#         // check if the clicked piece is next to the empty piece
#         if (isAdjacent(position, emptyPosition)) {
#             // swap the clicked piece with the empty piece
#             pieces[emptyPosition] = piece;
#             pieces[position] = null;

#             // update the puzzle
#             updatePuzzle();
#         }
#     });


# want to be able to move every piece using javascript.  
# Need to create a function that will check if the clicked piece is next to the empty piece.
# If it is, swap the two pieces and update the puzzle.

# create a function that will update the puzzle by rearranging the pieces on the board.

# check if the clicked piece is next to the empty piece. 
# This function will take two arguments: the position of the clicked piece and the position of the empty piece. 
# It will return true if the clicked piece is next to the empty piece, and false otherwise.


# function isAdjacent(position, emptyPosition) {

#     // get the row and column of the clicked piece
#     var row = Math.floor(position / cols);
#     var col = position % cols;

#     // get the row and column of the empty piece
#     var emptyRow = Math.floor(emptyPosition / cols);
#     var emptyCol = emptyPosition % cols;

#     // check if the clicked piece is next to the empty piece
#     if ((row === emptyRow && Math.abs(col - emptyCol) === 1) || (col === emptyCol && Math.abs(row - emptyRow) === 1)) {
#         return true;
#     } else {
#         return false;

# function updatePuzzle() {
#     // clear the board
#     board.innerHTML = '';

#     // add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);

#/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
    
#    for piece in pieces:
#     piece.addEventListener('click', function() {
#         // get the position of the clicked piece
#         var position = pieces.indexOf(piece);

#         // get the position of the empty piece
#         var emptyPosition = pieces.indexOf(null);

#         // check if the clicked piece is next to the empty piece
#         if (isAdjacent(position, emptyPosition)) {
#             // swap the clicked piece with the empty piece
#             pieces[emptyPosition] = piece;
#             pieces[position] = null;

#             // update the puzzle
#             updatePuzzle();
#         }
#     });


# want to be able to move every piece using javascript.  
# Need to create a function that will check if the clicked piece is next to the empty piece.
# If it is, swap the two pieces and update the puzzle.

# create a function that will update the puzzle by rearranging the pieces on the board.

# check if the clicked piece is next to the empty piece. 
# This function will take two arguments: the position of the clicked piece and the position of the empty piece. 
# It will return true if the clicked piece is next to the empty piece, and false otherwise.


# function isAdjacent(position, emptyPosition) {

#     // get the row and column of the clicked piece
#     var row = Math.floor(position / cols);
#     var col = position % cols;

#     // get the row and column of the empty piece
#     var emptyRow = Math.floor(emptyPosition / cols);
#     var emptyCol = emptyPosition % cols;

#     // check if the clicked piece is next to the empty piece
#     if ((row === emptyRow && Math.abs(col - emptyCol) === 1) || (col === emptyCol && Math.abs(row - emptyRow) === 1)) {
#         return true;
#     } else {
#         return false;

# function updatePuzzle() {
#     // clear the board
#     board.innerHTML = '';

#     // add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);

#/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });
# }

# function shufflePuzzle() {
#     // shuffle the pieces
#     pieces.sort(function() {
#         return Math.random() - 0.5;
#     });

#     // update the puzzle
#     updatePuzzle();
# }

# // add event listener to the shuffle button
# shuffleButton.addEventListener('click', shufflePuzzle);

# // update the puzzle

# updatePuzzle();
# }

# // add event listener to the window
# window.addEventListener('load', init);/ add the pieces to the board
#     pieces.forEach(function(piece) {
#         if (piece) {
#             board.appendChild(piece);
#         } else {
#             board.appendChild(emptyPiece);
#         }
#     });