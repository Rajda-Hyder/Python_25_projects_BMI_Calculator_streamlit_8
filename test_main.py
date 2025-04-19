# test_main.py
from main import calculate_bmi
import pytest

def test_bmi_normal_case():
    assert round(calculate_bmi(170, 65), 2) == 22.49

def test_bmi_underweight():
    assert round(calculate_bmi(180, 50), 2) == 15.43

def test_bmi_overweight():
    assert round(calculate_bmi(160, 75), 2) == 29.30

def test_bmi_obese():
    assert calculate_bmi(165, 95) == pytest.approx(34.89, abs=0.01)
