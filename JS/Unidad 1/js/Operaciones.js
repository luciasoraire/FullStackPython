//operaciones
//0,Nan, " "son vacio, cuentan como false

console.log(8 * null)
// → 0 coercion de tipo el null se convierte a 0
console.log("5" - 1)
// → 4 el string se convierte de string a numero
console.log("5" + 1)
// → 51 se convierte de numero a string
console.log(1 + "5")
// → 15
console.log("cinco" * 2)
// → NaN

console.log(false == 0)
// → true
console.log(null == undefined);// verdadero solo si son null o undefined
// → true
console.log(null == 0);//
// → false

console.log(5==5)
console.log(5=="5")

//usando ===
console.log(5===5)
console.log(5==="5")



//operacion por cero 
console.log(0/0)

//Uso de parentesis

console.log(100+4*11);
console.log((100+4)*11);

