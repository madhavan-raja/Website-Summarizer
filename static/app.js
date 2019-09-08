input.addEventListener("keyup", function(event)
{
    if (event.keyCode === 13)
    {
        event.preventDefault();
        convert();
    }
});

function convert()
{
    document.getElementById("output").value = "Loading...";

    var xhttp = new XMLHttpRequest();
    var url = 'http://localhost:5000/main';

    xhttp.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
            document.getElementById("output").value = xhttp.responseText;
    };

    input_text = document.getElementById("input").value;
    xhttp.open('POST', url, true);
    xhttp.send(JSON.stringify({"input_text": input_text}));
}