import pytest
from  utils import calcul_total_commande, valider_transition_statut

# Test pour calcul_total_commande
def test_calcul_total_commande_nominal():
    lignes = [{'repas': 5, 'quantite': 2}, {'repas': 3, 'quantite': 1}]
    assert calcul_total_commande(lignes) == 13

def test_calcul_total_commande_vide():
    assert calcul_total_commande([]) == 0

def test_calcul_total_commande_negatif():
    lignes = [{'repas': -5, 'quantite': 2}]
    assert calcul_total_commande(lignes) == -10


# Test pour valider_transition_statut
def test_transition_valide():
    assert valider_transition_statut("en_attente", "en_preparation") is True

def test_transition_invalide():
    assert valider_transition_statut("prete", "en_preparation") is False

def test_transition_inconnue():
    assert valider_transition_statut("inexistant", "en_preparation") is False