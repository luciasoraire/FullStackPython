class Personaje {
    name;
    energy;
  
    constructor(name, energy = 10) {
      this.name = name;
      this.energy = energy;
    }
  
    get status() {
      return '⭐'.repeat(this.energy);
    }
  }



const mario = new Personaje("Mario");
const luigi=new Personaje("Luigi",5)
console.log(mario.energy)  // 10
console.log(mario.status)   // '⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐'
console.log(luigi.energy)  // 10
console.log(luigi.status)


