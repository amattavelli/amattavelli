# Modelli di Altman Z Score e varianti per l’Italia

# Modelli di Altman Z-Score e varianti per l’Italia
## Executive summary
Lo Z-Score nasce come funzione discriminante lineare per distinguere imprese “in bonis” e imprese prossime all’insolvenza usando poche variabili di bilancio (liquidità, redditività cumulata, redditività operativa, leva/solvibilità e rotazione dell’attivo). La versione “classica” (1968) è costruita su imprese manifatturiere quotate e incorpora un indicatore di mercato (valore di mercato del capitale proprio), quindi non è direttamente applicabile alle non quotate senza adattamenti strutturali. [1]
Nel corpus ufficiale ricostruibile con fonti verificabili emergono quattro “pilastri” della famiglia Z-score: (i) Z-Score (1968) per manifatturiere quotate; (ii) Z’-Score (1983) come ricalibrazione per manifatturiere non quotate sostituendo la variabile di mercato con una variabile contabile; (iii) Z’’-Score (1995) per non manifatturiere e applicazioni internazionali, eliminando la rotazione (Sales/Total Assets) per ridurre il bias settoriale e cambiando i pesi; (iv) EM-Score (modello “emerging markets”) che introduce un termine costante +3,25 per rendere confrontabili i punteggi con una scala tipo-rating (D = 0). [2]
Per l’Italia, le varianti più rilevanti (perché ricalibrate su dati italiani) sono: (a) il modello “Z-Score applicato alle PMI” di Pietro Bottani[3], Letizia Cipriani[4] e Francescomaria Serao[5] (2004), stimato con analisi discriminante su un campione bilanciato di 66 PMI manifatturiere italiane; (b) la famiglia ZI-Score (modelli logit settoriali) proposta da Maurizio Esentato[6] e Gabriele Sabato[7] con applicazione al mercato dei minibond, basata su un ampio dataset AIDA di PMI italiane e con metriche di performance (errori di I e II tipo, accuratezza, accuracy ratio) anche su campioni hold-out; (c) la revisione post‑pandemica che combina logica Z-score e “sistemi di allerta” italiani (2022) su un campione di PMI italiane 2015–2019. [8]
I punti critici, costanti nel tempo, sono: dipendenza da qualità/omogeneità contabile, sensibilità a definizioni (working capital, EBIT/EBITDA, riserve, riclassificazioni), trasferibilità “as-is” tra paesi/settori e instabilità dei cut-off al variare della popolazione (da cui la preferenza, in Italia, per ricalibrazioni e validazioni locali, soprattutto su PMI e in ottica early warning). [9]
## Fondamenti: logica dello Z-Score e significato delle variabili
Nella formulazione base, lo Z-score è una combinazione lineare di pochi rapporti, stimata con multiple discriminant analysis (MDA) per massimizzare la separazione tra due gruppi (distressed vs non‑distressed). L’idea economica è che la crisi non sia visibile in un solo indice, ma nel profilo congiunto di liquidità, redditività e struttura finanziaria. [10]
Le variabili della versione “classica” (1968) sono:
- X1 = Working capital / Total assets: liquidità netta a breve rispetto alla dimensione dell’attivo;
- X2 = Retained earnings / Total assets: redditività cumulata e “maturità”/capacità di autofinanziamento;
- X3 = EBIT / Total assets: efficienza operativa indipendente da leva e fiscalità;
- X4 = Market value of equity / Book value of total liabilities: “cuscinetto” di capitale (di mercato) rispetto all’indebitamento;
- X5 = Sales / Total assets: rotazione/efficienza d’impiego dell’attivo. [11]
Due implicazioni operative derivano direttamente da queste definizioni: (i) la presenza di X4 di mercato rende la versione 1968 coerente con società quotate; (ii) X5 è intrinsecamente settore‑sensibile, motivo per cui nelle evoluzioni successive viene eliminata per aumentare la trasferibilità a servizi/non manifatturiero e contesti internazionali. [12]
## La famiglia dei modelli Altman: modelli “canonici” e formule ufficiali
Di seguito sono riportati i modelli che, nelle fonti primarie e quasi‑primarie disponibili, risultano parte della “famiglia” Z-score (incluse le revisioni strutturali e l’EM‑Score). Le formule sono riportate con virgola decimale (notazione italiana), preservando i coefficienti originali.
Z-Score (1968) – manifatturiere quotate (USA)
Anno e riferimento primario: 1968 (sviluppo), ricostruzione e sintesi metodologica nel working paper/chapter 2002 del NYU Salomon Center[13] della New York University[14]. [15]
Formula completa:
con definizioni X1–X5 come sopra. [16]
Dataset e stima: campione iniziale di 66 imprese (33 distressed + 33 non‑distressed), manifatturiere; distressed = imprese che hanno presentato istanza di bankruptcy (Chapter X) nel periodo 1946–1965; campione “paired” stratificato per industria e dimensione; asset range limitato tra $1 e $25 milioni. [17]
Performance riportate: nel documento 2002 sono presentate accuratezze di classificazione anche su campioni successivi e con cut‑off 2,67 (e confronto con 1,81). In particolare, una tabella riporta accuratezze a 1 e 2 anni prima del failure per campione originale, holdout e campioni predittivi storici (1969–1975, 1976–1995, 1997–1999). [18]
Commenti critici e limiti: presupposti statistici della MDA (normalità multivariata, indipendenza/struttura di covarianza) sono spesso violati nei dati contabili; inoltre la trasferibilità temporale richiede cautela perché la distribuzione dei ratios cambia; nel documento 2002 è esplicitato che anche la scelta del cut‑off impatta sensibilmente errori e risultati. [19]
Z’-Score (1983) – manifatturiere non quotate
Anno e riferimento primario: 1983 (adattamento), formula riportata nel documento 2002. [20]
Formula completa:
dove X1, X2, X3 e X5 sono definiti come nel modello 1968; X4 viene sostituita (in logica) da una versione contabile (book value of equity / total liabilities), perché la variabile di mercato non è disponibile per imprese non quotate. [20]
Uso tipico: manifattura, imprese private/non quotate; utile quando l’obiettivo è mantenere la struttura a 5 variabili ma rendere il modello applicabile senza dati di borsa. [20]
Limiti: l’autore sottolinea che sostituzioni “ad hoc” in un modello pensato per quotate non sono “scientificamente valide” e preferisce una re‑stima completa; ciò rende Z’ concettualmente una ricalibrazione più solida rispetto a semplici proxy. [21]
Z’’-Score (1995) – non manifatturiere e applicazioni internazionali (“emerging markets”)
Anno e riferimento primario: 1995 (introduzione), formula e motivazione nel documento 2002. [22]
Formula completa (versione a 4 variabili):
dove X1 = working capital/total assets; X2 = retained earnings/total assets; X3 = EBIT/total assets; X4 = (book) equity/total liabilities. La variabile X5 (Sales/TA) viene rimossa per minimizzare distorsioni legate a settore e paese. [23]
Contesto d’uso dichiarato: non manifatturiero e imprese non‑US/mercati emergenti; nel documento 2002 si cita applicazione a imprese messicane emittenti Eurobonds in USD. [24]
Limiti: miglioramento di trasferibilità settoriale non elimina la necessità di tarature locali (cut‑off e prior aggiornati) e resta sensibile a riclassificazioni/qualità dei bilanci. [25]
EM-Score (emerging market score) – standardizzazione con costante
Anno e riferimento primario: formalizzato nel documento 2002 come estensione del modello “emerging market” con costante. [26]
Formula completa (standardizzazione):
La costante +3,25 è introdotta per standardizzare i punteggi ponendo 0 ≈ rating D (default) nella scala di equivalenza. [26]
Output “interpretativo”: nel documento 2002 sono riportate soglie di equivalenza rating basate su EM Score (AAA…D). [26]
Nota metodologica: l’equivalenza rating è una mappatura empirica (non un rating “ufficiale”), utile per comunicare rischio in linguaggio di mercato. [27]
ZETA® (1977) – “second generation” credit risk model
Anno e riferimento: 1977; nel documento 2002 è descritto come evoluzione “second‑generation” e viene esplicitato che il modello è proprietario e che i parametri non vengono completamente divulgati. [28]
Formula matematica: non specificata nelle fonti accessibili qui utilizzate, perché l’autore dichiara di non poter “fully disclose” i parametri in quanto proprietary. [28]
Contesto dichiarato: campione di corporations (manufacturers e retailers) e capacità di classificazione fino a 5 anni nel testo di sintesi; è inoltre citata sperimentazione con forme non lineari (es. quadratic) e confronto tra prestazioni in-sample e out-of-sample. [28]
Limite strutturale: la non piena trasparenza rende difficile replicare validazioni indipendenti, e sposta l’utilizzo verso contesti “vendor/proprietary model” più che verso implementazioni open. [28]
timeline
    title Evoluzione sintetica di modelli Z-score e affini
    1968 : Z-Score (quotate manifatturiere)
    1977 : ZETA (second generation, proprietario)
    1983 : Z'-Score (non quotate manifatturiere)
    1995 : Z''-Score (non manifatturiere / contesti internazionali)
    2002 : EM-Score (costante +3,25 e mapping a rating equivalenti)
    2004 : Ricalibrazione Italia PMI (Bottani-Cipriani-Serao)
    2016 : ZI-Score logit per PMI italiane e minibond
    2022 : Revisione Z-score per PMI italiane e sistemi di allerta
