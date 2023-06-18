class Personaje2 {
    name;
    energy;
  
    constructor(name, energy = 10) {
      this.name = name;
      this.energy = energy;
    }
  
    get status() {
      return '⭐'.repeat(this.energy);
    }
  
    set status(stars) {
      this.energy = stars.length;
    }
  }
  
  const mario = new Personaje2("Mario");
  console.log(mario.energy) ;// 10
  mario.status = '⭐⭐⭐';
  console.log(mario.energy)   // 3
  console.log(mario.status )   // '⭐⭐⭐'

  