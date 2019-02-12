var fname = prompt("Olar! Qual é o seu primeiro nome?");
var lname = prompt("Ah sim, e o sobrenome?");
var age = prompt("Certo... E qual é a sua idade?");
var height = prompt("Hmmm que jovem! Agora me diga sua altura, em cm");
var pet = prompt("Última pergunta. Qual o nome de seu bichinho de estimação?");

if( (fname[0] == lname[0]) && (age > 20 && age < 30) && (height > 175) && (pet[pet.length - 1] === "y") ){
    console.log("Olá bonitão, vemk vem");
} else{
    console.log("Nada pra ver aqui... ");
}

alert("Muito bem! Obrigado e volte sempre!");
