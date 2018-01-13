$( document ).ready(function() {
  loadRecommends();
  updateCoins();
});

function loadRecommends(){
  $.ajax({url: "/recommends", success: function(result){
    $('#recommend-coins>*:not(first-child)').remove();
    for (i = 0; i < result.length; i++) {
      let coin = result[i];
      $('#recommend-coins').append(createElement(coin));
    }

  }});
}

function updateCoins(){
  loadRecommends();
  $.ajax({url: "/coins", success: function(result){
    $('#all-coins>*:not(first-child)').remove();
    for (i = 0; i < result.length; i++) {
      let coin = result[i];
      $('#all-coins').append(createElement(coin));
    }
    setTimeout(updateCoins, 3000)
  }});
}

function createElement(coin){
  return ('<tr>'
    + '<th></th>'
    + '<th>'+coin['_id']+'</th>'
    + '<th>'+coin['name']+'</th>'
    + '<th>'+coin['rate']+'</th>'
    + '</tr>')
}
