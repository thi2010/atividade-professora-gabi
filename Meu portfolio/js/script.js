
const menuBtn = document.getElementById("menu-btn");
const menu = document.getElementById("menu");
const temaBtn = document.getElementById("tema-btn");

// Abre e fecha o menu
menuBtn.addEventListener("click", function () {
    menu.classList.toggle("aberto");

    const aberto = menu.classList.contains("aberto");

    menuBtn.setAttribute("aria-expanded", aberto);
    menuBtn.setAttribute(
        "aria-label",
        aberto ? "Fechar menu" : "Abrir menu"
    );
});

// Fecha o menu depois de clicar em um link
document.querySelectorAll("#menu a").forEach(function (link) {
    link.addEventListener("click", function () {
        menu.classList.remove("aberto");
        menuBtn.setAttribute("aria-expanded", "false");
        menuBtn.setAttribute("aria-label", "Abrir menu");
    });
});

// Saudação de acordo com o horário
const hora = new Date().getHours();
const saudacao = document.getElementById("saudacao");

if (hora < 12) {
    saudacao.textContent = "Bom dia! Seja bem-vindo.";
} else if (hora < 18) {
    saudacao.textContent = "Boa tarde! Seja bem-vindo.";
} else {
    saudacao.textContent = "Boa noite! Seja bem-vindo.";
}

// Troca entre tema escuro e claro
temaBtn.addEventListener("click", function () {
    document.body.classList.toggle("claro");

    const claro = document.body.classList.contains("claro");

    temaBtn.textContent = claro ? "🌙" : "☀️";
    temaBtn.setAttribute(
        "aria-label",
        claro ? "Ativar tema escuro" : "Ativar tema claro"
    );
});

// Atualiza o ano automaticamente
document.getElementById("ano").textContent =
    new Date().getFullYear();

// Validação do formulário
const formulario = document.getElementById("formulario");
const retorno = document.getElementById("retorno");

formulario.addEventListener("submit", function (evento) {
    evento.preventDefault();

    if (!formulario.checkValidity()) {
        formulario.reportValidity();
        return;
    }

    retorno.textContent =
        "Formulário validado! Este exemplo não envia os dados.";

    formulario.reset();
});
