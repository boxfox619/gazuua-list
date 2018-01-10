$( document ).ready(function() {
  loadRecommends();
  updateCoins();
});

function loadRecommends(){
  $.ajax({url: "/recommends", success: function(result){
    console.log(result);
  }});
}

function updateCoins(){
  $.ajax({url: "/coins", success: function(result){
    console.log(result);

    setTimeout(updateCoins, 3000)
  }});
}
