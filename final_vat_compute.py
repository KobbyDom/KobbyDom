
class ComputeVAT:

    def __init__(self, item_price):
        self.my_item = item_price

    def vat_components(self):
        nhil_component = item_price * 0.025
        getfund_component = item_price * 0.025
        covid19_component = item_price * 0.01
        total_non_vat_levy = nhil_component + getfund_component + covid19_component
        taxable_value = item_price + total_non_vat_levy
        vat_amount = taxable_value * 0.125
        total_amount = taxable_value + vat_amount
        total_price = (f'''
Item Price:                     GH¢{item_price}
NHIL Amount:      GH¢{round(nhil_component, 2)}
GETFUND Amount:   GH¢{round(getfund_component, 2)}
COVID19 Amount:   GH¢{round(covid19_component, 2)}
                                GH¢{round(total_non_vat_levy, 2)}
                                __________________
Taxable Amount:                 GH¢{round(taxable_value, 2)}
VAT Amount:                     GH¢{round(vat_amount, 2)}
                                __________________
Total Amount                    GH¢{round(total_amount, 2)}
''')
        return total_price


item_price = float(input('Item Price:-> '))

vat_compute = ComputeVAT(item_price)
print(f'The VAT inclusive amount for your item price of GH¢{item_price} is')
print()
print(vat_compute.vat_components())

