// Class for display the answer of GrandpyBot or Anonymous
class ContChat {
    constructor(chatClass, avatar, avatClass) {
        this.chatClass = chatClass;
        this.avatar = avatar;
        this.avatClass = avatClass;
    }

    send(answer) {
        // Remove load animation
        $('#load').remove();
        chat.append('<div class="row"><div class="' + this.chatClass + '">' +
            '<img class="' + this.avatClass + '" src="../static/img/' + this.avatar + '" alt="Avatar"><p>' + answer +
            '</p></div></div>');
        $('html, body').animate({
            scrollTop: $('#addMsg').offset().top
        }, 'slow');
    }

    add(answer) {
        // Remove load animation
        $('#load').remove();
        chat.append('<div class="row"><div class="' + this.chatClass + '">' +
            '<img class="' + this.avatClass + '" src="../static/img/' + this.avatar + '" alt="Avatar">' + answer +
            '</div></div>');
        $('html, body').animate({
            scrollTop: $('#addMsg').offset().top
        }, 'slow');
    }
}


// Function for adding load animation
function loadBot() {
    chat.append('<div class="row"><div class="cont-chat text-center col-lg-12" id="load">' +
        '<div id="loader"></div></div></div>');
}


// Function of the bot message that includes address and weather
function resultBot(response) {
    // adding weather for the desired location
    let weather = response['weather'];
    if (weather) {
        console.log('[BACK END] WEATHER TEMP : ' + weather['temp']);
        chatBot.add(
            '<p>' + response['answers'][0] +
            '<br>Vous trouvez ci-dessous la météo pour cette adresse:</p>' +
            '<p><img class="float-right" src="' + weather['icon'] + '" alt="weather" width="20%" />' +
            '<strong>- Température:</strong> ' + weather['temp'] + '<br>' +
            '<strong>- couverture nuageuse:</strong> ' + weather['desc'] + '<br>' +
            '<strong>- Humidité de l\'air:</strong> ' + weather['humidity'] + ' %<br>' +
            '<strong>- Pression atmosphérique:</strong> ' + weather['pressure'] + ' mb<br>' +
            '<strong>- Vitesse du vent:</strong> ' + weather['speed_wind'] + ' m/s</p>'
        );
    } else {
        chatBot.send(response['answers'][0] + '<br>Désolé, nous n\'avons pas pu trouver la météo pour ce lieu.');
    }

}