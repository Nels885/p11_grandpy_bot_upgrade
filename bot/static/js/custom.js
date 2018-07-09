// Suppression du contenu de la balise avec identifiant "chat"
var chatElt = document.getElementById("chat");
var form = document.getElementById("addMsg");
//chatElt.innerHTML = "";

// Class of create chat elements
var Message = {
    // Initialise Le message
    init: function (userClass, userImg, imgClass) {
        this.userClass = userClass;
        this.userImg = userImg;
        this.imgClass = imgClass;
    },
    chat: function (msg) {
        var divElt = document.createElement("div");
        this.userClass.forEach(function (val) {
            divElt.classList.add(val);
        });
        var imgElt = document.createElement("img");
        imgElt.classList.add(this.imgClass);
        imgElt.setAttribute("src", this.userImg);
        imgElt.setAttribute("alt", "Avatar");
        var paraElt = document.createElement("p");
        paraElt.textContent = msg;
        divElt.appendChild(imgElt);
        divElt.appendChild(paraElt);
        chatElt.appendChild(divElt);
    }
};


function response(msg) {
    if (msg === "Hello PapyBot") {
        bot.chat("Bonjour Je suis PapyBot, bienvenue sur mon site !");
    } else if (msg === "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?") {
        bot.chat("Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris.");
        bot.chat("Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? " +
            "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.\n" +
            "Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au\n" +
            "57 rue d'Hauteville et la troisième en impasse. [En savoir plus sur Wikipedia]");
    } else {
        bot.chat("Je ne comprends pas la question !!");
    }
}


// Create Object User
var user = Object.create(Message);
user.init(["cont-chat", "darker", "text-right"], "../static/img/invite.png", "right");

// Create Object GrandPy Bot
var bot = Object.create(Message);
bot.init(["cont-chat"], "../static/img/papybot.png", "left");



form.addEventListener("submit", function (e) {
    $("#msgPres").hide();
    var saisie = form.elements.content.value;
    console.log(saisie);
    user.chat(saisie);
    response(saisie);
    saisie = "";
    e.preventDefault();
});
