from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for puzzle pieces
puzzle_pieces = [
    {'id': 1, 'x': 100, 'y': 100},
    {'id': 2, 'x': 200, 'y': 200},
    # Add more pieces as needed
]

@app.route('/')
def index():
    return render_template('index.html', pieces=puzzle_pieces)

@app.route('/move_piece', methods=['POST'])
def move_piece():
    piece_id = request.json['id']
    new_x = request.json['x']
    new_y = request.json['y']
    
    # Update the position of the piece
    for piece in puzzle_pieces:
        if piece['id'] == piece_id:
            piece['x'] = new_x
            piece['y'] = new_y
            break
    
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
