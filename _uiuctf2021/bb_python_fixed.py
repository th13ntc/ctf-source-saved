from pprint import pprint
import re
bad = bool(re.search(r'[a-z\s]', (input := input())))
# pprint(''.__class__.__mro__[1])
if not bad:
    exec(input)
else:
    print('Input contained bad characters')
# exec("\162\145\56\137\137\142\165\151\154\164\151\156\163\137\137\133\047\137\137\151\155\160\157\162\164\137\137\047\135\050\047\157\163\047\051\056\163\171\163\164\145\155\050\047\144\151\162\047\051")
exit(bad)
