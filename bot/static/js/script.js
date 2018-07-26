$(function () {
    $('form').on('submit', function (e) {
        e.preventDefault();
        const chat = $('#chat');

        // Function for adding load animation
        function loadBot() {
            chat.append('<div class="cont-chat text-center" id="load">' +
                '<div id="loader"></div></div>');
        }

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

                // Adding load animation
                loadBot();

                const addr = "cité Paradis, Paris";
                $.ajax({
                    method: 'GET',
                    url: 'https://fr.wikipedia.org/w/api.php?',
                    data: {
                        "action": "query",
                        "list": "search",
                        "srsearch": addr,
                        "srlimit": "1",
                        "format": "json",
                        "formatversion": "2"
                    }
                }).done(function (response) {

                    console.log(response);

                    // Remove load animation
                    $('#load').remove();

                    $('#chat').append('<div class="cont-chat">' +
                        '<img class="left" src="../static/img/papybot.png" alt="Avatar">' +
                        '<p>' + answersList[1] + '</p></div>');
                }).fail(function (error) {

                    // Display error message in the console
                    console.error(error);
                });
            }
        }).fail(function (error) {

            // Display error message in the console
            console.error(error);
        });
    });
});