const chat = $("#chat");
let numId = 0;
let backEnd, geoLocation, pageId;


// Class to make ajax request
let RequestAjax = {
    // Initialize
    init: function (method, url) {
        this.method = method;
        this.url = url;
        this.dataType = "json";
    },
    ajax: function (data, result) {
        $.ajax({
            method: this.method,
            url: this.url,
            data: data,
            dataType: this.dataType,
        }).done(result).fail(ajaxError)
    }
};


// Class for display the answer of GrandpyBot or Anonymous
let ContChat = {
    init: function (chatClass, avatar, avatClass) {
        this.chatClass = chatClass;
        this.avatar = avatar;
        this.avatClass = avatClass;
    },
    add: function (answer) {
        // Remove load animation
        $('#load').remove();
        chat.append('<div class="row"><div class="' + this.chatClass + '">' +
            '<img class="' + this.avatClass + '" src="../static/img/' + this.avatar + '" alt="Avatar"><p>' + answer + '</p></div></div>');
    }
};

// Create Ajax Objects
let backEndObject = Object.create(RequestAjax);
backEndObject.init("POST", "/");
let mediaWikiObject = Object.create(RequestAjax);

// Create Chat Objects
let chatBot = Object.create(ContChat);
chatBot.init("cont-chat mr-auto", "papybot.png", "left avatar");
let chatUser = Object.create(ContChat);
chatUser.init("cont-chat darker text-right ml-auto", "invite.png", "right avatar");
let chatMap = Object.create(ContChat);
chatMap.init("cont-chat col-lg-12 mr-auto", "papybot.png", "left avatar");


// Function for adding load animation
function loadBot() {
    chat.append('<div class="row"><div class="cont-chat text-center col-lg-12" id="load">' +
        '<div id="loader"></div></div></div>');
}


// Function for the error with Ajax
function ajaxError(error) {
    chatBot.add("Je suis désolé, je ne peux pas vous répondre pour le moment, mon cerveau est en surchauffe :( !!");

    // Display error message in the console
    console.error("[AJAX] ERROR : " + error);
}


// Function for search with API MediaWiki
function mediawikiSearchCallback(response) {
    const pageIdList = response["query"]["geosearch"];
    pageId = pageIdList[0]["pageid"];
    // Number of the searched page
    for (let i = 0; i < pageIdList.length; i++) {
        if (pageIdList[i]["title"] === geoLocation["route"]) {
            pageId = pageIdList[i]["pageid"];
        }
    }

    console.log("[MEDIAWIKI] PAGE_ID : " + pageId);

    backEnd["dataPageId"]["pageids"] = pageId;
    mediaWikiObject.ajax(backEnd["dataPageId"], mediawikiPageidCallback);
}


// Function for displaying the response of the MediaWiki API
function mediawikiPageidCallback(response) {
    const lien = "https://fr.wikipedia.org/wiki?curid=" + pageId;
    const result = response["query"]["pages"][0]["extract"];
    msgBot = backEnd["answers"][1] + result;
    console.log("[MEDIAWIKI] ANSWER_BOT : " + msgBot);

    chatBot.add(msgBot + ' [<a href="' + lien + '">En savoir plus sur Wikipedia</a>]');
}


// Function for displaying the google map
function initMap(location, mapId) {
    let map = new google.maps.Map(document.getElementById(mapId), {
        center: location,
        zoom: 14
    });
    let marker = new google.maps.Marker({
        position: location,
        map: map,
        title: "C\'est ici !"
    });
}


$(function () {

    $("form").on("submit", function (e) {
        e.preventDefault();

        // Adding the user message in the chat window
        const msgUser = $("#content").val();
        chatUser.add(msgUser);

        // Adding load animation
        loadBot();

        // AJAX requests to the post and displays the PapyBot message according to the user message
        backEndObject.ajax({content: msgUser}, function (response) {
            backEnd = response;
            mediaWikiObject.init("GET", backEnd["urlApiWiki"]);
            geoLocation = backEnd["geoLocation"];
            console.log("[BACK END] LOCATION : " + geoLocation);

            chatBot.add(response["answers"][0]);

            // if geolocation then we display the Google Map
            if (geoLocation["route"].length !== 0) {
                let mapId = "map" + String(numId);
                chatMap.add('<div id=' + mapId + ' class="map"></div>');
                initMap(geoLocation["geometry"], mapId);
                numId += 1;
                // Adding load animation
                loadBot();
                backEnd["dataSearch"]["gscoord"] = geoLocation["geometry"]["lat"] + "|" + geoLocation["geometry"]["lng"];
                mediaWikiObject.ajax(backEnd["dataSearch"], mediawikiSearchCallback);
            }
        });
    });
});