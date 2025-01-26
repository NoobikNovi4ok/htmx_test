"use strict";
// Product_detail.html => Add to cart
$(document).on("click", "#add-button", function (e) {
  e.preventDefault();

  $.ajax({
    type: "POST",
    url: $(this).attr("data-url"),
    data: {
      product_id: $("#add-button").val(),
      product_qty: $("#select option:selected").text(),
      csrfmiddlewaretoken: $(this).attr("data-csrf"),
      action: "post",
    },
    success: function (response) {
      document.getElementById("lblCartCount").textContent = response.qty;
      const add_button = document.getElementById("add-button");
      add_button.disabled = true;
      add_button.innerText = "Added to cart";
      add_button.className = "btn btn-success btn-sm";
    },
    error: function (error) {
      console.log(error);
    },
  });
});
