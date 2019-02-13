var restart = document.querySelector('#butao');

var celulas = document.querySelectorAll('td');

restart.addEventListener("click", clearTable);

function clearTable(){
    celulas.forEach(function(item){
        item.textContent = '';
    })
}

celulas.forEach(function(item){
    item.addEventListener("click",mark);
})

function mark(){
    if( this.textContent === '' ){
        this.textContent = 'X';
    } else if( this.textContent === 'X' ){
        this.textContent = 'O';
    } else if( this.textContent === 'O' ){
        this.textContent = '';
    }
}
