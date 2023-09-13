# Variables
PYTHON = python
PIP = $(PYTHON) -m pip
REQUIREMENTS = requirements.txt

# Cible pour installer les bibliothèques
install:
	$(PIP) install -r $(REQUIREMENTS)

# Cible pour désinstaller les bibliothèques
uninstall:
	$(PIP) uninstall -r $(REQUIREMENTS) -y

# Cible pour nettoyer les fichiers générés
clean:
	rm -rf __pycache__

.PHONY: all install uninstall clean
