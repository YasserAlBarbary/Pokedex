# Pokedex API
## This Readme file simply explains:
* ### [How to run/install the the API](##how-to-run/install-the-the-api)
* ### [How to use the API](##how-to-use-the-api)
* ### [What could have gone better for production( and maybe how to do it?)](##what-could-have-gone-better-for-production)
** if you would like a more detailed guide on the steps read the ```Guide.md``` file **
## How to run/install the the API
This API us built using Django REST Framework, and is hosted on Docker.<br>
So basically it is all you need to install and it will take care of the rest for you.<br>
https://www.docker.com/get-started <br>
* install Docker from the previous link
* open a terminal window and navigate to this project (\Pokedex)
* run the commands 
```bash
$ docker build .
$ docker-compose up
```
Docker will take some time the first time it runs to build your image<br>
If you wish to terminate your Docker image, press ```ctrl + c``` then run:
```bash
$ docker-compose down
```
## How to use the API
the API is now hosted and you can run it with these examples 
```bash 
# The genral version
http://127.0.0.1:8000/pokemon/mewtwo/ 
http://127.0.0.1:8000/pokemon/<pokemon_name>/
# the translated version
http://127.0.0.1:8000/pokemon/translated/pikachu/ 
http://127.0.0.1:8000/pokemon/translated/<pokemon_name>/ 

```
 ## What could have gone better for production
* Obviously in this project Python(Django) is used, that means by default all methods are synchronus which can lead to slowdowns. a compiled language like C# can overcome this( and recent versions of Django but that needs more suupport according to documentation in DRF)
* The Pokemon views classes (PokemonCardView, PokemonCardTranslatedView) are calling services everytime, if we can have our own databse so we can cache the pokemons that we already found that would lower the traffic on network.
* 	* look up the Pokemon in databse
* 	* if found return it if not use 3rd party API and save it in DB
