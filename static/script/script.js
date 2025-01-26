"use strict";

document.addEventListener("DOMContentLoaded", function () {
  // Находим все элементы с классом "card_from_category"
  const cards = document.querySelectorAll(".card_from_category");

  // Проходим по каждому элементу и добавляем обработчик клика
  cards.forEach((card) => {
    // Получаем URL из атрибута data-url
    const productUrl = card.getAttribute("data-url");

    // Добавляем обработчик клика
    card.addEventListener("click", function () {
      if (productUrl) {
        window.location.href = productUrl; // Перенаправление на URL
      }
    });
  });
});
