import socket

# ===== CONFIGURAZIONE =====
ADDRESS_FAMILY = socket.AF_INET     # IPv4
SOCKET_TYPE = socket.SOCK_STREAM    # TCP
SERVER_HOST = 'localhost'           # Indirizzo di ascolto
SERVER_PORT = 5000                  # Porta di ascolto

# Domande del Quiz
quiz = [
    {"domanda": "Qual è la capitale d'Italia?", "risposta": "roma"},
    {"domanda": "Quanto fa 5 + 7?", "risposta": "12"},
    {"domanda": "Di che colore era il cavallo bianco di Napoleone?", "risposta": "bianco"},
    {"domanda": "Qual è il pianeta più vicino al Sole?", "risposta": "mercurio"},
    {"domanda": "In che continente si trova il Brasile?", "risposta": "sud america"},
    {"domanda": "Quante dita ha una mano umana?", "risposta": "5"},
    {"domanda": "Come si chiama il mouse in italiano?", "risposta": "topo"}
]

print("\n=== SERVER TCP - Avvio ===")
server = socket.socket(ADDRESS_FAMILY, SOCKET_TYPE)
print(f"[1] Socket creato")

server.bind(("0.0.0.0", SERVER_PORT))
print(f"[2] Bind su {SERVER_HOST}:{SERVER_PORT}")

server.listen(1)  # backlog = una connessione a volta
print(f"[3] Server in ascolto...")

try:
    while True:  
        
        client_socket, client_address = server.accept()
        print(f"\n[4] Giocatore connesso: {client_address}")

        punteggio = 0

        for i, item in enumerate(quiz, 1):
            try:
                # Invia la domanda
                domanda_testo = f"Domanda {i}: {item['domanda']}"
                client_socket.sendall(domanda_testo.encode('utf-8'))

                # Riceve la risposta dal client
                risposta_client = client_socket.recv(1024).decode('utf-8').strip().lower()
                
                print(f"[Log] Risposta da {client_address} per domanda {i}: {risposta_client}")

                # Verifica risposta
                if risposta_client == item["risposta"]:
                    feedback = "CORRETTO!"
                    punteggio += 1
                else:
                    feedback = f"SBAGLIATO! La risposta corretta era: {item['risposta']}"

                client_socket.sendall(feedback.encode('utf-8'))
            
            except ConnectionResetError:
                print(f"[!] Il client si è disconnesso bruscamente.")
                break

        # Fine quiz
        try:
            client_socket.sendall(messaggio_finale.encode('utf-8'))
        except:
            pass

        client_socket.close()
        print(f"[7] Connessione con {client_address} chiusa")

except KeyboardInterrupt:
    print("\n\n[!] Server interrotto (Ctrl+C)")
finally:
    #close() - Chiude socket server
    server.close()
    print("[8] Socket server chiusa\n")