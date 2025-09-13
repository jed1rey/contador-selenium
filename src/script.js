let contador = 0;
const botaoContar = document.getElementById('botao-contar');
const historico = document.getElementById('historico');

botaoContar.addEventListener('click', function (e) {
  e.preventDefault();
  contador++;
  const li = document.createElement('li'); 
  li.textContent = `Clique nº ${contador}`;
  historico.appendChild(li);
});
