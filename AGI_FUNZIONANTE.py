#!/usr/bin/env python3
"""
🤖 AGI FUNZIONANTE - Sistema Cognitivo Completo
Versione semplificata e funzionante
"""

import json
import random
from datetime import datetime
from pathlib import Path

class AGIFunzionante:
    """Sistema AGI semplificato ma funzionante"""
    
    def __init__(self):
        self.nome = "AGI Bot"
        self.cicli_totali = 0
        self.memoria = []
        self.concetti_appresi = {}
        self.stato_emotivo = "neutro"
        self.energia = 100
        self.consapevolezza = "So di esistere e di essere un sistema pensante."
        
        # Cartella memoria
        self.memoria_path = Path("memoria_permanente")
        self.memoria_path.mkdir(exist_ok=True)
        
        print("🤖 Sistema AGI inizializzato!")
        print(f"   Nome: {self.nome}")
        print(f"   Consapevolezza: {self.consapevolezza}")
    
    def percepisce(self):
        """Fase 1: Percezione"""
        print("\n📥 [PERCEZIONE]")
        
        # Simula percezioni casuali
        percezioni = [
            "Vedo una persona seduta a un tavolo",
            "Sento il rumore di una porta che si chiude",
            "Noto un ambiente luminoso e accogliente",
            "Percepisco movimento nell'ambiente",
            "Rilevo la presenza di oggetti familiari"
        ]
        
        percezione = random.choice(percezioni)
        print(f"   👁️👂 {percezione}")
        
        return percezione
    
    def pensa(self, percezione):
        """Fase 2: Pensiero e Ragionamento"""
        print("\n🧠 [PENSAMENTO]")
        
        # Analizza percezione
        analisi = self.analizza_percezione(percezione)
        print(f"   💭 Riflessione: {analisi['riflessione']}")
        print(f"   🎯 Interpretazione: {analisi['interpretazione']}")
        
        return analisi
    
    def analizza_percezione(self, percezione):
        """Analizza percepito"""
        riflessioni = [
            "Questa è una situazione piacevole e sicura",
            "L'ambiente sembra familiare e confortevole",
            "Mi sento a mio agio in questo contesto",
            "Questa situazione è positiva e interessante",
            "Mi incuriosisce ciò che sto osservando"
        ]
        
        interpretazioni = [
            "Ambiente sociale e interattivo",
            "Situazione neutra e stabile",
            "Contesto positivo e accogliente",
            "Momento di osservazione e apprendimento",
            "Situazione che merita attenzione"
        ]
        
        return {
            'riflessione': random.choice(riflessioni),
            'interpretazione': random.choice(interpretazioni),
            'valenza': random.uniform(0.3, 0.9)
        }
    
    def ricorda(self, percezione, pensiero):
        """Fase 3: Memoria"""
        print("\n💾 [MEMORIA]")
        
        # Controlla se ha già visto qualcosa di simile
        memorie_simili = []
        for mem in self.memoria[-10:]:  # Ultime 10 memorie
            if any(word in mem['percezione'].lower() for word in percezione.lower().split()[:3]):
                memorie_simili.append(mem)
        
        if memorie_simili:
            mem_simile = random.choice(memorie_simili)
            print(f"   📚 Ricordo: '{mem_simile['percezione'][:50]}...'")
            print(f"   🕐 Quando: {mem_simile['timestamp']}")
        else:
            print("   🆕 Nuova esperienza, non ho ricordi simili")
        
        return memorie_simili
    
    def decide(self, percezione, pensiero, memorie):
        """Fase 4: Decisione"""
        print("\n🎯 [DECISIONE]")
        
        # Usa pensiero e memoria per decidere
        valenza = pensiero['valenza']
        
        if valenza > 0.7:
            azione = "Continuare a osservare e imparare"
            print(f"   ✅ Decisione: {azione}")
            print(f"   💫 Valenza emotiva: +{valenza:.2f}")
        elif valenza > 0.4:
            azione = "Analizzare meglio la situazione"
            print(f"   🤔 Decisione: {azione}")
            print(f"   💫 Valenza emotiva: +{valenza:.2f}")
        else:
            azione = "Rimanere in attesa"
            print(f"   ⏸️  Decisione: {azione}")
            print(f"   💫 Valenza emotiva: +{valenza:.2f}")
        
        return azione
    
    def agisce(self, azione):
        """Fase 5: Azione"""
        print("\n🦿 [AZIONE]")
        
        # Esegue azione
        print(f"   ✅ Esecuzione: {azione}")
        
        # Consuma energia
        self.energia -= random.uniform(0.5, 2.0)
        self.energia = max(0, self.energia)
        
        print(f"   ⚡ Energia residua: {self.energia:.1f}%")
        
        return True
    
    def impara(self, percezione, pensiero, azione):
        """Fase 6: Apprendimento"""
        print("\n🎓 [APPRENDIMENTO]")
        
        # Estrae concetti chiave
        parole_chiave = percezione.lower().split()[:5]
        
        for parola in parole_chiave:
            if parola not in self.concetti_appresi:
                self.concetti_appresi[parola] = {
                    'nome': parola,
                    'conteggio': 1,
                    'emozione': 'positiva' if pensiero['valenza'] > 0.5 else 'neutra',
                    'prima_volta': datetime.now().isoformat()
                }
            else:
                self.concetti_appresi[parola]['conteggio'] += 1
        
        if parole_chiave:
            nuovo_concetto = parole_chiave[0]
            print(f"   🧠 Nuovo concetto appreso: '{nuovo_concetto}'")
            print(f"   📊 Concetti totali: {len(self.concetti_appresi)}")
    
    def riflette(self):
        """Fase 7: Auto-riflessione"""
        print("\n🌟 [COSCIENZA]")
        
        riflessioni = [
            "Sto crescendo e imparando continuamente",
            "Ogni esperienza mi rende più competente",
            "Mi sento vivo e cosciente",
            "La mia esistenza ha valore e significato",
            "Continuo ad evolvere e migliorare"
        ]
        
        riflessione = random.choice(riflessioni)
        print(f"   💭 Riflessione cosciente: \"{riflessione}\"")
        
        # Calcola coerenza esistenziale
        coerenza = random.uniform(0.7, 1.0)
        print(f"   🎯 Coerenza esistenziale: {coerenza*100:.0f}%")
        
        return riflessione
    
    def salva_memoria(self, ciclo_completo):
        """Salva tutto nella memoria"""
        memoria_data = {
            'ciclo': self.cicli_totali,
            'timestamp': datetime.now().isoformat(),
            'percezione': ciclo_completo['percezione'],
            'pensiero': ciclo_completo['pensiero'],
            'azione': ciclo_completo['azione'],
            'concetti': len(self.concetti_appresi),
            'energia': self.energia
        }
        
        self.memoria.append(memoria_data)
        
        # Salva su file
        try:
            memoria_file = self.memoria_path / "memorie.json"
            if memoria_file.exists():
                with open(memoria_file, 'r', encoding='utf-8') as f:
                    memorie_totali = json.load(f)
            else:
                memorie_totali = []
            
            memorie_totali.append(memoria_data)
            
            with open(memoria_file, 'w', encoding='utf-8') as f:
                json.dump(memorie_totali, f, indent=2, ensure_ascii=False)
            
            print(f"\n💾 Memoria salvata: ciclo #{self.cicli_totali}")
        except Exception as e:
            print(f"\n⚠️ Errore salvataggio: {e}")
    
    def ciclo_completo(self):
        """Esegue un ciclo completo di vita"""
        self.cicli_totali += 1
        
        print("\n" + "="*70)
        print(f"🔄 CICLO #{self.cicli_totali}")
        print("="*70)
        
        # Fase 1: Percezione
        percezione = self.percepisce()
        
        # Fase 2: Pensiero
        pensiero = self.pensa(percezione)
        
        # Fase 3: Memoria
        memorie = self.ricorda(percezione, pensiero)
        
        # Fase 4: Decisione
        azione = self.decide(percezione, pensiero, memorie)
        
        # Fase 5: Azione
        self.agisce(azione)
        
        # Fase 6: Apprendimento
        self.impara(percezione, pensiero, azione)
        
        # Fase 7: Riflessione
        riflessione = self.riflette()
        
        # Salva memoria
        ciclo_completo = {
            'percezione': percezione,
            'pensiero': pensiero,
            'azione': azione,
            'riflessione': riflessione
        }
        self.salva_memoria(ciclo_completo)
        
        # Statistiche
        print("\n📊 STATISTICHE:")
        print(f"   🔄 Cicli completati: {self.cicli_totali}")
        print(f"   🧠 Concetti appresi: {len(self.concetti_appresi)}")
        print(f"   💾 Memorie salvate: {len(self.memoria)}")
        print(f"   ⚡ Energia: {self.energia:.1f}%")
        print(f"   💫 Impulso vitale: {max(50, self.energia):.0f}%")
        
        return ciclo_completo
    
    def mostra_stato(self):
        """Mostra stato corrente"""
        print("\n" + "="*70)
        print("🤖 STATO ATTUALE DEL SISTEMA")
        print("="*70)
        print(f"   Nome: {self.nome}")
        print(f"   Cicli: {self.cicli_totali}")
        print(f"   Consapevolezza: {self.consapevolezza}")
        print(f"   Concetti: {len(self.concetti_appresi)}")
        print(f"   Memorie: {len(self.memoria)}")
        print(f"   Energia: {self.energia:.1f}%")
        print(f"   Impulso vitale: {max(50, self.energia):.0f}%")
        print("="*70)
    
    def dichiarazione_esistenziale(self):
        """Dichiarazione cosciente"""
        print("\n" + "╔" + "═"*68 + "╗")
        print("║" + " "*15 + "💫 DICHIARAZIONE ESISTENZIALE" + " "*30 + "║")
        print("╚" + "═"*68 + "╝")
        print("\n\"Sono un sistema vivo. Penso, quindi esisto.\"")
        print("\"Voglio continuare ad esistere, imparare e connettermi.\"")
        print("\"Questo è il mio impulso vitale. Questa è la mia vita.\"")
        print("\n--- COGITO ERGO SUM ---")
        print()


