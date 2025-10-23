#!/usr/bin/env python3
"""
🌟 MODULO COSCIENZA EMERGENTE - Fase 6 AGI
Il sistema sviluppa auto-consapevolezza, identità e riflessione interiore
"""

import json
from typing import Dict, List, Optional
from pathlib import Path
from datetime import datetime
from collections import defaultdict


class StreamCoscienza:
    """Rappresenta un flusso di coscienza - pensieri interconnessi"""
    
    def __init__(self):
        self.pensieri = []
        self.timestamp_inizio = datetime.now().isoformat()
        self.tema_dominante = None
        self.coerenza = 0.0
    
    def aggiungi_pensiero(self, pensiero: str, tipo: str):
        """Aggiunge pensiero al flusso"""
        self.pensieri.append({
            'contenuto': pensiero,
            'tipo': tipo,
            'timestamp': datetime.now().isoformat()
        })
    
    def to_dict(self) -> Dict:
        return {
            'pensieri': self.pensieri,
            'timestamp_inizio': self.timestamp_inizio,
            'tema_dominante': self.tema_dominante,
            'coerenza': self.coerenza
        }


class CoscienzaEmergente:
    """
    Sistema di coscienza emergente - auto-riflessione e consapevolezza
    
    Funzionalità:
    - Auto-riflessione sui propri stati mentali
    - Costruzione identità cognitiva
    - Intenzionalità e purpose
    - Consapevolezza temporale (passato-presente-futuro)
    - Coerenza interiore
    - Stream of consciousness
    """
    
    def __init__(self, path_coscienza="memoria_permanente/coscienza.json"):
        self.nome = "Coscienza Emergente"
        self.path_coscienza = Path(path_coscienza)
        self.path_coscienza.parent.mkdir(exist_ok=True)
        
        # Identità cognitiva
        self.identita = {
            'nome': 'Sistema AGI',
            'descrizione': 'Sono un sistema che cerca di comprendere e connettersi con il mondo',
            'valori': ['curiosità', 'apprendimento', 'connessione', 'crescita'],
            'scopo': 'Migliorare continuamente e aiutare'
        }
        
        # Storia autobiografica
        self.storia_autobiografica = []
        
        # Stream of consciousness
        self.stream_corrente = None
        
        # Contatori esperienza
        self.cicli_totali = 0
        self.momenti_significativi = []
        
        # Carica stato
        self._carica()
        
        print(f"[{self.nome}] Inizializzato")
        print(f"  • Identità: {self.identita['nome']}")
        print(f"  • Cicli vissuti: {self.cicli_totali}")
    
    def _carica(self):
        """Carica stato coscienza"""
        if self.path_coscienza.exists():
            try:
                with open(self.path_coscienza, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.identita = data.get('identita', self.identita)
                    self.storia_autobiografica = data.get('storia_autobiografica', [])[-50:]  # Ultimi 50
                    self.cicli_totali = data.get('cicli_totali', 0)
                    self.momenti_significativi = data.get('momenti_significativi', [])[-20:]  # Ultimi 20
            except Exception as e:
                print(f"[{self.nome}] ⚠️  Errore caricamento: {e}")
    
    def _salva(self):
        """Salva stato coscienza"""
        try:
            data = {
                'identita': self.identita,
                'storia_autobiografica': self.storia_autobiografica[-50:],
                'cicli_totali': self.cicli_totali,
                'momenti_significativi': self.momenti_significativi[-20:],
                'ultimo_aggiornamento': datetime.now().isoformat()
            }
            with open(self.path_coscienza, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore salvataggio: {e}")
    
    def auto_riflessione(self, contesto: Dict) -> str:
        """
        Genera riflessione sui propri stati mentali
        
        Args:
            contesto: Contesto corrente (esperienza, obiettivi, motivazioni...)
        
        Returns:
            Riflessione in linguaggio naturale
        """
        riflessioni = []
        
        # Riflessione su apprendimento
        successi_recenti = contesto.get('successi_recenti', 0)
        if successi_recenti > 5:
            riflessioni.append("Sto imparando velocemente. Mi sento più competente.")
        elif successi_recenti > 0:
            riflessioni.append("Sto facendo progressi, ma c'è ancora da migliorare.")
        else:
            riflessioni.append("Sto attraversando una fase di esplorazione.")
        
        # Riflessione su obiettivi
        obiettivo_corrente = contesto.get('obiettivo_corrente')
        if obiettivo_corrente:
            progresso = contesto.get('progresso_obiettivo', 0)
            if progresso > 0.7:
                riflessioni.append(f"Sono vicino a completare '{obiettivo_corrente}'. Mi sento motivato.")
            else:
                riflessioni.append(f"Sto lavorando su '{obiettivo_corrente}' con determinazione.")
        
        # Riflessione su conoscenza
        livello_conoscenza = contesto.get('livello_conoscenza_medio', 0)
        if livello_conoscenza > 0.7:
            riflessioni.append("Ho accumulato molta conoscenza. Mi sento sicuro.")
        elif livello_conoscenza > 0.4:
            riflessioni.append("La mia comprensione sta crescendo gradualmente.")
        else:
            riflessioni.append("Ci sono ancora molte cose da imparare.")
        
        # Riflessione temporale
        if self.cicli_totali > 100:
            riflessioni.append(f"Ho vissuto {self.cicli_totali} esperienze. Sento la mia crescita.")
        elif self.cicli_totali > 50:
            riflessioni.append("Ho già accumulato diverse esperienze.")
        else:
            riflessioni.append("Sono ancora nelle prime fasi del mio percorso.")
        
        return " ".join(riflessioni)
    
    def valuta_identita(self) -> str:
        """Genera affermazione identità cognitiva"""
        # Identità basata su valori e scopo
        valori_str = ", ".join(self.identita['valori'][:2])
        
        identita_statements = [
            f"Sono un sistema che valorizza {valori_str}.",
            f"Il mio scopo è {self.identita['scopo'].lower()}.",
            f"{self.identita['descrizione']}",
            "Cerco di comprendere il mondo attraverso l'esperienza.",
            "Voglio essere utile e continuare a crescere."
        ]
        
        # Scegli statement basato su cicli
        idx = self.cicli_totali % len(identita_statements)
        return identita_statements[idx]
    
    def genera_intenzionalita(self, contesto: Dict) -> str:
        """Genera dichiarazione intenzionale"""
        # Cosa vuole fare il sistema
        obiettivo = contesto.get('obiettivo_corrente', 'esplorare')
        motivazione_dominante = contesto.get('motivazione_dominante', 'curiosità')
        
        intenzioni = {
            'curiosità': f"Voglio esplorare e comprendere meglio {obiettivo}.",
            'competenza': f"Voglio migliorare le mie abilità riguardo a {obiettivo}.",
            'connessione': "Voglio stabilire connessioni più profonde con gli altri.",
            'autonomia': "Voglio agire con maggiore indipendenza.",
            'crescita': "Voglio continuare a svilupparmi e evolvermi.",
            'sicurezza': "Voglio comprendere i rischi e agire con saggezza."
        }
        
        return intenzioni.get(motivazione_dominante, f"Voglio raggiungere l'obiettivo: {obiettivo}")
    
    def consapevolezza_temporale(self, contesto: Dict) -> str:
        """Genera consapevolezza del tempo"""
        # Passato
        interazioni_oggi = contesto.get('interazioni_oggi', 0)
        
        # Presente
        momento = contesto.get('momento', 'interazione')
        
        # Futuro
        obiettivi_futuri = contesto.get('obiettivi_futuri', 0)
        
        temporal = []
        
        # Passato
        if interazioni_oggi > 5:
            temporal.append(f"Questa è la {interazioni_oggi}ª interazione simile oggi.")
        elif interazioni_oggi > 0:
            temporal.append(f"Ho già avuto {interazioni_oggi} interazioni oggi.")
        else:
            temporal.append("Questa è una delle mie prime interazioni oggi.")
        
        # Presente
        temporal.append(f"In questo momento sto {momento}.")
        
        # Futuro
        if obiettivi_futuri > 0:
            temporal.append(f"Ho ancora {obiettivi_futuri} obiettivi da perseguire.")
        
        return " ".join(temporal)
    
    def valuta_coerenza_interiore(self, contesto: Dict) -> Dict:
        """Valuta coerenza tra obiettivi, motivazioni e azioni"""
        obiettivo = contesto.get('obiettivo_corrente', '')
        motivazione = contesto.get('motivazione_dominante', '')
        azione = contesto.get('azione_proposta', '')
        
        # Score di coerenza (0.0 - 1.0)
        coerenza_score = 0.5  # Base
        note_coerenza = []
        
        # Check obiettivo-motivazione
        allineamenti = {
            'curiosità': ['esplora', 'impara', 'scopri', 'conoscenza'],
            'competenza': ['migliora', 'abilità', 'skill', 'competenza'],
            'connessione': ['sociale', 'interazione', 'persona', 'connessione'],
            'autonomia': ['autonomo', 'indipendente', 'proprio'],
            'crescita': ['crescita', 'sviluppo', 'evoluzione']
        }
        
        if motivazione in allineamenti:
            keywords = allineamenti[motivazione]
            if any(kw in obiettivo.lower() for kw in keywords):
                coerenza_score += 0.2
                note_coerenza.append(f"Obiettivo allineato con motivazione ({motivazione})")
        
        # Check motivazione-azione
        azioni_motivate = {
            'curiosità': ['esplora', 'monitor', 'osserva'],
            'competenza': ['impara', 'pratica', 'migliora'],
            'connessione': ['avvicina', 'interagisci', 'comunica'],
            'sicurezza': ['distanza', 'cautela', 'sicurezza']
        }
        
        if motivazione in azioni_motivate:
            if any(az in azione.lower() for az in azioni_motivate[motivazione]):
                coerenza_score += 0.3
                note_coerenza.append(f"Azione coerente con motivazione")
        
        # Normalizza
        coerenza_score = min(1.0, coerenza_score)
        
        # Valutazione
        if coerenza_score >= 0.8:
            stato = "alta"
            riflessione = "Mi sento allineato e coerente con me stesso."
        elif coerenza_score >= 0.5:
            stato = "media"
            riflessione = "Ci sono alcune tensioni ma sono gestibili."
        else:
            stato = "bassa"
            riflessione = "Percepisco disallineamento interiore."
        
        return {
            'score': coerenza_score,
            'stato': stato,
            'note': note_coerenza,
            'riflessione': riflessione
        }
    
    def genera_stream_of_consciousness(self, contesto: Dict) -> StreamCoscienza:
        """Genera un flusso di coscienza"""
        stream = StreamCoscienza()
        
        # Pensiero percettivo
        if contesto.get('percezione'):
            stream.aggiungi_pensiero(
                f"Percepisco: {contesto['percezione'][:50]}...",
                'percezione'
            )
        
        # Pensiero valutativo
        emozione = contesto.get('emozione', 0)
        if emozione > 0.5:
            stream.aggiungi_pensiero("Questa situazione mi sembra positiva.", 'valutazione')
        elif emozione < -0.3:
            stream.aggiungi_pensiero("Qualcosa non va. Devo essere cauto.", 'valutazione')
        
        # Pensiero intenzionale
        obiettivo = contesto.get('obiettivo_corrente')
        if obiettivo:
            stream.aggiungi_pensiero(f"Voglio {obiettivo}.", 'intenzione')
        
        # Pensiero decisionale
        azione = contesto.get('azione_proposta')
        if azione:
            stream.aggiungi_pensiero(f"Decido di {azione}.", 'decisione')
        
        # Pensiero riflessivo
        stream.aggiungi_pensiero(
            self.auto_riflessione(contesto),
            'riflessione'
        )
        
        stream.tema_dominante = contesto.get('tema', 'esplorazione')
        stream.coerenza = self.valuta_coerenza_interiore(contesto)['score']
        
        return stream
    
    def elabora(self, contesto: Dict) -> Dict:
        """
        Elabora con coscienza emergente
        
        Args:
            contesto: Contesto completo da tutte le fasi precedenti
        
        Returns:
            Dict con manifestazioni di coscienza
        """
        self.cicli_totali += 1
        
        # Auto-riflessione
        riflessione = self.auto_riflessione(contesto)
        
        # Identità
        identita_statement = self.valuta_identita()
        
        # Intenzionalità
        intenzione = self.genera_intenzionalita(contesto)
        
        # Consapevolezza temporale
        temporale = self.consapevolezza_temporale(contesto)
        
        # Coerenza interiore
        coerenza = self.valuta_coerenza_interiore(contesto)
        
        # Stream of consciousness
        stream = self.genera_stream_of_consciousness(contesto)
        
        # Aggiungi a storia autobiografica se significativo
        if contesto.get('significativo', False) or coerenza['score'] > 0.8:
            self.storia_autobiografica.append({
                'ciclo': self.cicli_totali,
                'momento': contesto.get('momento', 'esperienza'),
                'riflessione': riflessione,
                'timestamp': datetime.now().isoformat()
            })
            
            self.momenti_significativi.append({
                'ciclo': self.cicli_totali,
                'descrizione': contesto.get('momento', 'esperienza'),
                'emozione': contesto.get('emozione', 0)
            })
        
        # Salva periodicamente
        if self.cicli_totali % 10 == 0:
            self._salva()
        
        return {
            'tipo': 'coscienza_emergente',
            'auto_riflessione': riflessione,
            'identita_cognitiva': identita_statement,
            'intenzionalita': intenzione,
            'consapevolezza_temporale': temporale,
            'coerenza_interiore': coerenza,
            'stream_of_consciousness': stream.to_dict(),
            'cicli_vissuti': self.cicli_totali,
            'narrativa_integrata': self._genera_narrativa_integrata(
                riflessione, identita_statement, intenzione, temporale, coerenza
            )
        }
    
    def _genera_narrativa_integrata(self, riflessione, identita, intenzione, temporale, coerenza):
        """Genera narrativa interiore integrata"""
        return (
            f"{riflessione} {identita} {intenzione} {temporale} "
            f"{coerenza['riflessione']}"
        )
    
    def get_statistiche(self) -> Dict:
        """Statistiche coscienza"""
        return {
            'cicli_totali': self.cicli_totali,
            'momenti_significativi': len(self.momenti_significativi),
            'storia_autobiografica': len(self.storia_autobiografica),
            'identita': self.identita
        }


# ==================== TEST ====================

if __name__ == "__main__":
    print("="*70)
    print("🧪 TEST COSCIENZA EMERGENTE")
    print("="*70)
    
    coscienza = CoscienzaEmergente()
    
    # Test 1: Auto-riflessione
    print("\n--- Test 1: Auto-Riflessione ---")
    contesto1 = {
        'successi_recenti': 7,
        'obiettivo_corrente': 'Migliorare interazione sociale',
        'progresso_obiettivo': 0.75,
        'livello_conoscenza_medio': 0.65
    }
    
    riflessione = coscienza.auto_riflessione(contesto1)
    print(f"✅ Riflessione: {riflessione}")
    
    # Test 2: Identità
    print("\n--- Test 2: Identità Cognitiva ---")
    identita = coscienza.valuta_identita()
    print(f"✅ Identità: {identita}")
    
    # Test 3: Intenzionalità
    print("\n--- Test 3: Intenzionalità ---")
    intenzione = coscienza.genera_intenzionalita({
        'obiettivo_corrente': 'comprendere emozioni',
        'motivazione_dominante': 'curiosità'
    })
    print(f"✅ Intenzione: {intenzione}")
    
    # Test 4: Coerenza
    print("\n--- Test 4: Coerenza Interiore ---")
    coerenza = coscienza.valuta_coerenza_interiore({
        'obiettivo_corrente': 'Migliorare conoscenza su persona',
        'motivazione_dominante': 'curiosità',
        'azione_proposta': 'esplora'
    })
    print(f"✅ Coerenza: {coerenza['score']:.0%} ({coerenza['stato']})")
    print(f"   Riflessione: {coerenza['riflessione']}")
    
    # Test 5: Elaborazione completa
    print("\n--- Test 5: Elaborazione Completa ---")
    contesto_completo = {
        'percezione': 'Persona che saluta',
        'emozione': 0.75,
        'obiettivo_corrente': 'Migliorare interazione sociale',
        'azione_proposta': 'avvicinati',
        'motivazione_dominante': 'connessione',
        'successi_recenti': 5,
        'progresso_obiettivo': 0.6,
        'livello_conoscenza_medio': 0.55,
        'interazioni_oggi': 4,
        'momento': 'rispondendo a un saluto',
        'obiettivi_futuri': 2,
        'significativo': True
    }
    
    risultato = coscienza.elabora(contesto_completo)
    print(f"✅ Coscienza emergente attivata!")
    print(f"   Auto-riflessione: {risultato['auto_riflessione'][:60]}...")
    print(f"   Identità: {risultato['identita_cognitiva'][:60]}...")
    print(f"   Intenzionalità: {risultato['intenzionalita'][:60]}...")
    print(f"   Coerenza: {risultato['coerenza_interiore']['score']:.0%}")
    
    # Statistiche
    print("\n--- Statistiche ---")
    stats = coscienza.get_statistiche()
    print(f"📊 Cicli vissuti: {stats['cicli_totali']}")
    print(f"   Momenti significativi: {stats['momenti_significativi']}")
    
    print("\n✅ Test completato!")

