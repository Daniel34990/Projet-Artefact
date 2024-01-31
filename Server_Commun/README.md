Protocole :

- Chaque robot envoie régulièrement : "Puis-je démarrer ?"
- Le serveur répond "Oui" ou "Non"
- Si le serveur répond "Oui", la raspberry lance le programme de déplacement
- Si le serveur répond "Non", la raspberry attend un certain temps avant de redemander si elle peut démarrer
- Le serveur ping régulièrement les robots pour savoir s'ils sont toujours connectés
- Si un robot ne répond pas, le serveur donne l'autorisation à un autre robot de démarrer
- Si la RPi est perdue, elle le signalera au serveur qui donnera l'autorisation à un autre robot de démarrer (et elle quitte le parcours)
- 