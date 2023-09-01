function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

let darkbutton = document.getElementById("dark-button")
let body = document.body
let titulo = document.getElementById("titulo");
let descricao = document.getElementById("descricao")
let formbutton = document.getElementById("form-button")
let appbar = document.getElementById("appbar")

darkbutton.addEventListener( 'change', function() {
  if(this.checked) {
      localStorage.setItem('dark',this.checked);

      body.classList.add('dark-mode')
      titulo.classList.add('dark-mode-form')
      descricao.classList.add('dark-mode-form')
      formbutton.classList.add('btn-dark')
      appbar.classList.add('appbar-dark')
      darkbutton.classList.add('btn-dark')
  } else{
      localStorage.removeItem('dark');
      body.classList.remove('dark-mode')
      titulo.classList.remove('dark-mode-form')
      descricao.classList.remove('dark-mode-form')
      formbutton.classList.remove('btn-dark')
      appbar.classList.remove('appbar-dark')
      darkbutton.classList.remove('btn-dark')  
  }
  });

if(localStorage.getItem('dark')) {
  darkbutton.checked = "true"
  body.classList.add('dark-mode')
  titulo.classList.add('dark-mode-form')
  descricao.classList.add('dark-mode-form')
  formbutton.classList.add('btn-dark')
  appbar.classList.add('appbar-dark')
  darkbutton.classList.add('btn-dark')
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
});