## Varianti calibrate per l’Italia e applicazioni “Italia‑centriche”
### Modello “Z-Score applicato alle PMI” (Italia, 2004)
Autori e fonte primaria: Pietro Bottani[3], Letizia Cipriani[4], Francescomaria Serao[5]; articolo pubblicato e diffuso come PDF istituzionale. [29]
Dataset (periodo, dimensione, fonte): campione bilanciato di 66 società (33 fallite + 33 non fallite), tutte PMI manifatturiere; il gruppo “fallite” è costituito da imprese dichiarate fallite nel 2002; bilanci analizzati: 1999 e 2000. [29]
Metodologia di stima: analisi discriminante lineare (funzione discriminante con coefficienti stimati). [29]
### Formula completa:
con area di classificazione:
- “sana” se 
- “destinata al fallimento” se 
- “area di incertezza” tra 4,846 e 8,105. [30]
Definizione delle variabili:
- 
- 
- 
- 
- 
dove (notazione del paper) AC attività correnti; PC passività correnti; AM imm. materiali; AI imm. immateriali; RF rimanenze finali; DL disponibilità liquide; RL riserva legale; RS riserva straordinaria; TA totale attività; UON utile operativo netto; PN patrimonio netto; TP totale passività; RV ricavi di vendita. [31]
Performance riportate: usando i dati di bilancio dell’esercizio 2000, gli autori riportano una percentuale di corretta classificazione pari al 94%; inoltre calcolano una misura di affidabilità via t‑test (con t = 7,14) che consente di attribuire alla funzione un “grado di accuratezza” del 99,9% nel senso indicato nel paper (hit ratio e verifica statistica). [32]
Commenti critici: i coefficienti molto elevati su  (riserve/attivo) rendono il modello potenzialmente sensibile a politiche di distribuzione/accantonamento e a differenze di schema contabile; inoltre la taratura è su un campione relativamente ridotto e settorialmente omogeneo (manifattura), quindi richiede re‑validazione out‑of‑sample per estensioni ad altri comparti o periodi. [33]
### Applicazione ad “amministrazione straordinaria” (Italia, 2000–2010)
Fonte e obiettivo dichiarato: una sintesi editoriale in Bancaria[34] descrive un test di accuratezza per l’Italia dello Z‑Score su imprese soggette a procedure di amministrazione straordinaria 2000–2010, indicando migliore efficacia della variante Z’’. [35]
Evidenza quantitativa accessibile: una versione testuale del lavoro (riprodotta online) riporta che il campione annuale utilizzato per l’analisi include, ad esempio, nell’anno 2009 1.575 imprese in sample e 413 “which met EA requirements”, con serie storica 2001–2009 e fonte dichiarata AIDA (nota nel testo). [36]
Dati non specificati nelle fonti qui accessibili: non risultano ricostruibili in modo completo (i) parametri “ad hoc” eventualmente stimati; (ii) metriche tipo AUC; (iii) dettagli completi su confusion matrix e cut‑off re‑stimati. Il testo editoriale, tuttavia, conclude che le peculiarità italiane “richiederebbero parametri ad hoc”. [37]
### ZI‑Score per PMI italiane e minibond (Italia, 2016; pubblicazione 2020)
Autori e contesto: studio su PMI italiane e minibond con affiliazioni che includono NYU Stern School of Business[38], Classis Capital SIM S.p.A[39] e WiserFunding Ltd[40]. [41]
Dataset (periodo, dimensione, fonte): database estratto da AIDA (fonte dichiarata), con 15.452 PMI “attive” e 1.000 “non‑attive”; dopo data cleansing circa 13% (2.032 imprese) è escluso. [42]
Per l’applicazione minibond: campione di 102 emittenti minibond (circa 5 non analizzabili per mancanza dati) e applicazione su 98 emittenti con dati disponibili; minibond quotati/tradati su Borsa Italiana[43] (piattaforma ExtraMOT Pro nel testo). [44]
Metodologia di stima: regressione logistica con selezione forward step‑wise; quattro modelli settoriali (manifattura, retail, servizi, costruzioni/real estate), con 6–8 variabili e trasformazioni; training su 80% e test su hold‑out 20% per ciascun settore. [42]
Forma matematica (logit): la forma generale di un modello logit per default (non essendo riportati qui i coefficienti puntuali settore‑specifici) è:
dove  sono gli indicatori/ratio (eventualmente trasformati) selezionati dal processo step‑wise, e  i coefficienti stimati. Il documento conferma l’uso della logistica e il numero di variabili per settore. [42]
Performance riportate (errori e accuracy ratio): nello studio sono pubblicati, per ciascun settore, errori di I tipo (miss su default), II tipo (false positive) e misure sintetiche di accuratezza e “accuracy ratio” (basato su CAP). Esempi principali (campione di sviluppo; tra parentesi hold‑out):
- Manifatturiero: Type I 6,92% (8,23%); Type II 26,57% (27,64%); accuratezza 83,26% (82,07%); accuracy ratio 93,08% (92,21%). [42]
- Retail: Type I 16,77% (18,54%); Type II 27,78% (28,89%); accuratezza 77,73% (76,29%); accuracy ratio 83,23% (81,76%). [42]
- Servizi: Type I 12,05% (14,88%); Type II 24,54% (26,43%); accuratezza 81,70% (79,35%); accuracy ratio 87,94% (84,12%). [42]
- Costruzioni & Real Estate: Type I 8,89% (10,12%); Type II 26,02% (28,24%); accuratezza 82,55% (80,82%); accuracy ratio 91,11% (89,86%). [42]
Mappatura a rating e PD: lo studio introduce i Bond Rating Equivalents (BRE) confrontando i punteggi logistici con profili medi di rating entity["company","Standard & Poor's","credit ratings"], e collega BRE a probabilità di default usando matrici di “mortality rates” (periodo 1971–2015; 2.903 emissioni) e un esempio di PD 1‑anno e 3‑anni per classe BRE. [45]
Commento critico: rispetto agli Z-score “canonici”, qui l’innovazione è duplice: (i) stima probabilistica (logit) invece di sola separazione discriminante; (ii) modello settoriale per ridurre il bias da rotazione/asset turnover. Rimane centrale la disponibilità/qualità di dati storici su default e una validazione “out‑of‑time” (oltre all’hold‑out) per stressare stabilità intertemporale. [46]
### Revisione post‑pandemica e integrazione con sistemi di allerta (Italia, 2022)
Autori: Federico Beltrame[47], Giulio Velliscig[48], Gianni Zorzi[49], Maurizio Polato[50]. [51]
Dataset (periodo, dimensione, fonte): dati annuali (2015–2019) da AIDA (Bureau van Dijk[52]) su un campione di PMI italiane dichiarato come “casual sample”; nel testo compare un refuso (“83”) ma la composizione indicata è 43 viable + 43 non‑viable, cioè 86 imprese. [51]
Disegno di confronto: confronto ex‑post tra “alert system” italiano del Consiglio Nazionale dei Dottori Commercialisti e degli Esperti Contabili[53] e Z‑score; applicazione di Z’ (manifattura, Ateco 2007 sezione C) e Z’’ (altri settori). [51]
### Formule riportate e usate nel confronto:
con definizioni delle variabili coerenti con la letteratura Altman (working capital/TA, retained earnings/TA, EBIT/TA, equity/total liabilities; e sales/TA per Z’). [51]
Metodologia di revisione: costruzione di funzioni discriminanti “aggiornate” (Z e Z*) usando software DTREG per ricalcolare coefficienti e cut‑off; valutazione tramite confusion matrix e confronti di corrette classificazioni. [51]
Performance riportate (in termini di corretta classificazione):
- per le non‑viable: Z‑score identifica correttamente 41/43 l’anno prima del fallimento vs alert system 33/43; inoltre è dichiarata maggiore rapidità media del segnale per Z‑score. [51]
- Z (versione NCCAAE del Z‑score) classifica correttamente 78/86; la nuova misura (alert system + Z) classifica correttamente 80/86 e identifica come non‑viable 41/43. [51]
Dati non specificati: nella versione disponibile risultano presenti placeholder (“Please insert Table …”), per cui i coefficienti numerici di Z e Z* e i cut‑off finali non sono integralmente ricostruibili dal testo mostrato. [51]
flowchart TD
A[Dati di bilancio] --> B[Scelta modello (Z, Z', Z'', EM o variante IT)]
B --> C[Calcolo ratio X (e riclassificazioni)]
C --> D[Applicazione formula / score]
D --> E[Classificazione o PD (se disponibile)]
E --> F[Azioni: covenant, rating interno, monitoraggio, early warning]
## Tabella comparativa dei modelli
Le formule e i vincoli d’uso dei modelli “canonici” (Z, Z’, Z’’, EM e ZETA) sono riportati nel documento 2002 e nei pannelli/tabelle associati. [54]
Le varianti italiane provengono dalle rispettive fonti: PMI Italia (2004), ZI‑Score (2016/2020) e revisione (2022). [55]
## Evidenza comparata e studi di confronto
Nel documento 2002, oltre alla formula, è presentata una tabella di accuratezza (Panel C) che confronta prestazioni del modello 1968 su campione originale, holdout e campioni storici, distinguendo tra 1 e 2 anni prima del failure e mostrando l’effetto del cutoff 2,67 vs 1,81 (tra parentesi). Questo è un esempio chiaro di come il parametro di classificazione sia parte integrante delle performance riportate. [18]
Nel blocco Italia‑PMI, il modello Bottani‑Cipriani‑Serao (2004) riporta un accurato esercizio di classificazione con correttezza 94% (bilanci 2000) e fornisce una procedura di verifica (t‑test) della significatività della hit ratio. È un caso “didattico” importante perché mostra l’effetto di riclassificazioni e definizioni contabili italiane sui ratio (es. uso di riserve legali/straordinarie). [33]
Per le PMI italiane in chiave “mercato dei capitali”, il modello ZI‑Score (logit) pubblica, settore per settore, sia le metriche tradizionali (errori di I e II tipo) sia una metrica “tipo‑AUC” derivata da CAP (accuracy ratio), e soprattutto riporta risultati anche su hold‑out. La figura seguente sintetizza due indicatori chiave (accuratezza complessiva e accuracy ratio) nei quattro settori. [42]
Infine, lo studio del 2022 combina Z-score e sistemi di allerta italiani mostrando un confronto diretto su confusion matrix: Z-score migliore sui non‑viable (41/43 vs 33/43) e una nuova misura integrata che raggiunge 80/86 corrette classificazioni nel campione (con i limiti di numerosità e di tabelle non pienamente visibili). [51]
Come esempio di confronto “macro” e di utilizzo dei proxy Z-score in contesti istituzionali, un lavoro della Banca d'Italia[56] confronta modelli (Distance‑to‑Default, Z‑scores e machine learning) e riporta misure di precision e false discovery rate per decili, evidenziando che approcci ML possono superare proxy come Z‑scores in specifici compiti (zombie/distress detection). [57]
## Limiti, trasferibilità e differenze tra quotate, non quotate, banche e PMI italiane
La principale differenza strutturale tra versioni per quotate e non quotate è la variabile X4: nella versione 1968 è un rapporto che richiede la capitalizzazione di mercato; per imprese non quotate l’adattamento coerente è una ricalibrazione (Z’) che sostituisce la variabile e modifica anche i pesi. Questo evita proxy arbitrari, ma mantiene la dipendenza da definizioni contabili di equity e debito. [58]
La differenza tra imprese manifatturiere e non manifatturiere è centrata su X5 (Sales/TA): la rotazione è fortemente settoriale e cross‑country; rimuoverla è la scelta esplicita che porta a Z’’ e al modello per mercati emergenti (con pesi modificati). Per l’Italia, questa scelta è particolarmente rilevante perché il tessuto produttivo è eterogeneo e l’asset turnover varia molto tra manifattura, servizi, costruzioni e real estate; infatti le ricalibrazioni italiane tendono a essere settoriali (ZI‑Score) o a segmentare per Ateco (revisione 2022). [59]
Per le banche (e, in generale, intermediari finanziari) lo Z-score “classico” non è progettato: (i) la struttura di bilancio è dominata da attività/passività finanziarie, (ii) il concetto di “sales” e la lettura di working capital non sono economicamente omogenei alle imprese industriali, (iii) la leva è fisiologicamente diversa. Nelle fonti qui utilizzate lo Z-score è trattato come modello per imprese non finanziarie e i confronti “bancari” compaiono soprattutto come proxy nei test comparativi, non come calibrazione dedicata. [60]
Per le PMI italiane, due traiettorie risultano empiricamente più coerenti delle applicazioni “as‑is”:
1) ricalibrazione MDA su campioni italiani omogenei (come nel modello 2004), che però richiede out‑of‑sample rigoroso; [32]
2) modelli probabilistici logit settoriali (ZI‑Score) con misure di errore e hold‑out, che sono più vicini all’uso bancario/creditizio moderno e possono essere collegati a PD e linguaggio di rating via BRE. [61]
In conclusione, l’evoluzione storica dei modelli Altman può essere letta come un progressivo spostamento da “un solo modello per tutti” a (i) segmentazione per popolazione (quotate/non quotate), (ii) robustezza settoriale (rimozione di X5), (iii) interpretabilità di mercato (rating equivalence e PD), fino alle ricalibrazioni locali e alle integrazioni con framework normativi di early warning (caso Italia 2022). [62]
[1] [2] [4] [5] [9] [10] [11] [12] [15] [16] [17] [18] [19] [20] [21] [22] [23] [24] [25] [26] [27] [28] [34] [39] [43] [47] [49] [50] [52] [53] [54] [56] [58] [59] [60] [62] https://web-docs.stern.nyu.edu/salomon/docs/S-02-11.pdf
### https://web-docs.stern.nyu.edu/salomon/docs/S-02-11.pdf
[3] [7] [8] [29] [30] [31] [32] [33] [55] https://www.to.camcom.it/sites/default/files/promozione-territorio/I_25.pdf
### https://www.to.camcom.it/sites/default/files/promozione-territorio/I_25.pdf
[6] [35] [37] https://www.bancaria.it/la-previsione-dell-insolvenza-l-applicazione-dello-z-score-alle-imprese-in-amministrazione-straordinaria/
https://www.bancaria.it/la-previsione-dell-insolvenza-l-applicazione-dello-z-score-alle-imprese-in-amministrazione-straordinaria/
[13] [40] [41] [42] [44] [45] [46] [61] https://www.greta.it/old/credit/credit2016/PAPERS/Friday/02_Altman_Esentato_Sabato.pdf
### https://www.greta.it/old/credit/credit2016/PAPERS/Friday/02_Altman_Esentato_Sabato.pdf
[14] [38] [51] https://www.unive.it/web/fileadmin/user_upload/dipartimenti/DMAN/pubblicazioni_scientifiche/working_papers/2022/2022wp09.pdf
https://www.unive.it/web/fileadmin/user_upload/dipartimenti/DMAN/pubblicazioni_scientifiche/working_papers/2022/2022wp09.pdf
[36] https://www.studocu.com/en-ca/document/royal-roads-university/financial-accounting/z-score-models-application-to/9384925
https://www.studocu.com/en-ca/document/royal-roads-university/financial-accounting/z-score-models-application-to/9384925
[48] [57] https://www.bancaditalia.it/pubblicazioni/altri-atti-convegni/2020-bi-frb-nontraditional-data/bargagli_stoffi_paper.pdf
https://www.bancaditalia.it/pubblicazioni/altri-atti-convegni/2020-bi-frb-nontraditional-data/bargagli_stoffi_paper.pdf