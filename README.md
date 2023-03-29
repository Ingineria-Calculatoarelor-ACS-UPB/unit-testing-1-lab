# unit-testing-1-lab

1. Factorial [4.5p].
  - [2p] Creați un fisier de test pentru factorial.py. Creați un test care să verifice că funcția factorial întoarce output-ul corect pentru un input introdus de voi.
  - [2.5p] În fisierul creat anterior:
    - Scrieți un test care să primească mai multe input-uri consecutive pentru funcția factorial folosind pytest.mark.parametrize.
    - Scrieți un test care să valideze aruncarea unei excepții în cazul în care se introduce ca input o valoare incorectă.

2. Stores and Products [5.5p].
  - [1p] Scrieți un test care să verifice crearea corectă de instanțe pentru Product și Store.
  - [1p] Scrieți o suită de teste(cel puțin 2) care să poată să fie rulată separat de restul testelor existente care să verifice add_product și remove_product din clasa Store folosind Markers.
  - [1.5p] Din cauza unui bug, scrieți un test care să dea skip atunci când versiunea de python este mai mare de 3.7.
  - [1p] Scrieți un test care se asteptă să eșueze atunci când un Product este creat fara expiration_date. Creați încă un test care se așteaptă să eșueze când se încearcă adăugare unui element invalid în Store (e.g. în loc să fie adăugat un Product, să fie adăugta un string).
  - [1p] Creați un fisier separat în care să testați atât pe success, cât și pe fail, metodele de determinare a celui mai scump produs și a produsului în cea mai mare cantitate.
