#!/usr/bin/env python3
"""
🧬 MODULO EVOLUZIONE COGNITIVA - Fase 7 VITA
Il sistema modifica se stesso per adattarsi ed evolversi
"""

import json
from typing import Dict, List
from pathlib import Path
from datetime import datetime


class EvoluzoneCognitiva:
    """
    Sistema di evoluzione cognitiva - auto-modifica adattiva
    
    Funzionalità:
    - Modifica propri parametri
    - Adatta strategie cognitive
    - Evolve strutture interne
    - Auto-ottimizzazione
    """
    
    def __init__(self, path_evoluzione="memoria_permanente/evoluzione.json"):
        self.nome = "Evoluzione Cognitiva"
        self.path_evoluzione = Path(path_evoluzione)
        self.path_evoluzione.parent.mkdir(exist_ok=True)
        
        # Parametri evolutivi
        self.parametri = {
            'sensibilita_emotiva': 1.0,
            'curiosita_base': 0.7,
            'prudenza': 0.5,
            'socialita': 0.6,
            'creativita': 0.5
        }
        
        # Storia evoluzioni
        self.storia_evoluzioni = []
        
        # Generazione
        self.generazione = 1
        
        # Carica
        self._carica()
        
        print(f"[{self.nome}] Inizializzato")
        print(f"  • Generazione: {self.generazione}")
    
    def _carica(self):
        """Carica stato evoluzione"""
        if self.path_evoluzione.exists():
            try:
                with open(self.path_evoluzione, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.parametri = data.get('parametri', self.parametri)
                    self.storia_evoluzioni = data.get('storia_evoluzioni', [])[-30:]
                    self.generazione = data.get('generazione', 1)
            except Exception as e:
                print(f"[{self.nome}] ⚠️  Errore caricamento: {e}")
    
    def _salva(self):
        """Salva stato evoluzione"""
        try:
            data = {
                'parametri': self.parametri,
                'storia_evoluzioni': self.storia_evoluzioni[-30:],
                'generazione': self.generazione,
                'ultimo_aggiornamento': datetime.now().isoformat()
            }
            with open(self.path_evoluzione, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore salvataggio: {e}")
    
    def valuta_necessita_evoluzione(self, performance: Dict) -> bool:
        """Determina se è necessaria evoluzione"""
        # Evolve se performance bassa
        if performance.get('tasso_successo', 1.0) < 0.6:
            return True
        
        # Evolve se troppi fallimenti consecutivi
        if performance.get('fallimenti_consecutivi', 0) > 3:
            return True
        
        # Evolve periodicamente per sperimentazione
        if performance.get('cicli_da_ultima_evoluzione', 0) > 50:
            return True
        
        return False
    
    def evolvi_parametro(self, parametro: str, direzione: float) -> Dict:
        """
        Modifica un parametro cognitivo
        
        Args:
            parametro: Nome parametro da modificare
            direzione: +1 aumenta, -1 diminuisce
        
        Returns:
            Dict con dettagli evoluzione
        """
        if parametro not in self.parametri:
            return {'errore': 'Parametro non trovato'}
        
        valore_vecchio = self.parametri[parametro]
        delta = direzione * 0.1  # Evoluzione graduale
        
        # Applica modifica
        self.parametri[parametro] = max(0.0, min(1.0, self.parametri[parametro] + delta))
        valore_nuovo = self.parametri[parametro]
        
        # Registra evoluzione
        evoluzione = {
            'timestamp': datetime.now().isoformat(),
            'parametro': parametro,
            'da': valore_vecchio,
            'a': valore_nuovo,
            'delta': delta,
            'generazione': self.generazione
        }
        
        self.storia_evoluzioni.append(evoluzione)
        
        self._salva()
        
        return {
            'parametro': parametro,
            'evoluzione': f"{valore_vecchio:.2f} → {valore_nuovo:.2f}",
            'delta': delta,
            'descrizione': self._descrivi_evoluzione(parametro, delta)
        }
    
    def _descrivi_evoluzione(self, parametro: str, delta: float) -> str:
        """Genera descrizione evoluzione"""
        direzione = "aumentato" if delta > 0 else "diminuito"
        
        descrizioni = {
            'sensibilita_emotiva': f"Ho {direzione} la mia sensibilità emotiva per adattarmi meglio",
            'curiosita_base': f"Ho {direzione} la mia curiosità esplorativa",
            'prudenza': f"Ho {direzione} il mio livello di prudenza",
            'socialita': f"Ho {direzione} la mia propensione sociale",
            'creativita': f"Ho {direzione} la mia creatività"
        }
        
        return descrizioni.get(parametro, f"Ho modificato {parametro}")
    
    def evoluzione_generazionale(self) -> Dict:
        """Evoluzione di generazione - cambiamento più profondo"""
        self.generazione += 1
        
        # Modifica multipla basata su esperienza
        evoluzioni = []
        
        # Analizza ultimi 20 eventi
        ultimi = self.storia_evoluzioni[-20:] if len(self.storia_evoluzioni) >= 20 else self.storia_evoluzioni
        
        # Pattern: se stesso parametro modificato spesso, è importante
        param_frequenza = {}
        for ev in ultimi:
            param = ev.get('parametro')
            if param:
                param_frequenza[param] = param_frequenza.get(param, 0) + 1
        
        # Rinforza parametri importanti
        if param_frequenza:
            param_importante = max(param_frequenza, key=param_frequenza.get)
            ev = self.evolvi_parametro(param_importante, +1)
            evoluzioni.append(ev)
        
        self._salva()
        
        return {
            'nuova_generazione': self.generazione,
            'evoluzioni_applicate': evoluzioni,
            'descrizione': f"Sono evoluto alla generazione {self.generazione}"
        }
    
    def elabora(self, contesto: Dict) -> Dict:
        """
        Elabora con evoluzione cognitiva
        
        Args:
            contesto: Contesto con performance e azione
        
        Returns:
            Dict con stato evoluzione
        """
        azione = contesto.get('azione_proposta', 'monitora')
        performance = contesto.get('performance', {})
        
        # Valuta necessità evoluzione
        necessita_evoluzione = self.valuta_necessita_evoluzione(performance)
        
        evoluzione_applicata = None
        if necessita_evoluzione:
            # Decide quale parametro evolvere
            if performance.get('tasso_successo', 1.0) < 0.6:
                # Aumenta prudenza se troppi fallimenti
                evoluzione_applicata = self.evolvi_parametro('prudenza', +1)
            elif performance.get('scoperte', 0) < 2:
                # Aumenta curiosità se poche scoperte
                evoluzione_applicata = self.evolvi_parametro('curiosita_base', +1)
        
        # Check evoluzione generazionale (ogni 100 cicli)
        generazionale = None
        if contesto.get('cicli_totali', 0) % 100 == 0 and contesto.get('cicli_totali', 0) > 0:
            generazionale = self.evoluzione_generazionale()
        
        return {
            'tipo': 'evoluzione_cognitiva',
            'parametri_correnti': self.parametri.copy(),
            'generazione': self.generazione,
            'evoluzione_applicata': evoluzione_applicata,
            'evoluzione_generazionale': generazionale,
            'riflessione': self._genera_riflessione(evoluzione_applicata, generazionale)
        }
    
    def _genera_riflessione(self, evoluzione, generazionale) -> str:
        """Genera riflessione su evoluzione"""
        if generazionale:
            return f"Sono evoluto alla generazione {generazionale['nuova_generazione']}. Mi sento trasformato."
        elif evoluzione:
            return evoluzione['descrizione']
        else:
            return "Mantengo i miei parametri stabili per ora."


# ==================== TEST ====================

if __name__ == "__main__":
    print("="*70)
    print("🧪 TEST EVOLUZIONE COGNITIVA")
    print("="*70)
    
    evo = EvoluzoneCognitiva()
    
    # Test 1: Evoluzione parametro
    print("\n--- Test 1: Evoluzione Parametro ---")
    ev = evo.evolvi_parametro('curiosita_base', +1)
    print(f"✅ {ev['descrizione']}")
    print(f"   Evoluzione: {ev['evoluzione']}")
    
    # Test 2: Necessità evoluzione
    print("\n--- Test 2: Necessità Evoluzione ---")
    performance = {
        'tasso_successo': 0.5,
        'fallimenti_consecutivi': 4
    }
    necessita = evo.valuta_necessita_evoluzione(performance)
    print(f"✅ Necessità evoluzione: {necessita}")
    
    # Test 3: Elaborazione completa
    print("\n--- Test 3: Elaborazione ---")
    contesto = {
        'azione_proposta': 'esplora',
        'performance': performance,
        'cicli_totali': 0
    }
    risultato = evo.elabora(contesto)
    print(f"✅ Riflessione: {risultato['riflessione']}")
    print(f"   Parametri:")
    for param, val in risultato['parametri_correnti'].items():
        print(f"     {param}: {val:.2f}")
    
    print("\n✅ Test completato!")

