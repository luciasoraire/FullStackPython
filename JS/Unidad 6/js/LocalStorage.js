const json = `{
    "name": "Manz",
    "life": 99
  }`;
  
  const user = JSON.parse(json);
  
  user.name;  // "Manz"
  user.life;  // 99

console.log(user.name)