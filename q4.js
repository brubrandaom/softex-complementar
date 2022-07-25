//Escreva um algoritmo que leia dois números inteiros e compare -os, mostrando na tela uma das mensagens abaixo:
//- O primeiro valor é o maior
//- O segundo valor é o maior
//- Não existe valor maior, os dois são iguais.

var num1=2
var num2=7
function compare(num1, num2){
    if (num1>num2){
        return "o primeiro valor é maior"
    }else if(num2>num1){
        return "o segundo valor é maior"
    }else{
        return "não existe valor maior, os dois são iguais"
    }
};
console.log(compare(num1, num2));