const images = document.querySelectorAll('.slider img');

let index = 0;

function changeImage() {
  images[index].classList.remove('active');
  index = (index + 1) % images.length;
  images[index].classList.add('active');
}

changeImage(); // call changeImage immediately to display image on landing

setInterval(changeImage, 3000);
