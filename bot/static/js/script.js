$(function () {
    $('form').on('submit', function (e) {
        e.preventDefault();
        const chat = $('#chat');

        // hide the message "Posez votre question à GrandPy Bot !"
        // $('#msgPres').hide();

        // Adding the user message in the chat window
        const msgUser = $('#content').val();
        chat.append('<div class="cont-chat darker text-right">' +
            '<img class="right" src="../static/img/invite.png" alt="Avatar">' +
            '<p>' + msgUser + '</p></div>');

        // Adding load animation
        chat.append('<div class="cont-chat text-center" id="load">' +
            '<div id="loader"></div></div>');

        // AJAX requests to the post and displays the PapyBot message according to the user message
        $.ajax({
            method: 'POST',
            url: '/',
            data: {content: msgUser},
        }).done(function(parameters) {

            $.ajax({
                method: 'GET',
                url: 'https://fr.wikipedia.org/w/api.php?',
                data : parameters
            }).done(function(response) {

                $.ajax({
                    method: 'POST',
                    url: '/wiki/',
                    data: response,
                }).done(function(msgsBot) {
                    // Remove load animation
                    $('#load').remove();

                    // Display the messages of GrandyBot
                    const answersList = JSON.parse(msgsBot).message;
                    answersList.forEach(function (answer) {
                        $('#chat').append('<div class="cont-chat">' +
                            '<img class="left" src="../static/img/papybot.png" alt="Avatar">' +
                            '<p>' + answer + '</p></div>');
                    });
                }).fail(function(error) {

                    // Display error message in the console
                    console.error(error);
                });
            }).fail(function(error) {

                // Display error message in the console
                console.error(error);
            });
        }).fail(function(error) {

            // Display error message in the console
            console.error(error);
        });
    });
});