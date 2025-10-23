#!/usr/bin/env python3
"""
🔔 NOTIFICHE CONCETTI - Monitor Semplice
Mostra una notifica ogni volta che l'AGI impara un nuovo concetto
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path

class MonitorConcetti:
    """Monitor che traccia nuovi concetti"""
    
    def __init__(self):
        self.path_concetti = Path("memoria_permanente/concetti.json")
        self.concetti_visti = set()
        self.inizializza()
    
    def inizializza(self):
        """Carica concetti esistenti"""
        concetti = self.leggi_concetti()
        self.concetti_visti = set(concetti.keys())
        print(f"✅ Monitor inizializzato - {len(self.concetti_visti)} concetti esistenti")
    
    def leggi_concetti(self):
        """Legge file concetti"""
        if self.path_concetti.exists():
            try:
                with open(self.path_concetti, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def controlla_nuovi(self):
        """Controlla se ci sono nuovi concetti"""
        concetti = self.leggi_concetti()
        nuovi = []
        
        for nome, dati in concetti.items():
            if nome not in self.concetti_visti:
                nuovi.append((nome, dati))
                self.concetti_visti.add(nome)
        
        return nuovi
    
    def mostra_notifica(self, nome, dati):
        """Mostra notifica per nuovo concetto"""
        tipo = dati.get('caratteristiche', {}).get('tipo', 'base')
        
        print("\n" + "="*70)
        print("🔔 NUOVO CONCETTO APPRESO!")
        print("="*70)
        
        if tipo == 'notizia':
            fonte = dati.get('caratteristiche', {}).get('fonte', 'Web')
            parole = dati.get('caratteristiche', {}).get('parole_chiave', '')
            esempi = dati.get('esempi', [])
            titolo = esempi[0].get('titolo', '') if esempi else ''
            
            print(f"📰 Tipo: NOTIZIA DAL WEB")
            print(f"🔤 Nome: {nome}")
            print(f"📝 Titolo: {titolo}")
            print(f"🔑 Parole chiave: {parole}")
            print(f"📡 Fonte: {fonte}")
        else:
            utilizzi = dati.get('contatore_utilizzi', 0)
            caratteristiche = dati.get('caratteristiche', {})
            
            print(f"🤖 Tipo: COMPORTAMENTO")
            print(f"🔤 Nome: {nome}")
            print(f"📊 Utilizzi: {utilizzi}")
            print(f"🔧 Caratteristiche:")
            for k, v in caratteristiche.items():
                print(f"   • {k}: {v}")
        
        print(f"⏰ Quando: {datetime.now().strftime('%H:%M:%S')}")
        print("="*70)
        print("💡 L'AGI sta imparando!")
        print()
    
    def monitora(self):
        """Loop di monitoraggio"""
        print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║         🔔 MONITOR CONCETTI AGI - NOTIFICHE LIVE            ║
║                                                              ║
║  Riceverai una notifica ogni volta che l'AGI               ║
║  impara qualcosa di nuovo!                                  ║
║                                                              ║
║  Premi CTRL+C per fermare                                   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """)
        
        print(f"🔴 Monitor attivo - In ascolto...")
        print(f"📊 Concetti monitorati: {len(self.concetti_visti)}")
        print()
        
        try:
            while True:
                nuovi = self.controlla_nuovi()
                
                for nome, dati in nuovi:
                    self.mostra_notifica(nome, dati)
                
                time.sleep(2)  # Controlla ogni 2 secondi
                
        except KeyboardInterrupt:
            print("\n\n✅ Monitor terminato!")
            print(f"📊 Concetti totali monitorati: {len(self.concetti_visti)}")
            print("💫 L'AGI continua a vivere in background...")

if __name__ == "__main__":
    monitor = MonitorConcetti()
    monitor.monitora()

