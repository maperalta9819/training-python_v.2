# Description
clases que se estan desarrollando para el aprendizaje del lenguaje python
# Capitulo 2: Game project
Para correr el juego debes seguir las siguientes instrucciones en la terminal:
´´´sh
cd game
python3 main.py
´´´
# Capitulo 3: App project

´´´´
git clone
cd app
python -m venv tutorial-env
source tutorial/scripts/activate
pip install requirements.txt
python main.py
´´´
# Capitulo 4: Dependencias de proyecto
Esta es una lista de los comandos usados en la terminal hasta el momento:

###Crear carpeta de virtualizacion
proyecto-env\Scripts\activate
source proyecto-env/Scripts/activate

###Levantar pagina usando uvicorn
uvicorn main:app --reload --port 5000

###SQlite y sqlalchemy es necesario
pip install sqlalchemy
descargar sqlite view si estas usando visual studio code
