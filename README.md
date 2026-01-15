# test-farawday

## Como se usa?

### Debes crear primero una red de docker, con el nombre que quieras.
ejemplo:
```
docker network create mi-red
```
### luego, iniciar el modulo b en la red que acabas de crear.
> asegurate de estar dentro de la carpeta de modulo b.
ejemplo:
```
docker run -d \
  --name modulo-b \
  --network mi-red \
  -p 8003:8003 \
  modulo-b:latest
```
  ### luego, haces lo mismo con el modulo a.
  > asegurate de estar dentro de la carpeta de modulo a.
```
  docker run -d \
  --name modulo-a \
  --network mi-red \
  -p 8001:8001 \
  modulo-a:latest
```
## Por ultimo, prueba el programa con:
```
  curl http://localhost:8001/enviar
```
## Y revisa los logs de el programa con: 
  ```
  docker logs modulo-a
  docker logs modulo-b
```


### Si ya no quieres tener las imagenes de los containers en tu pc, usa: 

```
docker stop modulo-a modulo-b
docker rm modulo-a modulo-b
docker network rm mi-red
```

