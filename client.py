import socket

# ===== CONFIGURAZIONE =====
# Devono coincidere con quelle del Server
ADDRESS_FAMILY = socket.AF_INET     # IPv4
SOCKET_TYPE = socket.SOCK_STREAM    # TCP
SERVER_HOST = '10.4.54.30'           
SERVER_PORT = 5000                  

print("\n=== CLIENT QUIZ TCP - Avvio ===")

# FASE 1: socket() - Creazione del socket
client = socket.socket(ADDRESS_FAMILY, SOCKET_TYPE)
print(f"[1] Socket creato")

try:
    # FASE 2: connect() - Connessione al server
    client.connect((SERVER_HOST, SERVER_PORT))
    print(f"[2] Connesso a {SERVER_HOST}:{SERVER_PORT}")
    print("--- Inizio Quiz ---\n")

    while True:
        # FASE 3: Ricezione della Domanda
        # Il server invia la domanda, restiamo in attesa
        data = client.recv(1024).decode('utf-8')
        
        # Se riceviamo una stringa vuota, il server ha chiuso la connessione
        if not data:
            break
            
        print(f"{data}")

        # FASE 4: Invio della Risposta
        risposta = input("Tua risposta: ")
        client.sendall(risposta.encode('utf-8'))

        # FASE 5: Ricezione del Feedback (Corretto/Sbagliato)
        feedback = client.recv(1024).decode('utf-8')
        print(f"Esito: {feedback}\n")

except ConnectionRefusedError:
    print("[!] Errore: Assicurati che il SERVER sia avviato prima del client!")
except ConnectionResetError:
    print("\n[!] Connessione interrotta dal server.")
except Exception as e:
    print(f"[!] Errore imprevisto: {e}")
finally:
    # FASE 6: close() - Pulizia finale
    client.close()
    print("\n[5] Connessione chiusa. Grazie per aver giocato!")