#!/usr/bin/env python3
"""
💪 MODULO MOTIVAZIONE INTERNA - Fase 5 AGI
Sistema di ricompensa interno che guida l'apprendimento autonomo
"""

import json
from typing import Dict, List
from pathlib import Path
from datetime import datetime
from collections import defaultdict


class SistemaMotivazione:
    """
    Sistema di motivazione interna - drive autonomo
    
    Funzionalità:
    - Genera ricompense interne per scoperte
    - Rinforza curiosità e esplorazione
    - Bilancia sicurezza ed esplorazione
    - Adatta motivazioni nel tempo
    """
    
    def __init__(self, path_motivazioni="memoria_permanente/motivazioni.json"):
        self.nome = "Motivazione Interna"
        self.path_motivazioni = Path(path_motivazioni)
        self.path_motivazioni.parent.mkdir(exist_ok=True)
        
        # Drive motivazionali (0.0 - 1.0)
        self.drives = {
            'curiosita': 0.7,  # Esplorare novità
            'competenza': 0.6,  # Migliorare abilità
            'autonomia': 0.5,  # Agire indipendentemente
            'connessione': 0.5,  # Interagire socialmente
            'sicurezza': 0.4,  # Evitare pericoli
            'crescita': 0.6  # Apprendere e svilupparsi
        }
        
        # Storia ricompense
        self.ricompense_storia = []
        
        # Soglie di sazietà (per evitare sovra-stimolazione)
        self.soglie_sazieta = {drive: 0.9 for drive in self.drives}
        
        # Carica stato
        self._carica()
        
        print(f"[{self.nome}] Inizializzato")
        print(f"  • Drive principali: curiosità ({self.drives['curiosita']:.0%}), " +
              f"competenza ({self.drives['competenza']:.0%})")
    
    def _carica(self):
        """Carica stato motivazionale"""
        if self.path_motivazioni.exists():
            try:
                with open(self.path_motivazioni, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.drives = data.get('drives', self.drives)
                    self.ricompense_storia = data.get('ricompense_storia', [])[-100:]  # Ultimi 100
            except Exception as e:
                print(f"[{self.nome}] ⚠️  Errore caricamento: {e}")
    
    def _salva(self):
        """Salva stato motivazionale"""
        try:
            data = {
                'drives': self.drives,
                'ricompense_storia': self.ricompense_storia[-100:],  # Solo ultimi 100
                'ultima_modifica': datetime.now().isoformat()
            }
            with open(self.path_motivazioni, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore salvataggio: {e}")
    
    def calcola_ricompensa_interna(self, esperienza: Dict) -> float:
        """
        Calcola ricompensa interna per un'esperienza
        
        Args:
            esperienza: Esperienza vissuta
        
        Returns:
            Ricompensa interna (0.0 - 1.0)
        """
        ricompensa = 0.0
        dettagli = []
        
        # Ricompensa per novità (curiosità)
        if esperienza.get('nuovo', False) or esperienza.get('scoperta', False):
            bonus_curiosita = self.drives['curiosita'] * 0.3
            ricompensa += bonus_curiosita
            dettagli.append(f"Novità: +{bonus_curiosita:.2f}")
        
        # Ricompensa per successo (competenza)
        if esperienza.get('successo', False):
            bonus_competenza = self.drives['competenza'] * 0.4
            ricompensa += bonus_competenza
            dettagli.append(f"Successo: +{bonus_competenza:.2f}")
        
        # Ricompensa per apprendimento (crescita)
        if esperienza.get('appreso', False) or esperienza.get('miglioramento', False):
            bonus_crescita = self.drives['crescita'] * 0.35
            ricompensa += bonus_crescita
            dettagli.append(f"Apprendimento: +{bonus_crescita:.2f}")
        
        # Ricompensa per interazione sociale (connessione)
        if 'persona' in str(esperienza.get('descrizione', '')).lower():
            if esperienza.get('valenza', 0) > 0:
                bonus_sociale = self.drives['connessione'] * 0.25
                ricompensa += bonus_sociale
                dettagli.append(f"Sociale positivo: +{bonus_sociale:.2f}")
        
        # Ricompensa per azione autonoma (autonomia)
        if esperienza.get('autonomo', False):
            bonus_autonomia = self.drives['autonomia'] * 0.2
            ricompensa += bonus_autonomia
            dettagli.append(f"Autonomia: +{bonus_autonomia:.2f}")
        
        # Penalità per fallimento che minaccia sicurezza
        if not esperienza.get('successo', True) and esperienza.get('pericoloso', False):
            penalita = -self.drives['sicurezza'] * 0.3
            ricompensa += penalita
            dettagli.append(f"Rischio: {penalita:.2f}")
        
        # Normalizza (0.0 - 1.0)
        ricompensa = max(0.0, min(1.0, ricompensa))
        
        # Registra
        self.ricompense_storia.append({
            'timestamp': datetime.now().isoformat(),
            'ricompensa': ricompensa,
            'dettagli': dettagli
        })
        
        return ricompensa
    
    def aggiorna_drives(self, esperienza: Dict, ricompensa: float):
        """
        Aggiorna drives motivazionali basati su esperienza
        
        Args:
            esperienza: Esperienza vissuta
            ricompensa: Ricompensa ottenuta
        """
        # Curiosità aumenta se scoperta qualcosa di nuovo e ricompensa alta
        if esperienza.get('nuovo', False) and ricompensa > 0.5:
            self.drives['curiosita'] = min(1.0, self.drives['curiosita'] + 0.05)
        
        # Curiosità diminuisce se troppo sazio
        if self.drives['curiosita'] > self.soglie_sazieta['curiosita']:
            self.drives['curiosita'] *= 0.95
        
        # Competenza aumenta con successi
        if esperienza.get('successo', False):
            self.drives['competenza'] = min(1.0, self.drives['competenza'] + 0.03)
        else:
            # Fallimenti aumentano voglia di migliorare
            self.drives['competenza'] = min(1.0, self.drives['competenza'] + 0.07)
        
        # Autonomia aumenta con azioni autonome riuscite
        if esperienza.get('autonomo', False) and esperienza.get('successo', False):
            self.drives['autonomia'] = min(1.0, self.drives['autonomia'] + 0.04)
        
        # Connessione aumenta con interazioni positive
        if 'persona' in str(esperienza.get('descrizione', '')).lower():
            if esperienza.get('valenza', 0) > 0:
                self.drives['connessione'] = min(1.0, self.drives['connessione'] + 0.05)
        
        # Sicurezza aumenta dopo fallimenti
        if not esperienza.get('successo', True):
            self.drives['sicurezza'] = min(1.0, self.drives['sicurezza'] + 0.1)
        else:
            # Successi riducono paura
            self.drives['sicurezza'] = max(0.2, self.drives['sicurezza'] - 0.02)
        
        # Crescita sempre attivo
        self.drives['crescita'] = max(0.5, self.drives['crescita'])
        
        self._salva()
    
    def suggerisci_azione_motivata(self, situazione: Dict, azioni_possibili: List[str]) -> Dict:
        """
        Suggerisce azione basata su motivazioni interne
        
        Args:
            situazione: Contesto corrente
            azioni_possibili: Azioni disponibili
        
        Returns:
            Dict con azione suggerita e motivazione
        """
        punteggi = {}
        
        for azione in azioni_possibili:
            punteggio = 0.0
            motivazioni = []
            
            # Esplora = curiosità
            if 'esplora' in azione or 'nuov' in azione:
                bonus = self.drives['curiosita'] * 0.8
                punteggio += bonus
                motivazioni.append(f"Curiosità ({self.drives['curiosita']:.0%})")
            
            # Impara = crescita
            if 'impara' in azione or 'studia' in azione:
                bonus = self.drives['crescita'] * 0.7
                punteggio += bonus
                motivazioni.append(f"Crescita ({self.drives['crescita']:.0%})")
            
            # Interagisci = connessione
            if 'avvicina' in azione or 'interag' in azione:
                bonus = self.drives['connessione'] * 0.6
                punteggio += bonus
                motivazioni.append(f"Connessione ({self.drives['connessione']:.0%})")
            
            # Mantieni distanza = sicurezza
            if 'distanza' in azione or 'sicur' in azione:
                bonus = self.drives['sicurezza'] * 0.5
                punteggio += bonus
                motivazioni.append(f"Sicurezza ({self.drives['sicurezza']:.0%})")
            
            # Migliora = competenza
            if 'migliora' in azione or 'pratica' in azione:
                bonus = self.drives['competenza'] * 0.7
                punteggio += bonus
                motivazioni.append(f"Competenza ({self.drives['competenza']:.0%})")
            
            punteggi[azione] = {
                'punteggio': punteggio,
                'motivazioni': motivazioni
            }
        
        # Trova azione con punteggio massimo
        if punteggi:
            azione_migliore = max(punteggi, key=lambda a: punteggi[a]['punteggio'])
            
            return {
                'azione_suggerita': azione_migliore,
                'punteggio': punteggi[azione_migliore]['punteggio'],
                'motivazioni': punteggi[azione_migliore]['motivazioni'],
                'tutti_punteggi': {a: p['punteggio'] for a, p in punteggi.items()}
            }
        
        return {
            'azione_suggerita': 'monitora',
            'punteggio': 0.0,
            'motivazioni': ['Nessuna motivazione particolare']
        }
    
    def elabora(self, contesto: Dict) -> Dict:
        """
        Elabora situazione con sistema motivazionale
        
        Args:
            contesto: Contesto con esperienza e azioni possibili
        
        Returns:
            Dict con motivazione e suggerimenti
        """
        esperienza = contesto.get('esperienza', {})
        azioni_possibili = contesto.get('azioni_possibili', [
            'esplora',
            'impara',
            'avvicinati',
            'mantieni_distanza',
            'migliora_abilita'
        ])
        
        # Calcola ricompensa interna
        ricompensa = self.calcola_ricompensa_interna(esperienza) if esperienza else 0.0
        
        # Aggiorna drives
        if esperienza:
            self.aggiorna_drives(esperienza, ricompensa)
        
        # Suggerisci azione motivata
        suggerimento = self.suggerisci_azione_motivata(contesto, azioni_possibili)
        
        return {
            'tipo': 'motivazione_interna',
            'ricompensa_interna': ricompensa,
            'drives_correnti': self.drives.copy(),
            'azione_suggerita': suggerimento['azione_suggerita'],
            'motivazioni': suggerimento['motivazioni'],
            'riflessione_motivazionale': self._genera_riflessione()
        }
    
    def _genera_riflessione(self) -> str:
        """Genera riflessione sui propri drives"""
        drive_dominante = max(self.drives, key=self.drives.get)
        valore = self.drives[drive_dominante]
        
        riflessioni = {
            'curiosita': f"Sono molto curioso ({valore:.0%}). Voglio scoprire cose nuove.",
            'competenza': f"Desidero migliorare le mie abilità ({valore:.0%}).",
            'autonomia': f"Mi piace agire in modo indipendente ({valore:.0%}).",
            'connessione': f"Cerco interazioni sociali ({valore:.0%}).",
            'sicurezza': f"Mi preoccupo della sicurezza ({valore:.0%}).",
            'crescita': f"Voglio continuare a crescere ({valore:.0%})."
        }
        
        return riflessioni.get(drive_dominante, "Sono in uno stato motivazionale equilibrato.")
    
    def get_statistiche(self) -> Dict:
        """Statistiche motivazionali"""
        ricompense_recenti = [r['ricompensa'] for r in self.ricompense_storia[-20:]]
        
        return {
            'drives': self.drives,
            'drive_dominante': max(self.drives, key=self.drives.get),
            'ricompensa_media_recente': sum(ricompense_recenti) / len(ricompense_recenti) if ricompense_recenti else 0.0,
            'totale_esperienze': len(self.ricompense_storia)
        }


# ==================== TEST ====================

if __name__ == "__main__":
    print("="*70)
    print("🧪 TEST MOTIVAZIONE INTERNA")
    print("="*70)
    
    mot = SistemaMotivazione()
    
    # Test 1: Ricompensa per scoperta
    print("\n--- Test 1: Ricompensa Scoperta ---")
    esperienza1 = {
        'descrizione': 'Nuovo ambiente scoperto',
        'nuovo': True,
        'successo': True,
        'valenza': 0.8
    }
    
    ricompensa = mot.calcola_ricompensa_interna(esperienza1)
    print(f"✅ Ricompensa interna: {ricompensa:.2f}")
    
    # Test 2: Suggerimento azione
    print("\n--- Test 2: Suggerimento Motivato ---")
    contesto = {
        'esperienza': esperienza1,
        'azioni_possibili': ['esplora', 'mantieni_distanza', 'avvicinati']
    }
    
    risultato = mot.elabora(contesto)
    print(f"✅ Azione suggerita: {risultato['azione_suggerita']}")
    print(f"   Motivazioni: {risultato['motivazioni']}")
    print(f"   Riflessione: {risultato['riflessione_motivazionale']}")
    
    # Test 3: Evoluzione drives
    print("\n--- Test 3: Evoluzione Drives ---")
    print("Drives iniziali:")
    for drive, val in mot.drives.items():
        print(f"  {drive}: {val:.0%}")
    
    # Simula 5 esperienze
    for i in range(5):
        exp = {
            'nuovo': i % 2 == 0,
            'successo': True,
            'autonomo': True
        }
        ric = mot.calcola_ricompensa_interna(exp)
        mot.aggiorna_drives(exp, ric)
    
    print("\nDrives dopo 5 esperienze:")
    for drive, val in mot.drives.items():
        print(f"  {drive}: {val:.0%}")
    
    # Statistiche
    print("\n--- Statistiche ---")
    stats = mot.get_statistiche()
    print(f"📊 Drive dominante: {stats['drive_dominante']}")
    print(f"   Ricompensa media: {stats['ricompensa_media_recente']:.2f}")
    print(f"   Esperienze totali: {stats['totale_esperienze']}")
    
    print("\n✅ Test completato!")

