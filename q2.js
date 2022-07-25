//Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos,
//mas especialmente para mulheres. Faça um programa que leia nome, sexo e o valor das
//compras do cliente e calcule o preço com desconto. Sabendo que: - Homens ganham 5% de desconto
//- Mulheres ganham 13% de desconto.

var sexo="m"
var valor=100
var nome="bruna"
novoValor = (sexo, valor) => {return sexo==="f"? valor-(valor*0.13):valor-(valor*0.05)}
console.log(`${nome}, sua conta totalizou ${novoValor(sexo, valor)} reais.`);
