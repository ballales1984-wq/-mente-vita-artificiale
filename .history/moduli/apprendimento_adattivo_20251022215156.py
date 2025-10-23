"""
🎓 MODULO APPRENDIMENTO ADATTIVO - Fase 3 AGI
Valuta pensieri, modifica comportamento, evolve nel tempo
"""

import json
from typing import Dict, List, Any
from pathlib import Path
from collections import defaultdict

class ApprendimentoAdattivo:
    """
    Sistema di apprendimento che migliora nel tempo
    Funzioni:
    - Valuta pensieri in base a esiti
    - Modifica probabilità decisioni
    - Rinforzo positivo/negativo
    - Evoluzione comportamentale
    """
    
    def __init__(self, path_pensieri="memoria_permanente/pensieri_valutati.jsonl"):
        self.nome = "Apprendimento Adattivo"
        self.path_pensieri = Path(path_pensieri)
        self.path_pensieri.parent.mkdir(exist_ok=True)
        
        # Probabilità decisioni (peso per ogni azione)
        self.probabilita_decisioni = defaultdict(lambda: 1.0)
        
        # Carica pesi se esistono
        path_pesi = Path("memoria_permanente/pesi_decisioni.json")
        if path_pesi.exists():
            with open(path_pesi, 'r') as f:
                loaded = json.load(f)
                self.probabilita_decisioni.update(loaded)
        
        print(f"[{self.nome}] Inizializzato")
        print(f"  • Pesi caricati: {len(self.probabilita_decisioni)} azioni")
    
    def valuta_pensiero(self, pensiero: Dict) -> int:
        """
        Valuta pensiero in base a esito
        
        Args:
            pensiero: Episodio cognitivo
            
        Returns:
            Punteggio: +1 (successo), 0 (neutro), -1 (fallimento)
        """
        # Valutazione da esito
        esito = pensiero.get("esito", "")
        successo = pensiero.get("successo", False)
        
        if successo:
            return +1
        elif "fallita" in str(esito).lower() or "errore" in str(esito).lower():
            return -1
        else:
            return 0
    
    def aggiorna_pensiero(self, pensiero: Dict) -> Dict:
        """
        Aggiunge valutazione al pensiero
        
        Args:
            pensiero: Episodio da valutare
            
        Returns:
            Pensiero con valutazione
        """
        punteggio = self.valuta_pensiero(pensiero)
        pensiero["valutazione"] = punteggio
        pensiero["timestamp_valutazione"] = str(datetime.now())
        
        return pensiero
    
    def aggiorna_comportamento(self, pensiero: Dict):
        """
        Modifica probabilità decisioni future
        
        Args:
            pensiero: Pensiero valutato
        """
        decisione = pensiero.get("azione", pensiero.get("decisione", ""))
        punteggio = pensiero.get("valutazione", 0)
        
        if decisione:
            # Rafforza o indebolisce
            self.probabilita_decisioni[decisione] += punteggio * 0.1
            
            # Limiti: 0.1 - 5.0
            self.probabilita_decisioni[decisione] = max(0.1, 
                min(self.probabilita_decisioni[decisione], 5.0))
    
    def salva_pensiero_valutato(self, pensiero: Dict):
        """Salva pensiero con valutazione"""
        with open(self.path_pensieri, "a", encoding="utf-8") as f:
            f.write(json.dumps(pensiero, ensure_ascii=False) + "\n")
    
    def salva_pesi(self):
        """Salva pesi decisioni"""
        path_pesi = Path("memoria_permanente/pesi_decisioni.json")
        with open(path_pesi, 'w', encoding="utf-8") as f:
            json.dump(dict(self.probabilita_decisioni), f, indent=2)
    
    def carica_pensieri_passati(self) -> List[Dict]:
        """Carica pensieri da file"""
        pensieri = []
        if self.path_pensieri.exists():
            with open(self.path_pensieri, "r", encoding="utf-8") as f:
                for riga in f:
                    try:
                        pensiero = json.loads(riga.strip())
                        pensieri.append(pensiero)
                    except:
                        continue
        return pensieri
    
    def trova_schemi(self, pensieri: List[Dict], soglia=5) -> Dict:
        """
        Trova schemi ricorrenti
        
        Args:
            pensieri: Lista pensieri passati
            soglia: Minimo occorrenze per schema
            
        Returns:
            Dict con schemi trovati
        """
        schemi = defaultdict(lambda: defaultdict(int))
        
        for p in pensieri:
            # Chiave: situazione (vista + udito + emozione)
            vista = p.get("descrizione", "")[:30]  # Prime 30 char
            udito = p.get("audio", "")[:20]
            emozione = p.get("emozione", "neutro")
            
            chiave = (vista, udito, emozione)
            decisione = p.get("azione", p.get("decisione", ""))
            valutazione = p.get("valutazione", 0)
            
            if decisione:
                schemi[chiave][decisione] += valutazione
        
        # Filtra per soglia
        schemi_significativi = {}
        for chiave, decisioni in schemi.items():
            for decisione, punteggio in decisioni.items():
                if punteggio >= soglia:
                    if chiave not in schemi_significativi:
                        schemi_significativi[chiave] = {}
                    schemi_significativi[chiave][decisione] = punteggio
        
        return schemi_significativi
    
    def genera_regole(self, schemi: Dict) -> List[Dict]:
        """
        Trasforma schemi in regole decisionali
        
        Args:
            schemi: Schemi ricorrenti trovati
            
        Returns:
            Lista regole applicabili
        """
        regole = []
        
        for chiave, decisioni in schemi.items():
            vista, udito, emozione = chiave
            
            for decisione, punteggio in decisioni.items():
                regola = {
                    "condizione": {
                        "vista": vista,
                        "udito": udito,
                        "emozione": emozione
                    },
                    "azione": decisione,
                    "punteggio": punteggio,
                    "confidenza": min(1.0, punteggio / 10.0)
                }
                regole.append(regola)
        
        # Ordina per punteggio
        regole.sort(key=lambda x: x['punteggio'], reverse=True)
        
        return regole
    
    def applica_regola(self, pensiero_nuovo: Dict, regole: List[Dict]) -> Dict:
        """
        Applica regola se match
        
        Args:
            pensiero_nuovo: Nuovo pensiero da elaborare
            regole: Regole disponibili
            
        Returns:
            Pensiero con regola applicata (se match)
        """
        vista_nuova = pensiero_nuovo.get("descrizione", "")[:30]
        udito_nuovo = pensiero_nuovo.get("audio", "")[:20]
        emozione_nuova = pensiero_nuovo.get("emozione", "neutro")
        
        # Cerca regola matching
        for regola in regole:
            cond = regola["condizione"]
            
            # Match fuzzy (contiene)
            if (cond["vista"] in vista_nuova or vista_nuova in cond["vista"]) and \
               (cond["udito"] in udito_nuovo or udito_nuovo in cond["udito"] or not udito_nuovo) and \
               cond["emozione"] == emozione_nuova:
                
                # Applica regola
                pensiero_nuovo["azione_suggerita"] = regola["azione"]
                pensiero_nuovo["regola_applicata"] = True
                pensiero_nuovo["confidenza_regola"] = regola["confidenza"]
                pensiero_nuovo["motivazione_apprendimento"] = f"Regola applicata (score: {regola['punteggio']})"
                
                return pensiero_nuovo
        
        # Nessuna regola applicata
        pensiero_nuovo["regola_applicata"] = False
        return pensiero_nuovo
    
    def elabora(self, pensiero: Dict, fase='valutazione') -> Dict:
        """
        Processo principale apprendimento
        
        Args:
            pensiero: Episodio cognitivo
            fase: 'valutazione' o 'applicazione'
            
        Returns:
            Risultati elaborazione
        """
        if fase == 'valutazione':
            # Valuta e aggiorna comportamento
            pensiero_valutato = self.aggiorna_pensiero(pensiero)
            self.aggiorna_comportamento(pensiero_valutato)
            self.salva_pensiero_valutato(pensiero_valutato)
            
            return {
                'valutazione': pensiero_valutato.get('valutazione'),
                'azione_rinforzata': pensiero.get('azione'),
                'peso_nuovo': self.probabilita_decisioni.get(pensiero.get('azione'), 1.0)
            }
        
        else:  # applicazione
            # Carica e applica regole
            pensieri_passati = self.carica_pensieri_passati()
            if len(pensieri_passati) >= 10:  # Minimo 10 per trovare pattern
                schemi = self.trova_schemi(pensieri_passati, soglia=3)
                regole = self.genera_regole(schemi)
                
                if regole:
                    pensiero_con_regola = self.applica_regola(pensiero, regole)
                    return {
                        'regole_trovate': len(regole),
                        'regola_applicata': pensiero_con_regola.get('regola_applicata', False),
                        'azione_suggerita': pensiero_con_regola.get('azione_suggerita'),
                        'pensiero': pensiero_con_regola
                    }
            
            return {'regole_trovate': 0, 'regola_applicata': False}


# Singleton
_instance = None

def get_instance() -> ApprendimentoAdattivo:
    global _instance
    if _instance is None:
        _instance = ApprendimentoAdattivo()
    return _instance


# Fix import datetime
from datetime import datetime

