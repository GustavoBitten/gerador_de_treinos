const joelho_bi_assimetrico = require('./execicios/força/mmii/joelho_bi_assimetrico');
const joelho_bi_simetrico = require('./execicios/força/mmii/joelho_bi_simetrico');
const joelho_unilateral = require('./execicios/força/mmii/joelho_unilateral');
const quadril_bi_simetrico = require('./execicios/força/mmii/quadril_bi_simetrico');
const quadril_unilateral = require('./execicios/força/mmii/quadril_unilateral');


const empurrar_horizontal = require('./execicios/força/mms/empurrar_horizontal');
const empurrar_vertical = require('./execicios/força/mms/empurrar_vertical');
const puxar_horizontal = require('./execicios/força/mms/puxar_horizontal');
const puxar_vertical = require('./execicios/força/mms/puxar_vertical');




function gerarExercicios() {
    const treino_a = [
        "Empurrar horizontal",
        "Empurrar horizontal",
        "Empurrar vertical",
        "Empurrar vertical",
        "Puxar horizontal",
        "Puxar vertical"
    ];

    return exercicios;
}



console.log(joelho_bi_assimetrico);

console.log(gerarExercicios());