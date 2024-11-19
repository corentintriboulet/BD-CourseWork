import pandas as pd
import matplotlib.pyplot as plt

# Les données
year_naissance = [
    1935, 1930, 1936, 1938, 1931, 1934, 1940, 1939, 1944, 1946, 1941, 1932, 
    1929, 1942, 1937, 1947, 1933, 1949, 1928, 1927, 1948, 1951, 1943, 1955, 
    1945, 1925, 1926, 1957, 1924, 1922, 1952, 1953, 1950, 1956, 1959, 1964, 
    1954, 1960, 1961, 1965, 1962, 1923, 1921, 1968, 1958, 1970, 1972, 1918, 
    1976, 1919, 1967, 1963, 1966, 1971, 1969, 1977, 1992, 1990, 1979, 1920, 
    1916, 1974, 1982, 1914, 1975, 1988, 1978, 1981
]

count_mort = [
    36, 36, 34, 34, 32, 32, 32, 31, 28, 27, 22, 22, 22, 22, 21, 21, 21, 20, 
    18, 18, 16, 16, 16, 14, 14, 13, 12, 11, 10, 10, 9, 8, 8, 7, 7, 7, 7, 6, 
    5, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
    1, 1, 1, 1, 1, 1
]

# Vérifier la longueur des deux listes
print(f"Longueur de 'year_naissance': {len(year_naissance)}")
print(f"Longueur de 'count_mort': {len(count_mort)}")

# S'assurer que les deux listes ont la même longueur
if len(year_naissance) == len(count_mort):
    # Créer le DataFrame
    df = pd.DataFrame({"year_naissance": year_naissance, "count_mort": count_mort})

    # Tracer l'histogramme
    plt.figure(figsize=(10, 6))
    plt.bar(df['year_naissance'], df['count_mort'], color='skyblue')

    # Ajouter des titres et des labels
    plt.title('Histogramme du nombre de décès par année de naissance')
    plt.xlabel('Année de naissance')
    plt.ylabel('Nombre de décès')

    # Afficher l'histogramme
    plt.xticks(rotation=90)  # Rotation des labels des années pour plus de lisibilité
    plt.tight_layout()  # Ajuster les marges
    plt.show()
else:
    print("Les deux listes n'ont pas la même longueur.")
