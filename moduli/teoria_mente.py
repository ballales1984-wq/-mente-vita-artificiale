"""
🤝 MODULO TEORIA DELLA MENTE - Cognizione Sociale
Capisce intenzioni, emozioni e stati mentali degli altri
"""

from typing import Dict, List, Any, Optional
from datetime import datetime

class TeoriaDellaMente:
    """
    Sistema di cognizione sociale
    Funzioni:
    - Riconosce emozioni altrui
    - Inferisce intenzioni
    - Modella stati mentali
    - Adatta comunicazione
    """
    
    def __init__(self):
        self.nome = "Teoria della Mente"
        self.modelli_persone = {}  # ID persona -> modello mentale
        self.interazioni_passate = []
        
        # Indicatori emotivi nel linguaggio
        self.indicatori_emozioni = {
            'felice': ['grazie', 'perfetto', 'ottimo', 'bene', 'fantastico'],
            'confuso': ['non capisco', 'cosa', 'perché', 'come', 'aiuto'],
            'irritato': ['no', 'basta', 'stop', 'mai', 'sbagliato'],
            'interessato': ['dimmi', 'raccontami', 'continua', 'poi'],
            'stanco': ['dopo', 'pausa', 'troppo', 'basta così']
        }
        
        # Indicatori di intenzione
        self.indicatori_intenzione = {
            'richiesta_azione': ['vieni', 'vai', 'prendi', 'porta', 'fermati'],
            'richiesta_info': ['cos\'è', 'dove', 'quando', 'perché', 'chi'],
            'socializzazione': ['ciao', 'come stai', 'ci sei', 'parliamo'],
            'comando_urgente': ['subito', 'ora', 'veloce', 'urgente']
        }
    
    def inferisci_emozione(self, audio: Dict, contesto: Dict) -> str:
        """
        Inferisce emozione della persona da audio
        
        Args:
            audio: Trascrizione e analisi audio
            contesto: Situazione generale
            
        Returns:
            Emozione inferita
        """
        testo = audio.get('testo', '').lower()
        tono = audio.get('tono', 'neutro')
        
        # Analisi parole chiave
        for emozione, keywords in self.indicatori_emozioni.items():
            if any(kw in testo for kw in keywords):
                return emozione
        
        # Fallback su tono
        if tono in ['amichevole', 'positivo']:
            return 'felice'
        elif tono in ['urgente', 'alto']:
            return 'irritato'
        else:
            return 'neutro'
    
    def inferisci_intenzione(self, audio: Dict) -> str:
        """
        Inferisce cosa vuole la persona
        
        Args:
            audio: Trascrizione audio
            
        Returns:
            Intenzione inferita
        """
        testo = audio.get('testo', '').lower()
        
        for intenzione, keywords in self.indicatori_intenzione.items():
            if any(kw in testo for kw in keywords):
                return intenzione
        
        return 'incerto'
    
    def modella_stato_mentale(self, persona_id: str, percezioni: Dict) -> Dict:
        """
        Costruisce modello dello stato mentale di una persona
        
        Args:
            persona_id: Identificatore persona
            percezioni: Dati percettivi
            
        Returns:
            Modello mentale
        """
        audio = percezioni.get('percezioni_uditive', {})
        
        emozione = self.inferisci_emozione(audio, percezioni)
        intenzione = self.inferisci_intenzione(audio)
        
        modello = {
            'persona_id': persona_id,
            'timestamp': datetime.now().isoformat(),
            'emozione_inferita': emozione,
            'intenzione_inferita': intenzione,
            'livello_certezza': 0.7,  # TODO: calcolare dalla confidenza
            'bisogni_possibili': self._inferisci_bisogni(emozione, intenzione)
        }
        
        # Salva modello
        self.modelli_persone[persona_id] = modello
        
        return modello
    
    def _inferisci_bisogni(self, emozione: str, intenzione: str) -> List[str]:
        """Inferisce possibili bisogni della persona"""
        bisogni = []
        
        if emozione == 'confuso':
            bisogni.append('spiegazione_chiara')
            bisogni.append('semplificazione')
        
        if emozione == 'irritato':
            bisogni.append('calma')
            bisogni.append('soluzione_rapida')
        
        if emozione == 'stanco':
            bisogni.append('pausa')
            bisogni.append('conclusione')
        
        if intenzione == 'richiesta_info':
            bisogni.append('informazione')
        
        if intenzione == 'comando_urgente':
            bisogni.append('azione_immediata')
        
        return bisogni
    
    def adatta_comunicazione(self, modello_mentale: Dict) -> Dict:
        """
        Adatta stile comunicazione in base a stato mentale altrui
        
        Args:
            modello_mentale: Modello stato mentale persona
            
        Returns:
            Suggerimenti comunicativi
        """
        emozione = modello_mentale['emozione_inferita']
        bisogni = modello_mentale['bisogni_possibili']
        
        adattamento = {
            'tono_consigliato': 'neutro',
            'velocita': 'normale',
            'dettaglio': 'medio',
            'suggerimenti': []
        }
        
        # Adatta in base a emozione
        if emozione == 'confuso':
            adattamento['tono_consigliato'] = 'paziente'
            adattamento['velocita'] = 'lenta'
            adattamento['dettaglio'] = 'alto'
            adattamento['suggerimenti'].append('Spiega passo per passo')
            adattamento['suggerimenti'].append('Usa esempi semplici')
        
        elif emozione == 'irritato':
            adattamento['tono_consigliato'] = 'calmo'
            adattamento['velocita'] = 'veloce'
            adattamento['dettaglio'] = 'essenziale'
            adattamento['suggerimenti'].append('Vai al sodo')
            adattamento['suggerimenti'].append('Risolvi rapidamente')
        
        elif emozione == 'felice':
            adattamento['tono_consigliato'] = 'cordiale'
            adattamento['suggerimenti'].append('Mantieni tono positivo')
        
        elif emozione == 'stanco':
            adattamento['velocita'] = 'veloce'
            adattamento['dettaglio'] = 'basso'
            adattamento['suggerimenti'].append('Concludi rapidamente')
        
        return adattamento
    
    def elabora(self, percezioni: Dict) -> Dict:
        """
        Processo principale teoria della mente
        
        Args:
            percezioni: Percezioni visive e uditive
            
        Returns:
            Analisi sociale e suggerimenti
        """
        # Rileva persone
        oggetti = percezioni.get('percezioni_visive', {}).get('oggetti', [])
        persone = [o for o in oggetti if o.get('classe') == 'person']
        
        risultato = {
            'persone_rilevate': len(persone),
            'modelli_mentali': [],
            'adattamenti': [],
            'motivazione': ''
        }
        
        if persone:
            # Per ogni persona, crea modello mentale
            for i, persona in enumerate(persone):
                persona_id = f"person_{i}"
                modello = self.modella_stato_mentale(persona_id, percezioni)
                adattamento = self.adatta_comunicazione(modello)
                
                risultato['modelli_mentali'].append(modello)
                risultato['adattamenti'].append(adattamento)
            
            # Motivazione
            emozione_principale = risultato['modelli_mentali'][0]['emozione_inferita']
            risultato['motivazione'] = f"Persona rilevata, sembra {emozione_principale}. Adatto comunicazione."
        
        else:
            risultato['motivazione'] = "Nessuna persona rilevata, nessun adattamento sociale necessario."
        
        return risultato


# Singleton
_instance = None

def get_instance() -> TeoriaDellaMente:
    global _instance
    if _instance is None:
        _instance = TeoriaDellaMente()
    return _instance

