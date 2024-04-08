const pathname = location.pathname;
console.log(pathname);
const navItems = document.querySelectorAll(".nav-item");
const navItemActive = document.querySelector(`.nav-text li[data-link='/${pathname.split("/")[1]}']`);

console.log(`.nav-item[data-link='/${pathname.split("/")[1]}']`);
navItems.forEach((navItem) => navItem.classList.remove("active"));
navItemActive.classList.add("active");

// JavaScript function to scroll to the top of the page

