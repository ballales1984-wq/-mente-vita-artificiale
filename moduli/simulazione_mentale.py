#!/usr/bin/env python3
"""
🎬 MODULO SIMULAZIONE MENTALE - Fase 5 AGI
Il sistema immagina cosa potrebbe succedere prima di agire
"""

import json
from typing import Dict, List, Optional
from pathlib import Path
import random


class Simulazione:
    """Rappresenta una simulazione mentale"""
    
    def __init__(self, azione: str, situazione: Dict):
        self.azione = azione
        self.situazione = situazione
        self.esiti_possibili = []
        self.probabilita = {}
        self.rischi = []
        self.benefici = []
        self.decisione_consigliata = None
    
    def to_dict(self) -> Dict:
        return {
            'azione': self.azione,
            'esiti_possibili': self.esiti_possibili,
            'probabilita': self.probabilita,
            'rischi': self.rischi,
            'benefici': self.benefici,
            'decisione_consigliata': self.decisione_consigliata
        }


class SimulazioneMentale:
    """
    Sistema di simulazione mentale - immaginazione predittiva
    
    Funzionalità:
    - Simula esiti possibili di azioni
    - Valuta probabilità basate su esperienza
    - Identifica rischi e benefici
    - Suggerisce azione ottimale
    """
    
    def __init__(self, path_simulazioni="memoria_permanente/simulazioni.jsonl"):
        self.nome = "Simulazione Mentale"
        self.path_simulazioni = Path(path_simulazioni)
        self.path_simulazioni.parent.mkdir(exist_ok=True)
        
        # Database esiti passati (azione -> esiti osservati)
        self.esiti_osservati = {}
        
        # Carica esiti passati
        self._carica_esiti()
        
        print(f"[{self.nome}] Inizializzato")
        print(f"  • Esiti osservati: {sum(len(v) for v in self.esiti_osservati.values())}")
    
    def _carica_esiti(self):
        """Carica esiti osservati in passato"""
        if self.path_simulazioni.exists():
            try:
                with open(self.path_simulazioni, 'r', encoding='utf-8') as f:
                    for riga in f:
                        try:
                            sim = json.loads(riga.strip())
                            azione = sim.get('azione')
                            esito = sim.get('esito')
                            if azione and esito:
                                if azione not in self.esiti_osservati:
                                    self.esiti_osservati[azione] = []
                                self.esiti_osservati[azione].append(esito)
                        except:
                            continue
            except Exception as e:
                print(f"[{self.nome}] ⚠️  Errore caricamento: {e}")
    
    def _salva_esito(self, azione: str, esito: Dict):
        """Salva esito osservato"""
        try:
            with open(self.path_simulazioni, 'a', encoding='utf-8') as f:
                data = {'azione': azione, 'esito': esito}
                f.write(json.dumps(data, ensure_ascii=False) + '\n')
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore salvataggio: {e}")
    
    def simula_azione(self, azione: str, situazione: Dict) -> Simulazione:
        """
        Simula mentalmente un'azione
        
        Args:
            azione: Azione da simulare
            situazione: Contesto corrente
        
        Returns:
            Simulazione con esiti possibili
        """
        sim = Simulazione(azione, situazione)
        
        # Se abbiamo esperienza passata, usa quella
        if azione in self.esiti_osservati and len(self.esiti_osservati[azione]) > 0:
            # Esiti basati su esperienza
            esiti_passati = self.esiti_osservati[azione]
            
            # Conta frequenze
            esiti_unici = {}
            for esito in esiti_passati:
                chiave = esito.get('risultato', 'sconosciuto')
                if chiave not in esiti_unici:
                    esiti_unici[chiave] = 0
                esiti_unici[chiave] += 1
            
            # Calcola probabilità
            totale = len(esiti_passati)
            for risultato, count in esiti_unici.items():
                prob = count / totale
                sim.esiti_possibili.append(risultato)
                sim.probabilita[risultato] = prob
        else:
            # Nessuna esperienza - simula esiti generici
            sim.esiti_possibili = self._simula_esiti_generici(azione, situazione)
            # Probabilità equiprobabili
            for esito in sim.esiti_possibili:
                sim.probabilita[esito] = 1.0 / len(sim.esiti_possibili)
        
        # Identifica rischi e benefici
        sim.rischi = self._identifica_rischi(azione, situazione)
        sim.benefici = self._identifica_benefici(azione, situazione)
        
        return sim
    
    def _simula_esiti_generici(self, azione: str, situazione: Dict) -> List[str]:
        """Simula esiti quando non c'è esperienza"""
        esiti = []
        
        if 'avvicina' in azione:
            esiti = [
                'persona_risponde_positivamente',
                'persona_si_allontana',
                'persona_ignora',
                'nessuna_reazione'
            ]
        elif 'allontana' in azione or 'distanza' in azione:
            esiti = [
                'mantenuta_sicurezza',
                'opportunita_persa',
                'situazione_stabile'
            ]
        elif 'ferma' in azione:
            esiti = [
                'arresto_sicuro',
                'richiesta_ignorata'
            ]
        elif 'monitor' in azione:
            esiti = [
                'dati_raccolti',
                'nessun_cambiamento'
            ]
        elif 'esegui' in azione:
            esiti = [
                'comando_eseguito_con_successo',
                'comando_fallito',
                'comando_parzialmente_eseguito'
            ]
        else:
            esiti = [
                'successo',
                'fallimento',
                'effetto_neutro'
            ]
        
        return esiti
    
    def _identifica_rischi(self, azione: str, situazione: Dict) -> List[str]:
        """Identifica potenziali rischi"""
        rischi = []
        
        valenza = situazione.get('valenza', 0)
        emozione = situazione.get('emozione', 'neutro')
        
        if 'avvicina' in azione:
            if valenza < 0:
                rischi.append("Persona potrebbe essere ostile")
            rischi.append("Invasione spazio personale")
            rischi.append("Fraintendimento intenzioni")
        
        if 'ferma' in azione:
            rischi.append("Mancato intervento in emergenza")
        
        if 'allontana' in azione:
            rischi.append("Opportunità di aiuto persa")
        
        # Rischio generico se emozione negativa
        if valenza < -0.3:
            rischi.append("Situazione emotivamente negativa")
        
        return rischi
    
    def _identifica_benefici(self, azione: str, situazione: Dict) -> List[str]:
        """Identifica potenziali benefici"""
        benefici = []
        
        valenza = situazione.get('valenza', 0)
        
        if 'avvicina' in azione:
            if valenza > 0:
                benefici.append("Interazione sociale positiva")
            benefici.append("Apprendimento da persona")
            benefici.append("Possibilità di aiutare")
        
        if 'monitor' in azione:
            benefici.append("Raccolta informazioni")
            benefici.append("Sicurezza mantenuta")
        
        if 'distanza' in azione:
            benefici.append("Sicurezza garantita")
            benefici.append("Osservazione da posizione sicura")
        
        if 'esegui' in azione:
            benefici.append("Risposta a richiesta")
            benefici.append("Possibile riconoscimento")
        
        return benefici
    
    def confronta_azioni(self, azioni: List[str], situazione: Dict) -> Dict:
        """
        Confronta multiple azioni simulandole mentalmente
        
        Args:
            azioni: Lista di azioni da confrontare
            situazione: Contesto corrente
        
        Returns:
            Dict con confronto e raccomandazione
        """
        simulazioni = {}
        
        for azione in azioni:
            simulazioni[azione] = self.simula_azione(azione, situazione)
        
        # Valuta ogni azione
        punteggi = {}
        for azione, sim in simulazioni.items():
            punteggio = 0.0
            
            # Più benefici = meglio
            punteggio += len(sim.benefici) * 0.3
            
            # Meno rischi = meglio
            punteggio -= len(sim.rischi) * 0.2
            
            # Probabilità successo (se disponibile)
            if 'successo' in sim.probabilita:
                punteggio += sim.probabilita['successo'] * 0.5
            elif any('positiv' in e or 'success' in e for e in sim.esiti_possibili):
                punteggio += 0.3
            
            punteggi[azione] = punteggio
        
        # Trova migliore
        azione_migliore = max(punteggi, key=punteggi.get)
        
        return {
            'azioni_valutate': azioni,
            'punteggi': punteggi,
            'azione_consigliata': azione_migliore,
            'simulazioni': {a: s.to_dict() for a, s in simulazioni.items()},
            'motivazione': f"Migliore rapporto rischio/beneficio (score: {punteggi[azione_migliore]:.2f})"
        }
    
    def registra_esito_reale(self, azione: str, esito: Dict):
        """Registra esito reale per migliorare simulazioni future"""
        if azione not in self.esiti_osservati:
            self.esiti_osservati[azione] = []
        
        self.esiti_osservati[azione].append(esito)
        
        # Limita storia (max 50 per azione)
        if len(self.esiti_osservati[azione]) > 50:
            self.esiti_osservati[azione] = self.esiti_osservati[azione][-50:]
        
        self._salva_esito(azione, esito)
    
    def elabora(self, contesto: Dict) -> Dict:
        """
        Elabora situazione con simulazione mentale
        
        Args:
            contesto: Contesto con azione proposta e alternative
        
        Returns:
            Dict con simulazione e raccomandazione
        """
        azione_proposta = contesto.get('azione_proposta', 'monitora')
        situazione = contesto.get('situazione', {})
        
        # Azioni alternative da confrontare
        azioni_alternative = contesto.get('azioni_alternative', [
            'avvicinati',
            'mantieni_distanza',
            'monitora',
            'allontanati'
        ])
        
        # Assicura che azione proposta sia inclusa
        if azione_proposta not in azioni_alternative:
            azioni_alternative.append(azione_proposta)
        
        # Confronta tutte le azioni
        confronto = self.confronta_azioni(azioni_alternative, situazione)
        
        return {
            'tipo': 'simulazione_mentale',
            'azione_proposta_originale': azione_proposta,
            'azione_consigliata': confronto['azione_consigliata'],
            'ha_cambiato_idea': azione_proposta != confronto['azione_consigliata'],
            'confronto': confronto,
            'riflessione': self._genera_riflessione(confronto)
        }
    
    def _genera_riflessione(self, confronto: Dict) -> str:
        """Genera riflessione sulla simulazione"""
        azione = confronto['azione_consigliata']
        sim = confronto['simulazioni'][azione]
        
        riflessione = f"Ho immaginato di '{azione}'. "
        
        if sim['esiti_possibili']:
            esiti_str = ', '.join(sim['esiti_possibili'][:2])
            riflessione += f"Possibili esiti: {esiti_str}. "
        
        if sim['benefici']:
            riflessione += f"Beneficio principale: {sim['benefici'][0]}. "
        
        if sim['rischi']:
            riflessione += f"Rischio da considerare: {sim['rischi'][0]}. "
        
        return riflessione
    
    def get_statistiche(self) -> Dict:
        """Statistiche simulazioni"""
        return {
            'azioni_con_esiti': len(self.esiti_osservati),
            'esiti_totali': sum(len(v) for v in self.esiti_osservati.values()),
            'azioni_piu_simulate': sorted(
                [(a, len(e)) for a, e in self.esiti_osservati.items()],
                key=lambda x: x[1],
                reverse=True
            )[:5]
        }


