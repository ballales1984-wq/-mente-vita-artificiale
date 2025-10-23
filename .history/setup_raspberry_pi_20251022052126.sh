#!/bin/bash
# 🧠 Setup script per Mente Artificiale su Raspberry Pi
# ======================================================

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🧠 MENTE ARTIFICIALE - Setup per Raspberry Pi / AI PC       ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Colori
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Funzione per messaggi
info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verifica sistema
info "Verifica sistema operativo..."
OS=$(uname -s)
ARCH=$(uname -m)
echo "  • OS: $OS"
echo "  • Architettura: $ARCH"

# Verifica Python
info "Verifica Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "  • $PYTHON_VERSION"
else
    error "Python 3 non trovato!"
    exit 1
fi

# Aggiorna sistema
info "Aggiornamento sistema..."
if [ "$OS" = "Linux" ]; then
    sudo apt-get update
    sudo apt-get upgrade -y
fi

# Installa dipendenze sistema
info "Installazione dipendenze di sistema..."
if [ "$OS" = "Linux" ]; then
    sudo apt-get install -y \
        python3-pip \
        python3-venv \
        libportaudio2 \
        libsndfile1 \
        ffmpeg \
        libopencv-dev \
        libatlas-base-dev \
        libjpeg-dev \
        libtiff5-dev \
        libpng-dev \
        libavcodec-dev \
        libavformat-dev \
        libswscale-dev \
        libv4l-dev \
        libxvidcore-dev \
        libx264-dev \
        libgtk-3-dev
fi

# Crea virtual environment
info "Creazione virtual environment..."
python3 -m venv venv_mente_ai
source venv_mente_ai/bin/activate

# Aggiorna pip
info "Aggiornamento pip..."
pip install --upgrade pip setuptools wheel

# Installa dipendenze Python (versione ottimizzata per Raspberry Pi)
info "Installazione pacchetti Python..."

# Installa PyTorch ottimizzato per ARM (se Raspberry Pi)
if [ "$ARCH" = "aarch64" ] || [ "$ARCH" = "armv7l" ]; then
    warn "Rilevato ARM: installazione PyTorch ottimizzato..."
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
else
    info "Installazione PyTorch standard..."
    pip install torch torchvision torchaudio
fi

# Installa OpenCV ottimizzato
info "Installazione OpenCV..."
pip install opencv-python-headless  # Versione senza GUI per Raspberry Pi

# Installa altri pacchetti
info "Installazione altri pacchetti AI..."
pip install ultralytics
pip install openai-whisper
pip install transformers accelerate
pip install sounddevice soundfile
pip install numpy scipy pillow

# Test hardware
info "Test hardware disponibile..."
python3 << 'EOF'
import sys

print("\n" + "="*60)
print("🔍 VERIFICA HARDWARE")
print("="*60)

# Test camera
try:
    import cv2
    camera = cv2.VideoCapture(0)
    if camera.isOpened():
        print("  ✅ Camera: OK")
        camera.release()
    else:
        print("  ❌ Camera: Non rilevata")
except Exception as e:
    print(f"  ❌ Camera: Errore - {e}")

# Test microfono
try:
    import sounddevice as sd
    devices = sd.query_devices()
    input_devices = [d for d in devices if d['max_input_channels'] > 0]
    if input_devices:
        print(f"  ✅ Microfono: OK ({len(input_devices)} dispositivi)")
    else:
        print("  ❌ Microfono: Non rilevato")
except Exception as e:
    print(f"  ❌ Microfono: Errore - {e}")

# Test GPU
try:
    import torch
    if torch.cuda.is_available():
        print(f"  ✅ GPU: {torch.cuda.get_device_name(0)}")
    else:
        print("  ℹ️  GPU: Non disponibile (usando CPU)")
except Exception as e:
    print(f"  ⚠️  GPU: Errore - {e}")

print("="*60)
EOF

# Download modelli (opzionale)
info "Vuoi scaricare i modelli AI ora? (richiede spazio e tempo)"
read -p "Scaricare modelli? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    info "Download modelli..."
    
    # YOLO nano (più leggero per Raspberry Pi)
    python3 -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
    
    # Whisper base
    python3 -c "import whisper; whisper.load_model('base')"
    
    info "Modelli scaricati!"
else
    warn "Modelli non scaricati. Verranno scaricati al primo utilizzo."
fi

# Crea script di avvio
info "Creazione script di avvio..."
cat > start_mente_ai.sh << 'SCRIPT'
#!/bin/bash
cd "$(dirname "$0")"
source venv_mente_ai/bin/activate
python3 mente_ai_reale.py
SCRIPT
chmod +x start_mente_ai.sh

# Test finale
info "Test del sistema..."
python3 -c "
try:
    from mente_ai_reale import Config
    print('✅ Mente Artificiale: OK')
except Exception as e:
    print(f'❌ Errore: {e}')
"

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                  ✅ SETUP COMPLETATO!                         ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
info "Per avviare la Mente Artificiale:"
echo "  1. Attiva l'ambiente: source venv_mente_ai/bin/activate"
echo "  2. Esegui: python3 mente_ai_reale.py"
echo "  Oppure: ./start_mente_ai.sh"
echo ""
info "File importanti:"
echo "  • mente_ai_reale.py - Script principale"
echo "  • requirements.txt - Dipendenze"
echo "  • test_hardware.py - Test componenti"
echo ""

