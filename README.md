# Client-Server
Questo progetto consiste nello sviluppo di un'applicazione distribuita in Python che permette a un utente di partecipare a un quiz testuale tramite comunicazione in rete. Il sistema si basa su un'architettura client/server e utilizza il protocollo TCP per garantire uno scambio di dati affidabile tra le due componenti.

L'applicazione è suddivisa in due parti principali: il server e il client. Il server si occupa della gestione completa della logica del quiz, inclusa la memorizzazione delle domande, la verifica delle risposte e il calcolo del punteggio. Il client, invece, gestisce l'interazione con l'utente, mostrando le domande ricevute e inviando le risposte al server.

Il funzionamento del programma si articola in diverse fasi. Inizialmente viene stabilita una connessione tra client e server tramite socket TCP. Una volta connessi, il server avvia il quiz inviando una serie di domande (almeno sette), organizzate tramite una struttura dati adeguata come una lista di dizionari.

Il gioco procede con un ciclo domanda/risposta: il server invia una domanda alla volta, il client la visualizza e acquisisce l'input dell'utente, quindi invia la risposta al server. Il server confronta la risposta ricevuta con quella corretta e restituisce un feedback immediato, indicando se la risposta è giusta o sbagliata. Contemporaneamente, aggiorna il punteggio totale.

Al termine del quiz, il server invia il risultato finale al client, mostrando il punteggio ottenuto. Infine, entrambi i programmi chiudono correttamente i socket per liberare le risorse di rete.

Il progetto è stato sviluppato in coppia, con la seguente suddivisione dei ruoli:

Butt: sviluppo della componente server
Tulgara: sviluppo della componente client
