#!/usr/bin/env python3
"""
MENTE VITA ARTIFICIALE v7.1 - WEB EDITION
Sistema AGI con accesso a:
- Webcam reale
- Microfono reale  
- Internet (RSS feeds, news, Wikipedia)
- API esterne

Per massimo apprendimento!
"""

import sys
import requests
from datetime import datetime
import feedparser
from MENTE_VITA_AUTO_LEARNING import MenteVitaAutoLearning

class MenteVitaWeb(MenteVitaAutoLearning):
    """
    Estensione con accesso al web e dati reali
    """
    
    def __init__(self):
        super().__init__()
        self.nome = "Mente Vita Web"
        
        # Feed RSS da monitorare
        self.rss_feeds = [
            "https://news.google.com/rss?hl=it",  # Google News IT
            "https://www.ansa.it/sito/notizie/tecnologia/tecnologia_rss.xml",  # ANSA Tech
            "https://feeds.bbci.co.uk/news/technology/rss.xml",  # BBC Tech
        ]
        
        # Cache notizie
        self.ultime_notizie = []
        self.notizie_lette = set()
        
        print(f"\n🌐 {self.nome} - CONNESSO A INTERNET!")
        print(f"📡 Feed RSS attivi: {len(self.rss_feeds)}")
    
    def leggi_notizie_rss(self):
        """Legge notizie da feed RSS"""
        try:
            for feed_url in self.rss_feeds:
                feed = feedparser.parse(feed_url)
                
                for entry in feed.entries[:5]:  # Prime 5 notizie
                    if entry.link not in self.notizie_lette:
                        notizia = {
                            'titolo': entry.title,
                            'link': entry.link,
                            'data': entry.get('published', 'N/A'),
                            'fonte': feed.feed.title
                        }
                        self.ultime_notizie.append(notizia)
                        self.notizie_lette.add(entry.link)
                        
                        # Crea concetto dalla notizia
                        self._apprendi_da_notizia(notizia)
            
            return len(self.ultime_notizie)
        except Exception as e:
            print(f"⚠️ Errore lettura RSS: {e}")
            return 0
    
    def _apprendi_da_notizia(self, notizia):
        """Crea un concetto da una notizia"""
        try:
            # Estrai parole chiave dal titolo
            parole = notizia['titolo'].lower().split()
            parole_chiave = [p for p in parole if len(p) > 4][:3]
            
            if parole_chiave:
                concetto = {
                    'nome': f"news_{len(self.generalizzazione.concetti) + 1}",
                    'parole_chiave': parole_chiave,
                    'fonte': notizia['fonte'],
                    'timestamp': datetime.now().isoformat()
                }
                
                # Aggiungi a concetti (se non esiste già)
                if concetto['nome'] not in [c.get('nome', '') for c in self.generalizzazione.concetti]:
                    self.generalizzazione.concetti.append(concetto)
                    print(f"📰 Nuovo concetto da news: {parole_chiave}")
        except Exception as e:
            print(f"⚠️ Errore apprendimento notizia: {e}")
    
    def cerca_wikipedia(self, query):
        """Cerca su Wikipedia italiano"""
        try:
            url = "https://it.wikipedia.org/w/api.php"
            params = {
                'action': 'query',
                'format': 'json',
                'list': 'search',
                'srsearch': query,
                'srlimit': 1
            }
            
            response = requests.get(url, params=params, timeout=5)
            data = response.json()
            
            if data['query']['search']:
                risultato = data['query']['search'][0]
                return {
                    'titolo': risultato['title'],
                    'snippet': risultato['snippet'],
                }
            return None
        except Exception as e:
            print(f"⚠️ Errore Wikipedia: {e}")
            return None
    
    def ottieni_dati_meteo(self):
        """Ottiene dati meteo (API gratuita)"""
        try:
            # wttr.in - API meteo gratuita
            response = requests.get("https://wttr.in/?format=j1", timeout=5)
            if response.status_code == 200:
                meteo = response.json()
                return {
                    'temperatura': meteo['current_condition'][0]['temp_C'],
                    'descrizione': meteo['current_condition'][0]['weatherDesc'][0]['value'],
                    'umidita': meteo['current_condition'][0]['humidity']
                }
        except Exception as e:
            print(f"⚠️ Errore meteo: {e}")
        return None
    
    def ciclo_agi_con_web(self):
        """Ciclo AGI esteso con dati web"""
        
        # Ogni 10 cicli, leggi notizie
        if self.stats['cicli_totali'] % 10 == 0:
            print(f"\n🌐 Aggiornamento notizie dal web...")
            num_notizie = self.leggi_notizie_rss()
            print(f"📰 Notizie lette: {num_notizie}")
        
        # Ogni 50 cicli, cerca su Wikipedia
        if self.stats['cicli_totali'] % 50 == 0 and self.stats['cicli_totali'] > 0:
            print(f"\n📚 Ricerca Wikipedia...")
            # Cerca un concetto esistente
            if self.generalizzazione.concetti:
                concetto = self.generalizzazione.concetti[-1]
                parole = concetto.get('parole_chiave', ['intelligenza', 'artificiale'])
                query = ' '.join(parole[:2])
                risultato = self.cerca_wikipedia(query)
                if risultato:
                    print(f"📖 Trovato: {risultato['titolo']}")
        
        # Ogni 100 cicli, controlla meteo
        if self.stats['cicli_totali'] % 100 == 0 and self.stats['cicli_totali'] > 0:
            print(f"\n🌤️ Controllo meteo...")
            meteo = self.ottieni_dati_meteo()
            if meteo:
                print(f"🌡️ Temperatura: {meteo['temperatura']}°C - {meteo['descrizione']}")
        
        # Ciclo AGI normale
        return super().ciclo_agi_completo(
            input_visivo=None,  # Webcam reale se disponibile
            input_audio=None    # Microfono reale se disponibile
        )
    
    def esegui_con_web(self, cicli_target=100):
        """Esecuzione con accesso web"""
        
        print("\n" + "="*80)
        print("🌐 AVVIO AUTO-LEARNING CON ACCESSO WEB")
        print("="*80)
        print(f"🎯 Target: {cicli_target} cicli")
        print(f"📡 Feed RSS: {len(self.rss_feeds)}")
        print(f"🌍 Wikipedia: Attiva")
        print(f"🌤️ API Meteo: Attiva")
        print(f"📹 Webcam: {'Attiva' if self.visione else 'Simulata'}")
        print(f"🎤 Microfono: {'Attivo' if self.udito else 'Simulato'}")
        print("="*80)
        
        # Lettura iniziale notizie
        print(f"\n📰 Lettura notizie iniziale...")
        num_notizie = self.leggi_notizie_rss()
        print(f"✅ {num_notizie} notizie caricate!")
        
        # Avvia ciclo
        self.stats['cicli_totali'] = 0
        self.stats['tempo_inizio'] = datetime.now()
        
        try:
            while self.stats['cicli_totali'] < cicli_target:
                # Ciclo con web
                self.ciclo_agi_con_web()
                self.stats['cicli_totali'] += 1
                
                # Statistiche ogni 10 cicli
                if self.stats['cicli_totali'] % 10 == 0:
                    self._mostra_statistiche_compatte()
                
                # Pulizia memoria ogni 50
                if self.stats['cicli_totali'] % 50 == 0:
                    self._pulisci_memoria()
            
            # Statistiche finali
            print("\n" + "="*80)
            print("🎊 AUTO-LEARNING WEB COMPLETATO!")
            print("="*80)
            self._mostra_statistiche_finali()
            
        except KeyboardInterrupt:
            print("\n\n" + "="*80)
            print("🛑 INTERRUZIONE UTENTE")
            print("="*80)
            self._mostra_statistiche_finali()


