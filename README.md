Primero clonar este repositorio y puedes hacer con una llave SSH
```bash
git clone git@github.com:angelcgar/cli-py.git
```

despues entra a la carpeta cli-py
```bash
cd cli-py
```

ahora asegurate de tener python en tu sistema
```bash
python --version
```

y ahora deverias de poder iniciar el entorno virtual
Esto es estado en windows
```bash
venv\Scripts\activate
```
y esto es estando Unix o MacOS
```bash
source venv/bin/activate
```

ahora esto es importante, esto solo funcionara en bash y si usas una shell 
alternativa como csh o fish hay un ligero cambio en como activarlo, para csh
```csh
source venv/bin/activate.csh
```

y para fish la shell interactiva
```fish
source venv/bin/activate.fish
```

ahora deverias de poder ejecutar los comandos, para verlos ejecuta
```bash
python cli.py
```

eso te dara una ayuda rapida.
