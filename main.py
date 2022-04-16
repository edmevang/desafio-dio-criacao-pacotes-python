from sales.calc_preco import aumento, desconto
from sales.format_price import preco as preco_formatado

preco = float(input('Enter price: '))
porc_aumento = float(input('Enter the increase percentage: '))
porc_desconto = float(input('Enter the discount percentage: '))

preco_com_aumento = aumento(valor=preco, porcentagem=porc_aumento, formata=True)
print(f'The price with the increase: {preco_com_aumento} (+{porc_aumento}%)')

preco_com_desconto = desconto(valor=preco, porcentagem=porc_desconto, formata=True)
print(f'The discounted price: {preco_com_desconto} (-{porc_desconto}%)')

print(f'The price was: {preco_formatado.real(preco)}')