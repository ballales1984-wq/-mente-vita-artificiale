"""
🎯 MODULO ATTENZIONE SELETTIVA - Sistema Reticolare Attivazione
Filtra stimoli rilevanti, ignora irrilevanti, focus dinamico
"""

from typing import Dict, List, Any, Tuple
import numpy as np

class AttenzionSelettiva:
    """
    Sistema di attenzione e focus
    Funzioni:
    - Filtra stimoli per rilevanza
    - Focus su elementi importanti
    - Ignora distrazioni
    - Shift attentivo dinamico
    """
    
    def __init__(self):
        self.nome = "Attenzione Selettiva"
        self.focus_corrente = None
        self.soglia_attenzione = 0.6
        self.storia_focus = []
        
        # Pesi rilevanza per tipo stimolo
        self.pesi_rilevanza = {
            'person': 0.9,
            'car': 0.7,
            'bottle': 0.3,
            'laptop': 0.5,
            'phone': 0.6,
            'comando_vocale': 1.0,
            'rumore': 0.1,
            'movimento': 0.8
        }
    
    def calcola_rilevanza(self, stimolo: Dict) -> float:
        """
        Calcola quanto uno stimolo è rilevante
        
        Args:
            stimolo: Oggetto o evento percepito
            
        Returns:
            Score 0.0-1.0
        """
        score = 0.5  # Base
        
        # Tipo oggetto
        tipo = stimolo.get('classe', stimolo.get('tipo', 'unknown'))
        score_tipo = self.pesi_rilevanza.get(tipo, 0.3)
        
        # Confidenza
        confidenza = stimolo.get('confidenza', 0.5)
        
        # Novità (primo oggetto di quel tipo oggi)
        novita = 0.2 if stimolo.get('prima_volta', False) else 0.0
        
        # Prossimità (se oggetto visivo)
        prossimita = 0.0
        if 'bbox' in stimolo:
            # Oggetti grandi/vicini sono più rilevanti
            area = stimolo.get('area_relativa', 0.1)
            prossimita = min(0.3, area)
        
        # Emotività (se audio)
        emotivita = 0.0
        if 'emozione' in stimolo:
            intensita_emo = abs(stimolo.get('valenza_emotiva', 0))
            emotivita = min(0.3, intensita_emo)
        
        # Score finale
        score = (score_tipo * 0.4 + 
                confidenza * 0.2 + 
                novita + 
                prossimita + 
                emotivita)
        
        return min(1.0, max(0.0, score))
    
    def filtra_stimoli(self, stimoli: List[Dict]) -> List[Dict]:
        """
        Filtra stimoli per rilevanza
        
        Args:
            stimoli: Lista tutti gli stimoli percepiti
            
        Returns:
            Lista stimoli rilevanti (sopra soglia)
        """
        stimoli_rilevanti = []
        
        for stimolo in stimoli:
            rilevanza = self.calcola_rilevanza(stimolo)
            stimolo['rilevanza'] = rilevanza
            
            if rilevanza >= self.soglia_attenzione:
                stimoli_rilevanti.append(stimolo)
        
        # Ordina per rilevanza
        stimoli_rilevanti.sort(key=lambda x: x['rilevanza'], reverse=True)
        
        return stimoli_rilevanti
    
    def shift_focus(self, nuovi_stimoli: List[Dict]):
        """
        Cambia focus verso stimolo più rilevante
        
        Args:
            nuovi_stimoli: Nuovi stimoli da valutare
        """
        if not nuovi_stimoli:
            self.focus_corrente = None
            return
        
        # Trova stimolo più rilevante
        stimoli_filtrati = self.filtra_stimoli(nuovi_stimoli)
        
        if stimoli_filtrati:
            nuovo_focus = stimoli_filtrati[0]
            
            # Verifica se focus è cambiato
            if self.focus_corrente != nuovo_focus.get('tipo'):
                self.focus_corrente = nuovo_focus.get('tipo', nuovo_focus.get('classe'))
                self.storia_focus.append({
                    'timestamp': datetime.now().isoformat(),
                    'focus': self.focus_corrente,
                    'rilevanza': nuovo_focus['rilevanza']
                })
    
    def elabora(self, percezioni: Dict) -> Dict:
        """
        Processo principale attenzione
        
        Args:
            percezioni: Dict con percezioni visive e uditive
            
        Returns:
            Risultati filtro attentivo
        """
        tutti_stimoli = []
        
        # Estrai oggetti visivi
        oggetti_visivi = percezioni.get('percezioni_visive', {}).get('oggetti', [])
        tutti_stimoli.extend(oggetti_visivi)
        
        # Estrai stimoli uditivi
        audio = percezioni.get('percezioni_uditive', {})
        if audio.get('testo'):
            tutti_stimoli.append({
                'tipo': 'comando_vocale',
                'contenuto': audio['testo'],
                'confidenza': 0.9,
                'emozione': audio.get('tono', 'neutro')
            })
        
        # Filtra
        stimoli_rilevanti = self.filtra_stimoli(tutti_stimoli)
        
        # Shift focus
        self.shift_focus(stimoli_rilevanti)
        
        # Risultati
        risultato = {
            'focus_corrente': self.focus_corrente,
            'stimoli_rilevanti': stimoli_rilevanti,
            'stimoli_ignorati': len(tutti_stimoli) - len(stimoli_rilevanti),
            'attenzione_su': stimoli_rilevanti[0] if stimoli_rilevanti else None,
            'motivazione': ''
        }
        
        # Genera motivazione
        if stimoli_rilevanti:
            top = stimoli_rilevanti[0]
            risultato['motivazione'] = f"Focalizzo su {top.get('tipo', top.get('classe'))} (rilevanza: {top['rilevanza']:.0%})"
        else:
            risultato['motivazione'] = "Nessuno stimolo rilevante, mantengo vigilanza generale"
        
        return risultato
    
    def get_focus_storia(self, ultimi_n: int = 10) -> List[Dict]:
        """Restituisce storia focus"""
        return self.storia_focus[-ultimi_n:]


# Singleton
_instance = None

def get_instance() -> AttenzionSelettiva:
    global _instance
    if _instance is None:
        _instance = AttenzionSelettiva()
    return _instance

