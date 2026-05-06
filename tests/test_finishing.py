import fishing
import builtins
import sys
import types
import importlib
import pytest


# ---------- Helper to run student code with fake inputs ----------
def run_with_input(module, inputs):
    inputs = inputs.copy()

    def mock_input(prompt=""):
        return inputs.pop(0)

    original_input = builtins.input
    builtins.input = mock_input

    try:
        module.collect_tour_info()
    finally:
        builtins.input = original_input


# ---------- Test 1: Function exists ----------
def test_function_exists():
    student = importlib.import_module("student")
    assert hasattr(student, "collect_tour_info"), \
        "collect_tour_info() function is missing"


# ---------- Test 2: Valid booking scenario ----------
def test_valid_tour(monkeypatch, capsys):
    student = importlib.import_module("student")

    inputs = [
        "2",        # number of people
        "3",        # Ships Cove
        "3",        # days
        "Maya", "28",
        "Ethan", "35"
    ]

    run_with_input(student, inputs)
    output = capsys.readouterr().out

    assert "Number of People: 2" in output
    assert "Destination: Ships Cove" in output
    assert "Length of Tour: 3" in output
    assert "Maya" in output
    assert "28" in output
    assert "Ethan" in output
    assert "35" in output


# ---------- Test 3: Invalid number of people forces retry ----------
def test_people_validation(monkeypatch, capsys):
    student = importlib.import_module("student")

    inputs = [
        "6",        # invalid
        "0",        # invalid
        "1",        # valid
        "1",        # destination
        "2",        # days
        "Alex", "20"
    ]

    run_with_input(student, inputs)
    output = capsys.readouterr().out

    assert "Number of People: 1" in output
    assert "Alex" in output


# ---------- Test 4: Invalid destination defaults to Kaikoura ----------
def test_destination_default(monkeypatch, capsys):
    student = importlib.import_module("student")

    inputs = [
        "1",
        "9",        # invalid destination
        "2",
        "Sam", "30"
    ]

    run_with_input(student, inputs)
    output = capsys.readouterr().out

    assert "Destination: Kaikoura" in output


# ---------- Test 5: Correct printing of people list ----------
def test_people_format(monkeypatch, capsys):
    student = importlib.import_module("student")

    inputs = [
        "2",
        "2",        # Port Underwood
        "1",
        "Lily", "14",
        "Ben", "15"
    ]

    run_with_input(student, inputs)
    output = capsys.readouterr().out

    assert "- Lily" in output or "Lily" in output
    assert "- Ben" in output or "Ben" in output