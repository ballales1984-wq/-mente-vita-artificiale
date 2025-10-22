"""
💬 MODULO LINGUAGGIO NATURALE - Area di Broca e Wernicke
Dialogo fluido, memoria contestuale, generazione risposte
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
from collections import deque

class SistemaLinguaggio:
    """
    Sistema di linguaggio naturale
    Funzioni:
    - Genera risposte fluide
    - Mantiene contesto conversazione
    - Ricorda topic discussi
    - Adatta registro linguistico
    """
    
    def __init__(self):
        self.nome = "Sistema Linguaggio"
        self.contesto_conversazione = deque(maxlen=10)  # Ultime 10 interazioni
        self.topic_corrente = None
        self.registro = 'formale'  # formale, informale, tecnico
        
        # Template risposte base
        self.template_risposte = {
            'saluto': [
                "Ciao! Come posso aiutarti?",
                "Salve, sono qui per te.",
                "Buongiorno! Cosa posso fare?"
            ],
            'conferma': [
                "Perfetto, ho capito.",
                "D'accordo, procedo.",
                "Ricevuto, eseguo."
            ],
            'incomprensione': [
                "Non ho capito bene, puoi ripetere?",
                "Scusa, potresti riformulare?",
                "Non sono sicuro di aver compreso."
            ],
            'completamento': [
                "Fatto! Ho completato l'azione.",
                "Operazione eseguita con successo.",
                "Ho finito, tutto a posto."
            ],
            'problema': [
                "C'è stato un problema, mi dispiace.",
                "Non sono riuscito a completare.",
                "Difficoltà rilevata, provo altro approccio."
            ]
        }
    
    def genera_risposta(self, input_text: str, contesto: Dict) -> str:
        """
        Genera risposta fluida e contestuale
        
        Args:
            input_text: Testo input utente
            contesto: Situazione e stato emotivo
            
        Returns:
            Risposta generata
        """
        import random
        
        input_lower = input_text.lower() if input_text else ''
        
        # Riconosci tipo interazione
        if any(sal in input_lower for sal in ['ciao', 'salve', 'buongiorno']):
            risposta = random.choice(self.template_risposte['saluto'])
        
        elif any(conf in input_lower for conf in ['ok', 'perfetto', 'bene', 'si']):
            risposta = random.choice(self.template_risposte['conferma'])
        
        elif any(cmd in input_lower for cmd in ['vieni', 'vai', 'prendi', 'fai']):
            azione = contesto.get('azione', 'azione')
            risposta = f"Ricevuto. Procedo con {azione}."
        
        elif any(dom in input_lower for dom in ['cosa', 'dove', 'perché', 'quando']):
            risposta = "È una buona domanda. Sto analizzando la situazione."
        
        else:
            # Risposta generica basata su emozione
            valenza = contesto.get('valenza', 0)
            if valenza > 0.5:
                risposta = "Capisco. La situazione sembra positiva, procedo con fiducia."
            elif valenza < 0:
                risposta = "Capisco. Procedo con cautela."
            else:
                risposta = "Capisco. Continuo l'osservazione."
        
        # Aggiungi a contesto
        self.contesto_conversazione.append({
            'timestamp': datetime.now().isoformat(),
            'input': input_text,
            'risposta': risposta
        })
        
        return risposta
    
    def mantieni_contesto(self, nuovo_input: str) -> Dict:
        """
        Mantiene contesto della conversazione
        
        Args:
            nuovo_input: Nuovo input ricevuto
            
        Returns:
            Contesto aggiornato
        """
        # Rileva riferimenti anaforic (questo, quello, quello lì, ecc.)
        if any(rif in nuovo_input.lower() for rif in ['questo', 'quello', 'lo', 'la', 'ne']):
            # Cerca riferimento in contesto precedente
            if self.contesto_conversazione:
                ultimo = self.contesto_conversazione[-1]
                return {
                    'riferimento_anaforico': True,
                    'riferisce_a': ultimo.get('topic', 'unknown')
                }
        
        return {'riferimento_anaforico': False}
    
    def adatta_registro(self, modello_persona: Dict) -> str:
        """
        Adatta registro linguistico in base a persona
        
        Args:
            modello_persona: Modello mentale persona (da teoria_mente)
            
        Returns:
            Registro consigliato
        """
        emozione = modello_persona.get('emozione_inferita', 'neutro')
        
        if emozione == 'confuso':
            return 'semplice'  # Linguaggio chiaro e diretto
        elif emozione == 'irritato':
            return 'conciso'  # Breve e al punto
        elif emozione == 'interessato':
            return 'dettagliato'  # Più informazioni
        else:
            return 'formale'  # Standard
    
    def elabora(self, input_audio: str, contesto: Dict) -> Dict:
        """
        Processo principale linguaggio
        
        Args:
            input_audio: Testo audio input
            contesto: Contesto generale
            
        Returns:
            Risposta e analisi linguistica
        """
        # Genera risposta
        risposta = self.genera_risposta(input_audio, contesto)
        
        # Mantieni contesto
        ctx = self.mantieni_contesto(input_audio)
        
        risultato = {
            'risposta': risposta,
            'contesto_conversazione': list(self.contesto_conversazione),
            'topic_corrente': self.topic_corrente,
            'registro_usato': self.registro,
            'riferimento_anaforico': ctx.get('riferimento_anaforico', False),
            'motivazione': f"Generata risposta contestuale: '{risposta[:50]}...'"
        }
        
        return risultato


# Singleton
_instance = None

def get_instance() -> SistemaLinguaggio:
    global _instance
    if _instance is None:
        _instance = SistemaLinguaggio()
    return _instance

