document.addEventListener('DOMContentLoaded', function() {
    
    fetch('/bestongoing/')
        .then(response => response.json())
        .then(movies => {
            const container = document.getElementById('bestongoing-view');
            movies.forEach(movie => {
                const movieelement = document.createElement('div');
                movieelement.innerHTML= `
                <h4>${movie.fields.title}</h4>
                <img src="${movie.fields.image_url}" alt="${movie.fields.title}" >
                
            `; //add imageurl
                container.appendChild(movieelement);
            });
        });

    fetch('/ongoing/')
        .then(response => response.json())
        .then(movies => {
            console.log(movies);
            const container = document.getElementById('ongoing-view');
            movies.forEach(movie => {
                const movieelement = document.createElement('div');
                movieelement.innerHTML= `
                <h4>${movie.fields.title}</h4>
                <img src="${movie.fields.image_url}" alt="${movie.fields.title}" style="width:200px; height:250px;">
                
            `; //add imageurl
                container.appendChild(movieelement);
            });
        
        });

    fetch('/upcoming/')
        .then(response => response.json())
        .then(movies => {
            console.log(movies);
            const container = document.getElementById('upcoming-view');
            movies.forEach(movie => {
                const movieelement = document.createElement('div');
                movieelement.innerHTML= `
                <h4>${movie.fields.title}</h4>
                <img src="${movie.fields.image_url}" alt="${movie.fields.title}" style="width:200px; height:250px;">
                
            `; //add imageurl
                container.appendChild(movieelement);
            });
        
        });
        

});