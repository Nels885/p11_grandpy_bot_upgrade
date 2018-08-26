const chat = $('#chat');
var numId = 0;


// Function for adding load animation
function loadBot() {
    chat.append('<div class="cont-chat text-center" id="load">' +
        '<div id="loader"></div></div>');
}


// Function for display the answer of GrandpyBot
function chatBot(answer) {
    // Remove load animation
    $('#load').remove();

    chat.append('<div class="cont-chat">' +
        '<img class="left avatar" src="../static/img/papybot.png" alt="Avatar">' +
        '<p>' + answer + '</p></div>');
}


// function for the error with Ajax
function ajaxError(error) {
    // Display error message in the console
    console.error("[AJAX] ERROR : " + error);

    chatBot("Je suis désolé, je ne peux pas vous répondre pour le moment, mon cerveau est en surchauffe :( !!");
    /*
    chatBot("{{ config['MSG_BOT_ERROR_API'] }}");
    */
}


// Function for search with API MediaWiki
function apiWiki(loc, resp) {
    var msgBot = resp['answers'][1];

    // Adding load animation
    loadBot();
    resp["dataSearch"]["gscoord"] = loc["geometry"]["lat"] + "|" + loc["geometry"]["lng"];
    $.get({
        url: resp['urlApiWiki'],
        data: resp['dataSearch'],
        dataType: "json",
    }).done(mediawikiSearchCallback).fail(ajaxError);

    function mediawikiSearchCallback(response) {
        const pageIdList = response["query"]["geosearch"];
        var pageId = pageIdList[0]["pageid"];
        // Number of the searched page
        for (i=0; i<pageIdList.length; i++){
            if (pageIdList[i]["title"] === loc["route"]) {
                pageId = pageIdList[i]["pageid"];
            }
        }

        console.log("[MEDIAWIKI] PAGE_ID : " + pageId);

        resp["dataPageId"]["pageids"] = pageId;
        $.get({
            url: resp["urlApiWiki"],
            data: resp["dataPageId"],
            dataType: "json",
        }).done(mediawikiPageidCallback).fail(ajaxError);

        function mediawikiPageidCallback(response) {

            const lien = "https://fr.wikipedia.org/wiki?curid=" + pageId;
            const result = response["query"]["pages"][0]["extract"];
            msgBot = msgBot + result;
            console.log("[MEDIAWIKI] ANSWER_BOT : " + msgBot);

            chatBot(msgBot + ' [<a href="' + lien + '">En savoir plus sur Wikipedia</a>]');
        }

    }
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
        title: 'C\'est ici !'
    });
}


$(function () {

    $('form').on('submit', function (e) {
        e.preventDefault();

        // Adding the user message in the chat window
        const msgUser = $('#content').val();
        chat.append('<div class="cont-chat darker text-right">' +
            '<img class="right avatar" src="../static/img/invite.png" alt="Avatar">' +
            '<p>' + msgUser + '</p></div>');

        // Adding load animation
        loadBot();

        // AJAX requests to the post and displays the PapyBot message according to the user message
        $.ajax({
            method: 'POST',
            url: '/',
            data: {content: msgUser},
        }).done(function (response) {
            const geoLocation = response['geoLocation'];
            console.log("[BACK END] LOCATION : " + geoLocation);

            chatBot(response['answers'][0]);

            // if geolocation then we display the Google Map
            if (geoLocation['geometry'].length !== 0) {
                var mapId = "map" + String(numId);
                chatBot('<div id=' + mapId + ' class="map"></div>');
                initMap(geoLocation['geometry'], mapId);
                numId += 1;
                apiWiki(geoLocation, response);
            }
        }).fail(ajaxError);
    });
});
