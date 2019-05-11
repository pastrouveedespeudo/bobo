
{% include "navebarre.html" %}
{% block content %}
{% endblock %}


 <!-- Masthead -->
  <header class="masthead">
    <div class="container h-100">
      <div class="row h-100 align-items-center justify-content-center text-center">
        <div class="col-lg-10 align-self-end">
        <br><br>

           <style>#autre{margin-left:-965px;;margin-top:-100px;}</style>

           <h1 class="text-uppercase text-white font-weight-bold">Coté administrateur !</h1>


  
          <style>#h{font:Serif; color:white;}</style>
          <br>

        
           <hr class="divider my-4">
          </div>

          
          <div class="col-lg-8 align-self-baseline">
             <p class="text-white-75 font-weight-light mb-5"></p>
          
            <div id='interface'>

                <input type='button' value='voir la database' onclick='database()'>

            </div>



            <script>

                function database(){
                    
                    document.getElementById('interface').innerHTML = ''
                    document.getElementById('interface').innerHTML = "<input type='button' value='voir la database femme' onclick='database()'> &nbsp;&nbsp;" +
                                                                    "<input type='button' value='voir la database homme' onclick='database()'>"



                    }

            </script>


            
            <br><br>
            <input type='button' value='revenir en arriere' onclick='arriere()'>

            
            <script>
            
                function arriere(){
                    document.location.href="/administrateur/mode"; 
                }
            </script>

            
        
      </div>
    </div>
  </div>
</header>





































