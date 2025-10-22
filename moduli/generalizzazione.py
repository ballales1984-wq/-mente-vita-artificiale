#!/usr/bin/env python3
"""
🧩 MODULO GENERALIZZAZIONE - Fase 4 AGI
Astrae concetti e riutilizza conoscenze in contesti nuovi
"""

import json
from typing import Dict, List, Any, Optional
from pathlib import Path
from collections import defaultdict
from datetime import datetime


class Concetto:
    """Rappresenta un concetto astratto"""
    
    def __init__(self, nome: str, caratteristiche: Dict, esempi: List[Dict]):
        self.nome = nome
        self.caratteristiche = caratteristiche  # Es: {'tipo': 'persona', 'interazione': 'amichevole'}
        self.esempi = esempi  # Episodi concreti
        self.contatore_utilizzi = 0
        self.successi = 0
        self.fallimenti = 0
        self.data_creazione = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        return {
            'nome': self.nome,
            'caratteristiche': self.caratteristiche,
            'esempi': self.esempi,
            'contatore_utilizzi': self.contatore_utilizzi,
            'successi': self.successi,
            'fallimenti': self.fallimenti,
            'data_creazione': self.data_creazione
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Concetto':
        concetto = Concetto(
            nome=data['nome'],
            caratteristiche=data['caratteristiche'],
            esempi=data['esempi']
        )
        concetto.contatore_utilizzi = data.get('contatore_utilizzi', 0)
        concetto.successi = data.get('successi', 0)
        concetto.fallimenti = data.get('fallimenti', 0)
        concetto.data_creazione = data.get('data_creazione', datetime.now().isoformat())
        return concetto


class ModuloGeneralizzazione:
    """
    Sistema di astrazione e generalizzazione concettuale
    
    Funzionalità:
    - Estrae pattern comuni da esperienze diverse
    - Crea categorie mentali astratte
    - Trasferisce conoscenza tra contesti
    - Valuta applicabilità concetti
    """
    
    def __init__(self, path_concetti="memoria_permanente/concetti.json"):
        self.nome = "Generalizzazione"
        self.path_concetti = Path(path_concetti)
        self.path_concetti.parent.mkdir(exist_ok=True)
        
        # Dizionario concetti: nome -> Concetto
        self.concetti: Dict[str, Concetto] = {}
        
        # Carica concetti esistenti
        self._carica_concetti()
        
        print(f"[{self.nome}] Inizializzato")
        print(f"  • Concetti caricati: {len(self.concetti)}")
    
    def _carica_concetti(self):
        """Carica concetti da file"""
        if self.path_concetti.exists():
            try:
                with open(self.path_concetti, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for nome, concetto_dict in data.items():
                        self.concetti[nome] = Concetto.from_dict(concetto_dict)
            except Exception as e:
                print(f"[{self.nome}] ⚠️  Errore caricamento: {e}")
    
    def _salva_concetti(self):
        """Salva concetti su file"""
        try:
            data = {nome: c.to_dict() for nome, c in self.concetti.items()}
            with open(self.path_concetti, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore salvataggio: {e}")
            return False
    
    def estrai_caratteristiche(self, episodio: Dict) -> Dict:
        """
        Estrae caratteristiche astratte da un episodio concreto
        
        Args:
            episodio: Episodio con descrizione, audio, emozione, azione, successo
        
        Returns:
            Dict di caratteristiche astratte
        """
        caratteristiche = {}
        
        # Tipo di oggetto/entità principale
        desc = episodio.get('descrizione', '').lower()
        if any(w in desc for w in ['person', 'persona', 'uomo', 'donna']):
            caratteristiche['entita_principale'] = 'persona'
        elif any(w in desc for w in ['animal', 'animale', 'cane', 'gatto']):
            caratteristiche['entita_principale'] = 'animale'
        elif any(w in desc for w in ['car', 'veicolo', 'auto']):
            caratteristiche['entita_principale'] = 'veicolo'
        elif any(w in desc for w in ['object', 'oggetto', 'cosa']):
            caratteristiche['entita_principale'] = 'oggetto'
        else:
            caratteristiche['entita_principale'] = 'ambiente'
        
        # Tipo di interazione
        audio = episodio.get('audio', '').lower()
        if any(w in audio for w in ['ciao', 'salve', 'buongiorno']):
            caratteristiche['interazione'] = 'saluto'
        elif any(w in audio for w in ['vieni', 'avvicinati']):
            caratteristiche['interazione'] = 'richiesta_avvicinamento'
        elif any(w in audio for w in ['fermati', 'stop']):
            caratteristiche['interazione'] = 'richiesta_arresto'
        elif any(w in audio for w in ['aiuto', 'help']):
            caratteristiche['interazione'] = 'richiesta_aiuto'
        elif audio:
            caratteristiche['interazione'] = 'comunicazione_generica'
        else:
            caratteristiche['interazione'] = 'nessuna'
        
        # Valenza emotiva
        emozione = episodio.get('emozione', 'neutro').lower()
        valenza = episodio.get('valenza', 0)
        if emozione == 'positivo' or valenza > 0.3:
            caratteristiche['valenza'] = 'positivo'
        elif emozione == 'negativo' or valenza < -0.3:
            caratteristiche['valenza'] = 'negativo'
        else:
            caratteristiche['valenza'] = 'neutro'
        
        # Tipo di azione
        azione = episodio.get('azione', '').lower()
        if 'avvicina' in azione:
            caratteristiche['risposta'] = 'avvicinamento'
        elif 'allontana' in azione or 'distanza' in azione:
            caratteristiche['risposta'] = 'mantenimento_distanza'
        elif 'ferma' in azione or 'stop' in azione:
            caratteristiche['risposta'] = 'arresto'
        elif 'monitor' in azione:
            caratteristiche['risposta'] = 'osservazione'
        elif 'esegui' in azione:
            caratteristiche['risposta'] = 'esecuzione_comando'
        else:
            caratteristiche['risposta'] = 'altra'
        
        # Contesto ambientale
        if 'indoor' in desc or 'stanza' in desc:
            caratteristiche['ambiente'] = 'interno'
        elif 'outdoor' in desc or 'esterno' in desc:
            caratteristiche['ambiente'] = 'esterno'
        else:
            caratteristiche['ambiente'] = 'indeterminato'
        
        return caratteristiche
    
    def trova_concetti_simili(self, caratteristiche: Dict, soglia_similarita=0.6) -> List[str]:
        """
        Trova concetti esistenti simili alle caratteristiche date
        
        Args:
            caratteristiche: Caratteristiche da cercare
            soglia_similarita: Soglia minima (0-1)
        
        Returns:
            Lista nomi concetti simili
        """
        simili = []
        
        for nome, concetto in self.concetti.items():
            # Calcola similarità (Jaccard)
            char_concetto = set(concetto.caratteristiche.items())
            char_nuove = set(caratteristiche.items())
            
            if len(char_concetto.union(char_nuove)) == 0:
                continue
            
            similarita = len(char_concetto.intersection(char_nuove)) / len(char_concetto.union(char_nuove))
            
            if similarita >= soglia_similarita:
                simili.append(nome)
        
        return simili
    
    def crea_concetto(self, nome: str, caratteristiche: Dict, episodio: Dict) -> Concetto:
        """
        Crea un nuovo concetto astratto
        
        Args:
            nome: Nome del concetto
            caratteristiche: Caratteristiche astratte
            episodio: Primo esempio concreto
        
        Returns:
            Concetto creato
        """
        concetto = Concetto(
            nome=nome,
            caratteristiche=caratteristiche,
            esempi=[episodio]
        )
        
        self.concetti[nome] = concetto
        self._salva_concetti()
        
        print(f"[{self.nome}] ✨ Nuovo concetto creato: '{nome}'")
        print(f"            Caratteristiche: {caratteristiche}")
        
        return concetto
    
    def aggiungi_esempio_a_concetto(self, nome_concetto: str, episodio: Dict):
        """Aggiunge esempio a un concetto esistente"""
        if nome_concetto in self.concetti:
            self.concetti[nome_concetto].esempi.append(episodio)
            
            # Limita numero esempi (max 20)
            if len(self.concetti[nome_concetto].esempi) > 20:
                self.concetti[nome_concetto].esempi = self.concetti[nome_concetto].esempi[-20:]
            
            self._salva_concetti()
    
    def elabora(self, episodio: Dict) -> Dict:
        """
        Elabora episodio e aggiorna concetti
        
        Args:
            episodio: Episodio cognitivo
        
        Returns:
            Dict con risultato elaborazione
        """
        # 1. Estrai caratteristiche astratte
        caratteristiche = self.estrai_caratteristiche(episodio)
        
        # 2. Trova concetti simili
        simili = self.trova_concetti_simili(caratteristiche, soglia_similarita=0.6)
        
        if simili:
            # Concetto esistente trovato
            nome_concetto = simili[0]  # Prendi il primo
            self.aggiungi_esempio_a_concetto(nome_concetto, episodio)
            
            return {
                'tipo': 'riconoscimento',
                'concetto': nome_concetto,
                'caratteristiche': caratteristiche,
                'simili': simili,
                'nuovo': False
            }
        else:
            # Crea nuovo concetto
            nome_nuovo = self._genera_nome_concetto(caratteristiche)
            self.crea_concetto(nome_nuovo, caratteristiche, episodio)
            
            return {
                'tipo': 'astrazione',
                'concetto': nome_nuovo,
                'caratteristiche': caratteristiche,
                'simili': [],
                'nuovo': True
            }
    
    def _genera_nome_concetto(self, caratteristiche: Dict) -> str:
        """Genera nome descrittivo per concetto"""
        parti = []
        
        if 'entita_principale' in caratteristiche:
            parti.append(caratteristiche['entita_principale'])
        
        if 'interazione' in caratteristiche:
            parti.append(caratteristiche['interazione'])
        
        if 'valenza' in caratteristiche:
            parti.append(caratteristiche['valenza'])
        
        nome_base = '_'.join(parti) if parti else 'concetto_generico'
        
        # Se esiste già, aggiungi numero
        if nome_base in self.concetti:
            i = 2
            while f"{nome_base}_{i}" in self.concetti:
                i += 1
            nome_base = f"{nome_base}_{i}"
        
        return nome_base
    
    def trasferisci_conoscenza(self, situazione_nuova: Dict) -> Optional[Dict]:
        """
        Trasferisce conoscenza da concetti esistenti a situazione nuova
        
        Args:
            situazione_nuova: Nuova situazione da valutare
        
        Returns:
            Suggerimento basato su conoscenza trasferita (o None)
        """
        caratteristiche_nuove = self.estrai_caratteristiche(situazione_nuova)
        
        # Trova il concetto più simile
        migliore_match = None
        migliore_score = 0
        
        for nome, concetto in self.concetti.items():
            char_concetto = set(concetto.caratteristiche.items())
            char_nuove = set(caratteristiche_nuove.items())
            
            if len(char_concetto.union(char_nuove)) == 0:
                continue
            
            score = len(char_concetto.intersection(char_nuove)) / len(char_concetto.union(char_nuove))
            
            if score > migliore_score:
                migliore_score = score
                migliore_match = (nome, concetto)
        
        if migliore_match and migliore_score >= 0.4:
            nome, concetto = migliore_match
            
            # Trova l'azione più comune negli esempi
            azioni = [ep.get('azione') for ep in concetto.esempi if ep.get('azione')]
            if azioni:
                azione_suggerita = max(set(azioni), key=azioni.count)
                
                # Calcola tasso successo del concetto
                tasso_successo = concetto.successi / max(1, concetto.contatore_utilizzi)
                
                return {
                    'concetto_applicato': nome,
                    'azione_suggerita': azione_suggerita,
                    'confidenza': migliore_score,
                    'tasso_successo': tasso_successo,
                    'num_esempi': len(concetto.esempi),
                    'motivazione': f"Situazione simile a '{nome}' (match: {migliore_score:.0%})"
                }
        
        return None
    
    def aggiorna_successo(self, nome_concetto: str, successo: bool):
        """Aggiorna statistiche successo di un concetto"""
        if nome_concetto in self.concetti:
            self.concetti[nome_concetto].contatore_utilizzi += 1
            if successo:
                self.concetti[nome_concetto].successi += 1
            else:
                self.concetti[nome_concetto].fallimenti += 1
            self._salva_concetti()
    
    def get_statistiche(self) -> Dict:
        """Ritorna statistiche sistema"""
        return {
            'totale_concetti': len(self.concetti),
            'concetti_piu_usati': sorted(
                [(nome, c.contatore_utilizzi) for nome, c in self.concetti.items()],
                key=lambda x: x[1],
                reverse=True
            )[:5],
            'concetti_migliori': sorted(
                [(nome, c.successi / max(1, c.contatore_utilizzi)) for nome, c in self.concetti.items()],
                key=lambda x: x[1],
                reverse=True
            )[:5]
        }


# ==================== TEST ====================

if __name__ == "__main__":
    print("="*70)
    print("🧪 TEST MODULO GENERALIZZAZIONE")
    print("="*70)
    
    gen = ModuloGeneralizzazione()
    
    # Test 1: Crea concetto da episodio
    print("\n--- Test 1: Astrazione Concetto ---")
    episodio1 = {
        'descrizione': 'Person rilevata in ambiente indoor',
        'audio': 'Ciao, come va?',
        'emozione': 'positivo',
        'valenza': 0.8,
        'azione': 'avvicinati',
        'successo': True
    }
    
    risultato = gen.elabora(episodio1)
    print(f"✅ Risultato: {risultato['tipo']}")
    print(f"   Concetto: {risultato['concetto']}")
    print(f"   Caratteristiche: {risultato['caratteristiche']}")
    
    # Test 2: Episodio simile
    print("\n--- Test 2: Riconoscimento Concetto ---")
    episodio2 = {
        'descrizione': 'Persona vista indoor',
        'audio': 'Buongiorno!',
        'emozione': 'positivo',
        'valenza': 0.7,
        'azione': 'avvicinati',
        'successo': True
    }
    
    risultato2 = gen.elabora(episodio2)
    print(f"✅ Risultato: {risultato2['tipo']}")
    print(f"   Concetto: {risultato2['concetto']}")
    print(f"   Simili: {risultato2['simili']}")
    
    # Test 3: Trasferimento conoscenza
    print("\n--- Test 3: Trasferimento Conoscenza ---")
    situazione_nuova = {
        'descrizione': 'Person detected',
        'audio': 'Salve!',
        'emozione': 'neutro',
        'valenza': 0.5
    }
    
    suggerimento = gen.trasferisci_conoscenza(situazione_nuova)
    if suggerimento:
        print(f"✅ Conoscenza trasferita!")
        print(f"   Da concetto: {suggerimento['concetto_applicato']}")
        print(f"   Azione suggerita: {suggerimento['azione_suggerita']}")
        print(f"   Confidenza: {suggerimento['confidenza']:.0%}")
        print(f"   Motivazione: {suggerimento['motivazione']}")
    
    # Statistiche
    print("\n--- Statistiche Finali ---")
    stats = gen.get_statistiche()
    print(f"📊 Concetti totali: {stats['totale_concetti']}")
    
    print("\n✅ Test completato!")

