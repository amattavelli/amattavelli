#!/usr/bin/env python3
"""Genera l'articolo AI Act per Ratio usando python-docx."""

from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__),
    "AI_Act_2026_Obblighi_Aziende_Italiane.docx")

def set_heading_style(paragraph, level=1):
    """Imposta colore e formattazione ai titoli."""
    run = paragraph.runs[0] if paragraph.runs else paragraph.add_run()
    run.bold = True
    if level == 1:
        run.font.size = Pt(16)
        run.font.color.rgb = RGBColor(0x1A, 0x3A, 0x5C)   # blu scuro
    elif level == 2:
        run.font.size = Pt(13)
        run.font.color.rgb = RGBColor(0x2E, 0x6D, 0xA4)   # blu medio
    elif level == 3:
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)   # grigio scuro


def add_separator(doc):
    p = doc.add_paragraph()
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '2E6DA4')
    pBdr.append(bottom)
    pPr.append(pBdr)
    p.paragraph_format.space_after = Pt(6)


def add_box_paragraph(doc, text, bg_hex="EAF2FB"):
    """Paragrafo con sfondo colorato (simulato con bordi)."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.5)
    p.paragraph_format.right_indent = Cm(0.5)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    for side in ('top', 'left', 'bottom', 'right'):
        el = OxmlElement(f'w:{side}')
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), '12')
        el.set(qn('w:space'), '4')
        el.set(qn('w:color'), '2E6DA4')
        pBdr.append(el)
    pPr.append(pBdr)
    run = p.add_run(text)
    run.font.size = Pt(10)
    run.italic = True
    return p


def build_document():
    doc = Document()

    # ── Margini pagina ──────────────────────────────────────────────
    section = doc.sections[0]
    section.top_margin    = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin   = Cm(3.0)
    section.right_margin  = Cm(2.5)

    # ── Stile base ──────────────────────────────────────────────────
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)

    # ════════════════════════════════════════════════════════════════
    # TESTATA
    # ════════════════════════════════════════════════════════════════
    rubrica = doc.add_paragraph()
    rubrica.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = rubrica.add_run("RATIO  ·  Approfondimenti per Professionisti e Aziende")
    r.font.name = 'Calibri'
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x2E, 0x6D, 0xA4)
    r.bold = True

    data_p = doc.add_paragraph()
    data_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = data_p.add_run("Marzo 2026")
    r2.font.size = Pt(9)
    r2.font.color.rgb = RGBColor(0x88, 0x88, 0x88)

    add_separator(doc)

    # ── Titolo principale ───────────────────────────────────────────
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    title.paragraph_format.space_before = Pt(12)
    title.paragraph_format.space_after  = Pt(4)
    r_title = title.add_run(
        "AI Act 2026: cosa devono fare concretamente\nprofessionisti e aziende italiane"
    )
    r_title.bold = True
    r_title.font.size = Pt(20)
    r_title.font.color.rgb = RGBColor(0x1A, 0x3A, 0x5C)

    # ── Sottotitolo ─────────────────────────────────────────────────
    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.LEFT
    sub.paragraph_format.space_after = Pt(10)
    r_sub = sub.add_run(
        "Il 2 agosto 2026 scattano gli obblighi pieni del Regolamento europeo sull'intelligenza artificiale. "
        "Una guida operativa per studi professionali, PMI e consulenti d'impresa."
    )
    r_sub.font.size = Pt(12)
    r_sub.italic = True
    r_sub.font.color.rgb = RGBColor(0x44, 0x44, 0x44)

    add_separator(doc)

    # ════════════════════════════════════════════════════════════════
    # SEZIONE 1 – Il contesto
    # ════════════════════════════════════════════════════════════════
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after  = Pt(4)
    run_h = h.add_run("1. Il contesto: perché il 2026 è l'anno della svolta")
    run_h.bold = True
    run_h.font.size = Pt(14)
    run_h.font.color.rgb = RGBColor(0x1A, 0x3A, 0x5C)

    body1 = (
        "L'Intelligenza Artificiale non è più una promessa tecnologica: è già presente negli strumenti "
        "quotidiani di milioni di professionisti e imprese. ChatGPT, Copilot, sistemi di scoring del "
        "credito, algoritmi di selezione del personale, chatbot per l'assistenza clienti — tutto questo "
        "rientra nel perimetro regolato dal Regolamento (UE) 2024/1689, entrato in vigore il 1° agosto "
        "2024 e comunemente noto come AI Act.\n\n"
        "La struttura normativa prevede un'applicazione progressiva. Le prime scadenze sono già scattate: "
        "il 2 febbraio 2025 sono entrati in vigore i divieti sulle pratiche di AI «a rischio inaccettabile» "
        "e l'obbligo di alfabetizzazione del personale (art. 4). Il 2 agosto 2025 si sono aggiunti gli "
        "obblighi sui modelli di IA a uso generale (GPAI). La data cruciale per imprese e studi è però "
        "il 2 agosto 2026, quando la normativa diventa pienamente applicabile per tutti i sistemi "
        "classificati «ad alto rischio».\n\n"
        "Parallelamente, il quadro italiano si è completato con la Legge 132/2025 (la normativa nazionale "
        "sull'AI) e il Decreto Ministeriale n. 180/2025, che introduce linee guida operative sull'uso "
        "dell'intelligenza artificiale nei contesti lavorativi. Non si può più attendere."
    )
    p1 = doc.add_paragraph(body1)
    p1.paragraph_format.space_after = Pt(8)
    for run in p1.runs:
        run.font.size = Pt(11)

    # ════════════════════════════════════════════════════════════════
    # SEZIONE 2 – La classificazione per livelli di rischio
    # ════════════════════════════════════════════════════════════════
    h2 = doc.add_paragraph()
    h2.paragraph_format.space_before = Pt(12)
    h2.paragraph_format.space_after  = Pt(4)
    r2h = h2.add_run("2. La classificazione per livelli di rischio: dove si collocano le vostre attività")
    r2h.bold = True
    r2h.font.size = Pt(14)
    r2h.font.color.rgb = RGBColor(0x1A, 0x3A, 0x5C)

    p2 = doc.add_paragraph(
        "L'AI Act adotta una logica risk-based: gli obblighi crescono proporzionalmente al potenziale impatto "
        "del sistema sulle persone. È fondamentale capire in quale categoria rientrano gli strumenti già "
        "in uso nella propria organizzazione."
    )
    p2.paragraph_format.space_after = Pt(6)

    # Tabella livelli di rischio
    table = doc.add_table(rows=5, cols=3)
    table.style = 'Table Grid'
    table.autofit = True

    headers = ["Livello di rischio", "Esempi tipici", "Obblighi principali"]
    hdr_row = table.rows[0]
    for i, text in enumerate(headers):
        cell = hdr_row.cells[i]
        cell.text = text
        cell.paragraphs[0].runs[0].bold = True
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'), 'clear')
        shd.set(qn('w:color'), 'auto')
        shd.set(qn('w:fill'), '1A3A5C')
        tcPr.append(shd)

    rows_data = [
        ("Inaccettabile (vietato)",
         "Social scoring, manipolazione subliminale, riconoscimento biometrico real-time in spazi pubblici",
         "Divieto assoluto di utilizzo dal 2 febbraio 2025"),
        ("Alto rischio",
         "Selezione del personale, scoring del credito, sistemi di valutazione scolastica, dispositivi medici",
         "Valutazione di conformità, documentazione tecnica, supervisione umana obbligatoria, registrazione nel DB UE"),
        ("Trasparenza obbligatoria",
         "Chatbot, generatori di testi e immagini, deepfake",
         "Obbligo di informare l'utente che sta interagendo con un sistema AI; etichettatura dei contenuti generati"),
        ("Rischio minimo",
         "Filtri antispam, videogame, strumenti di produttività",
         "Nessun obbligo specifico, ma raccomandazione di adottare codici di condotta volontari"),
    ]

    for i, (col1, col2, col3) in enumerate(rows_data):
        row = table.rows[i + 1]
        row.cells[0].text = col1
        row.cells[1].text = col2
        row.cells[2].text = col3
        # Sfondo alternato
        if i % 2 == 0:
            fill_color = 'EAF2FB'
        else:
            fill_color = 'FFFFFF'
        for cell in row.cells:
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            shd = OxmlElement('w:shd')
            shd.set(qn('w:val'), 'clear')
            shd.set(qn('w:color'), 'auto')
            shd.set(qn('w:fill'), fill_color)
            tcPr.append(shd)

    doc.add_paragraph()  # spazio dopo tabella

    # ════════════════════════════════════════════════════════════════
    # SEZIONE 3 – Gli obblighi concreti
    # ════════════════════════════════════════════════════════════════
    h3 = doc.add_paragraph()
    h3.paragraph_format.space_before = Pt(12)
    h3.paragraph_format.space_after  = Pt(4)
    r3h = h3.add_run("3. Gli obblighi concreti: cosa fare entro il 2 agosto 2026")
    r3h.bold = True
    r3h.font.size = Pt(14)
    r3h.font.color.rgb = RGBColor(0x1A, 0x3A, 0x5C)

    subsections = [
        ("3.1  Mappatura degli strumenti AI in uso",
         "Il primo passo, obbligatorio e urgente, è l'inventario. Ogni organizzazione deve censire tutti i "
         "sistemi basati su AI attualmente utilizzati, anche quelli acquisiti come servizi da terze parti "
         "(SaaS). La mappatura deve includere: finalità del sistema, fornitore, dati trattati, impatto sulle "
         "persone e classificazione di rischio.\n\n"
         "Per gli studi professionali, questo significa includere i software gestionali con funzioni "
         "predittive, gli strumenti di redazione assistita, i sistemi di analisi di bilancio automatizzata "
         "e qualsiasi chatbot o assistente virtuale adottato per la comunicazione con i clienti."),
        ("3.2  Formazione obbligatoria del personale (AI Literacy)",
         "L'articolo 4 dell'AI Act impone che il personale che utilizza sistemi AI disponga di un livello "
         "adeguato di «alfabetizzazione sull'AI» (AI literacy). Non si tratta di formare tutti come "
         "tecnici informatici, ma di garantire che chi usa questi strumenti ne comprenda il funzionamento "
         "di base, i limiti e i rischi.\n\n"
         "Le aziende devono documentare i percorsi formativi svolti e conservare i relativi registri, "
         "che potranno essere richiesti in sede di ispezione. La formazione va calibrata sul ruolo: "
         "un consulente fiscale che usa un tool AI per l'analisi documentale ha esigenze diverse "
         "rispetto a un responsabile HR che utilizza un algoritmo di screening dei curriculum."),
        ("3.3  Supervisione umana e procedure di controllo",
         "Per i sistemi ad alto rischio, l'AI Act richiede che le decisioni finali rimangano in capo a "
         "un essere umano (human-in-the-loop). Questo principio ha implicazioni pratiche immediate: "
         "i flussi di lavoro devono essere ridisegnati per garantire che nessuna decisione rilevante "
         "— un rifiuto di credito, una valutazione del personale, una diagnosi medica — venga eseguita "
         "in modo interamente automatico senza revisione umana qualificata.\n\n"
         "Per gli studi professionali, questo si traduce nel definire chi è responsabile della "
         "validazione dell'output AI e come questa validazione viene documentata."),
        ("3.4  Qualità dei dati e documentazione tecnica",
         "I sistemi ad alto rischio richiedono che i dati di addestramento e utilizzo siano «pertinenti, "
         "sufficientemente rappresentativi, esenti da errori» e liberi da bias sistematici. Le imprese "
         "che sviluppano o personalizzano sistemi AI (non solo che li acquistano) devono predisporre "
         "una documentazione tecnica che dimostri il rispetto di questi requisiti e la marcatura CE "
         "previo passaggio da un organismo notificato.\n\n"
         "Chi invece acquista sistemi AI come servizi (fornitore terzo) deve richiedere al fornitore "
         "la documentazione di conformità e inserire clausole specifiche nei contratti di fornitura."),
        ("3.5  Valutazione di impatto sui diritti fondamentali (FRIA)",
         "Le autorità pubbliche e, in alcuni casi, gli operatori privati che utilizzano sistemi AI "
         "ad alto rischio sono tenuti a effettuare una Fundamental Rights Impact Assessment (FRIA) "
         "prima della messa in uso. Si tratta di una valutazione strutturata che analizza i rischi "
         "per i diritti fondamentali (privacy, non discriminazione, equità) e definisce le misure "
         "di mitigazione adottate."),
    ]

    for title_sub, body_sub in subsections:
        hs = doc.add_paragraph()
        hs.paragraph_format.space_before = Pt(10)
        hs.paragraph_format.space_after  = Pt(3)
        rhs = hs.add_run(title_sub)
        rhs.bold = True
        rhs.font.size = Pt(12)
        rhs.font.color.rgb = RGBColor(0x2E, 0x6D, 0xA4)

        pb = doc.add_paragraph(body_sub)
        pb.paragraph_format.space_after = Pt(6)
        for run in pb.runs:
            run.font.size = Pt(11)

    # ════════════════════════════════════════════════════════════════
    # SEZIONE 4 – Il regime sanzionatorio
    # ════════════════════════════════════════════════════════════════
    h4 = doc.add_paragraph()
    h4.paragraph_format.space_before = Pt(12)
    h4.paragraph_format.space_after  = Pt(4)
    r4h = h4.add_run("4. Il regime sanzionatorio: i rischi concreti")
    r4h.bold = True
    r4h.font.size = Pt(14)
    r4h.font.color.rgb = RGBColor(0x1A, 0x3A, 0x5C)

    p4 = doc.add_paragraph(
        "L'AI Act prevede un sistema sanzionatorio che — per portata — supera persino quello del GDPR. "
        "Le sanzioni sono graduate in tre fasce:\n"
    )
    p4.paragraph_format.space_after = Pt(4)

    sanctions = [
        ("Fascia massima (7% del fatturato globale o € 35 milioni)",
         "Violazione dei divieti su pratiche di AI inaccettabili o inosservanza dei requisiti sui dati per "
         "sistemi ad alto rischio."),
        ("Fascia media (3% del fatturato globale o € 15 milioni)",
         "Inosservanza di altri obblighi del regolamento (es. trasparenza, supervisione umana, "
         "documentazione tecnica)."),
        ("Fascia minima (1,5% del fatturato globale o € 7,5 milioni)",
         "Fornitura di informazioni inesatte o fuorvianti alle autorità di controllo."),
    ]

    for title_s, body_s in sanctions:
        bullet_p = doc.add_paragraph(style='List Bullet')
        bullet_p.paragraph_format.left_indent = Cm(0.5)
        bullet_p.paragraph_format.space_after = Pt(4)
        r_b = bullet_p.add_run(f"{title_s}: ")
        r_b.bold = True
        r_b.font.size = Pt(11)
        r_b2 = bullet_p.add_run(body_s)
        r_b2.font.size = Pt(11)

    note_pmi = doc.add_paragraph()
    note_pmi.paragraph_format.space_before = Pt(6)
    note_pmi.paragraph_format.space_after  = Pt(8)
    r_note = note_pmi.add_run(
        "Per le PMI e le start-up si applica l'importo più basso tra i due parametri (percentuale del "
        "fatturato o cifra fissa), a tutela dell'ecosistema innovativo europeo. Resta però l'obbligo "
        "sostanziale di conformarsi."
    )
    r_note.font.size = Pt(11)
    r_note.italic = True

    # ════════════════════════════════════════════════════════════════
    # SEZIONE 5 – Roadmap pratica
    # ════════════════════════════════════════════════════════════════
    h5 = doc.add_paragraph()
    h5.paragraph_format.space_before = Pt(12)
    h5.paragraph_format.space_after  = Pt(4)
    r5h = h5.add_run("5. Roadmap pratica: i passi da compiere adesso")
    r5h.bold = True
    r5h.font.size = Pt(14)
    r5h.font.color.rgb = RGBColor(0x1A, 0x3A, 0x5C)

    roadmap_intro = doc.add_paragraph(
        "Con meno di cinque mesi alla scadenza del 2 agosto 2026, non c'è tempo per approcci "
        "attendisti. Ecco le azioni prioritarie, ordinate per urgenza."
    )
    roadmap_intro.paragraph_format.space_after = Pt(6)

    steps = [
        ("Aprile–Maggio 2026 — Inventario e classificazione",
         "Censire tutti gli strumenti AI in uso (inclusi quelli integrati in software gestionali, "
         "CRM, HR, analisi finanziaria). Classificare ciascuno per livello di rischio AI Act."),
        ("Maggio 2026 — Contratti con i fornitori",
         "Rivedere i contratti con i fornitori di software AI e richiedere la documentazione di "
         "conformità all'AI Act. Inserire clausole di garanzia e di aggiornamento normativo."),
        ("Maggio–Giugno 2026 — Formazione del personale",
         "Avviare i percorsi di AI literacy differenziati per ruolo. Documentare e archiviare "
         "i registri formativi. Designare un referente interno per la conformità AI."),
        ("Giugno 2026 — Ridisegno dei processi (sistemi alto rischio)",
         "Per i sistemi classificati ad alto rischio, ridefinire i flussi decisionali garantendo "
         "la supervisione umana. Predisporre la documentazione tecnica e le procedure di monitoraggio."),
        ("Luglio 2026 — Audit interno pre-scadenza",
         "Effettuare una verifica interna (o avvalersi di un consulente esterno) per validare "
         "la completezza degli adempimenti prima del 2 agosto 2026."),
    ]

    for num, (step_title, step_body) in enumerate(steps, 1):
        step_p = doc.add_paragraph()
        step_p.paragraph_format.space_before = Pt(6)
        step_p.paragraph_format.space_after  = Pt(2)
        r_st = step_p.add_run(f"  {num}.  {step_title}")
        r_st.bold = True
        r_st.font.size = Pt(11)
        r_st.font.color.rgb = RGBColor(0x2E, 0x6D, 0xA4)

        body_p = doc.add_paragraph(f"     {step_body}")
        body_p.paragraph_format.left_indent = Cm(0.5)
        body_p.paragraph_format.space_after = Pt(4)
        for run in body_p.runs:
            run.font.size = Pt(11)

    # ════════════════════════════════════════════════════════════════
    # SEZIONE 6 – Riflessione finale
    # ════════════════════════════════════════════════════════════════
    h6 = doc.add_paragraph()
    h6.paragraph_format.space_before = Pt(12)
    h6.paragraph_format.space_after  = Pt(4)
    r6h = h6.add_run("6. Una riflessione finale: conformità come opportunità")
    r6h.bold = True
    r6h.font.size = Pt(14)
    r6h.font.color.rgb = RGBColor(0x1A, 0x3A, 0x5C)

    closing = doc.add_paragraph(
        "Sarebbe un errore interpretare l'AI Act esclusivamente come un adempimento burocratico. "
        "Le imprese che governano bene i propri sistemi AI — con processi trasparenti, personale "
        "formato e documentazione ordinata — costruiscono un vantaggio competitivo reale: la fiducia "
        "di clienti, partner e investitori.\n\n"
        "In un mercato in cui l'AI diventa infrastruttura, la governance dell'intelligenza artificiale "
        "è la nuova frontiera della reputazione aziendale. I professionisti — avvocati, commercialisti, "
        "consulenti del lavoro, advisor strategici — hanno qui un'opportunità concreta di affiancare "
        "i propri clienti in un percorso che va ben oltre il mero adeguamento normativo: si tratta "
        "di ripensare processi, responsabilità e cultura organizzativa alla luce di un paradigma "
        "tecnologico che non tornerà indietro.\n\n"
        "Chi si adegua oggi non risponde soltanto a una norma. Costruisce l'azienda di domani."
    )
    closing.paragraph_format.space_after = Pt(12)
    for run in closing.runs:
        run.font.size = Pt(11)

    # ════════════════════════════════════════════════════════════════
    # BOX «In sintesi»
    # ════════════════════════════════════════════════════════════════
    add_separator(doc)
    box_title = doc.add_paragraph()
    box_title.paragraph_format.space_before = Pt(10)
    r_bt = box_title.add_run("IN SINTESI — Le date chiave dell'AI Act")
    r_bt.bold = True
    r_bt.font.size = Pt(11)
    r_bt.font.color.rgb = RGBColor(0x1A, 0x3A, 0x5C)

    key_dates = [
        "2 febbraio 2025: divieto pratiche AI inaccettabili + obbligo AI literacy.",
        "2 agosto 2025: applicazione obblighi su modelli GPAI (uso generale).",
        "2 agosto 2026: piena operatività AI Act — obblighi su sistemi ad alto rischio.",
        "2 agosto 2027: ulteriori obblighi per alcune categorie specifiche (art. 6(1)).",
    ]
    for date_item in key_dates:
        d_p = doc.add_paragraph(f"• {date_item}")
        d_p.paragraph_format.left_indent = Cm(0.5)
        d_p.paragraph_format.space_after = Pt(2)
        for run in d_p.runs:
            run.font.size = Pt(10)

    add_separator(doc)

    # ── Fonti ────────────────────────────────────────────────────────
    fonti_title = doc.add_paragraph()
    fonti_title.paragraph_format.space_before = Pt(10)
    r_ft = fonti_title.add_run("Riferimenti normativi e fonti")
    r_ft.bold = True
    r_ft.font.size = Pt(10)
    r_ft.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    sources = [
        "Regolamento (UE) 2024/1689 — AI Act (GU UE, 12 luglio 2024)",
        "Legge 132/2025 — Normativa italiana sull'intelligenza artificiale",
        "Decreto Ministeriale n. 180/2025 — Linee guida sull'uso dell'AI nei contesti lavorativi",
        "Commissione europea — Codice di buone pratiche sull'AI per le PMI",
        "Cefriel — Vademecum AI Act per le PMI italiane (2025)",
        "Cybersecurity360.it — AI Act: divieti, sanzioni e scadenze (marzo 2026)",
        "BSDLegal — AI Act: scadenze e obblighi per il 2026",
    ]
    for src in sources:
        s_p = doc.add_paragraph(f"· {src}")
        s_p.paragraph_format.left_indent = Cm(0.3)
        s_p.paragraph_format.space_after = Pt(2)
        for run in s_p.runs:
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    # ── Footer note ──────────────────────────────────────────────────
    footer_p = doc.add_paragraph()
    footer_p.paragraph_format.space_before = Pt(16)
    footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_footer = footer_p.add_run(
        "Articolo a cura della redazione Ratio  ·  Marzo 2026\n"
        "Il presente contributo ha finalità informative e non costituisce parere legale."
    )
    r_footer.font.size = Pt(8)
    r_footer.font.color.rgb = RGBColor(0x99, 0x99, 0x99)
    r_footer.italic = True

    # ── Salvataggio ─────────────────────────────────────────────────
    doc.save(OUTPUT_PATH)
    print(f"Documento salvato: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_document()
