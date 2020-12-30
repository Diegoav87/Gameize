const cartBtns = document.getElementsByClassName('cart-btn');

for (let i = 0; i < cartBtns.length; i++ ) {
    cartBtns[i].addEventListener('click', function() {
        const gameId = cartBtns[i].dataset.game;
        const action = cartBtns[i].dataset.action;
        console.log('Game id:', gameId, 'Action:', action)
        
        if (user === 'AnonymousUser') {
            console.log('Not logged in');
        } else {
            updateUserOrder(gameId, action)
        }
    })
}

function updateUserOrder(gameId, action) {
    console.log('Sending data...');

    const url = '/update_item/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'gameId': gameId, 'action': action})
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data)
    })
}