if __name__ == "__main__":
    print("""
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║           🌐 MENTE VITA ARTIFICIALE v7.1 - WEB EDITION 🌐           ║
║                                                                       ║
║  Sistema AGI con accesso a:                                          ║
║  • 📡 Internet (RSS feeds, news)                                     ║
║  • 📚 Wikipedia                                                       ║
║  • 🌤️ API Meteo                                                      ║
║  • 📹 Webcam reale                                                    ║
║  • 🎤 Microfono reale                                                 ║
║                                                                       ║
║  Per massimo apprendimento da dati REALI!                            ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
    """)
    
    # Numero cicli
    if len(sys.argv) > 1:
        try:
            cicli = int(sys.argv[1])
        except:
            cicli = 100
    else:
        cicli = 100
    
    print(f"\n🎯 Cicli richiesti: {cicli}")
    print(f"⏱️ Tempo stimato: {cicli * 6 / 60:.1f} minuti")
    
    # Crea e avvia
    mente = MenteVitaWeb()
    mente.esegui_con_web(cicli_target=cicli)
    
    print("\n✅ Esecuzione completata!")
    print(f"📊 Concetti appresi: {len(mente.generalizzazione.concetti)}")
    print(f"📰 Notizie lette: {len(mente.ultime_notizie)}")

