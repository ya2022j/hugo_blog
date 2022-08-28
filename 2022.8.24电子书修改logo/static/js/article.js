
$(function(){
    $(".search-reveal").click(function(){
        let status = $(".search-pc").css("display");
        if (status == null || status == "none") {
            $(".search-pc").css("display","block");
        } else {
            $(".search-pc").css("display","none");
        }
    });

    $("#pull").click(function(){
        let status = $(".col.left-column").css("display");
        if (status == null || status == "none") {
            $(".col.left-column").css("display","block");
        } else {
            $(".col.left-column").css("display","none");
        }
    });

});