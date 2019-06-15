
//Here we call database and analysa2.py for lyon

jQuery("#lyon").on("click", function(e){

    //we "raise" the pred div, display you choose lyon city
    //and display the loading logo

    document.getElementById('pred').innerHTML = ""
    document.getElementById('choix').innerHTML = 'Vous avez choisis Lyon';
    document.getElementById('chargement').style.display = "block";

    jQuery.ajax({
        data:{
            'lyon':'lyon',
        },
        type:"POST",
        url:"/polution/prediction"
    })
    .done(function(data){
        if (data.error){
            jQuery("#monCadreAlert").text(data.error);
            jQuery("#is_save"); 
        }
        else{
            jQuery("#is_save").html(data.data);
            jQuery("#monCadreAlert");

            document.getElementById('chargement').style.display = "none";      
            
            if (data == "pas de donn\u00e9e"){
                document.getElementById('pred').innerHTML = "<br><br><strong>pas de donn\u00e9e</strong>";
            }
            else{
              
              document.getElementById('pred').innerHTML = '<br><br>' +
                                                          'Nous pensons que le taux de polution est de: '+
                                                          '<strong>' +
                                                          data +
                                                          ' AQI</strong>';
            };      
        };
        
    });
});




//Here we call database and analysa2.py for paris
jQuery("#paris").on("click", function(e){


    //we "raise" the pred div, display you choose paris city
    //and display the loading logo
    document.getElementById('choix').innerHTML = 'Vous avez choisis Paris';
    document.getElementById('chargement').style.display = "block";
    document.getElementById('pred').innerHTML = ""
    
    jQuery.ajax({
        data:{
            'paris':'paris',
        },
        type:"POST",
        url:"/polution/prediction"
    })
    .done(function(data){
        if (data.error){
            jQuery("#monCadreAlert").text(data.error);
            jQuery("#is_save"); 
        }
        else{
            jQuery("#is_save").html(data.data);
            jQuery("#monCadreAlert");

            document.getElementById('chargement').style.display = "none";
            
          if (data == "pas de donn\u00e9e"){
                document.getElementById('pred').innerHTML = "<br><br><strong>pas de donn\u00e9e</strong>";
            }
            else{
            document.getElementById('pred').innerHTML = '<br><br>' +
                                                        'Nous pensons que le taux de polution est de : '+
                                                        '<strong>' +
                                                        data +
                                                        '</strong>';

            };            
        };
    });
});




//Here we call database and analysa2.py for marseille
jQuery("#marseille").on("click", function(e){


    //we "raise" the pred div, display you choose marseille city
    //and display the loading logo
    document.getElementById('choix').innerHTML = 'Vous avez choisis Marseille';
    document.getElementById('chargement').style.display = "block";
    document.getElementById('pred').innerHTML = ""
    
    jQuery.ajax({
        data:{
            'marseille':'marseille',
        },
        type:"POST",
        url:"/polution/prediction"
    })
    .done(function(data){
        if (data.error){
            jQuery("#monCadreAlert").text(data.error);
            jQuery("#is_save"); 
        }
        else{
            jQuery("#is_save").html(data.data);
            jQuery("#monCadreAlert");
            
            document.getElementById('chargement').style.display = "none";
            
          if (data == "pas de donn\u00e9e"){
                document.getElementById('pred').innerHTML = "<br><br><strong>pas de donn\u00e9e</strong>";
            }

            else{
              document.getElementById('pred').innerHTML = '<br><br>' +
                                                        'Nous pensons que le taux de polution est de : '+
                                                        '<strong>' +
                                                        data +
                                                        '</strong>';
            };            
        }; 
    });
});




