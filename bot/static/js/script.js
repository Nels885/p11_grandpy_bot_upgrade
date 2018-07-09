$(function(){
    $('form').on('submit', function(e) {
        e.preventDefault();

        // hide the message "Posez votre question à GrandPy Bot !"
        $('#msgPres').hide();

        // Adding the user message in the chat window
        var msgUser = $('#content').val();
        $('#chat').append('<div class="cont-chat darker text-right">' +
            '<img class="right" src="../static/img/invite.png" alt="Avatar">' +
            '<p>' + msgUser + '</p></div>');

        // AJAX requests to the post and displays the PapyBot message according to the user message
        $.ajax({
            url: '/post/',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response){

                // Display the messages of GrandyBot
                var obj = JSON.parse(response);
                answersList = obj.message;
                console.log(obj.message);
                answersList.forEach(function(answer) {
                    $('#chat').append('<div class="cont-chat">' +
                        '<img class="left" src="../static/img/papybot.png" alt="Avatar">' +
                        '<p>' + answer + '</p></div>');
                });
                },
            error: function(error){

                // Display error message in the console
                console.log(error);
            }
        });
    });
});