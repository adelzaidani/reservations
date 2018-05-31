$(document).ready(function(){
     $("#recherche").click(function(){
        var URL="https://api.theatredelaville-paris.com/events";
        $.ajax({
            dataType:"json",
            url:URL,
            success:success
        });
        function success(e){
            var result ="";
            $.each(e,function(index,value)
            { result+="<h2>"+value.title+"</h2>";
              result+="<p>"+ value.description + "</p>";
              result+="<p>--------------------------</p>";
            });
            $('#result').html(result);
        };

     });


});