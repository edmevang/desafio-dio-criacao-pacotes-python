# sales

### Description. 
The package sales and format_price is used to:
* From a value and a percentage entered, the new values ​​increased, reduced.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install vendas

```bash
pip install -i https://test.pypi.org/simple/ sales # TestPypi environment.
```

## Usage
```python
from sales.format_price import preco
preco.real(10) # Example for the price of 10.00.
```
```python
from sales.calc_preco import aumento, desconto
aumento(10, 15, True) # Example for the price in the amount of 10.00 and the application of a percentage increase of 15% and the boolean True to format the value for the Real currency.
desconto(10, 14, True) # Example for the price in the amount of 10.00 and the application of a discount percentage of 14% and the boolean True to format the value for the Real currency.
```

## Author
Edmilson

## License
[MIT](https://choosealicense.com/licenses/mit/)