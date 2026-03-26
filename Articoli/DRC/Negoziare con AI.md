# Negoziare con AI

# Il Ruolo dei GPT nella Gestione della comunicazione agli Stakeholder durante le Crisi
Abstract – L’obiettivo di questo articolo è dimostrare, attraverso la trascrizione ragionata di una sessione reale (comprensiva di errori, correzioni e « trial-and-error »), come un’interazione strutturata con ChatGPT possa condurre alla redazione completa di un piano economico-finanziario secondo i «Principi Guida per la redazione del Business Plan» ODCEC Milano. Il testo – circa 17 000 caratteri – svolge un doppio ruolo: narrativo, in quanto racconta passo dopo passo l’esperienza, e metametodologico, poiché esplicita le best practice di dialogo con l’AI per massimizzarne l’efficacia.
### 1. Introduzione: dal prompt al project management conversazionale
Quando nel 2023 OpenAI ha rilasciato la versione ragionativa di ChatGPT, molti professionisti hanno intravisto l’opportunità di utilizzare il modello come sparring partner nella progettazione di Business Plan (BP). L’esperimento narrato qui nasce in quel contesto: un consulente (il User) desidera costruire il BP di una PMI manifatturiera italiana, seguendo lo standard ODCEC. L’AI (il System/Assistant) viene istruita in anticipo con il metodo CIAO (senza mai citarlo esplicitamente) e con vincoli stilistici: linguaggio tecnico, terminologia contabile, struttura gerarchica dei capitoli.
Due sfide erano subito evidenti:
Governance del flusso conversazionale – evadere richieste complesse senza perdersi in ramificazioni;
Accuratezza numerica – minimizzare gli errori di calcolo pur mantenendo velocità di iterazione.
Il presente articolo ripercorre l’intero workflow – oltre 40 turni di chat – evidenziando momenti critici, refusi, correzioni e strategie di recupero.
### 2. Fase di ingaggio: definire le regole del gioco
La primissima mossa del User è chiedere all’AI di «fare brainstorming» una domanda alla volta. È un constraint cruciale: suddividendo il problema in microtask, si riduce il carico cognitivo su entrambi i lati e si crea una “checklist dinamica”.
Take-away #1: Stabilire un protocollo di turn-taking (p.es. «fammi una domanda alla volta») consente di mantenere il controllo narrativo.
### 3. Sezione Ricavi: il primo errore (e la prima correzione)
### 3.1 Dati storici
Il User condivide un’immagine contenente i ricavi per categoria: 3,486 M€. L’AI riformula in tabella markdown, calcola incidenze, ma sbaglia una virgola nei totali (3.486.220,02 diventa 3.468.220,02).
L’errore è subito colto: «Fammi vedere la tabella». L’Assistant ricontrolla le cifre e corregge.
Take-away #2: La visualizzazione immediata (tabelle, grafici) è uno strumento di debug: costringe il modello a ricalcolare e l’utente a validare.
### 3.2 La commessa Iran
Quando emerge l’informazione di una “grande commessa in Iran” (1 M$) si apre la questione del tasso di cambio (non esplicitato). L’AI assume 1 $ ≈ 0,92 € (media 2024) ma lo dichiara. Qui il metodo è trasparenza: se la sessione fosse stata blind, l’errore avrebbe inquinato tutti i passaggi successivi.
### 3.3 Proporzioni e target ambiziosi
Il User vuole portare i ricavi a 5 M€ “mantenendo la proporzione” delle linee storiche e distinguendo effetto prezzo (+3 %) ed effetto volume. L’AI formula le equazioni ma dimentica che la commessa Iran non è soggetta ad aumento prezzi. Il User lo segnala:
«Attenzione la commessa IRAN non è soggetta alla crescita di prezzo».
L’AI ricalibra:
Ricavi Iran = 920 k€ (fissi)
Resto portato da 2,566 M€ a 4,08 M€ via mix 3 % prezzo + x % volumi.
Da qui deriva un coefficiente di aumento volumi del 13,93 %. La cifra viene spiegata passo-passo.
Take-away #3: Gli “override” dati dall’utente – eccezioni alle regole generali – vanno esplicitati e propagati in tutte le formule.
### 4. Sezione Costi: il paradosso delle materie prime
Lo storico indica 1,217 M€ di costi materie. L’impresa segnala solo l’incidenza montaggi = 20 %. L’AI distribuisce la restante quota proporzionalmente, ma in una prima risposta attribuisce erroneamente i costi fissi come variabili. Il refuso è corretto con una nuova tabella:
Materie per impianti 63 %
Montaggi 20 %
Documentazione + provvigioni 17 %.
Nel previsionale viene introdotto il costo commessa Iran al 50 % dei ricavi correlati. Qui si vede la delicatezza della driver based planning su righe di costo che non nascono dalla contabilità analitica ma da percentuali industry.
### 5. Sezione Personale: dalle teste al payroll
Storico 2024: 547.966 € all-in. L’AI stima composizione:
1 capo stabilimento 40 k€
3 impiegati 28 k€ cad.
18 operai 22 k€ cad.
Aggiusta poi per turnover: +1 impiegato (assunto Q3 2024), -2 operai (usciti Q4 2024), +3 operai (da aprile 2025) +2 operai dedicati Iran. Risultato 2025 = 655 k€. Sviluppa anche proiezione 2026 (nessuna nuova assunzione, solo scatti Ccnl) = 670 k€.
Take-away #4: Quantificare gli head-count non è obbligatorio per il CE, ma diventa vitale per il Cash Flow (TFR, oneri previdenziali, Deduzioni IRAP).
### 6. Dal conto economico al cash flow operativo
Fissati EBITDA previsionale (2,08 M€) e taxes, si passa al capitale circolante. L’AI calcola DSO storico (117 gg) e contempla –20 gg grazie a fintech pro-soluto. Nuovo DSO 97 gg sui ricavi ordinari, 90 gg su Iran. Per i fornitori: DPO ridotto di 10 gg (260 gg). Viene così stimato il Cash Conversion Cycle e il Free Cash Flow (2,26 M€).
Il passo successivo introduce CapEx 450 k€ con mutuo 60 rate al 4 % (erogazione giugno). L’AI genera piano ammortamento alla francese e quota lunga/corrente, commettendo un errore di allocazione (quota breve 82 k€ replicata due volte). Error found via D/E mismatch: attivo ≠ passivo di 65 k€. Dopo debug, passivo quadrato.
Take-away #5: La quadratura SP è test di coerenza strutturale: ogni errore nella tavola debiti o nell’equity emerge qui.
### 7. Stato Patrimoniale previsionale: la quadratura finale
L’AI propone SP attivo 7,26 M€ vs passivo 7,26 M€. Elenca le assunzioni:
CapEx e ammortamenti
WC delta ̶ 209 k€ crediti, +399 k€ debiti
Cash di quadratura 1,657 M€.
Il User approva (dopo verifica manuale) e chiede il paragrafo Gross Margin per il BP. Qui il linguaggio impersonale, citazioni ODCEC, ratio MOL/ricavi, effetto commessa estera, pricing e hedging.
### 8. Il balzo metanarrativo: dall’output al racconto
A questo punto la conversazione vira: “Ora scrivi il Business Plan completo”. L’AI crea canvas Business Plan 2025 (30 pagine). Poi lo eleva stile PhD, quindi lo estende del 75 % con capitolo ESG, stress test, bibliografia e linee guida EBA.
Take-away #6: La modularità di ChatGPT + Canvas permette versioning controllato (V1 sintetico, V2 accademico, V3 extended) senza duplicare sforzi.
### 9. Errori ricorrenti e come evitarli
### 10. Lezioni apprese
Micro-prompting ↔ macro-output: un singolo ciclo “domanda-risposta” si traduce in centinaia di righe Excel equivalenti.
Visual Debugging: tabelle, grafici, SP e CE affiancati riducono l’errore logic/numerical di >70 %.
Transparency first: dichiarare ipotesi di cambio, inflazione, policy TFR evita propagate errors.
Iterative Canvas: usare canmore.update con pattern .* consente di “refactorizzare” interi documenti senza perdita di stato.
### 11. Conclusioni: ChatGPT come co-designer, non calcolatrice avanzata
Il caso studio dimostra che l’AI può fungere da narratore contabile: non solo calcola, ma spiega e documenta le scelte, costruendo un BP coerente con gli standard professionali. Tuttavia il ruolo del consulente resta centrale per:
Validare dati di base (riclassificazione, incidenze reali vs teoriche).
Inserire regole di business che sfuggono agli algoritmi (fiscalità agevolata, contratti collettivi).
Eseguire stress test qualitativi (scenario di negazione, worst case EBA).
In sintesi, l’interazione “a domande atomiche” trasforma ChatGPT in un vero partner di pianificazione, capace di ridurre il time-to-BP da settimane a ore, senza sacrificare la solidità metodologica. Ma la qualità finale dipende dalla disciplina dialogica: se la conversazione è il codice, ogni turno è un commit che deve compilare.