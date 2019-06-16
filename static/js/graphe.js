//Global variable
LISTE_AJAX = []
LISTE_AJAX_TYPE_GRAPHE = []


//we define the city to push into global array.
//We define type of graphe we want too
//and call to the views the city to search
//by Ajax style

//Choose Lyon city and graphe
function lyon(){
  document.getElementById('section_graphe').style.display = 'block';
  LISTE_AJAX.push('lyon')
};


//Choose Paris city and graphe
function paris(){
  document.getElementById('section_graphe').style.display = 'block';
  LISTE_AJAX.push('paris')
};


//Choose Marseille city and graphe
function marseille(){
  document.getElementById('section_graphe').style.display = 'block';
  LISTE_AJAX.push('marseille')
  };


//We call the city and graphe to back
function graphe(legraphe){
  LISTE_AJAX_TYPE_GRAPHE.push(legraphe)
     document.getElementById('graphique1').innerHTML = '';
     jQuery.ajax({
       data:{
           'csrfmiddlewaretoken': '{{csrf_token}}' , 
           'city':LISTE_AJAX[LISTE_AJAX.length - 1],
           'graph':LISTE_AJAX_TYPE_GRAPHE[LISTE_AJAX_TYPE_GRAPHE.length - 1]},

       
              type:"POST",
              url:"/polution/graphe"
          })
          .done(function(data){
              if (data.error){
                  jQuery("#monCadreAlert").text(data.error);
                  jQuery("#is_save");
                  
                  
              }
              else{
                  jQuery("#is_save").html(data.data);
                  jQuery("#monCadreAlert");
             
                  document.getElementById('graphique1').innerHTML = "<img src = '/static/popo/" +
                                                                    data +
                                                                    "'>"

       };
              
   });
};
