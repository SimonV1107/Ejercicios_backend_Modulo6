const http = require("http");
const url = require("url");

async function getPokemonData() {
  //hacemos la petición a la api
  const response = await fetch(
    "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json"
  );
  const data = await response.json();
  return data;
}

handleRequest = async (req, res) => {
  //recuperamos el nombre de la url
  pokemonName = decodeURI(req.url.substring(1));

  getPokemonData()
    .then((pokemonData) => {
      //Comprobamos que hay un pokemon con ese nombr o id
      const pokemon = pokemonData.find(
        (p) =>
          p.id == pokemonName ||
          p.name.english == pokemonName ||
          p.name.japanese == pokemonName ||
          p.name.chinese == pokemonName ||
          p.name.french == pokemonName
      );
      if (pokemon) {
        // Devolvemos los datos del pokemon
        res.writeHead(200, { "Content-Type": "application/json" });
        res.end(
          JSON.stringify({
            Tipo: pokemon.type,
            HP: pokemon.base.HP,
            Attack: pokemon.base.Attack,
            Defense: pokemon.base.Defense,
            "Sp. Attack": pokemon.base["Sp. Attack"],
            "Sp. Defense": pokemon.base["Sp. Defense"],
            Speed: pokemon.base.Speed,
          })
        );
      } else {
        // Devolvemos un mensaje de error si el pokemon no se encontró
        res.writeHead(404, { "Content-Type": "text/plain" });
        res.end('El pokemon no aparece en la pokedex');
      }
    })
    .catch((error) => console.error(error));
};

const server = http.createServer(handleRequest);

server.listen(3000, () => {
  console.log("Servidor escuchando en el puerto 3000");
});
