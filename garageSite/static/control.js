function receivedResponse(result) {
    console.log(result);
}
function doorControl(action) {
    dataForServer = {"action":action.toString()};
    $.ajax({
        type: "POST",
        url: "/doorControl",
        data: JSON.stringify(dataForServer),
        contentType: "application/json",
        dataType: "json",
        success: function(result) {
            receivedResponse(result);
        }
    });
}