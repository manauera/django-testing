var player1 = prompt("Jogador 1: Qual é o teu nome? Você será o vermelho.");
var player1Color = 'rgb(237,45,73)';

var player2 = prompt("Jogador 2: Qual é o teu nome? Você será o azul.");
var player2Color = 'rgb(86,151, 255)';

var game_on = true;
var table = $('table tr');

function reportWin(rowNum, colNum){
  console.log("You won starting at this row,col");
  console.log(rowNum);
  console.log(colNum);

}

function changeColor(rowIndex, colIndex, color){
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color);
}

function returnColor(rowIndex, colIndex){
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

function checkBottom(colIndex){
    var colorReport = returnColor(5,colIndex);
    for (var row = 5; row >-1; row--) {
        colorReport = returnColor(row, colIndex);
        if( colorReport === 'rgb(128, 128, 128)' ){
            return row;
        }
    }
}

function colorMatchCheck(one, two, three, four){
    return (one === two && one === three && one === four && one !== 'rgb(128, 128, 128)' && one != undefined);
}

function checkHorizontalWin(){
    for (var row = 0; row < 6; row++) {
        for (var col = 0; col < 4; col++) {
            if(colorMatchCheck(returnColor(row,col), returnColor(row,col+1), returnColor(row,col+2), returnColor(row,col+3))){
                console.log("horizontal win!");
                reportWin(row,col);
                return  true;
            }
        }
    }
}
function checkVerticalWin(){
    for (var col = 0; col < 7; col++) {
        for (var row = 0; row < 3; row++) {
            if(colorMatchCheck(returnColor(row,col), returnColor(row+1,col), returnColor(row+2,col), returnColor(row+3,col))){
                console.log("vertical win!");
                reportWin(row,col);
                return true;
            }
        }
    }
}
function checkDiagonalWin(){
    for (var col = 0; col < 5; col++) {
        for (var row = 0; row < 7; row++) {
            if(colorMatchCheck(returnColor(row,col), returnColor(row+1,col+1), returnColor(row+2,col+2), returnColor(row+3,col+3))){
                console.log("diagonal win!");
                reportWin(row,col);
                return true;
            } else if(colorMatchCheck(returnColor(row,col), returnColor(row-1,col+1), returnColor(row-2,col+2), returnColor(row-3,col+3))){
                console.log("diagonal win!");
                reportWin(row,col);
                return true;
            }
        }
    }
}

var currentPlayer = 1;
var currentName = player1;
var currentPlayerColor = player1Color;

$('h3').text(currentName + " sua vez de jogar, escolha uma coluna para jogar...");

$('.tabuleiro-ativo button').on('click', function(){
    var col = $(this).closest("td").index();
    var bottom = checkBottom(col);
    console.log(col,bottom);
    if( game_on ){
        changeColor(bottom, col, currentPlayerColor);


        currentPlayer = currentPlayer * -1;

        if( currentPlayer === 1 ){
            currentName = player1;
            currentPlayerColor = player1Color;
            $('h3').text(currentName + " sua vez de jogar, escolha uma coluna para jogar...");
        }else {
            currentName = player2;
            currentPlayerColor = player2Color;
            $('h3').text(currentName + " sua vez de jogar, escolha uma coluna para jogar...");
        }

        if(checkVerticalWin() || checkHorizontalWin() || checkDiagonalWin() ){
            $('h1').text(currentName + " ganhou!");
            $('h3').text("Fim de Jogo! Dá um réfréxi na página pra jogar de novo!");
            $('table').removeClass("tabuleiro-ativo");
            $('#overlay').css("display","block");
            game_on = false;
            reportWin(col,bottom);
        }
    }
})
