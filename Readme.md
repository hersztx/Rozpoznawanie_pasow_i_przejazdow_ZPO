# Projekt ZPO - Model Deepness do Rozpoznawania Przejść dla Pieszych i Przejazdów Rowerowych

Projekt koncentruje się na wykorzystaniu YOLOv8 do segmentacji semantycznej przejść dla pieszych i przejazdów rowerowych, zintegrowanej z QGIS i wtyczką Deepness.

---

## Zbiór Danych

### Źródło Danych
- **Główny Zbiór Danych**: Własny zbiór danych stworzony na podstawie precyzyjnej ortofotomapy Poznania (2023), oznaczony za pomocą narzędzia Roboflow (https://roboflow.com).

### Szczegóły Zbioru Danych
- **Liczba Adnotacji**: 993
  - Własny zbiór danych: 993
- **Format Danych**: Format segmentacji semantycznej zgodny z Roboflow i YOLO.
- **Przygotowanie Danych**: 
  - Stworzono w QGIS z wykorzystaniem ortofotomapy Poznania 2023.
  - Adnotacje wykonano w Roboflow, używając segmentacji semantycznej (klasy: pedestrian_cross, bicycle_cross).

### Przechowywanie Danych
- Zbiór danych wraz z adnotacjami jest przechowywany w: 'obrazy_zpo/Dane_do_przetwarzania' i dostępny pod w repozytorium.
- Skrypty do ładowania danych są kompatybilne z formatem YOLO i dostępne w folderze 'obrazy_zpo/pliki_programowe'.

---

## Trening

### Sieć i Parametry
- **Sieć**: YOLOv8n-seg (model segmentacji).
- **Parametry Treningu**:
- **patience:** 100
- **batch:** 16
- **imgsz:** 512
- **Liczba epok:** 10
- **Augmentacja**: Nie stosowano z uwagi na wymogi projektowe


### Skrypty i Środowisko
- **Skrypt Treningowy**: `trening_modelu.py` (znajduje się w repozytorium).
- **Środowisko**: Wersja Pythona: 3.11
# Wyniki

## Przykładowe Obrazy ze Zbioru Danych

- **Obraz 1:** Przejścia dla pieszych i przejazdy rowerowe w centrum miasta, dobrze oświetlone.
  - ![Obraz 1](https://github.com/hersztx/Rozpoznawanie_pasow_i_przejazdow_ZPO/blob/813722d7c8779eb6e0ee8ed427b9ce744d11b3d5/Przyk%C5%82adowe_wyniki_przetwarzania/Obraz_1.png)
  - **Adnotacje:** Segmentacja poprawna.
  

- **Obraz 2:** Przejście dla pieszych i przejazd rowerowy, dobre oświetlenie.
  - ![Obraz 2](obrazy_zpo/Przykładowe_wyniki_przetwarzania/Obraz_2.jpg)
  - **Adnotacje:** "Przejazd rowerowy" – segmentacja częściowo poprawna.
  

- **Obraz 3:** Przejście dla pieszych na czerwonym spowalniaczu dla samochodów.
  - ![Obraz 3](obrazy_zpo/Przykładowe_wyniki_przetwarzania/Obraz_3.jpg)
  - **Adnotacje:** Segmentacja częściowo poprawna.
  

- **Obraz 4:** Widok na dach budynku, który ma białe paski.
  - ![Obraz 4](obrazy_zpo/Przykładowe_wyniki_przetwarzania/Obraz_4.jpg)
  - **Adnotacje:** Segmentacja niepoprawna.


## Metryki

- **Intersection over Union (IoU): 0,40**

- **Resolution:** 10,00
- **Tile size:** 512
- **Batch size:** 1
- **Tiles overlap:** 10%
- 
---

## Wytrenowany Model w Formacie ONNX

### Szczegóły Modelu:
- Model został wytrenowany zapomocą sieci YOLO v8 i został wyeksportowany do formatu ONNX (dostępny w repozytorium).
- Zawiera metadane wymagane do integracji z Deepness (rozdzielczość przestrzenna: 10 px/cm).

---

## Skrypt Konwersji

- **Użyty skrypt:** `konwersja_modleu_na_onnx.py` (dostępny w repozytorium).

---

## Instrukcja uruchomienia


### Kroki:
1. Załaduj ortofotomapę Poznania 2023 do QGIS.
2. Wybierz odpowiednie ustawienia przetwarzania (opisane wyżej).
2. Ustal odpowiednią skalę mapy do obszaru zainteresowania.
3. Uruchom wtyczkę Deepness z modelem ONNX, aby znaleźć przejścia oraz przejazdy.
4. Poczekaj na zwizualizowanie zaznaczonych wyników segmentacji.

---

## Zespół

- **Jakub Czyszewski 147480**
- **Michał Gładysz 147639**
