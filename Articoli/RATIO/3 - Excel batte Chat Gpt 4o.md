# 3   Excel batte Chat Gpt 4o

### Excel 3.0 (1990) batte Chat GPT-4o (2024) e Claude OPUS (2024)
Con una sorpresa che ha suscitato anche un sorriso beffardo, Excel 3.0, rilasciato nel 1990, ha dimostrato la sua superiorità su Chat GPT-4o (rilasciato meno di un mese fa) in un calcolo non particolarmente sofisticato.
Si trattava di un semplice problema di gestione del personale stagionale.
Per minimizzare i costi e coprire la domanda giornaliera, un ristoratore deve pianificare i turni settimanali dello staff stagionale: 5 giorni di lavoro e 2 giorni di riposo di fila per ogni turno.
Dovranno essere necessariamente presenti
Lunedì: 23 persone
Martedì: 17 persone
Mercoledì: 13 persone
Giovedì: 14 persone
Venerdì: 15 persone
Sabato: 18 persone
Domenica: 24 persone
I costi settimanali per i 7 turni disponibili sono i seguenti:
Turno 1: Riposo sabato e domenica, costo 400
Turno 2: Riposo venerdì e sabato, costo 460
Turno 3: Riposo giovedì e venerdì, costo 500
Turno 4: Riposo mercoledì e giovedì, costo 500
Turno 5: Riposo martedì e mercoledì, costo 500
Turno 6: Riposo lunedì e martedì, costo 500
Turno 7: Riposo domenica e lunedì, costo 440
Lo scopo è distribuire un numero di persone su ogni turno per coprire esattamente la domanda giornaliera al costo più basso. Questa situazione si verifica spesso anche nel campo della pianificazione della produzione per le industrie manifatturiere e di conseguenza la sua corretta soluzione può far risparmiare denaro all’imprenditore.
Per risolvere occorre utilizzare la programmazione lineare, una tecnica di ottimizzazione matematica utilizzata per trovare il miglior risultato (come il minimo costo o il massimo profitto) in un modello che coinvolge variabili soggette a vincoli lineari.
Ogni problema di programmazione lineare può essere rappresentato da:
- Funzione obiettivo: Una funzione lineare che rappresenta l'obiettivo da ottimizzare (es. minimizzare i costi).
- Vincoli: Un insieme di equazioni o disuguaglianze lineari che rappresentano le limitazioni del problema (es. disponibilità giornaliera di personale).
- Variabili di decisione: Le variabili che influiscono sull'obiettivo e devono essere determinate (es. numero di persone assegnate a ciascun turno).
Non occorre essere dei matematici esperti, il  risolutore "Solver" presente nei componenti aggiuntivi di di Excel (occorre aggiungerlo dal menù opzioni) ha risolto brillantemente il problema in pochi secondi. Dopo aver impostato i vincoli: il numero di persone è un numero intero maggiore di 0 e il numero di persone disponibili per giornata deve essere almeno pari alla domanda, ha fornito la seguente distribuzione ottimale:
Turno 1: 1 persona
Turno 2: 6 persone
Turno 3: 4 persone
Turno 4: 6 persone
Turno 5: 6 persone
Turno 6: 2 persone
Turno 7: 0 persone
Minimizzando il costo settimale a 12.160 euro.
Invece i GPT, nonostante la loro avanzata architettura basata su reti neurali e la capacità di comprendere e generare testo complesso, hanno faticato con questo problema. Più tentativi sono stati fatti, ma le soluzioni fornite erano errate o incomplete: o non venivano rispettati i vincoli o venivano fornite distribuzioni di personale che andavano da 14.400 a 17.000.
Ho cercato di capire le cause tecniche del fallimento dei Chat Bot in questo contesto. Ho chiesto al Chat Gpt di spiegarmi scientificamente e matematicamente (archittettura, calcolo ecc.) l'epic fail impedendogli di dirmi il classico "Chat Gpt può commettere errori".
Ecco la risposta che è bene tenere presente quando ci si accosta a questi strumenti.
1. Architettura: Chat GPT-4o è progettato per l'elaborazione del linguaggio naturale, non per la risoluzione di problemi matematici complessi. Le reti neurali utilizzate sono ottimizzate per comprendere e generare testo, ma non per eseguire calcoli di ottimizzazione.
2. Modalità di Calcolo**: Il risolutore di Excel utilizza algoritmi specifici per l'ottimizzazione matematica, come il Simplex Method per la programmazione lineare. Questi algoritmi sono altamente ottimizzati per trovare soluzioni esatte a problemi di ottimizzazione.
3. Precisione e Efficienza**: Il risolutore è progettato per gestire vincoli e obiettivi in modo molto preciso e veloce. Chat GPT-4o, al contrario, approssima le risposte basandosi su pattern appresi dai dati di addestramento, il che può portare a errori in contesti che richiedono precisione numerica.
In conclusione, mentre Chat GPT-4o rappresenta un progresso incredibile nell'intelligenza artificiale per l'elaborazione del linguaggio naturale, strumenti come il risolutore di Excel dimostrano che, per alcuni compiti specifici di ottimizzazione matematica, a volte è meglio affidarsi a soluzioni classiche e consolidate. E così, Excel 3.0 si aggiudica la vittoria, dimostrando che a volte anche in tema di calcoli “nella botte vecchia c’è del buon vino”. Almeno per il momento (premessa fondamentale quando si parla di AI) meglio i metodi tradizionali.