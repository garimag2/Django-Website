// We define a variable 'text_box' for storing the html code structure of message that is displayed in the chat box.
var text_box = '<div class="card-panel right" style="width: 75%; position: relative">' +
        '<div style="position: absolute; top: 0; left:3px; font-weight: bolder" class="title">{sender}</div>' + 
        '{message}' +
        '</div>';
function scrolltoend() {
    $('#board').stop().animate({
        scrollTop: $('#board')[0].scrollHeight
    }, 800);
}
// Send takes three args: sender, receiver, message. sender & receiver are ids of users, and message is the text to be sent.
function send(sender, receiver, message) {
    //POST to '/api/messages', the data in JSON string format
    $.post('/myapp/messages/api/', '{"sender": "'+ sender +'", "receiver": "'+ receiver +'","message": "'+ message +'" }', function (data) {
        console.log(data);
        var box = text_box.replace('{sender}', "You"); // Replace the text '{sender}' with 'You'
        box = box.replace('{message}', message); // Replace the text '{message}' with the message that has been sent.
        $('#board').append(box); // Render the message inside the chat-box by appending it at the end.
        scrolltoend(); // Scroll to the bottom of he chat-box
    })
}
// Receive function sends a GET request to '/api/messages/<sender_id>/<receiver_id>' to get the list of messages. 
function receive() {
    // 'sender_id' and 'receiver_id' are global variable declared in the messages.html, which contains the ids of the users.
    console.log("receive!!")
    $.get('/myapp/messages/api/'+ sender_id + '/' + receiver_id, function (data) {
        console.log(data.length);
        var oldCountMessages = $("#board > div").length;
        console.log("Hello")
        console.log(oldCountMessages + " " + sender_id + " "  + receiver_id);
        if (data.length !== 0)
        {
            for(var i=0;i<data.length;i++) {
                console.log(data[i]);
                var box = text_box.replace('{sender}', data[i].sender);
                box = box.replace('{message}', data[i].message);
                box = box.replace('right', 'left blue lighten-5');
                if ((i+1) > oldCountMessages) {
                    // Initializing newMessageIndex with the new message index, to show it.
                    newMessageIndex = i;
                    $('#board').append(box);
                }
                //$('#board').html("");
                scrolltoend();
            }
        }
    })
}

