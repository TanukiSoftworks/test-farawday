# test-farawday

## Como se usa?

### 1. Crea una red de Docker
Crea una red personalizada para que los contenedores se comuniquen entre sí:
```bash
docker network create mi-red
```

### 2. Construye las imágenes Docker
Primero debes construir las imágenes de ambos módulos.

**Construir modulo-b:**
```bash
cd modulo-b
docker build -t modulo-b:latest .
cd ..
```

**Construir modulo-a:**
```bash
cd modulo-a
docker build -t modulo-a:latest .
cd ..
```

### 3. Inicia los contenedores
**Primero inicia modulo-b:**
```bash
docker run -d \
  --name modulo-b \
  --network mi-red \
  -p 8003:8003 \
  modulo-b:latest
```

**Luego inicia modulo-a:**
```bash
docker run -d \
  --name modulo-a \
  --network mi-red \
  -p 8001:8001 \
  modulo-a:latest
```

### 4. Prueba el programa
```bash
curl http://localhost:8001/enviar
```

Deberías ver una respuesta JSON con el resultado del procesamiento.

### 5. Revisa los logs
```bash
docker logs modulo-a
docker logs modulo-b
```

## Limpieza

Si ya no quieres tener los contenedores e imágenes en tu PC:

```bash
# Detener y eliminar contenedores
docker stop modulo-a modulo-b
docker rm modulo-a modulo-b

# Eliminar la red
docker network rm mi-red

# (Opcional) Eliminar las imágenes
docker rmi modulo-a:latest modulo-b:latest
```

