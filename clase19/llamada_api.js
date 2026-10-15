let url = "https://rickandmortyapi.com/api/character"
let respuesta = await fetch(url) // Llamada asincrónica
let personajes = await respuesta.json()
console.log(JSON.stringify(personajes, null, 4))
