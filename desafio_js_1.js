var num = 25
    horas = 100
    valorh = 5.50

salario = (h, val) => {return (h*val).toFixed(2)}

console.log(`NUMERO = ${num}\nSALARIO = U$ ${salario(horas, valorh)}`);
