#!/usr/bin/env python3
"""
💾 MEMORIA PERMANENTE - Storage persistente su disco
Gestisce fino a 2GB di memorie a lungo termine
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import shutil

class MemoriaPermanente:
    """
    Sistema di memoria permanente su disco
    Caratteristiche:
    - Storage persistente (non eliminato)
    - Limite 2GB
    - Compressione automatica
    - Indicizzazione per ricerca veloce
    """
    
    def __init__(self, max_size_gb=2):
        self.nome = "Memoria Permanente"
        self.max_size_bytes = max_size_gb * 1024 * 1024 * 1024  # 2GB in bytes
        
        # Directory storage
        self.storage_dir = Path("memoria_permanente")
        self.storage_dir.mkdir(exist_ok=True)
        
        # File principali
        self.memorie_file = self.storage_dir / "memorie.json"
        self.indice_file = self.storage_dir / "indice.json"
        self.stats_file = self.storage_dir / "stats.json"
        
        # Carica dati esistenti
        self.memorie = self._carica_memorie()
        self.indice = self._carica_indice()
        self.stats = self._carica_stats()
        
        print(f"[{self.nome}] Inizializzato")
        print(f"  • Limite: {max_size_gb}GB")
        print(f"  • Memorie caricate: {len(self.memorie)}")
        print(f"  • Spazio usato: {self.get_size_mb():.2f}MB")
    
    def _carica_memorie(self) -> List[Dict]:
        """Carica memorie dal disco"""
        if self.memorie_file.exists():
            try:
                with open(self.memorie_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def _carica_indice(self) -> Dict:
        """Carica indice di ricerca"""
        if self.indice_file.exists():
            try:
                with open(self.indice_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _carica_stats(self) -> Dict:
        """Carica statistiche"""
        if self.stats_file.exists():
            try:
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return self._stats_default()
        return self._stats_default()
    
    def _stats_default(self) -> Dict:
        """Statistiche di default"""
        return {
            'totale_memorie': 0,
            'data_creazione': datetime.now().isoformat(),
            'ultimo_salvataggio': None,
            'memorie_aggiunte': 0,
            'memorie_eliminate': 0,
            'ricerche_effettuate': 0
        }
    
    def _salva_tutto(self):
        """Salva tutto su disco"""
        try:
            # Salva memorie
            with open(self.memorie_file, 'w', encoding='utf-8') as f:
                json.dump(self.memorie, f, indent=2, ensure_ascii=False)
            
            # Salva indice
            with open(self.indice_file, 'w', encoding='utf-8') as f:
                json.dump(self.indice, f, indent=2)
            
            # Aggiorna e salva stats
            self.stats['totale_memorie'] = len(self.memorie)
            self.stats['ultimo_salvataggio'] = datetime.now().isoformat()
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(self.stats, f, indent=2)
            
            return True
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore salvataggio: {e}")
            return False
    
    def aggiungi_memoria(self, memoria: Dict) -> bool:
        """
        Aggiunge una memoria permanente
        
        Args:
            memoria: Dict con dati memoria
            
        Returns:
            bool: True se aggiunta con successo
        """
        # Verifica spazio disponibile
        if self.get_size_bytes() >= self.max_size_bytes:
            print(f"[{self.nome}] ⚠️  Limite 2GB raggiunto, comprimo vecchie memorie...")
            self._comprimi_vecchie()
        
        # Aggiungi timestamp
        if 'timestamp' not in memoria:
            memoria['timestamp'] = datetime.now().isoformat()
        
        # Aggiungi ID univoco
        memoria['id'] = f"mem_{len(self.memorie)}_{int(datetime.now().timestamp())}"
        
        # Aggiungi alla lista
        self.memorie.append(memoria)
        
        # Aggiorna indice (per ricerca veloce)
        self._aggiorna_indice(memoria)
        
        # Salva
        if self._salva_tutto():
            self.stats['memorie_aggiunte'] += 1
            print(f"[{self.nome}] ✅ Memoria salvata: {memoria['id']}")
            return True
        
        return False
    
    def _aggiorna_indice(self, memoria: Dict):
        """Aggiorna indice per ricerca veloce"""
        mem_id = memoria['id']
        
        # Indice per descrizione
        if 'descrizione' in memoria:
            desc = memoria['descrizione'].lower()
            parole = desc.split()
            for parola in parole:
                if parola not in self.indice:
                    self.indice[parola] = []
                if mem_id not in self.indice[parola]:
                    self.indice[parola].append(mem_id)
        
        # Indice per emozione
        if 'emozione' in memoria:
            emo = memoria['emozione'].lower()
            if emo not in self.indice:
                self.indice[emo] = []
            self.indice[emo].append(mem_id)
    
    def cerca_memorie(self, query: str, limite: int = 10) -> List[Dict]:
        """
        Cerca memorie per query
        
        Args:
            query: Testo di ricerca
            limite: Numero massimo risultati
            
        Returns:
            Lista di memorie trovate
        """
        self.stats['ricerche_effettuate'] += 1
        
        query_lower = query.lower()
        parole = query_lower.split()
        
        # Trova ID memorie rilevanti dall'indice
        id_trovati = set()
        for parola in parole:
            if parola in self.indice:
                id_trovati.update(self.indice[parola])
        
        # Recupera memorie complete
        risultati = []
        for memoria in self.memorie:
            if memoria['id'] in id_trovati:
                risultati.append(memoria)
                if len(risultati) >= limite:
                    break
        
        print(f"[{self.nome}] 🔍 Trovate {len(risultati)} memorie per '{query}'")
        return risultati
    
    def get_ultime_memorie(self, n: int = 10) -> List[Dict]:
        """Restituisce ultime N memorie"""
        return self.memorie[-n:] if len(self.memorie) > n else self.memorie
    
    def get_size_bytes(self) -> int:
        """Calcola dimensione totale in bytes"""
        total = 0
        if self.storage_dir.exists():
            for file in self.storage_dir.glob('*'):
                if file.is_file():
                    total += file.stat().st_size
        return total
    
    def get_size_mb(self) -> float:
        """Calcola dimensione totale in MB"""
        return self.get_size_bytes() / (1024 * 1024)
    
    def get_size_gb(self) -> float:
        """Calcola dimensione totale in GB"""
        return self.get_size_bytes() / (1024 * 1024 * 1024)
    
    def _comprimi_vecchie(self):
        """Comprimi o elimina vecchie memorie per fare spazio"""
        if len(self.memorie) < 100:
            return
        
        print(f"[{self.nome}] 🗜️  Compressione memorie vecchie...")
        
        # Ordina per timestamp (più vecchie prima)
        self.memorie.sort(key=lambda m: m.get('timestamp', ''))
        
        # Rimuovi 20% più vecchie
        to_remove = len(self.memorie) // 5
        self.memorie = self.memorie[to_remove:]
        
        # Ricostruisci indice
        self.indice = {}
        for memoria in self.memorie:
            self._aggiorna_indice(memoria)
        
        self.stats['memorie_eliminate'] += to_remove
        self._salva_tutto()
        
        print(f"[{self.nome}] ✅ Eliminate {to_remove} memorie vecchie")
    
    def get_statistiche(self) -> Dict:
        """Restituisce statistiche dettagliate"""
        return {
            'totale_memorie': len(self.memorie),
            'spazio_usato_mb': self.get_size_mb(),
            'spazio_usato_gb': self.get_size_gb(),
            'spazio_rimanente_gb': (self.max_size_bytes - self.get_size_bytes()) / (1024 * 1024 * 1024),
            'percentuale_usata': (self.get_size_bytes() / self.max_size_bytes) * 100,
            **self.stats
        }
    
    def pulisci_tutto(self):
        """ATTENZIONE: Elimina TUTTE le memorie permanenti"""
        try:
            shutil.rmtree(self.storage_dir)
            self.storage_dir.mkdir(exist_ok=True)
            self.memorie = []
            self.indice = {}
            self.stats = self._stats_default()
            self._salva_tutto()
            print(f"[{self.nome}] 🗑️  Tutte le memorie eliminate")
            return True
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore pulizia: {e}")
            return False
    
    def esporta_backup(self, percorso: str = "backup_memoria.json"):
        """Esporta backup completo"""
        try:
            backup = {
                'memorie': self.memorie,
                'indice': self.indice,
                'stats': self.stats,
                'data_backup': datetime.now().isoformat()
            }
            with open(percorso, 'w', encoding='utf-8') as f:
                json.dump(backup, f, indent=2, ensure_ascii=False)
            print(f"[{self.nome}] 💾 Backup salvato: {percorso}")
            return True
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore backup: {e}")
            return False
    
    def importa_backup(self, percorso: str):
        """Importa backup"""
        try:
            with open(percorso, 'r', encoding='utf-8') as f:
                backup = json.load(f)
            
            self.memorie = backup['memorie']
            self.indice = backup['indice']
            self.stats = backup['stats']
            self._salva_tutto()
            
            print(f"[{self.nome}] ✅ Backup importato: {len(self.memorie)} memorie")
            return True
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore import: {e}")
            return False


# Test modulo
if __name__ == "__main__":
    print("="*70)
    print("🧪 TEST MEMORIA PERMANENTE")
    print("="*70)
    
    # Crea istanza
    mem = MemoriaPermanente(max_size_gb=2)
    
    # Test 1: Aggiungi memoria
    print("\n[TEST 1] Aggiunta memoria")
    memoria_test = {
        'descrizione': 'Test memoria permanente',
        'emozione': 'positivo',
        'valenza': 0.8,
        'contenuto': 'Questo è un test del sistema di memoria permanente'
    }
    mem.aggiungi_memoria(memoria_test)
    
    # Test 2: Cerca
    print("\n[TEST 2] Ricerca")
    risultati = mem.cerca_memorie("test")
    print(f"Trovate: {len(risultati)} memorie")
    
    # Test 3: Statistiche
    print("\n[TEST 3] Statistiche")
    stats = mem.get_statistiche()
    for k, v in stats.items():
        if isinstance(v, float):
            print(f"  • {k}: {v:.2f}")
        else:
            print(f"  • {k}: {v}")
    
    print("\n✅ Test completato")

