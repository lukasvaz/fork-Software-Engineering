const open = document.getElementById("open-tutorial");
const close = document.getElementById("close-tutorial");
const modal_container = document.getElementById("popup-container");

open.addEventListener("click", () => {
    modal_container.classList.add("show");
})

close.addEventListener("click", () => {
    modal_container.classList.remove("show");
})