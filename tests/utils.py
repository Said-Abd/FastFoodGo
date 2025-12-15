# Fonction 1 : calculer le total d'une commande
def calcul_total_commande(lignes_commande):
    """
    lignes_commande : list de dicts [{'repas': prix, 'quantite': int}]

    lignes_commande = [
        {'repas': 10.0, 'quantite': 2},
        {'repas': 5.5, 'quantite': 1},
        {'repas': 7.25, 'quantite': 3},
    ]
    """
    return sum(item['repas'] * item['quantite'] for item in lignes_commande)


# Fonction 2 : valider la transition de statut d'une commande
def valider_transition_statut(statut_actuel, nouveau_statut):
    transitions_valides = {
        "en_attente": ["en_preparation", "annulee"],
        "en_preparation": ["prete", "annulee"],
        "prete": ["recuperee"],
        "recuperee": [],
        "annulee": [],
    }
    return nouveau_statut in transitions_valides.get(statut_actuel, [])
