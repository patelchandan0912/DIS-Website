const wrapper = document.querySelector(".sliderWrapper");
const menuItems = document.querySelectorAll(".category");

menuItems.forEach((item, index) => {
    item.addEventListener ("click", () => {
        wrapper.style.transform = `translateX(${-100 * index}vw)`;
    });
});

const images = document.querySelectorAll('.slider img');

let index = 0;

function changeImage() {
  images[index].classList.remove('active');
  index = (index + 1) % images.length;
  images[index].classList.add('active');
}

setInterval(changeImage, 3000);