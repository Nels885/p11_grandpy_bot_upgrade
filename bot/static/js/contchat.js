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