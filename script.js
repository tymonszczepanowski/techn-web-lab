$("#button-author").click(function(){
    $.ajax({
        url: "/api/data",
        type: "GET",
        dataType: "json",
        success: function(data) {
            $("#data").text(data.name + ", " + data.indeks);
    }});
});