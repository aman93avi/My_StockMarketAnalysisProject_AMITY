// Enable panel clickable
$(document).ready(function(){

    $("#NIFTY").click(function(e){
        e.preventDefault();
        window.location = "exchanges/NSE";
    });

    $("#SENSEX").click(function(e){
        e.preventDefault();
        window.location = "exchanges/BSE";
    });

});



// Periodic refresh
(function(){

  function updateStockDomestic(){
       // List of symbols to be queried to google finance!
       //  "SHA:000001", "INDEXSTOXX:SX5E", "TPE:TAIEX", "INDEXEURO:PX1"
       var SYMBOLS = ['NSE:NIFTY','INDEXBOM:SENSEX'];
       var placeholders = ["#nifty_quote", "#sensex_quote"]
       var API_URL = "http://finance.google.com/finance/info?client=ig&q="
       var final_url = API_URL+SYMBOLS.join(',')
       $.ajax({
        url: final_url,
        dataType: 'jsonp',
        success: function(data){
            $.each(data, function(index, object){
                $.each(object, function(key , value){
                    //console.log(key+ "  : "+ value);
                    if( key === 'c'){
                        if(value.indexOf('-') === -1 ){
                            $(placeholders[index]).parent().addClass("quoteboard-gain");
                            $(placeholders[index]).parent().find("span").toggleClass("glyphicon-circle-arrow-up")
                            $(placeholders[index]+"_change").html(value);
                        }else{
                            $(placeholders[index]).parent().addClass("quoteboard-loss")
                             $(placeholders[index]).parent().find("span").toggleClass("glyphicon-circle-arrow-down")
                             $(placeholders[index]+"_change").html(value);
                        }
                       }
                    if(key === 'cp'){
                        $(placeholders[index]+"_percentchange").html(value);
                    }

                    if( key === 'l_fix'){
                        $(placeholders[index]).html(value);
                    } }) }) } });
     }// end of func

            updateStockDomestic();
            setInterval(updateStockDomestic, 1000);

        }
)();