//Here we displaying exemple when user get click on an input.
// ---> Visual function <--- en gros on met une exemple quand le mec appuie


function stop(titre, div){
    
    document.getElementById(titre)
    if(div == '11'){
      document.getElementById(div).innerHTML = '<i>Par exemple Emma</i>'
    }
    else if(div == '22'){
      document.getElementById(div).innerHTML = '<i>Par exemple Emma@hotmail.fr</i>'
    }
    else if(div == '33'){
      document.getElementById(div).innerHTML = '<i>Confirme le pour etre sur !</i>'
    }
    else if(div == '44'){
      document.getElementById(div).innerHTML = '<i>Nous te conseillons de mettre des chiffres et des majuscules</i>'
    };
};


//Here we put an espace when user have finish to enter his info.
// ---> Visual function <--- on detruit l'exemple

function start(titre, div){
    document.getElementById(div).innerHTML = '&nbsp;';
};


//Here we change title color when user get his informations.
// ---> Visual function <--- en gros on change le titre de couleur selon
//l'input

function myFunction(titre){
    
    if(titre == '1'){
      document.getElementById(titre).style.color = 'green';
      }
    else if(titre == '2'){
      document.getElementById(titre).style.color = 'green';
    }
    else if(titre == '3'){
      document.getElementById(titre).style.color = 'green';
    };
};


//Function for a bug who is done.
//We let it in case

var c = 0
function myFunction2(titre){
    if (c == 0){
      c += 1
    }
    else{
      document.getElementById(titre).style.color = 'green';
    };
};
