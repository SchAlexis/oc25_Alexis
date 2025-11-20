console.log("Bonjour");

const statut = document.getElementById("statut");
const ctx_statut = statut.getContext("2d");


ctx_statut.fillStyle = "green";
ctx_statut.fillRect(0, 0, 300, 300);

const dessin = document.getElementById("dessin");
const context = dessin.getContext("2d");


context.beginPath();
context.strokeStyle = "red";
context.moveTo(250,100);
context.lineTo(100, 250);
context.lineTo(250, 400);
context.lineTo(400,250);
context.closePath();
context.fillStyle = "red",
context.fill();
context.stroke();


context.beginPath();
context.arc(250, 250, 50, 0, 2 * Math.PI)
context.fillStyle = "black";
context.fill();


// context.fillStyle = "black" 
// context.fillRect(0, 0, 100, 100)
// context.fillRect(100, 100, 100, 100)
// context.fillRect(200, 200, 100, 100)
// context.fillRect(300, 300, 100, 100)
// context.fillRect(400, 400, 100, 100)

// for (var i = 0; i < 5; i++) {
//     for ( var j = 0; 1 < 5; j++) {
//         if (( i + j) % 2 == 0) {
//             context.fillStyle = "black";
//         } else {
//             context.fillStyle = "white";
//         }
//         context.fillRect(i * 100, j * 100, 100, 100);
//     }
// }