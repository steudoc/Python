La musica folk irlandese fa spesso riferimento ad un non meglio precisato drunken sailor (What do we do with the drunken sailor).
Questo esercizio simula le vicende di un marinaio ubriaco intento a camminare lungo un molo per raggiungere la barca.
Dato lo stato di ebrezza, egli potrebbe cadere in acqua e nuotare verso l'infinito ed oltre.

La larghezza del molo da attraversare è definita a priori.
Dato un percorso random stimare visivamente la seria possibilità che egli affoghi.

L' esercizio richiede di installare la libreria <matplotlib> per visualizzare la figura risultante.
Questo esercizio è un esercizio bonus, da fare dopo aver completato gli esercizi del laboratorio 7.

Il file the_drunken_sailor.py contiene un semplice programma con tre funzioni:

- window_average_filter: si ispira all' esercizio 7.2.1 Rumore di misura.
                        L'obiettivo è scrivere una funzione che applichi il window average filter
                        in modo parametrico, cioé si può passare come parametro la lunghezza del filtro.
                        Per evitare casistiche, si può applicare il padding, una tecnica che aggiunge dei valori
                        all'inizio e alla fine di una lista. La funzione deve restituire la lista contenente
                        i valori filtrati (senza i valori di padding aggiunti).

- random_walk: Simulare il percorso svolto dal marinaio.
               Ad ogni passo in avanti il marinaio può procedere:
                   - dritto
                   - alla sua destra
                   - alla sua sinistra
               Il marinaio ubriaco parte dalla posizione 0, centrale quindi al molo.
               Ad ogni passo, il marinaio può salire di un metro (andando a sinistra),
               scendere di un metro (andando a destra), o camminare dritto.
               Creare una lista randomica, che aggiorni per ogni passo la distanza dal centro del molo
               del marinaio ubriaco.

- main: Questa funzione è in gran parte implementata. Seguire i #TODO.
        - creare due liste che definiscano i bordi del molo
        - provare a fare il plot di due filtri di lunghezza diversa, definendoli con colori
                  e labels diverse, per poterli distinguere e confrontare





