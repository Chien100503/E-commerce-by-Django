const pathname = location.pathname;
console.log(pathname);
const navItems = document.querySelectorAll(".nav-item");
const navItemActive = document.querySelector(`.nav-text li[data-link='/${pathname.split("/")[1]}']`);

console.log(`.nav-item[data-link='/${pathname.split("/")[1]}']`);
navItems.forEach((navItem) => navItem.classList.remove("active"));
navItemActive.classList.add("active");

// JavaScript function to scroll to the top of the page
document.addEventListener("DOMContentLoaded", function () {
  var products = document.querySelectorAll(".product-item");
  var loadMoreButton = document.getElementById("load-more");
  var displayLimit = 8;
  var currentIndex = 0;

  function showNextProducts() {
    for (var i = currentIndex; i < currentIndex + displayLimit; i++) {
      if (products[i]) {
        products[i].style.display = "block";
      }
    }
    currentIndex += displayLimit;

    // Hide load more button if all products are displayed
    if (currentIndex >= products.length) {
      loadMoreButton.style.display = "none";
    }
  }

  function init() {
    // Hide all products initially
    for (var i = 0; i < products.length; i++) {
      if (i >= displayLimit) {
        products[i].style.display = "none";
      }
    }

    // Show next products when load more button is clicked
    loadMoreButton.addEventListener("click", function () {
      showNextProducts();
    });
  }

  init();
});
