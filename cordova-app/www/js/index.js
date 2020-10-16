
var app = {
    // Application Constructor
    initialize: function() {
    
        var url = "https://domuapp.free.beeceptor.com/APN/02353060210000";
        
        $("#loadProperty").click(function(){
            $.ajax({
                url: url,
                success: handleResult
            }); // use promises
            
            // add cordova progress indicator https://www.npmjs.com/package/cordova-plugin-progress-indicator

            function handleResult(result){
                $("#propimage").attr("src", result.Property_Photo_Url);
                
                //http://responsiveimg.com/
                $("#propimage").responsiveImg();
                
                $("#address").text("Address:" + result.PARCEL_ADD) ;
                $("#city").text("City:" + result.CITY);
                $("#zip").text("Zip:" + result.TAXPAYER_Z);
                $("#age").text("Age:" + result.AGE);
                $("#size").text("Size:" + result.LAND_SQ_FT);
                $("#value").text("Assessed Value:" + "$" +result.TOTAL_VALU);
                $("#taxpayer").text("Taxpayer:" + result.TAXPAYER_NAME);
                
            }
        });
        
        $("#randomProperty").click(function(){
            $.ajax({
                url: url,
                success: handleResult
            }); // use promises
            
            // add cordova progress indicator https://www.npmjs.com/package/cordova-plugin-progress-indicator

            function handleResult(result){

                $("#propimage").attr("src", result.Property_Photo_Url);
                
                //http://responsiveimg.com/
                $("#propimage").responsiveImg();
                
                $("#address").text("Address:" + result.PARCEL_ADD) ;
                $("#city").text(result.CITY);
            }
        });        
    },
};

app.initialize();

// based on https://gist.github.com/miguelmota/5b67e03845d840c949c4
