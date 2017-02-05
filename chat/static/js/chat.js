$(function() {
    // WebSockets settings
    $('#handle').val(username);
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);

    chatsock.onmessage = function(message) {
        var data = JSON.parse(message.data);
        $('#chat').append(
            '<div class="col s4">' + data.handle + '</div>' +
            '<div class="col s8">' + data.message + ' </div>');
    };

    $("#chatform").on("submit", function(event) {
        var message = {
            handle: $('#handle').val(),
            message: $('#message').val(),
        }
        chatsock.send(JSON.stringify(message));
        $("#message").val('').focus();
        if ($('#handle').val() != '') {
            $('#handle').attr('disabled', 'disabled');
        }
        return false;
    });
});
