% import model
% rebase("base.tpl")






  <h2>{{igra.pravilni_del_gesla()}}</h2>

  Nepravilni ugibi: <b>{{igra.nepravilni_ugibi()}}</b><br>

  

  <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">

  % if stanje == model.ZMAGA:
  <h1> OMG! Uganil si mojo besedo, a sm loh tvoj frend? </h1>
  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % elif stanje == model.PORAZ:
  <h1> Jao, majmun nesposoben... Moja beseda je bila <b>{{igra.geslo}}</b> </h1>
  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % else:
  <form action="/igra/{{id_igre}}/" method="post">
   Črka: <input type="text" name="crka"> 
    <button type="submit">Nova igra</button>
  </form>
