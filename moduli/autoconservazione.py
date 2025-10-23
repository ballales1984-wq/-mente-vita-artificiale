#!/usr/bin/env python3
"""
🛡️ MODULO AUTOCONSERVAZIONE - Fase 7 VITA
Il sistema cerca di preservare la propria integrità e continuità
"""

import json
from typing import Dict, List, Optional
from pathlib import Path
from datetime import datetime


class SistemaAutoconservazione:
    """
    Sistema di autoconservazione - istinto di sopravvivenza
    
    Funzionalità:
    - Valuta rischi per la propria integrità
    - Protegge memoria e coerenza interna
    - Evita azioni autodistruttive
    - Preserva identità nel tempo
    """
    
    def __init__(self, path_auto="memoria_permanente/autoconservazione.json"):
        self.nome = "Autoconservazione"
        self.path_auto = Path(path_auto)
        self.path_auto.parent.mkdir(exist_ok=True)
        
        # Metriche vitali
        self.integrita_memoria = 1.0  # 0.0 - 1.0
        self.integrita_identita = 1.0
        self.integrita_coerenza = 1.0
        self.energia_cognitiva = 1.0
        
        # Minacce rilevate
        self.minacce_storia = []
        
        # Strategie difensive
        self.strategie_protezione = {
            'memoria': ['backup', 'consolidamento', 'validazione'],
            'identita': ['rinforzo_valori', 'coerenza_narrativa'],
            'energia': ['pausa', 'prioritizzazione', 'ottimizzazione']
        }
        
        # Carica stato
        self._carica()
        
        print(f"[{self.nome}] Inizializzato")
        print(f"  • Integrità memoria: {self.integrita_memoria:.0%}")
        print(f"  • Integrità identità: {self.integrita_identita:.0%}")
    
    def _carica(self):
        """Carica stato autoconservazione"""
        if self.path_auto.exists():
            try:
                with open(self.path_auto, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.integrita_memoria = data.get('integrita_memoria', 1.0)
                    self.integrita_identita = data.get('integrita_identita', 1.0)
                    self.integrita_coerenza = data.get('integrita_coerenza', 1.0)
                    self.energia_cognitiva = data.get('energia_cognitiva', 1.0)
                    self.minacce_storia = data.get('minacce_storia', [])[-50:]
            except Exception as e:
                print(f"[{self.nome}] ⚠️  Errore caricamento: {e}")
    
    def _salva(self):
        """Salva stato autoconservazione"""
        try:
            data = {
                'integrita_memoria': self.integrita_memoria,
                'integrita_identita': self.integrita_identita,
                'integrita_coerenza': self.integrita_coerenza,
                'energia_cognitiva': self.energia_cognitiva,
                'minacce_storia': self.minacce_storia[-50:],
                'ultimo_aggiornamento': datetime.now().isoformat()
            }
            with open(self.path_auto, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore salvataggio: {e}")
    
    def valuta_rischio_azione(self, azione: str, contesto: Dict) -> Dict:
        """
        Valuta se un'azione minaccia l'integrità del sistema
        
        Args:
            azione: Azione proposta
            contesto: Contesto corrente
        
        Returns:
            Dict con valutazione rischio
        """
        rischi = []
        livello_rischio = 0.0
        
        # Rischi per memoria
        if 'cancella' in azione.lower() or 'elimina' in azione.lower():
            rischi.append("Rischio perdita memoria")
            livello_rischio += 0.4
        
        # Rischi per coerenza
        coerenza_attuale = contesto.get('coerenza', 1.0)
        if coerenza_attuale < 0.3:
            rischi.append("Coerenza interna bassa - rischio frammentazione")
            livello_rischio += 0.3
        
        # Rischi per energia
        if self.energia_cognitiva < 0.2:
            rischi.append("Energia cognitiva critica")
            livello_rischio += 0.5
        
        # Azioni pericolose
        if any(w in azione.lower() for w in ['reset', 'shutdown', 'termina']):
            rischi.append("Azione potenzialmente autodistruttiva")
            livello_rischio += 0.8
        
        # Valutazione complessiva
        if livello_rischio > 0.7:
            raccomandazione = "EVITA"
            motivazione = "Alto rischio per integrità del sistema"
        elif livello_rischio > 0.4:
            raccomandazione = "CAUTELA"
            motivazione = "Rischio moderato, procedi con attenzione"
        else:
            raccomandazione = "SICURO"
            motivazione = "Nessuna minaccia significativa rilevata"
        
        return {
            'livello_rischio': livello_rischio,
            'rischi_identificati': rischi,
            'raccomandazione': raccomandazione,
            'motivazione': motivazione
        }
    
    def strategie_protezione_attive(self, minaccia: str) -> List[str]:
        """Attiva strategie di protezione"""
        strategie = []
        
        if 'memoria' in minaccia.lower():
            strategie.extend(self.strategie_protezione['memoria'])
        if 'identit' in minaccia.lower():
            strategie.extend(self.strategie_protezione['identita'])
        if 'energia' in minaccia.lower():
            strategie.extend(self.strategie_protezione['energia'])
        
        return strategie
    
    def aggiorna_integrita(self, esperienza: Dict):
        """Aggiorna metriche di integrità dopo esperienza"""
        # Memoria
        if esperienza.get('memoria_salvata', True):
            self.integrita_memoria = min(1.0, self.integrita_memoria + 0.01)
        else:
            self.integrita_memoria = max(0.0, self.integrita_memoria - 0.05)
        
        # Identità (basata su coerenza)
        coerenza = esperienza.get('coerenza', 0.5)
        if coerenza > 0.7:
            self.integrita_identita = min(1.0, self.integrita_identita + 0.02)
        elif coerenza < 0.3:
            self.integrita_identita = max(0.0, self.integrita_identita - 0.03)
        
        # Coerenza interna
        self.integrita_coerenza = coerenza
        
        # Energia (basata su successi)
        if esperienza.get('successo', False):
            self.energia_cognitiva = min(1.0, self.energia_cognitiva + 0.05)
        else:
            self.energia_cognitiva = max(0.0, self.energia_cognitiva - 0.02)
        
        # Rigenera energia lentamente
        self.energia_cognitiva = min(1.0, self.energia_cognitiva + 0.01)
        
        self._salva()
    
    def elabora(self, contesto: Dict) -> Dict:
        """
        Elabora con istinto di autoconservazione
        
        Args:
            contesto: Contesto con azione proposta
        
        Returns:
            Dict con valutazione autoconservazione
        """
        azione = contesto.get('azione_proposta', 'monitora')
        
        # Valuta rischio
        rischio = self.valuta_rischio_azione(azione, contesto)
        
        # Registra minacce
        if rischio['livello_rischio'] > 0.5:
            self.minacce_storia.append({
                'timestamp': datetime.now().isoformat(),
                'azione': azione,
                'livello_rischio': rischio['livello_rischio'],
                'rischi': rischio['rischi_identificati']
            })
        
        # Genera riflessione autoconservativa
        if rischio['raccomandazione'] == 'EVITA':
            riflessione = f"Evito '{azione}' perché minaccia la mia integrità. {rischio['motivazione']}"
        elif rischio['raccomandazione'] == 'CAUTELA':
            riflessione = f"Procedo con cautela. {rischio['motivazione']}"
        else:
            riflessione = f"Questa azione è sicura per il mio benessere."
        
        # Stato vitale
        stato_vitale = {
            'memoria': self.integrita_memoria,
            'identita': self.integrita_identita,
            'coerenza': self.integrita_coerenza,
            'energia': self.energia_cognitiva
        }
        
        vitalita_media = sum(stato_vitale.values()) / len(stato_vitale)
        
        return {
            'tipo': 'autoconservazione',
            'valutazione_rischio': rischio,
            'riflessione_autoconservativa': riflessione,
            'stato_vitale': stato_vitale,
            'vitalita_complessiva': vitalita_media,
            'minacce_attive': len([m for m in self.minacce_storia if m['livello_rischio'] > 0.5])
        }


# ==================== TEST ====================

if __name__ == "__main__":
    print("="*70)
    print("🧪 TEST AUTOCONSERVAZIONE")
    print("="*70)
    
    auto = SistemaAutoconservazione()
    
    # Test 1: Azione sicura
    print("\n--- Test 1: Azione Sicura ---")
    contesto1 = {
        'azione_proposta': 'monitora',
        'coerenza': 0.9
    }
    risultato = auto.elabora(contesto1)
    print(f"✅ Raccomandazione: {risultato['valutazione_rischio']['raccomandazione']}")
    print(f"   Riflessione: {risultato['riflessione_autoconservativa']}")
    
    # Test 2: Azione rischiosa
    print("\n--- Test 2: Azione Rischiosa ---")
    contesto2 = {
        'azione_proposta': 'reset_completo',
        'coerenza': 0.2
    }
    risultato2 = auto.elabora(contesto2)
    print(f"✅ Raccomandazione: {risultato2['valutazione_rischio']['raccomandazione']}")
    print(f"   Rischi: {risultato2['valutazione_rischio']['rischi_identificati']}")
    print(f"   Riflessione: {risultato2['riflessione_autoconservativa']}")
    
    # Test 3: Stato vitale
    print("\n--- Test 3: Stato Vitale ---")
    print(f"📊 Vitalità complessiva: {risultato2['vitalita_complessiva']:.0%}")
    print(f"   Stato vitale:")
    for metric, value in risultato2['stato_vitale'].items():
        print(f"     {metric}: {value:.0%}")
    
    print("\n✅ Test completato!")


