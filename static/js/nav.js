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
  var productItems = Array.from(products);
  var itemsPerPage = 12;
  var totalPages = Math.ceil(productItems.length / itemsPerPage);
  var currentPage = 1;

  function showPage(page) {
    var start = (page - 1) * itemsPerPage;
    var end = start + itemsPerPage;
    productItems.forEach(function (item, index) {
      if (index >= start && index < end) {
        item.style.display = "block";
      } else {
        item.style.display = "none";
      }
    });
  }

  function createPagination() {
    var pagination = document.getElementById("pagination");
    for (var i = 1; i <= totalPages; i++) {
      var pageNumber = document.createElement("span");
      pageNumber.textContent = i;
      pageNumber.className = "page-number";
      pageNumber.dataset.page = i;
      pageNumber.addEventListener("click", function () {
        var page = parseInt(this.dataset.page);
        currentPage = page;
        showPage(page);
      });
      pagination.appendChild(pageNumber);
    }
  }

  function init() {
    showPage(currentPage);
    createPagination();
  }

  init();
});
setTimeout(function () {
  var alert = document.getElementById("autoCloseAlert");
  alert.classList.remove("show");
}, 3000);