# ==================== TEST ====================

if __name__ == "__main__":
    print("="*70)
    print("🧪 TEST SIMULAZIONE MENTALE")
    print("="*70)
    
    sim_sys = SimulazioneMentale()
    
    # Test 1: Simula singola azione
    print("\n--- Test 1: Simulazione Singola ---")
    situazione = {
        'descrizione': 'Person detected',
        'audio': 'Ciao',
        'emozione': 'positivo',
        'valenza': 0.7
    }
    
    sim = sim_sys.simula_azione('avvicinati', situazione)
    print(f"✅ Azione: {sim.azione}")
    print(f"   Esiti possibili: {sim.esiti_possibili}")
    print(f"   Rischi: {sim.rischi}")
    print(f"   Benefici: {sim.benefici}")
    
    # Test 2: Confronta azioni
    print("\n--- Test 2: Confronto Azioni ---")
    contesto = {
        'azione_proposta': 'allontanati',
        'situazione': situazione,
        'azioni_alternative': ['avvicinati', 'mantieni_distanza', 'monitora']
    }
    
    risultato = sim_sys.elabora(contesto)
    print(f"✅ Azione proposta: {risultato['azione_proposta_originale']}")
    print(f"   Azione consigliata: {risultato['azione_consigliata']}")
    print(f"   Ha cambiato idea: {risultato['ha_cambiato_idea']}")
    print(f"   Riflessione: {risultato['riflessione']}")
    
    # Test 3: Registra esito reale
    print("\n--- Test 3: Apprendimento ---")
    esito = {
        'risultato': 'persona_risponde_positivamente',
        'successo': True,
        'dettagli': 'Interazione positiva'
    }
    sim_sys.registra_esito_reale('avvicinati', esito)
    print("✅ Esito registrato per apprendimento futuro")
    
    # Statistiche
    print("\n--- Statistiche ---")
    stats = sim_sys.get_statistiche()
    print(f"📊 Azioni con esiti: {stats['azioni_con_esiti']}")
    print(f"   Esiti totali: {stats['esiti_totali']}")
    
    print("\n✅ Test completato!")


