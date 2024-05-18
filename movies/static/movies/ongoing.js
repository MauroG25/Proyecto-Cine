let currentPage = 1;
function load_cartelera(pageNumber = 1) {
    fetch(`/cartelera2/?page=${pageNumber}`)
        .then(response => response.json())
        .then(movies => {
            console.log(movies);
            const container = document.getElementById('ongoing-cartelera-view');
            
            //cleaning the content to get a good pagination
            container.innerHTML = '';
            
            movies.forEach(movie => {
                const movieElement = document.createElement('div');
                movieElement.innerHTML= `
                <h4>${movie.fields.title}</h4>
                <img src="${movie.fields.image_url}" alt="${movie.fields.title}" style="width:200px; height:250px;">
                `;
                container.appendChild(movieElement);
            });
            document.querySelector('#page-indicator').textContent = 'Página ' + pageNumber;
            currentPage = pageNumber;
        });
}


document.addEventListener('DOMContentLoaded', function() {
    load_cartelera(currentPage);
    document.querySelector('.movie-image').addEventListener('click', handleMovieImageClick);
});