function receivedResponse(result) {
    console.log(result)
    document.getElementById("alertplaceholder").innerHTML += '<div class="alert alert-success alert-dismissible fade show" role="alert">' + result['status'].toString() + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'
}
function doorControl(action) {
    dataForServer = {"action":action.toString()};
    $.ajax({
        type: "POST",
        url: "./doorControl",
        data: JSON.stringify(dataForServer),
        contentType: "application/json",
        dataType: "json",
        success: function(result) {
            receivedResponse(result);
        }
    });
}