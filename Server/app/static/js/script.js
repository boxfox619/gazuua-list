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
  let rate = coin['rate'];
  rate = rate.toFixed(2);
  return ('<tr>'
    + '<td></td>'
    + '<td>'+coin['_id']+'</td>'
    + '<td>'+coin['name']+'</td>'
    + '<td>'+rate+'%</td>'
    + '</tr>')
}

function createRecommendElement(coin){
  let rate = coin['rate'];
  rate = rate.toFixed(2);
  return ('<li>'
    + '<div class="item">'
      + '<img class="card" onError="this.onerror=null;this.src=\'/static/img/icon-original.png\';" src="https://files.coinmarketcap.com/static/img/coins/128x128/'+String(coin['name']).toLowerCase().replace(/ /gi, "-")+'.png"/>'
      + '<div>'+coin['name']+'</div>'
      + '<div>'+rate+'%</div>'
    + '</div>'
  + '</li>')

}
