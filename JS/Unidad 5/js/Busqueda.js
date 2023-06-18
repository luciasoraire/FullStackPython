const names = [
    { name: "María", age: 20 },
    { name: "Bernardo", age: 28 },
    { name: "Pancracio", age: 22 },
    { name: "Andrea", age: 19 },
    { name: "Sara", age: 29 },
    { name: "Jorge", age: 32 },
    { name: "Yurena", age: 38 },
    { name: "Ayoze", age: 18 }
  ];
  
  // Busca el primer elemento con la edad indicada, sino devuelve -1
  const findElement = (array, searchedAge) => {
    for (let i = 0; i < array.length; i++) {
      const element = array[i];
      if (element.age === searchedAge) {
        return element;
      }
    }
    return -1;
  }
  
 console.log(findElement(names, 19));     // { name: "Andrea", age: 19 }
 console.log(findElement(names, 32));     // { name: "Jorge", age: 32 }
 console.log(findElement(names, 33));     // -1