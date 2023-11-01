$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $.each(data.results, function (i, result) {
    $('UL#list_movies').append('<li>' + result.title + '</li>');
  });
});
