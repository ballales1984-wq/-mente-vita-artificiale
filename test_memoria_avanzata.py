"""
🧪 TEST MEMORIA AVANZATA
========================
Test delle nuove funzionalità:
- Consolidamento automatico intelligente
- Richiamo contestuale con suggerimenti
"""

import time
from moduli.memoria import Ippocampo

def test_consolidamento():
    """Test consolidamento memorie"""
    print("="*70)
    print("🧪 TEST CONSOLIDAMENTO INTELLIGENTE")
    print("="*70)
    
    # Crea ippocampo
    ippocampo = Ippocampo("test_consolidamento.json")
    ippocampo.inizializza()
    
    print("\n📝 Creazione memorie di test...")
    
    # Memoria 1: BUONA (alta valenza, alta importanza) → DA CONSERVARE
    ippocampo.memorizza(
        "mem_buona",
        "Azione evita_ostacolo eseguita con successo",
        metadata={
            'valenza': 0.9,  # Alta valenza
            'importanza': 1.5,  # Alta importanza
            'contesto': {'azione': 'evita_ostacolo', 'successo': True}
        }
    )
    
    # Memoria 2: CATTIVA (bassa valenza, bassa importanza) → DA ELIMINARE
    ippocampo.memorizza(
        "mem_cattiva",
        "Azione monitora fallita senza conseguenze",
        metadata={
            'valenza': 0.2,  # Bassa valenza
            'importanza': 0.3,  # Bassa importanza
            'contesto': {'azione': 'monitora', 'successo': False}
        }
    )
    
    # Memoria 3: MEDIA (valenza ok, importanza bassa) → DA ELIMINARE
    ippocampo.memorizza(
        "mem_media",
        "Movimento semplice completato",
        metadata={
            'valenza': 0.4,
            'importanza': 0.5,
            'contesto': {'azione': 'movimento', 'successo': True}
        }
    )
    
    # Memoria 4: IMPORTANTE (alta importanza) → DA CONSERVARE
    ippocampo.memorizza(
        "mem_importante",
        "Primo contatto con umano registrato",
        metadata={
            'valenza': 0.6,
            'importanza': 2.0,  # Molto importante
            'contesto': {'azione': 'interazione', 'tipo': 'primo_contatto'}
        }
    )
    
    print(f"✓ Create 4 memorie di test")
    print(f"  • Memorie totali: {len(ippocampo.memoria_episodica)}")
    
    # Modifica timestamp per simulare età > 5 minuti
    print(f"\n⏰ Simulo invecchiamento memorie (10 minuti fa)...")
    for memoria in ippocampo.memoria_episodica[-4:]:
        memoria.timestamp = time.time() - 600  # 10 minuti fa
    
    # Esegui consolidamento manuale
    print(f"\n🗑️  Esecuzione consolidamento...")
    eliminate = ippocampo.consolida_memorie_intelligente()
    
    print(f"\n📊 RISULTATI:")
    print(f"   • Memorie eliminate: {eliminate}")
    print(f"   • Memorie conservate: {len(ippocampo.memoria_episodica)}")
    
    print(f"\n✓ Memorie conservate:")
    for i, mem in enumerate(ippocampo.memoria_episodica[-10:], 1):
        print(f"   {i}. {mem.contenuto[:40]}... (V:{mem.valenza_emotiva:+.1f}, I:{mem.importanza:.1f})")
    
    print(f"\n✅ Test consolidamento completato")
    print(f"   Risultato atteso: 2 eliminate (cattiva e media), 2 conservate (buona e importante)")
    
    ippocampo.chiudi()
    return eliminate


