const chat = $('#chat');
let numId = 0;
let backEnd, geoLocation, pageId;


// Class to make ajax request
class RequestAjax {
    // Initialize
    constructor(method, url) {
        this.method = method;
        this.url = url;
        this.dataType = 'json';
    }

    ajax(data, result) {
        $.ajax({
            method: this.method,
            url: this.url,
            data: data,
            dataType: this.dataType,
        }).done(result).fail(ajaxError)
    }
}


// Create Ajax Objects
let backEndObject = new RequestAjax('POST', '/');
let mediaWikiObject;

// Create Chat Objects
let chatBot = new ContChat('cont-chat mr-auto', 'papybot.png', 'left avatar');
let chatUser = new ContChat('cont-chat darker text-right ml-auto', 'invite.png', 'right avatar');
let chatMap = new ContChat('cont-chat col-lg-12 mr-auto', 'papybot.png', 'left avatar');


// Function for adding load animation
function loadBot() {
    chat.append('<div class="row"><div class="cont-chat text-center col-lg-12" id="load">' +
        '<div id="loader"></div></div></div>');
}


// Function for the error with Ajax
function ajaxError(error) {
    chatBot.add('Je suis désolé, je ne peux pas vous répondre pour le moment, mon cerveau est en surchauffe :( !!');

    // Display error message in the console
    console.error('[AJAX] ERROR : ' + error);
}


// Function for displaying the google map
function initMap(location, mapId) {
    geometry = location['geometry'];
    let map = new google.maps.Map(document.getElementById(mapId), {
        center: geometry,
        zoom: 14
    });
    let marker = new google.maps.Marker({
        position: geometry,
        map: map,
        title: 'C\'est ici !'
    });
}


$(function () {

    $('form').on('submit', function (e) {
        e.preventDefault();

        // Adding the user message in the chat window
        const msgUser = $('#content').val();
        chatUser.add(msgUser);

        // Adding load animation
        loadBot();

        // AJAX requests to the post and displays the PapyBot message according to the user message
        backEndObject.ajax({content: msgUser}, function (response) {
            backEnd = response;
            mediaWikiObject = new RequestAjax('GET', backEnd['urlApiWiki']);
            geoLocation = backEnd['geoLocation'];
            console.log('[BACK END] LOCATION : ' + geoLocation);

            chatBot.send(response['answers'][0]);

            // if geolocation then we display the Google Map
            if (geoLocation) {

                // adding weather for the desired location
                let weather = response['weather'];
                console.log('[BACK END] WEATHER : ' + weather);
                chatBot.add('<p>Température: ' + weather['temp'] + '<br>Description: ' + weather['desc'] + '</p>');

                let mapId = 'map' + String(numId);
                chatMap.add('<div id=' + mapId + ' class="map"></div>');
                initMap(geoLocation, mapId);
                numId += 1;
                // Adding load animation
                loadBot();
                backEnd['dataSearch']['gscoord'] = geoLocation['geometry']['lat'] + '|' + geoLocation['geometry']['lng'];
                mediaWikiObject.ajax(backEnd['dataSearch'], mediawikiSearchCallback);
            }
        });
    });
});