# 🤝 Contributing to Mente Artificiale

Grazie per l'interesse nel contribuire! 🎉

## 🎯 Come Contribuire

### 1. **Setup Ambiente**

```bash
# Fork e clone
git clone https://github.com/YOUR-USERNAME/mente-artificiale.git
cd mente-artificiale

# Crea virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Installa dipendenze development
pip install -r requirements.txt
pip install pytest black flake8
```

### 2. **Crea Branch**

```bash
git checkout -b feature/nome-funzionalita
```

Naming convention:
- `feature/` - Nuova funzionalità
- `fix/` - Bug fix
- `docs/` - Documentazione
- `test/` - Test

### 3. **Sviluppa**

Linee guida:
- ✅ Segui stile esistente
- ✅ Aggiungi docstring
- ✅ Scrivi test
- ✅ Documenta cambiamenti

### 4. **Test**

```bash
# Esegui test
python test_hardware.py
python test_memoria_avanzata.py

# Verifica codice
python -m pytest
```

### 5. **Commit**

```bash
git add .
git commit -m "feat: Aggiungi [nome funzionalità]"
```

Formato commit:
- `feat:` - Nuova feature
- `fix:` - Bug fix
- `docs:` - Documentazione
- `test:` - Test
- `refactor:` - Refactoring
- `style:` - Formatting

### 6. **Push e PR**

```bash
git push origin feature/nome-funzionalita
```

Poi apri Pull Request su GitHub.

---

## 🎯 Aree di Contribuzione

### 🧠 Moduli Cerebrali
- Nuovi moduli (es. cervelletto, gangli basali)
- Ottimizzazione moduli esistenti
- Nuovi algoritmi

### 🔧 Hardware
- Driver per nuovi sensori
- Driver per attuatori
- Supporto nuove piattaforme

### 🤖 AI Models
- Integrazione nuovi modelli
- Fine-tuning custom
- Ottimizzazione inferenza

### 📊 Visualizzazione
- Dashboard web
- Grafici real-time
- Animazioni pattern neurali

### 🧪 Testing
- Nuovi test cases
- Benchmark performance
- Test integrazione

### 📚 Documentazione
- Tutorial
- Esempi
- Traduzioni

---

## 📏 Code Style

### Python
```python
# Docstring completi
def funzione(param: str) -> dict:
    """
    Breve descrizione
    
    Args:
        param: Descrizione parametro
        
    Returns:
        Descrizione return
    """
    pass

# Type hints
def elabora(input_data: Dict[str, Any]) -> RisultatoElaborazione:
    pass

# Gestione errori
try:
    risultato = funzione()
except Exception as e:
    print(f"[Modulo] ⚠️ Errore: {e}")
    risultato = fallback()
```

### Naming
- `snake_case` per funzioni/variabili
- `PascalCase` per classi
- `UPPER_CASE` per costanti

---

## 🧪 Testing

Tutti i contributi devono includere test:

```python
# test_nuovo_modulo.py
def test_funzionalita():
    modulo = NuovoModulo()
    risultato = modulo.elabora(input_test)
    assert risultato['successo'] == True
```

---

## 📋 Checklist PR

Prima di aprire PR, verifica:

- [ ] Codice funziona
- [ ] Test passano
- [ ] Documentazione aggiornata
- [ ] Docstring completi
- [ ] No errori linter
- [ ] Branch aggiornato con main

---

## 🐛 Report Bug

Usa GitHub Issues con template:

```markdown
**Descrizione Bug:**
[Descrizione chiara]

**Come Riprodurre:**
1. Esegui X
2. Fai Y
3. Vedi errore Z

**Comportamento Atteso:**
[Cosa dovrebbe succedere]

**Ambiente:**
- OS: [Windows/Linux/Mac]
- Python: [versione]
- Modulo: [nome]

**Screenshot/Log:**
[Se applicabile]
```

---

## 💡 Feature Request

```markdown
**Funzionalità Proposta:**
[Descrizione]

**Motivazione:**
[Perché è utile]

**Implementazione Proposta:**
[Come implementarla]

**Alternative:**
[Altre soluzioni considerate]
```

---

## 🏆 Contributors

Grazie a tutti i contributori!

<!-- Inserire lista automatica da GitHub -->

---

## 📞 Supporto

- 💬 [Discussions](https://github.com/your-username/mente-artificiale/discussions)
- 🐛 [Issues](https://github.com/your-username/mente-artificiale/issues)
- 📧 Email: your-email@example.com

---

**Grazie per contribuire al progetto! 🙏**

