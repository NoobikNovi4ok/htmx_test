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
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

export { getCookie };
