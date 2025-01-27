"use strict";
// Использование токена из Cookie
import { getCookie } from "./script.js";

// Использование токена из meta тега
// const csrfToken = document
//   .querySelector('meta[name="csrf-token"]')
//   .getAttribute("content");

// Product_detail.html => Add to cart
$(document).on("click", "#add-button", function (e) {
  e.preventDefault();

  const csrfToken = getCookie("csrftoken");

  $.ajax({
    type: "POST",
    url: $(this).data("url"),
    data: {
      product_id: $("#add-button").val(),
      product_qty: $("#select_quantity option:selected").text(),
      csrfmiddlewaretoken: csrfToken,
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

// cart-view.html => delete product in cart
$(document).on("click", ".delete-button", function (e) {
  e.preventDefault();

  const csrfToken = getCookie("csrftoken");

  $.ajax({
    type: "POST",
    url: $(this).data("url"),
    data: {
      product_id: $(this).data("index"),
      csrfmiddlewaretoken: csrfToken,
    },
    success: function (response) {
      document.getElementById("lblCartCount").textContent = response.qty;
      document.getElementById("total").textContent = response.total;

      location.reload();
    },
    error: function (error) {
      console.log(error);
    },
  });
});

// cart-view.html => update product quantity in cart
$(document).on("click", ".update-button", function (e) {
  e.preventDefault();

  const csrfToken = getCookie("csrftoken");

  $.ajax({
    type: "POST",
    url: $(this).data("url"),
    data: {
      product_id: $(this).data("index"),
      product_qty: $(
        "#select" + $(this).data("index") + "option:selected"
      ).text(),
      csrfmiddlewaretoken: csrfToken,
    },
    success: function (response) {
      document.getElementById("lblCartCount").textContent = response.qty;
      document.getElementById("total").textContent = response.total;

      location.reload();
    },
    error: function (error) {
      console.log(error);
    },
  });
});
