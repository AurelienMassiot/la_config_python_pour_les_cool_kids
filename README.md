# la_config_python_pour_les_cool_kids
La config Python pour les cool kids.

## Run du container en local
```bash
docker build -t ultimate_cool_kid .
```

```bash
docker run -it ultimate_cool_kid
```

## Déploiement sur AWS
Récupérer des credentials :
```bash
awscli_saml_sso --show-browser
```

Vérifier que l'architecture de l'image construite précédemment est bien en amd64 : 
```bash
docker inspect ultimate_cool_kid | grep Architecture
```

Tagger l'image :
```bash
docker tag ultimate_cool_kid 431877925320.dkr.ecr.us-east-1.amazonaws.com/auma/cool-kids
``` 

Obtenir des credentials pour ECR :
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 431877925320.dkr.ecr.us-east-1.amazonaws.com
```

Pousser l'image sur ECR :
```bash
docker push 431877925320.dkr.ecr.us-east-1.amazonaws.com/auma/cool-kids
```

Ensuite, créer un cluster ECS sur AWS et une tâche.


## Images Docker x Mac M1
Si vous voulez builder des images Docker avec une architecture différente, c'est possible, par exemple :

### Avec Docker BuildX (au moment de la construction de l'image)

`docker buildx build --platform linux/amd64 -t <image_name> .`

### Avec Colima (au moment du démarrage de Colima)

`colima start x86_64 --arch x86_64`