def somma_numeri(numeri):
    """Restituisce la somma dei numeri della lista usando un ciclo for."""
    totale = 0
    for numero in numeri:
        totale += numero
    return totale


if __name__ == "__main__":
    numeri = [1, 2, 3, 4, 5]
    print(f"Numeri: {numeri}")
    print(f"Somma: {somma_numeri(numeri)}")
