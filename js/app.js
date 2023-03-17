const wrapper = document.querySelector(".sliderWrapper");
const menuItems = document.querySelectorAll(".category");

menuItems.forEach((item, index) => {
    item.addEventListener ("click", () => {
        wrapper.style.transform = `translateX(${-100 * index}vw)`;
    });
});