//Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele trabalha na empresa
//e mostre seu novo salário, reajustado de acordo com a tabela a seguir:
//- Até 3 anos de empresa: aumento de 3% - Entre 3 e 10 anos: aumento de 12.5%
//- 10 anos ou mais: aumento de 20%

var salario=1000
var anos=5
var nome="alice"
function novoSalario(salario, anos){
    if(anos<=3){
        return salario+(salario*0.03)
    }else if(anos>3 && anos<10){
        return salario+(salario*0.125)
    }else{
        return salario+(salario*0.2)
    }
};
console.log(`${nome}, seu novo salário é de ${novoSalario(salario, anos)} reais!`)