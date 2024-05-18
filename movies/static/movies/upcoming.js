let currentPage= 1;

function load_proximo(pageNumber=1 ){
    fetch(`/proximo2/?page=${pageNumber}`)
        .then(response => response.json())
        .then(movies => {
            console.log(movies);
            const container = document.getElementById('upcoming-cartelera-view');
            container.innerHTML = '';
            movies.forEach(movie => {
                const movieelement = document.createElement('div');
                movieelement.innerHTML= `
                <h4>${movie.fields.title}</h4>
                <img src="${movie.fields.image_url}" alt="${movie.fields.title}" style="width:200px; height:250px;">
                
            `; //add imageurl
                container.appendChild(movieelement);
            });
            document.querySelector('#page-indicator').textContent = 'Página ' + pageNumber;
            currentPage = pageNumber;
        });
}

document.addEventListener('DOMContentLoaded', function() {
    load_proximo(currentPage);
    document.querySelector('.img').addEventListener('click', handleMovieImageClick);
});

