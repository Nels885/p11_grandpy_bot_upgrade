const chat = $("#chat");
var numId = 0;
var backEnd, geoLocation, pageId;


// Class to make ajax request
var RequestAjax = {
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


// Create Objects
var backEndObject = Object.create(RequestAjax);
backEndObject.init("POST", "/");
var mediaWikiObject = Object.create(RequestAjax);


// Function for adding load animation
function loadBot() {
    chat.append('<div class="cont-chat text-center" id="load">' +
        '<div id="loader"></div></div>');
}


// Function for display the answer of GrandpyBot or Anonymous
function contChat(answer, bot = true) {
    var chatClass = "", avatar = "papybot.png", avatClass = "left";

    // Remove load animation
    $('#load').remove();
    if (!bot) {
        chatClass = "darker text-right", avatar = "invite.png", avatClass = "right";
    }
    chat.append('<div class="cont-chat ' + chatClass + '">' +
        '<img class="' + avatClass + ' avatar" src="../static/img/' + avatar + '" alt="Avatar"><p>' + answer + '</p></div>');
}


// Function for the error with Ajax
function ajaxError(error) {
    // Display error message in the console
    console.error("[AJAX] ERROR : " + error);

    contChat("Je suis désolé, je ne peux pas vous répondre pour le moment, mon cerveau est en surchauffe :( !!");
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

    contChat(msgBot + ' [<a href="' + lien + '">En savoir plus sur Wikipedia</a>]');
}


// Function for displaying the google map
function initMap(location, mapId) {
    var map = new google.maps.Map(document.getElementById(mapId), {
        center: location,
        zoom: 14
    });
    var marker = new google.maps.Marker({
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
        contChat(msgUser, false);

        // Adding load animation
        loadBot();

        // AJAX requests to the post and displays the PapyBot message according to the user message
        backEndObject.ajax({content: msgUser}, function (response) {
            backEnd = response;
            mediaWikiObject.init("GET", backEnd["urlApiWiki"]);
            geoLocation = backEnd["geoLocation"];
            console.log("[BACK END] LOCATION : " + geoLocation);

            contChat(response["answers"][0]);

            // if geolocation then we display the Google Map
            if (geoLocation["route"].length !== 0) {
                var mapId = "map" + String(numId);
                contChat('<div id=' + mapId + ' class="map"></div>');
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