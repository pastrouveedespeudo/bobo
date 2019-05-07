{% include "navebarre.html" %}

{% block content %}
{% endblock %}

  <!-- Masthead -->
  <header class="masthead">
  
    <div class="container h-100">
      <div class="row h-100 align-items-center justify-content-center text-center">
        <div class="col-lg-10 align-self-end">
        
          <h1 class="text-uppercase text-white font-weight-bold">Choisis TA mode</h1>
          <hr class="divider my-4">
          
        </div>
        
        <div class="col-lg-8 align-self-baseline">
        {% csrf_token %}
          <p class="text-white-75 font-weight-light mb-5"></p>
          <a class="btn btn-primary btn-xl js-scroll-trigger" onclick="button1()" href="#about">Pour les vetements</a>
          <a class="btn btn-primary btn-xl js-scroll-trigger" onclick="button2()"  href="#about">Pour la coupe de cheveux</a>
          
        </div>

        
      </div>
    </div>
  </header>




  <style>
    #containner {margin: 0px auto; width: 400px; height: 400px;}
    #videoElement {width: 400px; height: 400px; position:relative;}
    #patron{margin-left:105px; margin-top:100px; width: 200px; height: 200px;
      border: 3px solid red; border-radius:50%; position:absolute; z-index:1;}
  </style>



    <script>
        OPTION = [2]
        
        function button1(){
            
            document.getElementById("patron").style.width = '90px';
            document.getElementById("patron").style.height = '90px';
            document.getElementById("patron").style.marginLeft = '160px';
            document.getElementById("patron").style.marginTop = '50px';
            document.getElementById("patron").style.position = 'absolute';
            document.getElementById("patron").style.zIndex = '1';
            document.getElementById("hidden").innerHTML = '<input type="HIDDEN" value="habit" name="format" id="hidden">'
            OPTION.push(1);
            var a = OPTION[OPTION.length-1];
            var b = document.getElementById("hidden").value = OPTION[OPTION.length-1];
            
        };
        function button2(){
            document.getElementById("hidden").innerHTML = '<input type="HIDDEN" value="cheveux" name="format" id="hidden">'
            document.getElementById("patron").style.width = '200px';
            document.getElementById("patron").style.height = '200px';
            document.getElementById("patron").style.marginLeft = '105px';
            document.getElementById("patron").style.marginTop = '100px';
            document.getElementById("patron").style.position = 'absolute';
            document.getElementById("patron").style.zIndex = '1';
            OPTION.push(2)
            
            var a = OPTION[OPTION.length-1];
            var b = document.getElementById("hidden").value = OPTION[OPTION.length-1];
        };  
        function photo(){
            document.getElementById("patron").style.width = '0px';
            document.getElementById("patron").style.height = '0px';
            document.getElementById("patron").style.marginLeft = '-600px';
        }
    </script>



  <!-- About Section -->
  <section class="page-section bg-primary" id="about">
    <div class="container">


      <div class="row justify-content-center">
        <div class="col-lg-8 text-center">
          <h2 class="text-white mt-0">Veuillez mettre votre visage dans le cadre</h2>
        

          <div id="containner">
              <div id="patron"></div>
              <video autoplay="true" id="videoElement"></video>
          </div>

        
  
          {% csrf_token %}
          <form action="photo" method="POST" id="cc">
          {% csrf_token %}
          
              <input type="hidden" name="csrfmiddlewaretoken"
              value="hCsDoCbOI5WQh4CYKUQEPwkbTgEittUJgieBqNKPJE37pvwjtXsFpi1CzMa9qEs1">
              {% csrf_token %}
              
              <input type="HIDDEN" value="cheveux" name="format" id="hidden">
              {% csrf_token %}
    
              

            {% csrf_token %}
            <style>#emplacement{text-align:center;}</style>

            
            <div id='prems'>
              <input type='button' onclick="tuto()"
               value="Si ce n'est pas votre première fois laissez tomber sinon cliqué ;)"
               size=50px>
              <br>
            </div>

            
            <br><br>
            
            <input type="submit" id="yo" value="Prendre la photo" onclick="photo()"<a class="btn btn-light btn-xl js-scroll-trigger">

            {% csrf_token %}
            </a>
            {% csrf_token %}
              
          </form>
      
          
        </div>
      </div>
    </div>
  </section>
 


    <script>
      function tuto(){
        alert('coucou');
        document.getElementById('prems').innerHTML = '';
        document.getElementById('prems').innerHTML = '<input type="text" id="emplacement" placeholder="Svp dites nous le nom de vote ordinateur" size=50px;>'
        document.getElementById('prems').innerHTML = "<br><input type='button' value='je sais comment faire' onclick='oui()'>&nbsp;&nbsp;&nbsp;<input type='button' value='je ne sais pas comment faire' onclick='non()'>"

        }


      function oui(){

        document.getElementById('prems').innerHTML = '';
        document.getElementById('prems').innerHTML = '<input type="text" id="emplacement" placeholder="Svp dites nous le nom de vote ordinateur" size=50px;>'


        }

      function non(){
        document.getElementById('prems').innerHTML = '';
        document.getElementById('prems').innerHTML = " <center><strong> Ouvrez un dossier, récupérez le nom d'en haut</strong></center><img src='/static/img/portfolio/1.png'><br><br><input type='button' value='ok' onclick='oui()'>";
        
        }
    </script>




    <script>
    var video = document.querySelector("#videoElement");
    if (navigator.mediaDevices.getUserMedia) {     
        navigator.mediaDevices.getUserMedia({video: true})
      .then(function(stream) {
        video.srcObject = stream;
      })
      .catch(function(err0r) {
        console.log("Something went wrong!");
      });
    }
    </script>


{% include "bottom_page.html" %}

{% block content2 %}
{% endblock content2%}








</html>
