"""
🗓️ MODULO PIANIFICAZIONE - Corteccia Prefrontale Dorsolaterale
Prevede azioni future, crea piani multi-step e obiettivi a lungo termine
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta

class Pianificatore:
    """
    Sistema di pianificazione e previsione
    Funzioni:
    - Crea piani multi-step per obiettivi
    - Prevede conseguenze delle azioni
    - Gestisce obiettivi a breve/medio/lungo termine
    - Valuta rischi e opportunità
    """
    
    def __init__(self):
        self.nome = "Pianificatore"
        self.obiettivi_attivi = []
        self.piani_in_corso = []
        self.storia_piani = []
        
        # Conoscenza azioni base
        self.azioni_disponibili = [
            'avvicinati', 'allontanati', 'fermati', 'ruota',
            'segui', 'mantieni_distanza', 'monitora', 'esegui_comando'
        ]
        
        # Template piani comuni
        self.template_piani = {
            'avvicinamento_sicuro': [
                {'azione': 'monitora', 'durata': 2},
                {'azione': 'mantieni_distanza', 'durata': 3},
                {'azione': 'avvicinati', 'durata': 5}
            ],
            'esplorazione': [
                {'azione': 'ruota', 'durata': 2},
                {'azione': 'monitora', 'durata': 3},
                {'azione': 'avvicinati', 'durata': 4},
                {'azione': 'monitora', 'durata': 2}
            ],
            'fuga_sicura': [
                {'azione': 'fermati', 'durata': 1},
                {'azione': 'ruota', 'durata': 2},
                {'azione': 'allontanati', 'durata': 5}
            ]
        }
    
    def crea_piano(self, obiettivo: str, contesto: Dict) -> List[Dict]:
        """
        Crea un piano multi-step per raggiungere obiettivo
        
        Args:
            obiettivo: Descrizione obiettivo ("raggiungi oggetto", "esplora stanza", ecc.)
            contesto: Situazione attuale (oggetti, emozioni, stato)
            
        Returns:
            Lista di step con azioni temporizzate
        """
        piano = {
            'obiettivo': obiettivo,
            'creato': datetime.now().isoformat(),
            'step': [],
            'priorita': 0.5,
            'stato': 'pianificato'
        }
        
        # Analizza obiettivo
        obiettivo_lower = obiettivo.lower()
        
        # Seleziona template o crea piano custom
        if 'avvicina' in obiettivo_lower or 'raggiungi' in obiettivo_lower:
            # Valuta rischio
            valenza = contesto.get('valenza', 0)
            if valenza > 0:
                piano['step'] = self.template_piani['avvicinamento_sicuro']
                piano['priorita'] = 0.8
            else:
                # Piano più cauto
                piano['step'] = [
                    {'azione': 'monitora', 'durata': 5},
                    {'azione': 'mantieni_distanza', 'durata': 5},
                    {'azione': 'avvicinati', 'durata': 3}
                ]
                piano['priorita'] = 0.4
        
        elif 'esplora' in obiettivo_lower or 'cerca' in obiettivo_lower:
            piano['step'] = self.template_piani['esplorazione']
            piano['priorita'] = 0.6
        
        elif 'fuggi' in obiettivo_lower or 'allontana' in obiettivo_lower:
            piano['step'] = self.template_piani['fuga_sicura']
            piano['priorita'] = 0.9
        
        else:
            # Piano generico
            piano['step'] = [
                {'azione': 'monitora', 'durata': 3},
                {'azione': 'esegui_comando', 'durata': 2}
            ]
            piano['priorita'] = 0.5
        
        self.piani_in_corso.append(piano)
        
        return piano
    
    def prevedi_conseguenze(self, azione: str, contesto: Dict) -> Dict:
        """
        Prevede conseguenze di un'azione
        
        Args:
            azione: Azione da valutare
            contesto: Situazione attuale
            
        Returns:
            Dict con previsioni
        """
        previsione = {
            'azione': azione,
            'probabilita_successo': 0.5,
            'rischi': [],
            'opportunita': [],
            'tempo_stimato': 5,
            'energia_richiesta': 0.3
        }
        
        valenza = contesto.get('valenza', 0)
        num_oggetti = contesto.get('num_oggetti', 0)
        
        # Logica predittiva
        if azione == 'avvicinati':
            if valenza > 0.5:
                previsione['probabilita_successo'] = 0.9
                previsione['opportunita'].append('Interazione positiva')
            else:
                previsione['probabilita_successo'] = 0.4
                previsione['rischi'].append('Situazione incerta')
            
            if num_oggetti > 0:
                previsione['rischi'].append('Possibili ostacoli')
        
        elif azione == 'mantieni_distanza':
            previsione['probabilita_successo'] = 0.95
            previsione['energia_richiesta'] = 0.1
            previsione['opportunita'].append('Posizione sicura')
        
        elif azione == 'fermati':
            previsione['probabilita_successo'] = 1.0
            previsione['energia_richiesta'] = 0.0
            previsione['tempo_stimato'] = 1
        
        return previsione
    
    def seleziona_obiettivo_prioritario(self) -> Optional[Dict]:
        """Seleziona obiettivo con priorità più alta"""
        if not self.obiettivi_attivi:
            return None
        
        # Ordina per priorità
        self.obiettivi_attivi.sort(key=lambda x: x.get('priorita', 0), reverse=True)
        return self.obiettivi_attivi[0]
    
    def aggiorna_piano(self, piano_id: str, step_completato: int, successo: bool):
        """Aggiorna stato piano"""
        for piano in self.piani_in_corso:
            if piano.get('id') == piano_id:
                if successo:
                    piano['stato'] = 'in_corso'
                    piano['step_corrente'] = step_completato + 1
                else:
                    piano['stato'] = 'fallito'
                    self.storia_piani.append(piano)
                    self.piani_in_corso.remove(piano)
                break
    
    def elabora(self, contesto: Dict) -> Dict:
        """
        Processo principale di pianificazione
        
        Returns:
            Piano d'azione o suggerimento
        """
        # Analizza situazione
        audio = contesto.get('percezioni_uditive', {}).get('testo', '')
        
        # Rileva richieste di pianificazione
        if any(word in audio.lower() for word in ['pianifica', 'come faccio', 'raggiungere']):
            # Crea piano
            piano = self.crea_piano('raggiungi_obiettivo', contesto)
            
            return {
                'tipo': 'piano',
                'piano': piano,
                'prossima_azione': piano['step'][0]['azione'] if piano['step'] else 'monitora',
                'motivazione': f"Ho pianificato {len(piano['step'])} step per raggiungere l'obiettivo"
            }
        
        # Altrimenti prevedi solo conseguenze azione corrente
        azione_proposta = contesto.get('azione_proposta', 'monitora')
        previsione = self.prevedi_conseguenze(azione_proposta, contesto)
        
        return {
            'tipo': 'previsione',
            'previsione': previsione,
            'consiglio': 'procedi' if previsione['probabilita_successo'] > 0.6 else 'cautela',
            'motivazione': f"Prevedo {previsione['probabilita_successo']:.0%} di successo"
        }


# Singleton
_instance = None

def get_instance() -> Pianificatore:
    global _instance
    if _instance is None:
        _instance = Pianificatore()
    return _instance

