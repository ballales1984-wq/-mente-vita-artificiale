#!/usr/bin/env python3
"""
🎯 MODULO OBIETTIVI AUTONOMI - Fase 5 AGI
Il sistema genera e persegue i propri obiettivi autonomamente
"""

import json
from typing import Dict, List, Optional
from pathlib import Path
from datetime import datetime
from enum import Enum


class StatoObiettivo(Enum):
    """Stati possibili di un obiettivo"""
    GENERATO = "generato"
    IN_CORSO = "in_corso"
    COMPLETATO = "completato"
    FALLITO = "fallito"
    SOSPESO = "sospeso"


class Obiettivo:
    """Rappresenta un obiettivo autonomo"""
    
    def __init__(self, descrizione: str, tipo: str, priorita: float):
        self.id = f"obj_{int(datetime.now().timestamp())}"
        self.descrizione = descrizione
        self.tipo = tipo  # 'conoscenza', 'sociale', 'miglioramento', 'esplorazione'
        self.priorita = priorita  # 0.0 - 1.0
        self.stato = StatoObiettivo.GENERATO
        self.motivazione = ""
        self.passi = []  # Lista di azioni da compiere
        self.progresso = 0.0  # 0.0 - 1.0
        self.data_creazione = datetime.now().isoformat()
        self.data_completamento = None
        self.ricompensa_attesa = 0.0
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'descrizione': self.descrizione,
            'tipo': self.tipo,
            'priorita': self.priorita,
            'stato': self.stato.value,
            'motivazione': self.motivazione,
            'passi': self.passi,
            'progresso': self.progresso,
            'data_creazione': self.data_creazione,
            'data_completamento': self.data_completamento,
            'ricompensa_attesa': self.ricompensa_attesa
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Obiettivo':
        obj = Obiettivo(
            descrizione=data['descrizione'],
            tipo=data['tipo'],
            priorita=data['priorita']
        )
        obj.id = data['id']
        obj.stato = StatoObiettivo(data.get('stato', 'generato'))
        obj.motivazione = data.get('motivazione', '')
        obj.passi = data.get('passi', [])
        obj.progresso = data.get('progresso', 0.0)
        obj.data_creazione = data.get('data_creazione', datetime.now().isoformat())
        obj.data_completamento = data.get('data_completamento')
        obj.ricompensa_attesa = data.get('ricompensa_attesa', 0.0)
        return obj


