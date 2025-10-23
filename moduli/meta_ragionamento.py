#!/usr/bin/env python3
"""
🤔 MODULO META-RAGIONAMENTO - Fase 4 AGI
Il sistema valuta quanto sa su un argomento e decide se agire o imparare di più
"""

import json
from typing import Dict, List, Optional
from pathlib import Path
from datetime import datetime
from collections import defaultdict


class ConoscenzaArgomento:
    """Rappresenta quanto il sistema conosce un argomento"""
    
    def __init__(self, argomento: str):
        self.argomento = argomento
        self.livello_conoscenza = 0.0  # 0.0 = nulla, 1.0 = esperto
        self.esperienze = 0
        self.successi = 0
        self.fallimenti = 0
        self.ultima_interazione = datetime.now().isoformat()
        self.incertezze = []  # Lista di domande/dubbi
    
    def aggiorna(self, successo: bool):
        """Aggiorna conoscenza dopo esperienza"""
        self.esperienze += 1
        if successo:
            self.successi += 1
            # Aumenta conoscenza
            self.livello_conoscenza = min(1.0, self.livello_conoscenza + 0.05)
        else:
            self.fallimenti += 1
            # Diminuisci leggermente
            self.livello_conoscenza = max(0.0, self.livello_conoscenza - 0.02)
        
        self.ultima_interazione = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        return {
            'argomento': self.argomento,
            'livello_conoscenza': self.livello_conoscenza,
            'esperienze': self.esperienze,
            'successi': self.successi,
            'fallimenti': self.fallimenti,
            'ultima_interazione': self.ultima_interazione,
            'incertezze': self.incertezze
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'ConoscenzaArgomento':
        c = ConoscenzaArgomento(data['argomento'])
        c.livello_conoscenza = data.get('livello_conoscenza', 0.0)
        c.esperienze = data.get('esperienze', 0)
        c.successi = data.get('successi', 0)
        c.fallimenti = data.get('fallimenti', 0)
        c.ultima_interazione = data.get('ultima_interazione', datetime.now().isoformat())
        c.incertezze = data.get('incertezze', [])
        return c


class MetaRagionamento:
    """
    Sistema di meta-ragionamento: il sistema riflette su sé stesso
    
    Funzionalità:
    - Valuta quanto sa su ogni argomento
    - Identifica lacune conoscenza
    - Decide se agire o esplorare
    - Monitora affidabilità decisioni
    """
    
    def __init__(self, path_meta="memoria_permanente/meta_conoscenza.json"):
        self.nome = "Meta-Ragionamento"
        self.path_meta = Path(path_meta)
        self.path_meta.parent.mkdir(exist_ok=True)
        
        # Conoscenze per argomento
        self.conoscenze: Dict[str, ConoscenzaArgomento] = {}
        
        # Carica dati
        self._carica()
        
        print(f"[{self.nome}] Inizializzato")
        print(f"  • Argomenti conosciuti: {len(self.conoscenze)}")
    
    def _carica(self):
        """Carica meta-conoscenza"""
        if self.path_meta.exists():
            try:
                with open(self.path_meta, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for arg, cono_dict in data.items():
                        self.conoscenze[arg] = ConoscenzaArgomento.from_dict(cono_dict)
            except Exception as e:
                print(f"[{self.nome}] ⚠️  Errore caricamento: {e}")
    
    def _salva(self):
        """Salva meta-conoscenza"""
        try:
            data = {arg: c.to_dict() for arg, c in self.conoscenze.items()}
            with open(self.path_meta, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore salvataggio: {e}")
    
    def identifica_argomento(self, situazione: Dict) -> str:
        """Identifica l'argomento principale della situazione"""
        # Combina info per creare argomento
        entita = 'generico'
        azione = 'osservazione'
        
        desc = situazione.get('descrizione', '').lower()
        if 'person' in desc or 'persona' in desc:
            entita = 'persona'
        elif 'car' in desc or 'veicolo' in desc:
            entita = 'veicolo'
        elif 'animal' in desc:
            entita = 'animale'
        
        audio = situazione.get('audio', '').lower()
        if any(w in audio for w in ['vieni', 'avvicinati']):
            azione = 'avvicinamento'
        elif any(w in audio for w in ['fermati', 'stop']):
            azione = 'arresto'
        elif any(w in audio for w in ['ciao', 'salve']):
            azione = 'saluto'
        
        return f"{entita}_{azione}"
    
    def valuta_conoscenza(self, argomento: str) -> Dict:
        """
        Valuta quanto il sistema sa su un argomento
        
        Returns:
            Dict con valutazione conoscenza
        """
        if argomento not in self.conoscenze:
            # Argomento nuovo
            return {
                'argomento': argomento,
                'livello': 0.0,
                'stato': 'sconosciuto',
                'confidenza': 0.0,
                'bisogno_imparare': True,
                'suggerimento': 'Esplora con cautela, questo è nuovo'
            }
        
        cono = self.conoscenze[argomento]
        
        # Calcola confidenza
        if cono.esperienze > 0:
            confidenza = cono.successi / cono.esperienze
        else:
            confidenza = 0.0
        
        # Determina stato
        if cono.livello_conoscenza >= 0.8:
            stato = 'esperto'
            bisogno_imparare = False
            suggerimento = 'Puoi agire con sicurezza'
        elif cono.livello_conoscenza >= 0.5:
            stato = 'competente'
            bisogno_imparare = False
            suggerimento = 'Puoi agire, ma con attenzione'
        elif cono.livello_conoscenza >= 0.3:
            stato = 'principiante'
            bisogno_imparare = True
            suggerimento = 'Procedi con cautela e impara'
        else:
            stato = 'novizio'
            bisogno_imparare = True
            suggerimento = 'Esplora e raccogli più informazioni'
        
        return {
            'argomento': argomento,
            'livello': cono.livello_conoscenza,
            'stato': stato,
            'confidenza': confidenza,
            'esperienze': cono.esperienze,
            'bisogno_imparare': bisogno_imparare,
            'suggerimento': suggerimento
        }
    
    def decidi_strategia(self, situazione: Dict) -> Dict:
        """
        Decide se agire subito o esplorare prima
        
        Args:
            situazione: Situazione corrente
        
        Returns:
            Dict con strategia consigliata
        """
        argomento = self.identifica_argomento(situazione)
        valutazione = self.valuta_conoscenza(argomento)
        
        # Strategia basata su livello conoscenza
        if valutazione['livello'] >= 0.7:
            strategia = 'agisci'
            motivazione = f"Ho esperienza con '{argomento}' (livello: {valutazione['livello']:.0%})"
        elif valutazione['livello'] >= 0.4:
            strategia = 'agisci_cautamente'
            motivazione = f"Conosco '{argomento}' moderatamente, procedo con cautela"
        elif valutazione['livello'] >= 0.2:
            strategia = 'esplora_poi_agisci'
            motivazione = f"Poca esperienza con '{argomento}', raccolgo più dati prima"
        else:
            strategia = 'esplora'
            motivazione = f"'{argomento}' è nuovo, esploro prima di agire"
        
        return {
            'argomento': argomento,
            'strategia': strategia,
            'motivazione': motivazione,
            'valutazione': valutazione,
            'meta_riflessione': self._genera_riflessione(valutazione)
        }
    
    def _genera_riflessione(self, valutazione: Dict) -> str:
        """Genera riflessione metacognitiva"""
        livello = valutazione['livello']
        stato = valutazione['stato']
        
        if livello >= 0.8:
            return f"So cosa fare in queste situazioni. Sono {stato}."
        elif livello >= 0.5:
            return f"Ho una buona comprensione, ma posso migliorare."
        elif livello >= 0.3:
            return f"Sto ancora imparando su questo argomento."
        else:
            return f"Questo è nuovo per me. Devo imparare di più."
    
    def aggiorna_esperienza(self, situazione: Dict, successo: bool):
        """Aggiorna conoscenza dopo esperienza"""
        argomento = self.identifica_argomento(situazione)
        
        if argomento not in self.conoscenze:
            self.conoscenze[argomento] = ConoscenzaArgomento(argomento)
        
        self.conoscenze[argomento].aggiorna(successo)
        self._salva()
    
    def identifica_lacune(self) -> List[Dict]:
        """Identifica lacune nella conoscenza"""
        lacune = []
        
        for arg, cono in self.conoscenze.items():
            if cono.livello_conoscenza < 0.5 and cono.esperienze > 0:
                lacune.append({
                    'argomento': arg,
                    'livello': cono.livello_conoscenza,
                    'esperienze': cono.esperienze,
                    'tasso_successo': cono.successi / max(1, cono.esperienze),
                    'priorita': 'alta' if cono.fallimenti > cono.successi else 'media'
                })
        
        # Ordina per priorità
        lacune.sort(key=lambda x: (x['priorita'] == 'alta', -x['livello']), reverse=True)
        
        return lacune
    
    def elabora(self, situazione: Dict) -> Dict:
        """
        Elabora situazione con meta-ragionamento
        
        Args:
            situazione: Situazione da valutare
        
        Returns:
            Dict con decisione strategica
        """
        decisione = self.decidi_strategia(situazione)
        
        return {
            'tipo': 'meta_ragionamento',
            'argomento': decisione['argomento'],
            'strategia': decisione['strategia'],
            'motivazione': decisione['motivazione'],
            'valutazione_conoscenza': decisione['valutazione'],
            'riflessione': decisione['meta_riflessione'],
            'suggerimenti': self._genera_suggerimenti(decisione)
        }
    
    def _genera_suggerimenti(self, decisione: Dict) -> List[str]:
        """Genera suggerimenti pratici"""
        suggerimenti = []
        
        if decisione['strategia'] == 'esplora':
            suggerimenti.append("Raccogli informazioni prima di agire")
            suggerimenti.append("Osserva senza intervenire")
        elif decisione['strategia'] == 'esplora_poi_agisci':
            suggerimenti.append("Valuta le opzioni disponibili")
            suggerimenti.append("Agisci solo se sicuro")
        elif decisione['strategia'] == 'agisci_cautamente':
            suggerimenti.append("Procedi gradualmente")
            suggerimenti.append("Monitora risultati attentamente")
        else:
            suggerimenti.append("Agisci con decisione")
            suggerimenti.append("Applica conoscenza acquisita")
        
        return suggerimenti
    
    def get_statistiche(self) -> Dict:
        """Statistiche meta-conoscenza"""
        if not self.conoscenze:
            return {
                'totale_argomenti': 0,
                'livello_medio': 0.0,
                'argomenti_esperti': 0,
                'lacune': []
            }
        
        livelli = [c.livello_conoscenza for c in self.conoscenze.values()]
        
        return {
            'totale_argomenti': len(self.conoscenze),
            'livello_medio': sum(livelli) / len(livelli),
            'argomenti_esperti': len([l for l in livelli if l >= 0.8]),
            'argomenti_principianti': len([l for l in livelli if l < 0.5]),
            'lacune': self.identifica_lacune()
        }


# ==================== TEST ====================

if __name__ == "__main__":
    print("="*70)
    print("🧪 TEST META-RAGIONAMENTO")
    print("="*70)
    
    meta = MetaRagionamento()
    
    # Test 1: Situazione nuova
    print("\n--- Test 1: Situazione Nuova ---")
    situazione1 = {
        'descrizione': 'Person detected',
        'audio': 'Vieni qui',
        'emozione': 'neutro'
    }
    
    risultato = meta.elabora(situazione1)
    print(f"✅ Argomento: {risultato['argomento']}")
    print(f"   Strategia: {risultato['strategia']}")
    print(f"   Riflessione: {risultato['riflessione']}")
    print(f"   Suggerimenti: {risultato['suggerimenti']}")
    
    # Test 2: Aggiungi esperienza
    print("\n--- Test 2: Apprendimento ---")
    for i in range(5):
        meta.aggiorna_esperienza(situazione1, successo=True)
        print(f"  Esperienza {i+1} aggiunta")
    
    # Test 3: Rivaluta
    print("\n--- Test 3: Rivalutazione ---")
    risultato2 = meta.elabora(situazione1)
    print(f"✅ Livello conoscenza: {risultato2['valutazione_conoscenza']['livello']:.0%}")
    print(f"   Stato: {risultato2['valutazione_conoscenza']['stato']}")
    print(f"   Strategia: {risultato2['strategia']}")
    print(f"   Riflessione: {risultato2['riflessione']}")
    
    # Statistiche
    print("\n--- Statistiche ---")
    stats = meta.get_statistiche()
    print(f"📊 Argomenti conosciuti: {stats['totale_argomenti']}")
    print(f"   Livello medio: {stats['livello_medio']:.0%}")
    
    print("\n✅ Test completato!")


