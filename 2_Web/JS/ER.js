console.log("Bonjour");

function createParticle() {
    const particles = document.getElementById("particles");
    const p = document.createElement("div");
    p.classList.add("particule");

    // Position horizontale aléatoire
    p.style.left = Math.random() * window.innerWidth + "px";

    // Taille aléatoire
    const size = Math.random() * 6 + 4;
    p.style.width = size + "px";
    p.style.height = size + "px";

    // Durée aléatoire
    p.style.animationDuration = (Math.random() * 2 + 3) + "s";

    particles.appendChild(p);

    // Supprime la particule après l’animation
    setTimeout(() => {
        p.remove();
    }, 5000);
}

// Création régulière de particules
setInterval(createParticle, 300);

const canvas = document.getElementById("image");
const ctx = canvas.getContext("2d");

const img = new Image();
img.src = "images/horse.svg";

let angle = 0;
let direction = 1; // 1 = va vers 5° ; -1 = revient vers -5°

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Déterminer l'angle d'oscillation
    angle += 0.02 * direction;

    if (angle > 0.2) direction = -1;   // limite haute (~8.6°)
    if (angle < -0.2) direction = 1;   // limite basse (~-8.6°)

    // Sauvegarde du contexte
    ctx.save();

    // Déplacer le point de rotation au centre de l'image
    ctx.translate(100, 100);

    // Appliquer rotation
    ctx.rotate(angle);

    // Dessiner l'image centrée
    ctx.drawImage(img, -65, -70, 100, 100);

    // Restaurer
    ctx.restore();

    requestAnimationFrame(draw);
}

img.onload = draw;