class SistemaObiettiviAutonomi:
    """
    Sistema che genera e persegue obiettivi autonomamente
    
    Funzionalità:
    - Genera obiettivi basati su curiosità, lacune, emozioni
    - Prioritizza obiettivi dinamicamente
    - Crea piani multi-step
    - Monitora progresso
    - Si adatta se fallisce
    """
    
    def __init__(self, path_obiettivi="memoria_permanente/obiettivi.json"):
        self.nome = "Obiettivi Autonomi"
        self.path_obiettivi = Path(path_obiettivi)
        self.path_obiettivi.parent.mkdir(exist_ok=True)
        
        # Obiettivi attivi
        self.obiettivi: List[Obiettivo] = []
        
        # Sistema motivazionale
        self.motivazioni = {
            'curiosita': 0.5,  # Desiderio di esplorare
            'miglioramento': 0.5,  # Desiderio di migliorare abilità
            'sociale': 0.5,  # Desiderio di interagire
            'sicurezza': 0.3  # Evitare pericoli
        }
        
        # Carica obiettivi
        self._carica()
        
        print(f"[{self.nome}] Inizializzato")
        print(f"  • Obiettivi attivi: {len([o for o in self.obiettivi if o.stato == StatoObiettivo.IN_CORSO])}")
        print(f"  • Obiettivi completati: {len([o for o in self.obiettivi if o.stato == StatoObiettivo.COMPLETATO])}")
    
    def _carica(self):
        """Carica obiettivi da file"""
        if self.path_obiettivi.exists():
            try:
                with open(self.path_obiettivi, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.obiettivi = [Obiettivo.from_dict(o) for o in data.get('obiettivi', [])]
                    self.motivazioni = data.get('motivazioni', self.motivazioni)
            except Exception as e:
                print(f"[{self.nome}] ⚠️  Errore caricamento: {e}")
    
    def _salva(self):
        """Salva obiettivi su file"""
        try:
            data = {
                'obiettivi': [o.to_dict() for o in self.obiettivi],
                'motivazioni': self.motivazioni
            }
            with open(self.path_obiettivi, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore salvataggio: {e}")
    
    def genera_obiettivo(self, contesto: Dict) -> Optional[Obiettivo]:
        """
        Genera un nuovo obiettivo basato sul contesto
        
        Args:
            contesto: Situazione corrente e storia
        
        Returns:
            Nuovo obiettivo (o None se non necessario)
        """
        # Analizza contesto per trovare opportunità
        lacune = contesto.get('lacune_conoscenza', [])
        emozione = contesto.get('emozione', 'neutro')
        valenza = contesto.get('valenza', 0)
        esperienze_recenti = contesto.get('esperienze_recenti', [])
        
        # Genera obiettivo basato su lacune
        if lacune and self.motivazioni['curiosita'] > 0.4:
            lacuna = lacune[0]
            obiettivo = Obiettivo(
                descrizione=f"Migliorare conoscenza su '{lacuna['argomento']}'",
                tipo='conoscenza',
                priorita=0.8
            )
            obiettivo.motivazione = f"Ho poca esperienza con {lacuna['argomento']} (livello: {lacuna['livello']:.0%})"
            obiettivo.passi = [
                f"Cerca situazioni con {lacuna['argomento']}",
                "Osserva e raccogli dati",
                "Prova azioni diverse",
                "Valuta risultati"
            ]
            obiettivo.ricompensa_attesa = 0.5
            return obiettivo
        
        # Genera obiettivo sociale se emozione positiva
        if valenza > 0.5 and 'persona' in str(esperienze_recenti).lower():
            if self.motivazioni['sociale'] > 0.5:
                obiettivo = Obiettivo(
                    descrizione="Migliorare interazione sociale",
                    tipo='sociale',
                    priorita=0.6
                )
                obiettivo.motivazione = "Interazioni recenti positive, voglio migliorare"
                obiettivo.passi = [
                    "Riconosci segnali sociali",
                    "Rispondi appropriatamente",
                    "Valuta reazioni",
                    "Adatta comportamento"
                ]
                obiettivo.ricompensa_attesa = 0.7
                return obiettivo
        
        # Genera obiettivo esplorazione
        if self.motivazioni['curiosita'] > 0.6:
            if len([o for o in self.obiettivi if o.tipo == 'esplorazione' and o.stato == StatoObiettivo.IN_CORSO]) == 0:
                obiettivo = Obiettivo(
                    descrizione="Esplorare nuovi ambienti/situazioni",
                    tipo='esplorazione',
                    priorita=0.5
                )
                obiettivo.motivazione = "Curiosità elevata, voglio scoprire cose nuove"
                obiettivo.passi = [
                    "Cerca stimoli nuovi",
                    "Analizza novità",
                    "Sperimenta risposte",
                    "Memorizza risultati"
                ]
                obiettivo.ricompensa_attesa = 0.6
                return obiettivo
        
        return None
    
    def aggiorna_motivazioni(self, esperienza: Dict):
        """Aggiorna motivazioni basate su esperienza"""
        # Curiosità aumenta con scoperte
        if esperienza.get('nuovo', False):
            self.motivazioni['curiosita'] = min(1.0, self.motivazioni['curiosita'] + 0.05)
        
        # Sociale aumenta con interazioni positive
        if 'persona' in esperienza.get('descrizione', '').lower():
            if esperienza.get('successo', False):
                self.motivazioni['sociale'] = min(1.0, self.motivazioni['sociale'] + 0.05)
        
        # Miglioramento aumenta con successi
        if esperienza.get('successo', False):
            self.motivazioni['miglioramento'] = min(1.0, self.motivazioni['miglioramento'] + 0.03)
        else:
            self.motivazioni['miglioramento'] = min(1.0, self.motivazioni['miglioramento'] + 0.07)
        
        # Sicurezza aumenta con fallimenti
        if not esperienza.get('successo', True):
            self.motivazioni['sicurezza'] = min(1.0, self.motivazioni['sicurezza'] + 0.1)
    
    def seleziona_obiettivo_corrente(self) -> Optional[Obiettivo]:
        """Seleziona obiettivo prioritario da perseguire"""
        obiettivi_attivi = [o for o in self.obiettivi if o.stato in [StatoObiettivo.GENERATO, StatoObiettivo.IN_CORSO]]
        
        if not obiettivi_attivi:
            return None
        
        # Ordina per priorità (considerando anche progresso)
        obiettivi_attivi.sort(key=lambda o: o.priorita * (1.0 - o.progresso * 0.5), reverse=True)
        
        return obiettivi_attivi[0]
    
    def avanza_obiettivo(self, obiettivo_id: str, successo: bool) -> Dict:
        """Avanza progresso su obiettivo"""
        obiettivo = next((o for o in self.obiettivi if o.id == obiettivo_id), None)
        
        if not obiettivo:
            return {'errore': 'Obiettivo non trovato'}
        
        # Aggiorna progresso
        if successo:
            obiettivo.progresso += 0.25  # +25% per successo
        else:
            obiettivo.progresso += 0.1  # +10% anche per fallimento (esperienza)
        
        obiettivo.progresso = min(1.0, obiettivo.progresso)
        
        # Check completamento
        if obiettivo.progresso >= 1.0:
            obiettivo.stato = StatoObiettivo.COMPLETATO
            obiettivo.data_completamento = datetime.now().isoformat()
        else:
            obiettivo.stato = StatoObiettivo.IN_CORSO
        
        self._salva()
        
        return {
            'obiettivo_id': obiettivo_id,
            'progresso': obiettivo.progresso,
            'stato': obiettivo.stato.value,
            'completato': obiettivo.stato == StatoObiettivo.COMPLETATO
        }
    
    def elabora(self, contesto: Dict) -> Dict:
        """
        Elabora situazione e gestisce obiettivi
        
        Args:
            contesto: Contesto corrente
        
        Returns:
            Dict con obiettivo corrente e suggerimenti
        """
        # Aggiorna motivazioni
        if 'esperienza' in contesto:
            self.aggiorna_motivazioni(contesto['esperienza'])
        
        # Genera nuovo obiettivo se necessario
        if len([o for o in self.obiettivi if o.stato == StatoObiettivo.IN_CORSO]) < 2:
            nuovo_obj = self.genera_obiettivo(contesto)
            if nuovo_obj:
                self.obiettivi.append(nuovo_obj)
                self._salva()
                print(f"[{self.nome}] 🎯 Nuovo obiettivo: {nuovo_obj.descrizione}")
        
        # Seleziona obiettivo corrente
        obiettivo_corrente = self.seleziona_obiettivo_corrente()
        
        if obiettivo_corrente:
            # Attiva se non ancora attivo
            if obiettivo_corrente.stato == StatoObiettivo.GENERATO:
                obiettivo_corrente.stato = StatoObiettivo.IN_CORSO
                self._salva()
            
            # Trova prossimo passo
            passo_idx = int(obiettivo_corrente.progresso * len(obiettivo_corrente.passi))
            passo_corrente = obiettivo_corrente.passi[passo_idx] if passo_idx < len(obiettivo_corrente.passi) else "Completa obiettivo"
            
            return {
                'tipo': 'obiettivo_autonomo',
                'obiettivo': {
                    'id': obiettivo_corrente.id,
                    'descrizione': obiettivo_corrente.descrizione,
                    'tipo': obiettivo_corrente.tipo,
                    'priorita': obiettivo_corrente.priorita,
                    'progresso': obiettivo_corrente.progresso,
                    'motivazione': obiettivo_corrente.motivazione
                },
                'passo_corrente': passo_corrente,
                'motivazioni': self.motivazioni,
                'suggerimento_azione': self._suggerisci_azione(obiettivo_corrente, contesto)
            }
        else:
            return {
                'tipo': 'nessun_obiettivo',
                'motivazioni': self.motivazioni,
                'suggerimento': 'Osserva e attendi opportunità'
            }
    
    def _suggerisci_azione(self, obiettivo: Obiettivo, contesto: Dict) -> str:
        """Suggerisce azione concreta per obiettivo"""
        if obiettivo.tipo == 'conoscenza':
            return "Cerca situazioni che coinvolgono questo argomento"
        elif obiettivo.tipo == 'sociale':
            return "Interagisci con persone quando possibile"
        elif obiettivo.tipo == 'esplorazione':
            return "Esplora ambienti nuovi o diversi"
        elif obiettivo.tipo == 'miglioramento':
            return "Prova tecniche diverse e confronta risultati"
        else:
            return "Continua ad osservare e imparare"
    
    def get_statistiche(self) -> Dict:
        """Statistiche sistema obiettivi"""
        return {
            'totale_obiettivi': len(self.obiettivi),
            'in_corso': len([o for o in self.obiettivi if o.stato == StatoObiettivo.IN_CORSO]),
            'completati': len([o for o in self.obiettivi if o.stato == StatoObiettivo.COMPLETATO]),
            'falliti': len([o for o in self.obiettivi if o.stato == StatoObiettivo.FALLITO]),
            'motivazioni': self.motivazioni,
            'obiettivo_corrente': self.seleziona_obiettivo_corrente().descrizione if self.seleziona_obiettivo_corrente() else None
        }


# ==================== TEST ====================

if __name__ == "__main__":
    print("="*70)
    print("🧪 TEST OBIETTIVI AUTONOMI")
    print("="*70)
    
    sistema = SistemaObiettiviAutonomi()
    
    # Test 1: Genera obiettivo da lacuna
    print("\n--- Test 1: Generazione Obiettivo ---")
    contesto = {
        'lacune_conoscenza': [
            {'argomento': 'persona_avvicinamento', 'livello': 0.3}
        ],
        'emozione': 'neutro',
        'valenza': 0.0
    }
    
    risultato = sistema.elabora(contesto)
    if risultato['tipo'] == 'obiettivo_autonomo':
        print(f"✅ Obiettivo generato: {risultato['obiettivo']['descrizione']}")
        print(f"   Motivazione: {risultato['obiettivo']['motivazione']}")
        print(f"   Passo corrente: {risultato['passo_corrente']}")
    
    # Test 2: Avanza obiettivo
    print("\n--- Test 2: Avanzamento ---")
    obj_id = risultato['obiettivo']['id']
    for i in range(3):
        avanzamento = sistema.avanza_obiettivo(obj_id, successo=True)
        print(f"  Step {i+1}: Progresso {avanzamento['progresso']:.0%}")
    
    # Test 3: Statistiche
    print("\n--- Test 3: Statistiche ---")
    stats = sistema.get_statistiche()
    print(f"📊 Obiettivi totali: {stats['totale_obiettivi']}")
    print(f"   In corso: {stats['in_corso']}")
    print(f"   Completati: {stats['completati']}")
    print(f"   Motivazioni: {stats['motivazioni']}")
    
    print("\n✅ Test completato!")


