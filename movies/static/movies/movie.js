function handleMovieImageClick(event) {
    var movieId = event.target.dataset.movieId;

    fetch(`/movie/${movieId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            
        })
    })
    .then(response => response.json())
    .then(data => {
        
    });
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}