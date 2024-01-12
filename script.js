$("#buttonAuthor").click(function(){
    $.ajax({
        url: "/api/author",
        type: "GET",
        dataType: "json",
        success: function(data) {
            $("#pAuthor").text(data.name + ", " + data.indeks);
    }});
});