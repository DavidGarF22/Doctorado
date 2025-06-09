# TID-A2RAERCI
Respositorio para el código relacionado con el TID Aproximación a la Adquisición Remota y Automática de Evidencias en Redes Corporativas e Industriales

El objetivo principal del trabajo es analizar una aproximación a la adquisición de evidencias para el análisis forense de forma automática y remota, con especial énfasis en la adquisición de memoria, teniendo en cuenta las casuísticas de una red corporativa distribuida y las circunstancias especiales de una red industrial.

Comandos de ejecución:

    ansible-playbook -i inventories/tid_hosts.yml site_memoryLinux.yml --ask-vault-pass
