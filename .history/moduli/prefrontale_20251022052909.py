"""
🧠 MODULO PREFRONTALE - Corteccia Prefrontale
==============================================
Ragionamento di alto livello, decision making e pianificazione.
Equivalente: Corteccia prefrontale dorsolaterale e orbitofrontale

Funzioni principali:
- Ragionamento astratto usando LLM
- Decision making basato su contesto
- Pianificazione sequenze di azioni
- Working memory temporanea
"""

from typing import Dict, Any, List, Optional
from .base import ModuloCerebrale, ProcessoreCognitivo, TipoModulo, RisultatoElaborazione
from .base import gestisci_eccezione_hardware, richiede_inizializzazione, log_elaborazione

# Import condizionali
try:
    from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
    import torch
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False


class CortecciaPrefrontale(ModuloCerebrale, ProcessoreCognitivo):
    """
    Modulo di ragionamento e decision making
    
    Usa LLM (GPT-2, GPT-J, LLaMA) per:
    - Analizzare percezioni multimodali
    - Generare decisioni contestuali
    - Pianificare azioni complesse
    - Mantenere working memory
    """
    
    def __init__(self, model_name: str = "gpt2", use_gpu: bool = False):
        """
        Inizializza corteccia prefrontale
        
        Args:
            model_name: Nome modello HuggingFace (gpt2, gpt-j-6b, ecc.)
            use_gpu: Se usare GPU per inferenza
        """
        super().__init__("Corteccia Prefrontale", TipoModulo.COGNITIVO)
        
        self.model_name = model_name
        self.use_gpu = use_gpu and TRANSFORMERS_AVAILABLE
        self.device = "cuda" if self.use_gpu and torch.cuda.is_available() else "cpu"
        
        self.generator = None
        self.tokenizer = None
        self.working_memory = []  # Memoria di lavoro (ultimi N eventi)
        self.max_working_memory = 5
        
    def inizializza(self) -> bool:
        """
        Carica modello LLM
        
        Returns:
            bool: True se caricamento riuscito
        """
        print(f"[{self.nome}] Inizializzazione modello {self.model_name}...")
        
        if not TRANSFORMERS_AVAILABLE:
            print(f"[{self.nome}] ⚠️ Transformers non disponibile, modalità rule-based")
            self.modalita_reale = False
            self.attivo = True
            return True
        
        try:
            # Carica pipeline per text generation
            print(f"[{self.nome}] Caricamento su device: {self.device}")
            
            self.generator = pipeline(
                'text-generation',
                model=self.model_name,
                device=0 if self.device == "cuda" else -1,
                max_length=200
            )
            
            self.modalita_reale = True
            self.attivo = True
            
            print(f"[{self.nome}] ✅ Modello caricato")
            return True
            
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore caricamento: {e}")
            print(f"[{self.nome}] Fallback a modalità rule-based")
            self.modalita_reale = False
            self.attivo = True
            return True
    
    @richiede_inizializzazione
    @log_elaborazione
    @gestisci_eccezione_hardware
    def elabora(self, input_data: Dict[str, Any]) -> RisultatoElaborazione:
        """
        Elabora input multimodali e genera decisione
        
        Args:
            input_data: Dict con chiavi:
                - percezioni_visive: Output da modulo visione
                - percezioni_uditive: Output da modulo udito
                - stato_emotivo: Output da modulo emozione
                - memoria_contestuale: Info da ippocampo
                
        Returns:
            RisultatoElaborazione con decisione e piano d'azione
        """
        # Estrai informazioni
        visione = input_data.get('percezioni_visive', {})
        udito = input_data.get('percezioni_uditive', {})
        emozione = input_data.get('stato_emotivo', 'neutro')
        memoria = input_data.get('memoria_contestuale', [])
        
        # Costruisci contesto
        contesto = self._costruisci_contesto(visione, udito, emozione, memoria)
        
        # Aggiungi a working memory
        self._aggiorna_working_memory(contesto)
        
        # Ragionamento
        if self.modalita_reale:
            decisione = self._ragionamento_llm(contesto)
        else:
            decisione = self._ragionamento_rule_based(contesto)
        
        return RisultatoElaborazione(
            tipo="reale" if self.modalita_reale else "simulato",
            successo=True,
            dati=decisione,
            metadata={
                'contesto': contesto,
                'working_memory_size': len(self.working_memory)
            }
        )
    
    def ragiona(self, contesto: Dict[str, Any]) -> Dict[str, Any]:
        """
        Implementa ProcessoreCognitivo.ragiona()
        
        Args:
            contesto: Informazioni contestuali
            
        Returns:
            Decisione strutturata
        """
        return self.elabora(contesto).dati
    
    def pianifica(self, obiettivo: str, vincoli: Dict = None) -> List[Dict]:
        """
        Pianifica sequenza di azioni per raggiungere obiettivo
        
        Args:
            obiettivo: Descrizione obiettivo
            vincoli: Vincoli (energia, tempo, sicurezza, ecc.)
            
        Returns:
            Lista di azioni pianificate
        """
        print(f"[{self.nome}] Pianificazione per obiettivo: {obiettivo}")
        
        # Pianificazione base
        piano = []
        
        if "avvicinati" in obiettivo.lower():
            piano = [
                {'azione': 'ruota', 'parametri': {'angolo': 0}},
                {'azione': 'avvicinati', 'parametri': {'velocita': 0.5, 'distanza': 2.0}},
                {'azione': 'fermati', 'parametri': {}}
            ]
        elif "esplora" in obiettivo.lower():
            piano = [
                {'azione': 'avvicinati', 'parametri': {'distanza': 3.0}},
                {'azione': 'ruota', 'parametri': {'angolo': 90}},
                {'azione': 'avvicinati', 'parametri': {'distanza': 3.0}},
                {'azione': 'ruota', 'parametri': {'angolo': 90}}
            ]
        else:
            piano = [{'azione': 'monitora_ambiente', 'parametri': {}}]
        
        return piano
    
    def _costruisci_contesto(self, visione: Dict, udito: Dict, 
                            emozione: str, memoria: List) -> str:
        """
        Costruisce stringa di contesto per LLM
        
        Args:
            visione: Dati dalla corteccia visiva
            udito: Dati dalla corteccia uditiva
            emozione: Stato emotivo corrente
            memoria: Informazioni dalla memoria
            
        Returns:
            str: Contesto formattato
        """
        parti_contesto = []
        
        # Informazioni visive
        if visione:
            desc_visiva = visione.get('descrizione', 'Nessuna informazione visiva')
            parti_contesto.append(f"Visione: {desc_visiva}")
            
            focus = visione.get('attenzione', {})
            if focus.get('focus'):
                parti_contesto.append(f"Focus su: {focus['focus']}")
        
        # Informazioni uditive
        if udito:
            testo = udito.get('testo', '')
            if testo:
                parti_contesto.append(f"Audio: '{testo}'")
                parti_contesto.append(f"Tono: {udito.get('tono', 'neutro')}")
                parti_contesto.append(f"Intenzione: {udito.get('intenzione', 'incerta')}")
        
        # Stato emotivo
        parti_contesto.append(f"Stato emotivo: {emozione}")
        
        # Memoria contestuale
        if memoria:
            parti_contesto.append(f"Memoria recente: {len(memoria)} eventi")
        
        return " | ".join(parti_contesto)
    
    def _ragionamento_llm(self, contesto: str) -> Dict[str, Any]:
        """
        Ragionamento usando LLM reale
        
        Args:
            contesto: Contesto testuale
            
        Returns:
            Decisione generata
        """
        try:
            # Prompt engineering
            prompt = f"""Situazione: {contesto}
Domanda: Quale azione dovrebbe intraprendere il robot?
Risposta breve:"""
            
            # Genera risposta
            output = self.generator(
                prompt,
                max_length=150,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True
            )
            
            risposta_llm = output[0]['generated_text']
            risposta_llm = risposta_llm.replace(prompt, "").strip()
            
            # Interpreta risposta in decisione strutturata
            decisione = self._interpreta_risposta_llm(risposta_llm, contesto)
            
            return decisione
            
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore LLM: {e}")
            return self._ragionamento_rule_based(contesto)
    
    def _ragionamento_rule_based(self, contesto: str) -> Dict[str, Any]:
        """
        Ragionamento basato su regole (fallback)
        
        Args:
            contesto: Contesto testuale
            
        Returns:
            Decisione basata su regole
        """
        contesto_lower = contesto.lower()
        
        # Regole di decisione
        azione = "monitora_ambiente"
        priorita = 0.3
        ragionamento = "Situazione normale, continuo monitoraggio"
        
        # Pericolo rilevato
        if any(word in contesto_lower for word in ['pericolo', 'car', 'veicolo']):
            azione = "evita_ostacolo"
            priorita = 0.9
            ragionamento = "Pericolo rilevato, manovra evasiva necessaria"
        
        # Comando vocale ricevuto
        elif "comando" in contesto_lower or "vieni" in contesto_lower:
            azione = "esegui_comando"
            priorita = 0.8
            ragionamento = "Comando vocale ricevuto, esecuzione richiesta"
        
        # Persona rilevata
        elif "person" in contesto_lower or "persona" in contesto_lower:
            azione = "mantieni_distanza"
            priorita = 0.6
            ragionamento = "Presenza umana, mantengo distanza di sicurezza"
        
        # Stato emotivo negativo
        elif "negativo" in contesto_lower or "paura" in contesto_lower:
            azione = "allontanati"
            priorita = 0.7
            ragionamento = "Stato emotivo negativo, allontanamento preventivo"
        
        return {
            'azione': azione,
            'priorita': priorita,
            'ragionamento': ragionamento,
            'parametri': self._genera_parametri(azione),
            'contesto_usato': contesto
        }
    
    def _interpreta_risposta_llm(self, risposta: str, contesto: str) -> Dict[str, Any]:
        """
        Interpreta risposta LLM in decisione strutturata
        
        Args:
            risposta: Testo generato da LLM
            contesto: Contesto originale
            
        Returns:
            Decisione strutturata
        """
        risposta_lower = risposta.lower()
        
        # Mappa parole chiave -> azioni
        azioni_map = {
            'avvicin': 'avvicinati',
            'allontan': 'allontanati',
            'evita': 'evita_ostacolo',
            'ruota': 'ruota',
            'ferm': 'fermati',
            'segui': 'segui'
        }
        
        azione = "monitora_ambiente"
        for keyword, azione_mapped in azioni_map.items():
            if keyword in risposta_lower:
                azione = azione_mapped
                break
        
        return {
            'azione': azione,
            'priorita': 0.7,
            'ragionamento': risposta[:200],  # Limita lunghezza
            'parametri': self._genera_parametri(azione),
            'fonte': 'llm'
        }
    
    def _genera_parametri(self, azione: str) -> Dict[str, Any]:
        """
        Genera parametri appropriati per un'azione
        
        Args:
            azione: Nome azione
            
        Returns:
            Parametri per l'azione
        """
        parametri_default = {
            'avvicinati': {'velocita': 0.5, 'distanza': 2.0, 'modalita': 'cautela'},
            'allontanati': {'velocita': 0.8, 'distanza': 3.0},
            'evita_ostacolo': {'direzione': 'destra', 'angolo': 45},
            'ruota': {'angolo': 90, 'velocita_angolare': 30},
            'fermati': {},
            'segui': {'target': 'person', 'distanza_sicurezza': 1.5},
            'mantieni_distanza': {'distanza': 1.0},
            'monitora_ambiente': {}
        }
        
        return parametri_default.get(azione, {})
    
    def _aggiorna_working_memory(self, evento: str):
        """
        Aggiorna memoria di lavoro (FIFO)
        
        Args:
            evento: Nuovo evento da memorizzare
        """
        self.working_memory.append(evento)
        
        # Mantieni solo ultimi N eventi
        if len(self.working_memory) > self.max_working_memory:
            self.working_memory = self.working_memory[-self.max_working_memory:]
    
    def get_working_memory(self) -> List[str]:
        """
        Ottieni contenuto working memory
        
        Returns:
            Lista eventi recenti
        """
        return self.working_memory.copy()
    
    def chiudi(self):
        """
        Rilascia risorse
        """
        print(f"[{self.nome}] Chiusura...")
        
        # Libera modello da memoria
        if self.generator:
            del self.generator
            self.generator = None
        
        if TRANSFORMERS_AVAILABLE and torch.cuda.is_available():
            torch.cuda.empty_cache()
        
        self.attivo = False
        print(f"[{self.nome}] ✅ Chiuso")


