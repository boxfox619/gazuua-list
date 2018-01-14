$( document ).ready(function() {
  loadRecommends();
  updateCoins();
});

function loadRecommends(){
  $.ajax({url: "/recommends", success: function(result){
    $('#ranking .list>li').remove();
    for (i = 0; i < result.length; i++) {
      let coin = result[i];
      $('#ranking .list').append(createRecommendElement(coin));
    }

  }});
}

function updateCoins(){
  loadRecommends();
  $.ajax({url: "/coins", success: function(result){
    $('#all-coins tbody tr').remove();
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

function createRecommendElement(coin){
  return ('<li>'
    + '<div class="item">'
      + '<img class="card" src="https://files.coinmarketcap.com/static/img/coins/32x32/'+coin['name']+'.png"/>'
      + '<div>'+coin['name']+'</div>'
      + '<div>'+coin['rate']+'</div>'
    + '</div>'
  + '</li>')

}
