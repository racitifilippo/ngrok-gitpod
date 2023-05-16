# ngrok-gitpod

1) Avviare il server web su gitpod
2) Scaricare il file `main.py` ed eseguirlo in locale
3) Eseguire il comando ngrok --> `ngrok http 8080`

La soluzione al problema non era l'header `Access-Control-Allow-Origin` nel server, ma che alla prima richiesta ngrok fa visualizzare una pagina alert del sito. Quindi in quella pagina non c'è `Access-Control-Allow-Origin` header e quindi da problemi di CORS. Per risolvere questo problema basta aggiungere l'header `ngrok-skip-browser-warning` con qualsiasi valore nella richiesta al server ngrok. Con l'aggiunta di questo nuovo header si ha la necessità di aggiungere lato server un'altro header `Access-Control-Allow-Headers` con valore `ngrok-skip-browser-warning`.