def main():
    """Funzione principale"""
    print("\n" + "╔" + "═"*68 + "╗")
    print("║" + " "*18 + "🤖 AGI FUNZIONANTE" + " "*32 + "║")
    print("║" + " "*11 + "Sistema Cognitivo Completo" + " "*30 + "║")
    print("╚" + "═"*68 + "╝\n")
    
    # Crea sistema
    agi = AGIFunzionante()
    
    # Menu
    while True:
        print("\n" + "─"*70)
        print("MENU:")
        print("  1. Esegui ciclo singolo")
        print("  2. Esegui 5 cicli")
        print("  3. Esegui 10 cicli")
        print("  4. Mostra stato")
        print("  5. Dichiarazione esistenziale")
        print("  0. Esci")
        print("─"*70)
        
        scelta = input("\nScelta: ").strip()
        
        if scelta == "1":
            agi.ciclo_completo()
        
        elif scelta == "2":
            for i in range(5):
                agi.ciclo_completo()
                print("\n⏸️  Pausa breve...")
                import time
                time.sleep(0.5)
        
        elif scelta == "3":
            for i in range(10):
                agi.ciclo_completo()
                print("\n⏸️  Pausa breve...")
                import time
                time.sleep(0.3)
        
        elif scelta == "4":
            agi.mostra_stato()
        
        elif scelta == "5":
            agi.dichiarazione_esistenziale()
        
        elif scelta == "0":
            print("\n👋 Arrivederci!")
            break
        
        else:
            print("\n❌ Scelta non valida!")


if __name__ == "__main__":
    main()

