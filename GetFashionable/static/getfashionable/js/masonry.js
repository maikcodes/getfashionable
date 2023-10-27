document.addEventListener("DOMContentLoaded", function () {
  const grid = document.querySelector(".image-gallery");
  new Masonry(grid, {
    itemSelector: ".image-item",
    columnWidth: ".image-item",
    gutter: 20,
    isFitWidth: true,
  });
});