def test_richiamo_contestuale():
    """Test richiamo contestuale"""
    print("\n" + "="*70)
    print("🧪 TEST RICHIAMO CONTESTUALE")
    print("="*70)
    
    # Crea ippocampo
    ippocampo = Ippocampo("test_richiamo.json")
    ippocampo.inizializza()
    
    print("\n📝 Creazione memorie di test...")
    
    # Memorie con diverse azioni e contesti
    memorie_test = [
        {
            'contenuto': "Comando vocale 'vieni qui' eseguito con successo",
            'valenza': 0.8,
            'importanza': 1.2,
            'azione': 'esegui_comando'
        },
        {
            'contenuto': "Rilevato veicolo in avvicinamento, evitato",
            'valenza': 0.9,
            'importanza': 1.8,
            'azione': 'evita_ostacolo'
        },
        {
            'contenuto': "Persona riconosciuta, mantenuta distanza",
            'valenza': 0.7,
            'importanza': 1.1,
            'azione': 'mantieni_distanza'
        },
        {
            'contenuto': "Comando 'vieni qui' ripetuto, avvicinamento",
            'valenza': 0.85,
            'importanza': 1.5,
            'azione': 'avvicinati'
        }
    ]
    
    for mem_data in memorie_test:
        ippocampo.memorizza(
            f"mem_{int(time.time())}",
            mem_data['contenuto'],
            metadata={
                'valenza': mem_data['valenza'],
                'importanza': mem_data['importanza'],
                'contesto': {'azione': mem_data['azione'], 'successo': True}
            }
        )
    
    print(f"✓ Create {len(memorie_test)} memorie di test")
    
    # Test richiamo con contesti diversi
    print(f"\n🔍 Test richiami contestuali:\n")
    
    # Scenario 1: Comando vocale simile
    print("--- Scenario 1: 'Ricevuto comando vieni qui' ---")
    memorie, suggerimenti = ippocampo.richiama_contestuale("comando vieni qui persona", top_k=3)
    
    print(f"Memorie trovate: {len(memorie)}")
    for i, mem in enumerate(memorie, 1):
        print(f"  {i}. {mem.contenuto[:50]}...")
    
    print(f"\nSuggerimenti:")
    print(f"  • Tipo: {suggerimenti['suggerimento']}")
    print(f"  • Confidence: {suggerimenti['confidence']:.2f}")
    print(f"  • Azione consigliata: {suggerimenti['azione_consigliata']}")
    print(f"  • Valenza media ricordi: {suggerimenti['valenza_media']:+.2f}")
    
    # Scenario 2: Pericolo
    print(f"\n--- Scenario 2: 'Rilevato veicolo pericolo' ---")
    memorie2, suggerimenti2 = ippocampo.richiama_contestuale("veicolo pericolo avvicinamento", top_k=3)
    
    print(f"Memorie trovate: {len(memorie2)}")
    for i, mem in enumerate(memorie2, 1):
        print(f"  {i}. {mem.contenuto[:50]}...")
    
    print(f"\nSuggerimenti:")
    print(f"  • Tipo: {suggerimenti2['suggerimento']}")
    print(f"  • Confidence: {suggerimenti2['confidence']:.2f}")
    print(f"  • Azione consigliata: {suggerimenti2['azione_consigliata']}")
    
    print(f"\n✅ Test richiamo contestuale completato")
    
    ippocampo.chiudi()
    return memorie, suggerimenti


def test_integrato():
    """Test integrato: consolidamento + richiamo"""
    print("\n" + "="*70)
    print("🧪 TEST INTEGRATO: Sistema Memoria Completo")
    print("="*70)
    
    ippocampo = Ippocampo("test_integrato.json")
    ippocampo.inizializza()
    
    print("\n📝 Simulazione sessione lunga...")
    
    # Crea 10 memorie con valori variabili
    for i in range(10):
        valenza = (i % 3 - 1) * 0.6  # Alterna tra -0.6, 0, +0.6
        importanza = 0.5 + (i % 5) * 0.3  # Varia 0.5-1.7
        
        ippocampo.memorizza(
            f"evento_{i}",
            f"Evento #{i}: azione test con valenza {valenza:.1f}",
            metadata={
                'valenza': valenza,
                'importanza': importanza,
                'contesto': {'ciclo': i, 'test': True}
            }
        )
    
    print(f"✓ Create 10 memorie")
    print(f"  Memorie totali: {len(ippocampo.memoria_episodica)}")
    
    # Simula invecchiamento
    print(f"\n⏰ Simulo invecchiamento (7 minuti fa)...")
    for memoria in ippocampo.memoria_episodica[-10:]:
        memoria.timestamp = time.time() - 420  # 7 minuti
    
    # Esegui consolidamento
    print(f"\n🗑️  Consolidamento automatico...")
    eliminate = ippocampo.consolida_memorie_intelligente()
    print(f"   ✓ Eliminate: {eliminate}")
    print(f"   ✓ Conservate: {len(ippocampo.memoria_episodica)}")
    
    # Test richiamo
    print(f"\n🔍 Test richiamo contestuale...")
    memorie, suggerimenti = ippocampo.richiama_contestuale("azione test evento", top_k=5)
    
    print(f"   ✓ Memorie richiamate: {len(memorie)}")
    print(f"   ✓ Suggerimento: {suggerimenti['suggerimento']}")
    
    # Statistiche finali
    print(f"\n📊 STATISTICHE FINALI:")
    stats = ippocampo.get_statistiche()
    for key, value in stats.items():
        print(f"   • {key}: {value}")
    
    ippocampo.chiudi()
    print(f"\n✅ Test integrato completato")


if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║           🧪 TEST MEMORIA AVANZATA                            ║
    ║                                                                ║
    ║     Consolidamento + Richiamo Contestuale                     ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """)
    
    # Esegui test
    test_consolidamento()
    time.sleep(1)
    
    test_richiamo_contestuale()
    time.sleep(1)
    
    test_integrato()
    
    print("\n" + "="*70)
    print("✅ TUTTI I TEST COMPLETATI!")
    print("="*70)

