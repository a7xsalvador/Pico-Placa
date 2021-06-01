# Pico-Placa

Class that allows knowing if a vehicle with a certain license plate is allowed to transit on a certain day and time according to the restrictions in the city of Quito-Ecuador. Written by **Gabriel Salvador**.

## Parameters

- **plateNumber:** It has to finish with a number.
- **date:** In format d/m/Y.
- **time:** In format H:M.

## Example
Checking if a vehicle is allowed.

`>>> import PicoPlaca as pp`

`>>> a = pp.PicoPlaca('ABC211','31/05/2021','7:00')`

`>>> a.message()`

`The vehicle is NOT allowed to road`

## Automated testing
Usign [pytest!](https://docs.pytest.org/en/6.2.x/)

`pytest test.py`
