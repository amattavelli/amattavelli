# Modelli Z Score di Altman

### Tutti i Modelli Z-Score di Altman: Storia, Formule, Autori e Applicazioni Italiane
### 1. Z-Score Originale (1968) — Imprese Manifatturiere Quotate USA
### Autore e riferimento
Edward I. Altman, all'epoca Assistant Professor of Finance presso la NYU Stern School of Business. Il modello fu pubblicato nel paper seminale "Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy" (Journal of Finance, 1968).[1][2]
### Formula
### Variabili
### Zone di discriminazione
Safe Zone: Z > 2,99
Grey Zone: 1,81 < Z < 2,99
Distress Zone: Z < 1,81[3][1]
### Campione e accuratezza
Il modello fu costruito su un campione di 66 imprese manifatturiere quotate USA (33 fallite e 33 sane), con attività inferiori a 25 milioni di dollari, nel periodo 1946–1965. L'accuratezza predittiva risultò del 95% un anno prima del fallimento e del 72% due anni prima. In test successivi (1997–1999 su 120 imprese), il modello mantenne un'accuratezza del 94% con cutoff a 2,67 e dell'84% con cutoff a 1,81.[4][5][2][3]
### Commento
Il modello originale è applicabile esclusivamente a imprese manifatturiere quotate in borsa. Il suo limite principale è l'uso del valore di mercato dell'equity (X₄), non disponibile per le imprese non quotate. Altman stesso ha osservato che il cutoff di 1,81, definito sul campione originale degli anni '60, è ormai obsoleto: nei dati recenti (2017) la mediana dello Z-Score per imprese con rating B è 1,65, e un valore prossimo a zero è più indicativo di default effettivo.[2][3]
### 2. Z'-Score (1983) — Imprese Manifatturiere Private (Non Quotate)
### Autore e riferimento
Edward I. Altman, pubblicato nella prima edizione del libro "Corporate Financial Distress: A Complete Guide to Predicting, Avoiding, and Dealing with Bankruptcy" (1983).[5][3]
### Formula
### Variabili
### Zone di discriminazione
Safe Zone: Z' > 2,90
Grey Zone: 1,23 < Z' < 2,90
Distress Zone: Z' < 1,23[3]
### Modifica chiave
L'unica differenza sostanziale rispetto al modello originale è la sostituzione del valore di mercato dell'equity con il valore contabile del patrimonio netto nella variabile X₄, poiché le imprese private non dispongono di capitalizzazione di mercato. I coefficienti sono stati ricalibrati di conseguenza, e il peso di X₄ si riduce da 0,6 a 0,420.[5][3]
### Accuratezza
Il modello Z' ha dimostrato un'accuratezza del 91% nella classificazione delle imprese fallite (30 su 33 nel campione originale) e del 97% per le imprese non fallite.[3]
### Commento
Questo modello ha reso possibile l'applicazione dell'analisi Z-Score all'enorme platea delle imprese non quotate, incluse le PMI. È il modello più utilizzato per l'analisi delle imprese italiane non quotate del settore manifatturiero.[6][4]
### 3. Z''-Score (1995) — Imprese Non Manifatturiere (Pubbliche e Private)
### Autore e riferimento
Edward I. Altman, pubblicato in "Corporate Financial Distress and Bankruptcy" (seconda edizione, 1993) e formalizzato nel paper "Emerging Market Corporate Bonds — A Scoring System" (Altman, Hartzell, Peck, 1995).[7][8][3]
### Formula (senza costante — versione base per non-manifatturiero)
### Variabili
### Zone di discriminazione
Safe Zone: Z'' > 2,60
Grey Zone: 1,10 < Z'' < 2,60
Distress Zone: Z'' < 1,10[9][3]
### Modifica chiave
La variabile X₅ (Sales / Total Assets) viene eliminata per rimuovere l'effetto settoriale legato alla rotazione degli asset, che varia enormemente tra industrie diverse (manifatturiero vs. servizi vs. retail). Il modello diventa così a 4 variabili, applicabile trasversalmente a tutti i settori industriali.[9][3]
### Commento
L'eliminazione del rapporto fatturato/attivo ha reso il modello molto più versatile e adatto a comparazioni cross-settoriali. È diventato il modello di riferimento per le analisi multi-settoriali a livello internazionale.[8][2]
### 4. Z''-Score EMS — Emerging Market Scoring Model (1995)
### Autori e riferimento
Edward I. Altman, John Hartzell e Matthew Peck, pubblicato nel paper "Emerging Market Corporate Bonds — A Scoring System" (Salomon Brothers, 1995) e approfondito nel paper "An Emerging Market Credit Scoring System for Corporate Bonds" (2005).[7][8][3]
### Formula
### Variabili
Identiche al modello Z'' (punto 3), con l'aggiunta di una costante pari a 3,25 che standardizza i punteggi in modo che uno score pari a zero equivalga a un rating D (default).[8][9][3]
### Zone di discriminazione (uguali al Z'' base)
Safe Zone: Z'' > 2,60
Grey Zone: 1,10 < Z'' < 2,60
Distress Zone: Z'' < 1,10[9][3]
### Bond Rating Equivalents (BRE) — Mediane Z''-Score per rating (2013)
### Commento
Il modello EMS è stato testato con successo su imprese messicane durante la crisi del peso (1994–1996), prevedendo correttamente ogni default. Il modello fu progettato per mercati dove mancano rating delle agenzie e dati di mercato liquidi; richiede però un'integrazione con fattori qualitativi aggiuntivi (rischio paese, rischio valutario, posizione competitiva). La costante 3,25 è stata aggiunta poiché la media degli Z''-Score nei mercati emergenti tendeva a essere significativamente più bassa rispetto ai mercati sviluppati.[10][3][9]
### 5. ZETA® Credit Risk Model (1977) — Proprietario
### Autori e riferimento
Edward I. Altman, Robert G. Haldeman e Paul Narayanan, pubblicato nel paper "ZETA™ Analysis: A New Model to Identify Bankruptcy Risk of Corporations" (Journal of Banking and Finance, 1977).[11][3]
### Struttura (7 variabili — coefficienti proprietari)
Il modello ZETA utilizza 7 variabili:
I coefficienti esatti sono proprietari e disponibili solo agli abbonati di ZETA Services, Inc.. Il cutoff è fissato a zero.[12][2][3]
### Campione e accuratezza
Il modello fu sviluppato su un campione di 53 imprese fallite e 58 non fallite, con attivi medi di circa 100 milioni di dollari, includendo sia imprese manifatturiere che retail. L'accuratezza fu superiore al 90% un anno prima del fallimento e del 70% fino a 5 anni prima — un miglioramento significativo rispetto allo Z-Score originale su orizzonti temporali lunghi.[2][3]
### Commento
Il modello ZETA rappresenta la "seconda generazione" degli Z-Score. Le principali innovazioni sono: (a) l'inclusione di imprese retail con capitalizzazione dei leasing; (b) l'introduzione della variabile di stabilità degli utili (trend pluriennale); (c) la variabile di dimensione (size). Il modello rimane in uso tra i professionisti ma la formula non è pubblica.[2]
### 6. Altman Z-Score Plus (2012) — Proprietario (Web App)
### Autori e riferimento
Edward I. Altman in collaborazione con Business Compass LLC (2012), disponibile come applicazione web e mobile su altmanzscore.com.[3]
### Caratteristiche
Non è un modello a sé stante, ma una piattaforma che calcola automaticamente lo Z, Z' o Z'' appropriato in base alle caratteristiche dell'impresa (quotata/non quotata, manifatturiera/non manifatturiera, mercato sviluppato/emergente). In aggiunta allo score, fornisce:
Probabilità di default stimata da 1 a 10 anni
Percentile di rischio rispetto al settore
Bond Rating Equivalent (BRE)[3]
### Commento
Il modello è proprietario e i dettagli completi non sono pubblici. Rappresenta la commercializzazione più completa della famiglia Z-Score.[3]
### 7. Modello SME per gli USA — Altman & Sabato (2007)
### Autori e riferimento
Edward I. Altman e Gabriele Sabato, pubblicato nel paper "Modelling Credit Risk for SMEs: Evidence from the U.S. Market" (Abacus, 2007).[13][14]
### Metodologia
A differenza dei modelli Z-Score classici basati sull'analisi discriminante lineare, questo modello utilizza la regressione logistica (logit) su dati panel di oltre 2.000 imprese USA con fatturato inferiore a 65 milioni di dollari, nel periodo 1994–2002. Le 5 variabili selezionate tramite procedura stepwise coprono le dimensioni di redditività, leva, liquidità, copertura e attività.[14][15][13]
### Risultati
Il modello logit per PMI ha una capacità predittiva out-of-sample circa il 30% superiore rispetto a un modello generico corporate (come lo Z''-Score).[14]
### Commento
Questo modello segna il passaggio dall'analisi discriminante alla regressione logistica per le PMI, con trasformazioni logaritmiche delle variabili per migliorare la capacità predittiva. È il predecessore diretto del modello italiano ZI-Score.[13][2]
### 8. Modello SME per il Regno Unito — Altman, Sabato & Wilson (2010)
### Autori e riferimento
Edward I. Altman, Gabriele Sabato e Nicholas Wilson, pubblicato nel paper "The Value of Non-Financial Information in SME Risk Management" (Journal of Credit Risk, 2010).[16][17]
### Innovazione chiave
Oltre alle variabili finanziarie del modello Altman-Sabato (2007), il modello include informazioni non finanziarie: azioni legali dei creditori, storia dei depositi di bilancio, opinioni di revisione, e caratteristiche specifiche dell'impresa. Il campione comprende oltre 5,8 milioni di set contabili di imprese non quotate UK, di cui 66.000 fallite nel periodo 2000–2007.[17]
### Risultati
L'inclusione dei dati non finanziari migliora significativamente il potere predittivo: l'AUC (Area Under the Curve) passa da 0,719 (solo variabili finanziarie) a 0,765 con l'inclusione delle variabili non finanziarie.[18]
### Commento
Questo studio ha dimostrato che le informazioni non finanziarie (compliance normativa, eventi legali, caratteristiche aziendali) possono essere determinanti nella previsione del default delle PMI, dove i dati contabili sono spesso limitati o ritardati.[17]
### 9. Modelli Specifici per l'Italia
9.1 Applicazione Z-Score alle Imprese Italiane in Amministrazione Straordinaria — Altman, Danovi & Falini (2013)
Autori: Edward I. Altman (NYU Stern), Alessandro Danovi (Università degli Studi di Bergamo) e Alberto Falini (Università degli Studi di Brescia).[19][20]
Riferimento: "Z-Score Models' Application to Italian Companies Subject to Extraordinary Administration", Journal of Applied Finance, No. 1, 2013, pp. 128–137. Pubblicato anche su Bancaria, aprile 2013.[21][22]
Contenuto: Lo studio applica i modelli Z-Score (sia Z' che Z'') a un campione di imprese italiane sottoposte ad Amministrazione Straordinaria (procedura concorsuale italiana paragonabile al Chapter 11 statunitense) nel periodo 2000–2010.[23][19]
Risultati chiave: Il modello ha confermato una buona efficacia predittiva, classificando correttamente il 72% delle imprese come già in zona distress prima dell'avvio della procedura. Tuttavia, gli autori concludono che le peculiarità italiane (struttura proprietaria concentrata, rapporto banca-impresa, normativa fallimentare differente) potrebbero richiedere lo sviluppo di parametri ad hoc per il contesto italiano.[21][23]
Commento: Questo è il primo studio che applica formalmente i modelli Z-Score di Altman alle grandi imprese italiane in crisi. L'osservazione sulla necessità di parametri specifici per l'Italia è particolarmente rilevante e ha ispirato lavori successivi.[21]
### 9.2 Test Empirico Z-Score su Imprese Quotate Italiane — Celli (2015)
Autore: Massimiliano Celli (Università degli Studi Roma Tre).
Riferimento: "Can Z-Score Model Predict Listed Companies' Failures in Italy? An Empirical Test", International Journal of Business and Management, Vol. 10, No. 3, 2015.[24]
Campione: 102 imprese industriali quotate alla Borsa Italiana nel periodo 1995–2013, di cui 51 con azioni sospese/delistate per default e 51 di controllo (stesso settore e anno).[24]
Risultati: Lo Z-Score funziona efficacemente nella previsione dei fallimenti delle imprese italiane, sebbene con un grado di affidabilità leggermente inferiore rispetto a quando applicato in contesti anglosassoni. Lo studio evidenzia che il modello è applicabile al contesto italiano, purché si tengano in considerazione alcune criticità specifiche illustrate nella ricerca.[24]
### 9.3 SME ZI-Score — Modello Specifico per PMI Italiane (2016)
Autori: Edward I. Altman, Gabriele Sabato e il team di Wiserfunding Ltd (co-fondata da Altman), in collaborazione con Classis Capital, Borsa Italiana e Confindustria.[25][26][27]
Riferimento: "Assessing the Credit Worthiness of Italian SMEs and Mini-Bond Issuers", Global Finance Journal, 2017 (working paper dal 2016).[27]
Struttura: Il modello ZI-Score è stato sviluppato specificamente per le PMI italiane e si articola in quattro modelli settoriali distinti:
### Manifatturiero
### Servizi
### Retail
Real Estate[25][7]
Ogni modello settoriale incorpora tre moduli:
Modulo finanziario — il driver principale del punteggio, basato su una selezione stepwise di variabili con validazione statistica[28]
Modulo non finanziario — esperienza del management, eventi legali, struttura societaria, engagement sui social media e copertura mediatica[28]
Modulo macroeconomico — variabili per riflettere lo stato corrente dell'economia e fornire stime forward-looking[28]
Campione: Oltre 14.500 PMI localizzate nel Nord Italia, poi certificato per rilevanza a livello nazionale.[7][25]
Output: Oltre allo score, il modello fornisce un Bond Rating Equivalent e una probabilità di default stimata.[26][25]
Applicazione ai Mini-Bond: Nel 2015, applicato a 97 emittenti di mini-bond quotati sull'ExtraMOT di Borsa Italiana, il modello ha rivelato che la maggioranza degli emittenti era classificata come non-investment grade, con il 32% in classe B e il 14% in classe CCC. Il profilo di rischio non sembrava influenzare significativamente il pricing dei bond.[26][7]
Commento: Questo è il modello più avanzato e specifico per la realtà italiana. A differenza dello Z-Score tradizionale, integra informazioni non finanziarie e macroeconomiche ed è calibrato sulla struttura dimensionale e settoriale del tessuto imprenditoriale italiano. I coefficienti esatti sono proprietari (Wiserfunding Ltd).[27][28]
### 9.4 Revisione dello Z-Score per PMI Italiane — Beltrame, Velliscig, Zorzi & Polato (2022)
Autori: Federico Beltrame e Gianni Zorzi (Ca' Foscari Venezia), Giulio Velliscig e Maurizio Polato (Università di Udine).[29]
Riferimento: "A Revision of Altman's Z-Score for SMEs: Suggestions from the Italian Bankruptcy Law and Pandemic Perspectives", Working Paper n. 9/2022, Università Ca' Foscari Venezia.[30][29]
Contesto: Lo studio è nato dall'introduzione del Codice della Crisi d'Impresa e dell'Insolvenza (D.Lgs. 14/2019) e del sistema di allerta elaborato dal CNDCEC (Consiglio Nazionale dei Dottori Commercialisti), confrontando questo sistema con lo Z-Score tradizionale.[29]
Campione: 86 PMI italiane (43 viable e 43 non-viable, con procedure avviate nel 2020), dati dal database AIDA (Bureau Van Dijk), periodo 2015–2019.[29]
Modelli sviluppati:
Z*-Score (revisione dello Z''-Score con coefficienti aggiornati):
Dove le variabili X₁–X₄ sono le stesse del modello Z''. Soglie: viable > 0,286; non-viable < 0,227.[29]
Z**-Score (Z-Score costruito con i 5 indici settoriali del CNDCEC):
Dove:
X₁ = Oneri finanziari / Ricavi
X₂ = Patrimonio netto / Debiti totali
X₃ = Cash flow / Totale attivo
X₄ = Attività correnti / Passività correnti
X₅ = Debiti previdenziali e tributari / Totale attivo
Soglie: viable > 1,476; non-viable < 1,146.[29]
Risultati comparativi (anno 2019, campione di 86 imprese):
Commento: Lo studio evidenzia i limiti sia dello Z-Score tradizionale (troppi falsi positivi tra le imprese sane italiane) sia del sistema di allerta CNDCEC (meno tempestivo nel segnalare le crisi). La combinazione dei due approcci — analisi discriminante multivariata con gli indici del CNDCEC — produce il miglior risultato predittivo. Lo Z-Score tradizionale sovraperforma il sistema di allerta nel classificare le imprese non viable (41 vs 33 su 43), ma fallisce clamorosamente nel classificare le imprese viable (solo 9 su 43 correttamente classificate come sane), probabilmente per le specificità strutturali delle PMI italiane (sottocapitalizzazione, bassi utili non distribuiti, elevato ricorso al debito).[29]
### 9.5 Varetto (1998) — Algoritmi Genetici per il Contesto Italiano
Autore: Franco Varetto (Centrale dei Bilanci, oggi Cerved).
Riferimento: "Genetic Algorithms Applications in the Analysis of Insolvency Risk", Journal of Banking & Finance, Vol. 22, 1998.[31][32]
Contenuto: Varetto confrontò la metodologia classica dell'analisi discriminante lineare (LDA) con gli algoritmi genetici (GA) su un campione di imprese italiane, per la previsione del fallimento a uno e tre anni. Lo studio conclude che i modelli LDA producono risultati leggermente migliori, ma i GA richiedono tempi computazionali inferiori e sono meno dipendenti dalla selezione manuale delle variabili.[32][31]
Commento: Questo lavoro rappresenta uno dei contributi più significativi alla modellistica di previsione dell'insolvenza specificamente italiana, e ha aperto la strada all'applicazione di tecniche di intelligenza artificiale all'analisi del rischio di credito in Italia.[31]
### 10. Tavola Riepilogativa di Tutti i Modelli
### 11. Nota sulla Versione "Re-Estimated Z-Score"
Sul sito ufficiale altmanzscore.com è riportata anche una versione ri-stimata dello Z-Score:
[12]
Questa versione è stata ottenuta ri-stimando i coefficienti del modello originale su campioni più recenti utilizzando la regressione logistica anziché l'analisi discriminante lineare. I segni negativi di alcuni coefficienti riflettono la diversa struttura della funzione logistica rispetto alla funzione discriminante. Altman stesso ha tuttavia suggerito cautela nell'uso di questa versione, in quanto i risultati non sono sistematicamente superiori al modello originale.[18][12]
### 12. Considerazioni Finali sull'Applicabilità al Contesto Italiano
L'applicazione dei modelli Z-Score alle imprese italiane presenta alcune sfide strutturali documentate in letteratura:
Sottocapitalizzazione cronica: le PMI italiane presentano tipicamente valori di patrimonio netto molto bassi rispetto al debito, generando Z-Score sistematicamente bassi e un eccesso di falsi positivi (imprese sane classificate come distressed)[29]
Utili non distribuiti limitati: la variabile X₂ (Retained Earnings / Total Assets) penalizza fortemente le imprese giovani e quelle con politiche di distribuzione degli utili aggressive[3]
Settore manifatturiero predominante: il tessuto industriale italiano è dominato da PMI manifatturiere, per le quali il modello Z' è teoricamente appropriato, ma i coefficienti calibrati su imprese USA potrebbero non catturare adeguatamente le dinamiche italiane[24][29]
Normativa fallimentare: il sistema italiano di prevenzione della crisi (CCII) ha introdotto un sistema di allerta basato su indici diversi da quelli dello Z-Score, creando l'opportunità di modelli "ibridi" come lo Z**-Score[29]
La direzione più promettente per il contesto italiano sembra essere l'integrazione tra la metodologia multivariata dello Z-Score e gli indici settoriali specifici elaborati dal CNDCEC, come dimostrato dal lavoro di Beltrame et al. (2022), che ha prodotto il modello con la migliore accuratezza complessiva nel campione testato.[29]