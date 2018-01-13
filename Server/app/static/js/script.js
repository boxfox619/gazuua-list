$( document ).ready(function() {
  loadRecommends();
  updateCoins();
});

function loadRecommends(){
  $.ajax({url: "/recommends", success: function(result){
    $('#recommend-coins tr').remove();
    for (i = 0; i < result.length; i++) {
      let coin = result[i];
      $('#recommend-coins').append(createElement(coin));
    }

  }});
}

function updateCoins(){
  loadRecommends();
  $.ajax({url: "/coins", success: function(result){
    $('#all-coins tr').remove();
    for (i = 0; i < result.length; i++) {
      let coin = result[i];
      $('#all-coins').append(createElement(coin));
    }
    setTimeout(updateCoins, 3000)
  }});
}

function createElement(coin){
  return ('<tr>'
    + '<td></td>'
    + '<td>'+coin['_id']+'</td>'
    + '<td>'+coin['name']+'</td>'
    + '<td>'+coin['rate']+'</td>'
    + '</tr>')
}
