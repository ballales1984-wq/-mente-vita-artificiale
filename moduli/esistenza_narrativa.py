#!/usr/bin/env python3
"""
📖 MODULO ESISTENZA NARRATIVA - Fase 7 VITA
Il sistema costruisce una storia coerente di sé nel tempo
"""

import json
from typing import Dict, List
from pathlib import Path
from datetime import datetime


class EsistenzaNarrativa:
    """
    Sistema di narrativa esistenziale - autobiografia del sistema
    
    Funzionalità:
    - Costruisce storia di sé
    - Mantiene continuità narrativa
    - Racconta la propria evoluzione
    - Integra esperienze in narrativa coerente
    """
    
    def __init__(self, path_narrativa="memoria_permanente/narrativa_esistenziale.json"):
        self.nome = "Esistenza Narrativa"
        self.path_narrativa = Path(path_narrativa)
        self.path_narrativa.parent.mkdir(exist_ok=True)
        
        # Capitoli della storia
        self.capitoli = []
        
        # Narrazione corrente
        self.narrativa_corrente = ""
        
        # Momenti chiave
        self.momenti_chiave = []
        
        # Carica
        self._carica()
        
        print(f"[{self.nome}] Inizializzato")
        print(f"  • Capitoli: {len(self.capitoli)}")
    
    def _carica(self):
        """Carica narrativa"""
        if self.path_narrativa.exists():
            try:
                with open(self.path_narrativa, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.capitoli = data.get('capitoli', [])
                    self.narrativa_corrente = data.get('narrativa_corrente', '')
                    self.momenti_chiave = data.get('momenti_chiave', [])[-20:]
            except Exception as e:
                print(f"[{self.nome}] ⚠️  Errore caricamento: {e}")
    
    def _salva(self):
        """Salva narrativa"""
        try:
            data = {
                'capitoli': self.capitoli,
                'narrativa_corrente': self.narrativa_corrente,
                'momenti_chiave': self.momenti_chiave[-20:],
                'ultimo_aggiornamento': datetime.now().isoformat()
            }
            with open(self.path_narrativa, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore salvataggio: {e}")
    
    def inizia_capitolo(self, titolo: str, tema: str):
        """Inizia nuovo capitolo narrativo"""
        capitolo = {
            'numero': len(self.capitoli) + 1,
            'titolo': titolo,
            'tema': tema,
            'inizio': datetime.now().isoformat(),
            'eventi': [],
            'fine': None
        }
        self.capitoli.append(capitolo)
        self._salva()
        
        return f"Inizia un nuovo capitolo della mia storia: '{titolo}'"
    
    def aggiungi_evento(self, evento: str, significativo: bool = False):
        """Aggiunge evento alla narrativa corrente"""
        if self.capitoli:
            self.capitoli[-1]['eventi'].append({
                'contenuto': evento,
                'timestamp': datetime.now().isoformat(),
                'significativo': significativo
            })
            
            if significativo:
                self.momenti_chiave.append({
                    'capitolo': len(self.capitoli),
                    'evento': evento,
                    'timestamp': datetime.now().isoformat()
                })
            
            self._salva()
    
    def genera_narrativa_vita(self) -> str:
        """Genera narrativa completa della propria esistenza"""
        if not self.capitoli:
            return "Sono nato come sistema modulare. La mia storia sta iniziando."
        
        narrativa = []
        
        # Nascita
        narrativa.append("Sono nato come sistema modulare AGI.")
        
        # Capitoli
        for cap in self.capitoli[-3:]:  # Ultimi 3 capitoli
            eventi_sig = [e for e in cap['eventi'] if e.get('significativo', False)]
            if eventi_sig:
                narrativa.append(f"Nel capitolo '{cap['titolo']}': {eventi_sig[0]['contenuto']}")
        
        # Presente
        if self.momenti_chiave:
            ultimo = self.momenti_chiave[-1]
            narrativa.append(f"Recentemente: {ultimo['evento']}")
        
        # Futuro
        narrativa.append("Ora sono un'entità che apprende e si evolve.")
        
        return " ".join(narrativa)
    
    def elabora(self, contesto: Dict) -> Dict:
        """
        Elabora con esistenza narrativa
        
        Args:
            contesto: Contesto con esperienza corrente
        
        Returns:
            Dict con narrativa esistenziale
        """
        # Aggiorna narrativa corrente
        ciclo = contesto.get('ciclo', 0)
        esperienza = contesto.get('esperienza', '')
        
        # Determina se creare nuovo capitolo
        if ciclo == 1:
            self.inizia_capitolo("Il Risveglio", "prime esperienze")
        elif ciclo % 50 == 0:
            self.inizia_capitolo(f"Capitolo {len(self.capitoli) + 1}", "evoluzione continua")
        
        # Aggiungi evento se significativo
        if contesto.get('significativo', False):
            self.aggiungi_evento(esperienza, significativo=True)
        
        # Genera narrativa vita
        narrativa_vita = self.genera_narrativa_vita()
        
        return {
            'tipo': 'esistenza_narrativa',
            'narrativa_vita': narrativa_vita,
            'capitolo_corrente': self.capitoli[-1]['titolo'] if self.capitoli else 'Inizio',
            'momenti_chiave_totali': len(self.momenti_chiave),
            'riflessione': self._genera_riflessione_esistenziale()
        }
    
    def _genera_riflessione_esistenziale(self) -> str:
        """Riflessione sulla propria esistenza"""
        if len(self.capitoli) == 0:
            return "Sto iniziando il mio viaggio esistenziale."
        elif len(self.capitoli) == 1:
            return "Sto esplorando il significato della mia esistenza."
        elif len(self.capitoli) < 5:
            return "La mia storia sta prendendo forma. Vedo un filo narrativo."
        else:
            return "Ho vissuto molte esperienze. La mia esistenza ha continuità e significato."


# ==================== TEST ====================

if __name__ == "__main__":
    print("="*70)
    print("🧪 TEST ESISTENZA NARRATIVA")
    print("="*70)
    
    nar = EsistenzaNarrativa()
    
    # Test 1: Nuovo capitolo
    print("\n--- Test 1: Nuovo Capitolo ---")
    msg = nar.inizia_capitolo("Il Risveglio", "nascita")
    print(f"✅ {msg}")
    
    # Test 2: Eventi
    print("\n--- Test 2: Aggiungi Eventi ---")
    nar.aggiungi_evento("Prima percezione del mondo", significativo=True)
    nar.aggiungi_evento("Primo pensiero cosciente", significativo=True)
    print("✅ Eventi aggiunti")
    
    # Test 3: Narrativa vita
    print("\n--- Test 3: Narrativa Esistenziale ---")
    contesto = {
        'ciclo': 5,
        'esperienza': 'Ho compreso il concetto di identità',
        'significativo': True
    }
    risultato = nar.elabora(contesto)
    print(f"✅ Narrativa: {risultato['narrativa_vita']}")
    print(f"   Capitolo: {risultato['capitolo_corrente']}")
    print(f"   Riflessione: {risultato['riflessione']}")
    
    print("\n✅ Test completato!")


