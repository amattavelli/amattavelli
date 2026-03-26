# ISTRUZIONI EDITORIALI — Ratio

Questo file definisce le regole editoriali per la creazione degli articoli
nella cartella `Ratio/articoli/`. Deve essere letto prima di ogni sessione
di scrittura.

---

## Identità editoriale

**Ratio** è una rubrica di approfondimento sull'intelligenza artificiale
rivolta a professionisti (commercialisti, consulenti, controller) e
responsabili aziendali di piccole e medie imprese italiane.

L'obiettivo non è informare su novità tecnologiche in astratto, ma aiutare
il lettore a capire cosa cambia concretamente nel suo lavoro.

---

## Struttura degli articoli

Ogni articolo segue questa sequenza:

1. **Apertura** — descrizione di un fenomeno, problema o situazione concreta
   che il lettore riconosce. Niente definizioni. Niente "cos'è X".
2. **Sviluppo** — analisi con esempi pratici, implicazioni operative,
   eventuali riferimenti normativi o gestionali pertinenti.
3. **Chiusura** — una riflessione o un'indicazione operativa. Non un
   riassunto di quanto detto sopra.

---

## Tono e stile

- Prima parte: divulgativo, scorrevole, accessibile anche a chi non è tecnico.
- Parte centrale: progressivamente più tecnico-pratico.
- Lunghezza: **800–1000 parole**.
- Persona: prima plurale ("noi", "ci troviamo") oppure seconda singolare
  diretta ("se gestisci uno studio..."). Mai la terza impersonale distante.

---

## Regole da rispettare sempre

- Niente punti elenco nel corpo dell'articolo. Usare prosa continua.
- Niente grassetti sparsi. Il grassetto è riservato ai titoli di sezione
  se presenti.
- Niente frasi che iniziano con "E..." come congiunzione di apertura.
- Niente strutture del tipo "Non è X... è Y".
- Niente incipit del tipo "Nell'era digitale", "Viviamo in un momento
  storico", "L'intelligenza artificiale sta cambiando tutto".
- Niente conclusione-riassunto ("In sintesi abbiamo visto che...").
- Niente trattino em (—) per gli incisi. Usare la virgola o le parentesi.
- Evitare locuzioni tipiche dell'AI: "è fondamentale sottolineare",
  "è importante ricordare", "non bisogna dimenticare", "in questo contesto".

---

## Titolo

Il titolo deve essere specifico e concreto. Evitare titoli generici
("AI e lavoro", "Il futuro dell'intelligenza artificiale").
Preferire titoli che enunciano un problema o una tesi
("Quando l'AI sbaglia e nessuno se ne accorge",
"Delegare all'AI: cosa firma davvero il professionista").

---

## Ricerca

Prima di scrivere, cercare sul web un tema recente (ultimi 30 giorni)
rilevante per professionisti italiani o aziende. Privilegiare:
- nuovi modelli o strumenti con impatto pratico immediato
- sviluppi normativi (AI Act, responsabilità, privacy)
- casi d'uso concreti nel settore contabile, legale o gestionale

---

## Salvataggio

Salvare ogni articolo come file `.docx` nel percorso:

```
Ratio/articoli/YYYY-MM-DD_titolo-breve.docx
```

Usare `python-docx` per generare il file. Il nome breve nel filename
deve essere in minuscolo con trattini, senza spazi né accenti
(es. `2026-03-21_responsabilita-ai-professionisti.docx`).
