
var app = {
    // Application Constructor
    initialize: function() {
    
        var url = "https://run.mocky.io/v3/1d2a2ece-c332-4b37-9d1d-49c726a0ca54";
        
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
