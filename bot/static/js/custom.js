// Suppression du contenu de la balise avec identifiant "chat"
var chatElt = document.getElementById("chat")
chatElt.innerHTML = "";


// Fonction de création des éléments du chat
function message(msg, listClass, img, imgClass) {
    var divElt = document.createElement("div");
    listClass.forEach(function (val) {
        divElt.classList.add(val);
    });
    var imgElt = document.createElement("img");
    imgElt.classList.add(imgClass);
    imgElt.setAttribute("src", "static/img/invite.png");
    imgElt.setAttribute("alt", "Avatar");
    var paraElt = document.createElement("p");
    paraElt.textContent = msg;
    divElt.appendChild(imgElt);
    divElt.appendChild(paraElt);
    chatElt.appendChild(divElt);
}

// message utilisateur
function userMessage(msg) {
    var userListClass = ["cont-chat", "darker", "text-right"];
    var userImg = "static/img/invite.png";
    message(msg, userListClass, userImg, "right");
}

// message GrandPy Bot
function robotMessage(msg) {
    var botListClass = ["cont-chat"];
    var botImg = "static/img/papybot.png";
    message(msg, botListClass, botImg, "left")

}

// message de tests
userMessage("Hello PapyBot");
robotMessage("Bonjour Je suis PapyBot, bienvenue sur mon site !");
userMessage("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?");
robotMessage("Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris.");
robotMessage("Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? " +
    "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.\n" +
    "Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au\n" +
    "57 rue d'Hauteville et la troisième en impasse. [En savoir plus sur Wikipedia]");
