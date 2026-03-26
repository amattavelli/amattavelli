# Analizzare un bilancio con Power BI e AI

Monitoraggio dei Flussi di Cassa: L’Intelligenza Artificiale per Ottimizzare la Stabilità Finanziaria
### Di Alessandro Mattavelli
Nel contesto economico odierno, la gestione efficace dei flussi di cassa rappresenta una priorità assoluta per le aziende, indipendentemente dalla loro dimensione. Le imprese si trovano a fronteggiare sfide crescenti, tra cui incertezza economica, variazioni nei mercati e una competizione sempre più agguerrita. In tale scenario, l'Intelligenza Artificiale (AI) si presenta come un alleato strategico per tracciare, analizzare e ottimizzare i flussi di cassa, contribuendo significativamente alla riduzione del rischio di insolvenza.
## Perché il Monitoraggio dei Flussi di Cassa è Cruciale: avvertenze d’uso della AI
## Il flusso di cassa rappresenta il cuore pulsante di ogni attività imprenditoriale. Una gestione inadeguata può portare a una crisi di liquidità, compromettendo la capacità di un'azienda di operare e rispettare i propri obblighi finanziari. Tradizionalmente, il monitoraggio del cash flow si basa su fogli di calcolo e processi manuali che, sebbene affidabili, spesso risultano lenti da aggiornare e soggetti a errori di compilazione. Inoltre, una conoscenza non approfondita degli strumenti può compromettere anche la fase di progettazione.
## Grazie ai recenti progressi tecnologici, l’AI offre strumenti avanzati in grado di automatizzare e migliorare l’analisi dei dati finanziari. Ciò consente di ottenere una visione chiara e tempestiva delle entrate e delle uscite di cassa, identificando potenziali problemi prima che diventino critici.
## Quando si utilizza l'intelligenza artificiale, è essenziale evitare di trattare argomenti che non si conoscono bene. Il rischio è di incorrere negli errori comuni dei chatbot, soprattutto se non si formulano domande chiare a causa della scarsa conoscenza del tema.
## Nel caso dei flussi di cassa, è consigliabile, qualora non si avesse una conoscenza approfondita dell'argomento, rivedere alcuni concetti consultando testi specifici o facendosi assistere dall’AI, che, in questo contesto, può essere considerata un vero e proprio personal trainer per il ripasso della materia.
## Solo padroneggiando le componenti di un rendiconto finanziario sarà possibile interrogare l’AI in merito a simulazioni e analisi "what if", verificando l’efficacia delle risposte fornite.
## Un primo test: la riconciliazione bancaria con l’AI
Per testare un sistema di AI per la riconciliazione bancaria, è consigliabile iniziare con un campione già riconciliato.
Potremo così comprendere le funzionalità di base del sistema. Successivamente, si dovrebbe aumentare gradualmente la complessità dei dati e il numero delle righe da riconciliare, per mettere alla prova la robustezza del sistema. È utile poi passare all'utilizzo di dati reali, preferibilmente ben strutturati come quelli contenuti in un file Excel, per verificarne l'affidabilità.
Durante questo processo, è fondamentale correggere eventuali discrepanze che emergono, migliorando continuamente il sistema in base ai feedback ottenuti. Una volta che il sistema è stato affinato e ha raggiunto un livello soddisfacente di accuratezza, si può applicare l'IA a periodi non riconciliati, mantenendo sempre una supervisione attenta sui risultati, per garantire la correttezza delle operazioni svolte.
A tal proposito, abbiamo proposto a Chat Gpt due elenchi numerici di 1000 righe invitandolo a trovare i dati non corrispondenti. L’esercizio è stato strutturato per livelli di difficoltà.
In un primo test l’elenco B non conteneva alcuni elementi dell’elenco A: l’AI ha riconosciuto facilmente i dati non corrispondenti. È bastato però aggiungere elementi in B non contenuto in A per cominciare a ricevere risposte non corrette e allucinate.
Il problema può essere affrontato però da un punto di vista diverso che riflette l’approccio che dovremmo tenere con l’AI. Dovremmo abituarci a sostituire la mera richiesta di esecuzione di un compito con l’invito a fornirci una soluzione in grado di eseguire quel compito. Proviamo quindi a chiedere:
Ho creato un tool che:
Permette l'inserimento di due liste con formato "descrizione, importo"
- Identifica elementi presenti solo in una lista
- Evidenzia elementi ripetuti con frequenza diversa
- Formatta gli importi in euro
Per usarlo, inserisci i dati nei due riquadri e clicca "Analizza Differenze".
Necessiti chiarimenti sul suo funzionamento?
Il risultato è un listato compilato in vba, python o come nel caso degli Artifacts di Claude direttamente un eseguibile come mostrato in figura.
Gli Artifacts di Claude sono finestre dedicate all'interno dell'interfaccia di Claude.ai che permettono di visualizzare, modificare e sviluppare contenuti generati dall'intelligenza artificiale in modo interattivo e collaborativo. Questi contenuti possono includere frammenti di codice, diagrammi di flusso, grafici SVG, siti web e dashboard interattive.
## Un’intelligenza artificiale come CFO?
Chiarito l’approccio corretto, possiamo osare un po’ di più e, poiché il miglior modo per comprendere quali risultati si possono ottenere dalla AI è chiederlo direttamente, possiamo formulare il seguente prompt:
‍️Considera tutte le attività connesse alla gestione dei flussi di cassa. Dai un voto da 1 a 10, motivandolo, alle tue capacità di sostituzione al lavoro di un CFO spiegando concretamente nei casi superiori all'8 che tipo di operazioni occorrerebbe fare per attuare la sostituzione.
La risposta, come spesso accade, ci ha un po’ sorpreso e anche un po' preoccupato
Analizzerò sistematicamente le capacità di un sistema AI come me nella gestione dei flussi di cassa, utilizzando un framework strutturato di valutazione basato su aree funzionali chiave.
Valutazione complessiva: 7.5/10
Analisi dettagliata per area funzionale:
Analisi e Previsione dei Flussi di Cassa (9/10)
Eccellente capacità di processare grandi volumi di dati storici, Analisi predittiva accurata basata su pattern ricorrenti, Identificazione rapida di anomalie e trend, Generazione automatica di proiezioni multi-scenario
Gestione della Liquidità Operativa (8/10)
Monitoraggio continuo delle posizioni di cassa, Ottimizzazione del capitale circolante, Sincronizzazione efficiente tra incassi e pagamenti, Gestione automatizzata dello scadenzario
Pianificazione Finanziaria (7/10)
Modellizzazione finanziaria complessa, Generazione di budget e forecast, Limitazioni nella valutazione qualitativa di variabili macro
Relazioni con Stakeholder (6/10)
Capacità limitate nella negoziazione, Impossibilità di gestire relazioni personali, Supporto efficace nella preparazione documentale
Per implementare una sostituzione nelle aree con votazione superiore a 8, occorrerebbe:
Per l'Analisi e Previsione (9/10): Implementare un sistema di data ingestion automatizzato per tutti i flussi finanziari, sviluppare dashboard real-time con KPI personalizzati, creare modelli predittivi con machine learning per forecasting, stabilire soglie automatiche per alert su anomalie, integrare fonti dati esterne per arricchire l'analisi
Per la Gestione della Liquidità (8/10): Automatizzare il matching tra incassi e pagamenti, implementare algoritmi di ottimizzazione del working capital, creare workflow automatici per approvazioni, integrare sistemi di tesoreria e ERP, sviluppare meccanismi di controllo automatico delle disponibilità
Limitazioni critiche da considerare: necessità di supervisione umana per decisioni strategiche. importanza del giudizio qualitativo in situazioni complesse, gestione delle relazioni con stakeholder, valutazione di fattori macro e geopolitici
La sostituzione richiederebbe quindi un approccio ibrido, dove l'AI gestisce gli aspetti quantitativi e ripetitivi, mentre mantiene un ruolo di supporto per gli aspetti strategici e relazionali che richiedono competenze umane distintive.
Se fosse vero quanto affermato, nonostante le rassicurazioni finali, al CFO, se non direttamente coinvolto in scelte strategiche, non resterebbe molto.
Entrare nel merito di ogni singolo compito richiederebbe ben più spazio di quanto ci è concesso da questo articolo ma vale la pena vedere se la risposta ha qualche fondamento o è stata emessa per quel talvolta irresistibile bisogno che ha l’AI di darci sempre comunque una risposta soddisfacente (con esiti non sempre esaltanti).
‍️Ok ti metto alla prova. All’abilità 1 hai dato 9, caspita! Costruisci un’analisi di dei movimenti bancari
Per iniziare potremmo partire anche solo con il primo file dei movimenti effettivi. In questo modo potrei mostrarle:
L'analisi dei pattern storici
Il calcolo degli indicatori chiave come DSO e DPO
Una prima previsione basata sui trend identificati
Una volta verificata l'accuratezza di queste prime analisi, potremmo poi integrare gli altri dati per sviluppare previsioni più sofisticate e strategie di ottimizzazione della tesoreria.
Il risultato finale, dopo qualche aggiustamento (sempre in linguaggio naturale) è stato il seguente.
Qualcuno potrebbe giustamente osservare che si sarebbero potuti ottenere risultati migliori con Office (Excel e Power BI), ma a quale costo di tempo e competenze?
## Chiedere parere dell’AI: il ruolo del capitale circolante netto
Se L'AI vuole essere di supporto alla direzione finanziaria dell’impresa, deve saper interpretare e risolvere problemi tipici del CFO per supportarlo efficacemente.
Recentemente, la Fondazione nazionale dei commercialisti ha pubblicato un documento che esplora la gestione del capitale circolante netto (CCN) come leva strategica per la solidità finanziaria delle imprese. Il paper esamina le configurazioni commerciali, operative e finanziarie del CCN e fornisce strumenti per monitorare efficacemente i flussi finanziari e prevenire crisi aziendali e mostra anche un esempio interessante su uno scenario ipotetico.
Proviamo a sottoporre a Chat Gpt il caso proposto dal documento
e vediamo che tipo di analisi è in grado di condurre e se le conclusioni vanno un po’ al di là di quanto possiamo leggere nella ricerca di FNC che si limita a calcolare il maggior costo finanziario derivante dalla formula:
Abbiamo quindi domandato a O1:
‍️Sei il CFO di una piccola media impresa ti vengono proposte queste due alternative (il costo del denaro è pari al 10%) quali osservazioni ti senti di formulare? Quali informazioni ritieni opportuno integrare prima di avanzare un giudizio definitivo?
Una prima osservazione è che l’aumento di fatturato (da 100.000 a 120.000) porta un incremento del margine lordo (il 40% di 100.000 è 40.000, mentre il 40% di 120.000 è 48.000), quindi teoricamente la seconda opzione genera un utile operativo più alto di 8.000. Tuttavia, la dilazione di pagamento più lunga (150 gg anziché 90 gg) espone l’impresa a un maggior fabbisogno di capitale circolante e a un maggiore costo del denaro (10%). In linea di principio:
Costo finanziario aggiuntivo: se consideriamo il finanziamento del fatturato per 60 giorni in più (da 90 a 150), i maggiori oneri finanziari potrebbero ridurre parte (o tutto) del beneficio di extra margine.
Rischio di liquidità: allungare troppo i tempi d’incasso potrebbe mettere sotto pressione la cassa aziendale, soprattutto se l’impresa deve pagare costi fissi e fornitori senza incassare in tempi adeguati.
Rischio di insolvenza: non è detto che un cliente a cui si concede più credito (dilazione maggiore) non diventi anche meno puntuale o addirittura insolvente. Soprattutto se la concessione di più giorni di dilazione attrae clienti meno solidi finanziariamente.
Prima di un giudizio definitivo, sarebbe opportuno disporre di ulteriori informazioni, tra cui:
Affidabilità e rating dei clienti: per capire il rischio di mancato pagamento e la puntualità degli incassi.
Eventuali costi fissi o spese commerciali aggiuntive connesse all’incremento di fatturato (ad es. sconti, promozioni, costi di marketing, provvigioni più alte).
Capacità dell’azienda di finanziare il maggior capitale circolante: l’azienda ha sufficiente liquidità o deve ricorrere a linee di credito bancarie, con relativi costi e garanzie?
Condizioni di pagamento ai fornitori: è possibile allungare a propria volta i tempi di pagamento (o negoziare condizioni migliori) per ridurre il mismatch finanziario?
Volumi sostenibili: l’incremento di fatturato porta con sé anche eventuali costi di produzione più elevati (materiali, manodopera, logistica) e bisogna valutare la capacità produttiva dell’impresa.
Analisi di sensitività: capire a che livello di mancato incasso o di tasso di interesse la convenienza verrebbe annullata.
In sintesi, la maggiore redditività potenziale della seconda opzione deve essere valutata alla luce dei possibili rischi di liquidità, insolvenza e costi finanziari. Senza queste ulteriori informazioni (in particolare sugli aspetti di credito commerciale, sugli oneri di finanziamento e sul reale comportamento di pagamento dei clienti), è prematuro esprimere un parere definitivo.
A questo punto possiamo anche integrare l’analisi chiedendo il calcolo dell’effetto sulla liquidità: quello che otteniamo è un’analisi puntuale che giunge a conclusioni diverse da quelle della FNC. Le conclusioni dell’Intelligenza Artificiale sono infatti riportate in figura e sono sensibilmente diverse da quelle contenute nel documento.
Se il costo del denaro è del 10% annuo, l’onere finanziario aggiuntivo per sostenere questo maggiore fabbisogno di capitale circolante è pari a 2.500,00 e non 1.500,00 come riportato nella ricerca.
E interrogata sulla discrepanza delle conclusioni risponde così:
Dal punto di vista strettamente finanziario, l’importo da finanziare è la differenza tra i due crediti medi (nuovo meno vecchio), e a tale valore va applicato il tasso d’interesse (10%). Se l’obiettivo è quantificare il “costo del denaro aggiuntivo” dovuto all’allungamento della dilazione, non c’è una ragione logica per moltiplicare anche per 0,60.
Quel fattore 0,6 potrebbe provenire dal rapporto costi variabili / fatturato (o da altre ipotesi di calcolo), ma non è giustificato se si sta semplicemente calcolando il costo del capitale circolante sul credito verso clienti. In altre parole, tutta la somma che rimane “bloccata” nei crediti (non solo la quota “variabile”) va finanziata, e su di essa si paga il 10% annuo.
Per ulteriore verifica, abbiamo girato la domanda anche a Deep Seek, un modello apparso di recente di origine cinese e la risposta è ancora più argomentata e profonda.
## Conclusioni: lavorare in team con l’AI
Per quanto sorprendente possano sembrare alcuni risultati ottenuti e descritti in questo articolo, è essenziale e quasi superfluo ricordare che l'AI non può sostituire completamente il giudizio umano, specialmente in ambiti strategici e relazionali. Il futuro della gestione finanziaria sembra destinato a un approccio ibrido, dove l'AI supporta i processi quantitativi e ripetitivi, mentre l'uomo si concentra su decisioni complesse e relazioni con gli stakeholder. Per massimizzare i benefici dell'AI, le aziende dovranno investire non solo in tecnologia, ma anche nella formazione e nella supervisione umana, garantendo un equilibrio tra innovazione e prudenza.