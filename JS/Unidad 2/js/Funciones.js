// //void no retorna valor
//daclaracion de funcion
// function imprimir(){
//     console.log("JS");

// }

// imprimir();
// imprimir();

//funcion por expresion
// var saludo=function saludar(){
//     console.log("Hola");
// }

// function sumar(num,num2){
//     var resultado=num+num2;
//     console.log(resultado);
// }

// sumar();//NaN
// sumar(54,9);


// function producto(num,num2){

//     return num * num2;
 
// }

// console.log(producto(6,3));

// var resultado=producto(5,9);

// console.log(resultado);





//  function numeroMaximo (valor1, valor2) {
//   if (valor1 > valor2) { 
//   return valor1 
// }
//   return valor2
// }
//   var v1 = parseInt(prompt("Ingrese un número entero"));
//   var v2 = parseInt(prompt("Ingrese otro número entero"));
//   console.log("El número máximo es:", numeroMaximo(v1,v2));

  



// const potencia2 = function(base, exponente) {
//     let resultado = 1;
//     for (let cuenta = 0; cuenta < exponente; cuenta++) {
//       resultado *= base;
//     }
//     return resultado;
//   };
  
//   console.log(potencia2(2, 10));
//   // → 1024


// let x = 10;
// if (true) {
//   let y = 20;//
//   var z = 30;
//   console.log(x + y + z);
//   // → 60
// }
// // y no es visible desde aqui
// console.log(x + z);



// function potencia(base, exponente = 2) {
//     let resultado = 1;
//     for (let cuenta = 0; cuenta < exponente; cuenta++) {
//       resultado *= base;//resultado=resultado*base
//     }
//     return resultado;
//   }
  
//   console.log(potencia(4));
//   // → 16
//   console.log(potencia(2, 6));
//   // → 64


//   //alcance
//   var a = 5
//   var b = 10
//   if (a === 5) {
//   let a = 4 // El alcance es dentro del bloque if
//   var b = 15 // El alcance es global, sobreescribe a 10
//   console.log(a) // 4, por alcance a nivel de bloque
//   console.log(b) // 15, por alcance global
//   }
//   console.log(a) // 5, por alcance global
//   console.log(b) //

//   //callback  

//   function saludar(nombre) {
//     alert('Hola ' + nombre);
//     }
//     function procesarEntradaUsuario(callback) {
//     var nombre = prompt('Por favor ingresa tu nombre.');
//     callback(nombre);
//     }
//     procesarEntradaUsuario(saludar);


    // const mensaje = function() {  
    //     console.log("Este mensaje se muestra después de 3 segundos");
    // }
     
    // setTimeout(mensaje, 3000);


//     //Clausuras

function iniciar() {
    var nombre = "Codo a Codo" // La variable nombre es una variable local creada por iniciar.
    function mostrarNombre() { // La función mostrarNombre es una función interna, una clausura.
    alert(nombre); // Usa una variable declarada en la función externa.
    }
    mostrarNombre()
    }
    iniciar();

// function creaSumador(x) {
//     return function(y) {
//     return x + y;
//         };
//     }
//     var suma5 = creaSumador(5);
//     var suma10 = creaSumador(10);
//     console.log(suma5(2)); // muestra 7
//     console.log(suma10(2)); // muestra 12