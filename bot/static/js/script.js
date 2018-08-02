const chat = $('#chat');

// Function for adding load animation
function loadBot() {
    chat.append('<div class="cont-chat text-center" id="load">' +
        '<div id="loader"></div></div>');
}


// Function for search with API MediaWiki
function apiWiki(location, answer, urlWiki, dataSearch, dataPageId) {

    var msgBot = answer;

    // Adding load animation
    loadBot();

    dataSearch["gscoord"] = location["lat"] + "|" + location["lng"];
    // dataSearch["srsearch"] = addr;
    $.get({
        url: urlWiki + 'callback=?',
        data: dataSearch,
        dataType: "json",
    }).done(mediawikiSearchCallback).fail(function (error) {

        // Display error message in the console
        console.error(error);

    });

    function mediawikiSearchCallback(response) {

        // Number of the searched page
        // const pageid = response["query"]["search"][0]["pageid"];
        const pageid = response["query"]["geosearch"][0]["pageid"];
        console.log(pageid);

        dataPageId["pageids"] = pageid;
        $.get({
            url: urlWiki + 'callback=?',
            data: dataPageId,
            dataType: "json",
        }).done(mediawikiPageidCallback).fail(function (error) {

            // Display error message in the console
            console.error(error);

        });

        function mediawikiPageidCallback(response) {

            const result = response["query"]["pages"][0]["extract"];
            const posCitation = result.indexOf("==\n");
            // msgBot = msgBot + result.substr(posCitation);
            msgBot = msgBot + result;
            console.log(msgBot);

            // Remove load animation
            $('#load').remove();

            $('#chat').append('<div class="cont-chat">' +
                '<img class="left" src="../static/img/papybot.png" alt="Avatar">' +
                '<p>' + msgBot + '</p></div>');

        }

    }
}


$(function () {

    $('form').on('submit', function (e) {
        e.preventDefault();

        // hide the message "Posez votre question à GrandPy Bot !"
        // $('#msgPres').hide();

        // Adding the user message in the chat window
        const msgUser = $('#content').val();
        chat.append('<div class="cont-chat darker text-right">' +
            '<img class="right" src="../static/img/invite.png" alt="Avatar">' +
            '<p>' + msgUser + '</p></div>');

        // Adding load animation
        loadBot();

        // AJAX requests to the post and displays the PapyBot message according to the user message
        $.ajax({
            method: 'POST',
            url: '/',
            data: {content: msgUser},
        }).done(function (response) {

            // Remove load animation
            $('#load').remove();

            // Display the messages of GrandyBot
            const answersList = JSON.parse(response).messages;
            const keyWords = JSON.parse(response).keyWords;

            console.log(keyWords);

            $('#chat').append('<div class="cont-chat">' +
                '<img class="left" src="../static/img/papybot.png" alt="Avatar">' +
                '<p>' + answersList[0] + '</p></div>');

            if (keyWords.length !== 0) {
                // const addr = "cité Paradis, Paris";
                // const addr = "Elysée, Paris"
                const urlWiki = JSON.parse(response).urlApiWiki;
                const dataSearch = JSON.parse(response).dataSearch;
                const dataPageId = JSON.parse(response).dataPageId;

                apiWiki(keyWords, answersList[1], urlWiki, dataSearch, dataPageId);
            }
        }).fail(function (error) {

            // Display error message in the console
            console.error(error);

        });
    });
});
