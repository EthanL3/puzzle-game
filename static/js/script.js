function drag(event) {
  event.dataTransfer.setData("text", event.target.id);
}

function allowDrop(event) {
  event.preventDefault();
}

function drop(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  var droppedPiece = document.getElementById(data);
  var target = event.target;

  // Swap positions of the dragged piece and the target piece
  if (target.className === "puzzle-piece") {
    var temp = { top: target.style.top, left: target.style.left };
    target.style.top = droppedPiece.style.top;
    target.style.left = droppedPiece.style.left;
    droppedPiece.style.top = temp.top;
    droppedPiece.style.left = temp.left;
  }
}

// Add event listeners to puzzle pieces and container
var puzzleContainer = document.getElementById("puzzle-container");
var pieces = document.getElementsByClassName("puzzle-piece");
for (var i = 0; i < pieces.length; i++) {
  pieces[i].addEventListener("dragover", allowDrop);
  pieces[i].addEventListener("drop", drop);
}
puzzleContainer.addEventListener("dragover", allowDrop);
puzzleContainer.addEventListener("drop", drop);

// want to be able to move every piece using javascript.
// Need to create a function that will check if the clicked piece is next to the empty piece.
// If it is, swap the two pieces and update the puzzle.

// create a function that will update the puzzle by rearranging the pieces on the board.

// check if the clicked piece is next to the empty piece.
// This function will take two arguments: the position of the clicked piece and the position of the empty piece.
// It will return true if the clicked piece is next to the empty piece, and false otherwise.

// function isAdjacent(position, emptyPosition) {

//     // get the row and column of the clicked piece
//     var row = Math.floor(position / cols);
//     var col = position % cols;

//     // get the row and column of the empty piece
//     var emptyRow = Math.floor(emptyPosition / cols);
//     var emptyCol = emptyPosition % cols;

//     // check if the clicked piece is next to the empty piece
//     if ((row === emptyRow && Math.abs(col - emptyCol) === 1) || (col === emptyCol && Math.abs(row - emptyRow) === 1)) {
//         return true;
//     } else {
//         return false;

// function updatePuzzle() {
//     // clear the board
//     board.innerHTML = '';

//     // add the pieces to the board
//     pieces.forEach(function(piece) {
//         if (piece) {
//             board.appendChild(piece);
//         } else {
//             board.appendChild(emptyPiece);
//         }
//     });
// }

// function shufflePuzzle() {
//     // shuffle the pieces
//     pieces.sort(function() {
//         return Math.random() - 0.5;
//     });

//     // update the puzzle
//     updatePuzzle();
// }

// // add event listener to the shuffle button
// shuffleButton.addEventListener('click', shufflePuzzle);

// // update the puzzle

// updatePuzzle();
// }

// // add event listener to the window
// window.addEventListener('load', init);