# Istanza globale
_corteccia_prefrontale = None

def get_instance() -> CortecciaPrefrontale:
    """Ottieni istanza singleton"""
    global _corteccia_prefrontale
    if _corteccia_prefrontale is None:
        _corteccia_prefrontale = CortecciaPrefrontale()
        _corteccia_prefrontale.inizializza()
    return _corteccia_prefrontale


# API semplificata
def ragiona(percezioni_visive: Dict = None, percezioni_uditive: Dict = None,
            stato_emotivo: str = "neutro", memoria: List = None) -> Dict[str, Any]:
    """
    Ragionamento di alto livello
    
    Args:
        percezioni_visive: Output modulo visione
        percezioni_uditive: Output modulo udito
        stato_emotivo: Stato emotivo corrente
        memoria: Memoria contestuale
        
    Returns:
        Decisione strutturata
    """
    corteccia = get_instance()
    
    input_data = {
        'percezioni_visive': percezioni_visive or {},
        'percezioni_uditive': percezioni_uditive or {},
        'stato_emotivo': stato_emotivo,
        'memoria_contestuale': memoria or []
    }
    
    risultato = corteccia.elabora(input_data)
    return risultato.dati


# Test del modulo
if __name__ == "__main__":
    print("="*60)
    print("🧪 Test Modulo Prefrontale")
    print("="*60)
    
    # Crea istanza
    corteccia = CortecciaPrefrontale()
    corteccia.inizializza()
    
    # Test con input simulati
    input_test = {
        'percezioni_visive': {
            'descrizione': 'Rilevati: 1 person, 1 chair',
            'attenzione': {'focus': 'person', 'rilevanza': 0.85}
        },
        'percezioni_uditive': {
            'testo': 'Vieni qui per favore',
            'tono': 'amichevole',
            'intenzione': 'comando'
        },
        'stato_emotivo': 'positivo',
        'memoria_contestuale': ['evento_1', 'evento_2']
    }
    
    print("\n--- Test Elaborazione ---")
    risultato = corteccia.elabora(input_test)
    
    print(f"\nRisultato:")
    print(f"  Tipo: {risultato.tipo}")
    print(f"  Azione: {risultato.dati['azione']}")
    print(f"  Priorità: {risultato.dati['priorita']}")
    print(f"  Ragionamento: {risultato.dati['ragionamento']}")
    
    print("\n--- Test Pianificazione ---")
    piano = corteccia.pianifica("avvicinati al target")
    print(f"\nPiano d'azione ({len(piano)} step):")
    for i, step in enumerate(piano, 1):
        print(f"  {i}. {step['azione']} - {step['parametri']}")
    
    corteccia.chiudi()
    print("\n✅ Test completato")

