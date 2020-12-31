const cartBtns = document.getElementsByClassName('cart-btn');
const cartIcon = document.querySelector('.cart-circle');

for (let i = 0; i < cartBtns.length; i++ ) {
    cartBtns[i].addEventListener('click', function() {
        const gameId = cartBtns[i].dataset.game;
        const action = cartBtns[i].dataset.action;
        console.log('Game id:', gameId, 'Action:', action)
        
        if (user === 'AnonymousUser') {
            console.log('Not logged in');
        } else {
            updateUserOrder(gameId, action, cartBtns[i])
        }
    })
}

function updateUserOrder(gameId, action, btn) {
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
        cartIcon.textContent = data['item_count'];

        if (btn.classList.contains('quantity-btn-add')) {
            let currentNum = parseInt(btn.previousSibling.previousSibling.textContent);
            currentNum += 1;

            if (currentNum > 0) {
                btn.previousSibling.previousSibling.textContent = currentNum;
                const totalBtn = btn.parentElement.nextSibling.nextSibling.nextSibling.nextSibling;
                let price = btn.parentElement.previousSibling.previousSibling.textContent;
                price = price.substring(1);
                price = parseFloat(price);
                totalBtn.textContent = `$${price * currentNum}`;
            }
            
        } else if (btn.classList.contains('quantity-btn-remove')) {
            let currentNum = parseInt(btn.nextSibling.nextSibling.textContent);
            currentNum -= 1;

            if (currentNum > 0) {
                btn.nextSibling.nextSibling.textContent = currentNum;
                const totalBtn = btn.parentElement.nextSibling.nextSibling.nextSibling.nextSibling;
                let price = btn.parentElement.previousSibling.previousSibling.textContent;
                price = price.substring(1);
                price = parseFloat(price);
                totalBtn.textContent = `$${price * currentNum}`;
            }
        }
    })
}