const canvas_image = document.getElementById("image");
const ctx_image = canvas_image.getContext("2d");

const img_perso = new Image();

img_perso.onload = function() {
    ctx_image.drawImage(img_perso,1 ,1, 200, 200);
 }
img_perso.src = "/2_Web/images/perso.svg";


const canvasSizeX = 500;
const canvasSizeY = 500;
const dx = 1;
const dy = 1;
var x = 1;
var y = 1;



function init() {
    img_perso.scr = "/2_Web/images/perso.svg";
    window.requestAnimationFrame(draw);
}

function draw() {
    console.log("hello");
    ctx_image.clearRect(0, 0, 500, 500);

    if (x > canvasSizeX){
        ctx_image.translate(-canvasSizeX, -canvasSizeY);
        x = 1;
        y = 1;
    } else{
        ctx_image.drawImage(img_perso, 1, 1, 200, 200);
        ctx_image.translate(1, 1);

    x = x + dx;
    y = y + dy;
    }
    
    window.requestAnimationFrame(draw);
}

init()