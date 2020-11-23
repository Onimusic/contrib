# Contrib Oni

Conjunto de funções de propósito geral para facilitar o desenvolvimento. Essas funções não são dependentes de um projeto, podendo ser usadas em qualquer projeto.

## Configuração

Ao baixar o aplicativo como um submódulo do seu projeto não se esqueça de configurar o arquivo `apps.py`.
``` python
from django.apps import AppConfig


class ArtistsConfig(AppConfig):
    name = '<app_name>.apps.contrib'
    label = 'contrib'
```

OBS: Troque `<app_name>` pelo nome do seu projeto.
