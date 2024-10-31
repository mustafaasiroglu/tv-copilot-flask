//Initiate jQuery on load.
$(function() {
  //Translate text with flask route
  $("#send").on("click", function(e) {
    e.preventDefault();
    var oinput = document.getElementById("text-to-send");
    oinput.disabled = true;
    //hide introcards div
    document.getElementById("introcards").style.display = "none";

    var translateVal = oinput.value;
    var translateRequest = { 'text': translateVal }

    var div = document.createElement("div");
    div.textContent = translateVal;
    div.className = "message_user";
    document.getElementById("messages").appendChild(div);

    if (translateVal !== "") {
      $.ajax({
        url: '/generate',
        method: 'POST',
        headers: {
            'Content-Type':'application/json'
        },
        dataType: 'json',
        data: JSON.stringify(translateRequest),
        success: function(data) {
            //messages id div içine yeni bir div ekle içinde metin olsun.
            var response = data['choices'][0]['message']['content'];
            var response2 = response.replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank">$1</a>');
            var div = document.createElement("div");
            div.innerHTML = response2;
            div.className = "message_assistant";
            document.getElementById("messages").appendChild(div);
            var objDiv = document.getElementById("messages");
            //objDiv.scrollTop = objDiv.scrollHeight;
            objDiv.lastElementChild.scrollIntoView({behavior: "smooth", block: "end", inline: "nearest"})
            //document.getElementById("messages").scrollIntoView({behavior: "smooth", block: "start", inline: "nearest"})

            //call tts function
            let inputText = response.replace(/https?:\/\/[^\s]+/g, '').replace(/([\u2700-\u27BF]|[\uE000-\uF8FF]|\uD83C[\uDC00-\uDFFF]|\uD83D[\uDC00-\uDFFF]|[\u2011-\u26FF]|\uD83E[\uDD10-\uDDFF])/g, '');

            readTextLoudly(inputText);

            oinput.value = "";
            oinput.disabled = false;
            oinput.focus();
            document.getElementById("text-to-send").focus();
        }
      });
    };
    //auto scroll to bottom of messages smoothly
    var objDiv = document.getElementById("messages");
    //latest child element
    //objDiv.scrollTop = objDiv.scrollHeight;
    objDiv.lastElementChild.scrollIntoView({behavior: "smooth", block: "end", inline: "nearest"})

    
  });

  $(".ccard").on("click", function(e) {
      ccard = e.target;
      var oinput = document.getElementById("text-to-send");
      oinput.value = ccard.innerHTML;
      document.getElementById("send").disabled = false;
  });
 

//focus on input on load
document.getElementById("text-to-send").focus();

});


//function to read text loudly
function readTextLoudly(text) {

  let inputText = text.replace(/https?:\/\/[^\s]+/g, '').replace(/([\u2700-\u27BF]|[\uE000-\uF8FF]|\uD83C[\uDC00-\uDFFF]|\uD83D[\uDC00-\uDFFF]|[\u2011-\u26FF]|\uD83E[\uDD10-\uDDFF])/g, '');

  synthesizer.speakTextAsync(
      inputText,
      function (result) {
        window.console.log(result);
        // synthesizer.close();
        // synthesizer = undefined;
      },
      function (err) {
        window.console.log(err);
        // synthesizer.close();
        // synthesizer = undefined;
  });
}

document.addEventListener("DOMContentLoaded", function() {

  // Get the input field and send button
  var inputField = document.getElementById("text-to-send");
  var sendButton = document.getElementById("send");
  sendButton.disabled = true

  text = document.getElementById("messages").firstElementChild.textContent;
  readTextLoudly(text);

  // Add event listener to input field
  inputField.addEventListener("input", function() {
      if (inputField.value.length > 0) {
          sendButton.disabled = false;
      } else {
          sendButton.disabled = true;
      }
  });
});

