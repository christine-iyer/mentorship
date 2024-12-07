inventory = []
# def add_products(product,detail,unitMeasure,unitsAvailable,unitCost,cost,recipe):
#      pass
def display_inventory():
     pass


def add_products(product,detail,unitMeasure,unitsAvailable,unitCost,cost,recipe):
  for item in inventory:
    if item['product']==product:
      print(f"item: '{product}' does not exit")
      return
    
  item={"product": product,
    "detail":detail,
    "unitMeasure":unitMeasure,
    "unitsAvailable":unitsAvailable,
    "unitCost": unitCost,
    "cost": cost,
    "recipe":recipe}
  inventory.append(item)
  print(f"item: '{product}' created")
  
  
add_products("Raw Flower", "b", "c", 2, 12.00,47.00,False)
# print("Inventory", inventory)

inventory=[
   {
       "product": "Raw Flower",
       "detail": "R4",
       "unitMeasure": "oz",
       "unitsAvailable": 0,
       "unitCost": 0,
       "cost":0,
       "recipe": False
     },
     {
       "product": "Raw Flower",
       "detail": "ACDC",
       "unitMeasure": "oz",
       "unitsAvailable": 0,
       "unitCost": 0,
       "cost":0,
       "recipe": False
     }
     ,
     {
       "product": "Raw Flower",
       "detail": "MW",
       "unitMeasure": "oz",
       "unitsAvailable": 0,
       "unitCost": 0,
       "cost":0,
       "recipe": False
     },
     {
       "product": "Raw Flower",
       "detail": "DD",
       "unitMeasure": "oz",
       "unitsAvailable": 0,
       "unitCost": 0,
       "cost":0,
       "recipe": False
     },
     {
       "product": "Raw Flower",
       "detail": "MW/DHDS",
       "unitMeasure": "oz",
       "unitsAvailable": 0,
       "unitCost": 0,
       "cost":0,
       "recipe": False
     },
     {
       "product": "Raw Flower",
       "detail": "LemD",
       "unitMeasure": "oz",
       "unitsAvailable": 0,
       "unitCost": 0,
       "cost":0,
       "recipe": False
     },
     {
       "product": "Raw Flower",
       "detail": "Sativa",
       "unitMeasure": "oz",
       "unitsAvailable": 0,
       "unitCost": 0,
       "cost":0,
       "recipe": False
     },
     {
       "product": "Raw Flower",
       "detail": "Indica",
       "unitMeasure": "oz",
       "unitsAvailable": 0,
       "unitCost": 0,
       "cost":0,
       "recipe": False
     },
     {
       "product": "Raw Flower",
       "detail": "Cotton candy",
       "unitMeasure": "oz",
       "unitsAvailable": 0,
       "unitCost": 0,
       "cost":0,
       "recipe": False
     },
     {
       "product": "Raw Flower",
       "detail": "Cheese",
       "unitMeasure": "oz",
       "unitsAvailable": 0,
       "unitCost": 0,
       "cost":0,
       "recipe": False
     },
     {
       "product": "Raw Flower",
       "detail": "Lilac diesel",
       "unitMeasure": "oz",
       "unitsAvailable": 0,
       "unitCost": 0,
       "cost":0,
       "recipe": False
     },
     {
       "product": "Raw Flower",
       "detail": "Citral glue",
       "unitMeasure": "oz",
       "unitsAvailable": 0,
       "unitCost": 0,
       "cost":0,
       "recipe": False
     },
     {
       "product": "Gummies",
       "detail": "Sleep CBG",
       "unitMeasure": "1 oz per pack-packs",
       "unitsAvailable": 12,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Gummies",
       "detail": "Sleep CBD/ACDC",
       "unitMeasure": "1 oz per pack-packs",
       "unitsAvailable": 2,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Gummies",
       "detail": "Sleep Indica",
       "unitMeasure": "1 oz per pack-packs",
       "unitsAvailable": 2,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Gummies",
       "detail": "Lift",
       "unitMeasure": "1 oz per pack-packs",
       "unitsAvailable": 8,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Gummies",
       "detail": "Recovery",
       "unitMeasure": "1 oz per pack-packs",
       "unitsAvailable": 2,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Gummies",
       "detail": "Daytime CBG",
       "unitMeasure": "1 oz per pack-packs",
       "unitsAvailable": 14,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Candies",
       "detail": "CBD/CBN",
       "unitMeasure": "oz",
       "unitsAvailable": 4,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Candies",
       "detail": "Lemongrass",
       "unitMeasure": "oz",
       "unitsAvailable": 34,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Candies",
       "detail": "Watermelon",
       "unitMeasure": "oz",
       "unitsAvailable": 26,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Candies",
       "detail": "Woe",
       "unitMeasure": "oz",
       "unitsAvailable": 34,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Candies",
       "detail": "CBG",
       "unitMeasure": "oz",
       "unitsAvailable": 11,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Tinctures-Base Oil",
       "detail": "Indica glycerin",
       "unitMeasure": "oz",
       "unitsAvailable": 3,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Tinctures-Base Oil",
       "detail": "Sativa",
       "unitMeasure": "oz",
      "unitsAvailable": 9,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Tinctures-Base Oil",
       "detail": "Union custom",
       "unitMeasure": "oz",
       "unitsAvailable": 11,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Tinctures-Base Oil",
       "detail": "CBN MCT",
       "unitMeasure": "oz",
       "unitsAvailable": 2,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Tinctures-Base Oil",
       "detail": "Chaga",
       "unitMeasure": "oz",
       "unitsAvailable": 3,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Topicals",
       "detail": "Garden of Bloom",
       "unitMeasure": "oz",
       "unitsAvailable": 2,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Topicals",
       "detail": "Garden of Peace",
       "unitMeasure": "oz",
       "unitsAvailable": 5,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Topicals",
       "detail": "Lip Lover",
       "unitMeasure": "oz",
       "unitsAvailable": 50,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Topicals",
       "detail": "Massage Oil Cream",
       "unitMeasure": "oz",
       "unitsAvailable": 3,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Topicals",
       "detail": "No 10",
       "unitMeasure": "oz",
       "unitsAvailable": 2,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Topicals",
       "detail": "Therapeutic Touch",
       "unitMeasure": "oz",
       "unitsAvailable": 2,
       "unitCost": 0,
       "cost":0,
       "recipe": False
     },
     {
       "product": "Topicals",
       "detail": "Soaps",
       "unitMeasure": "each",
       "unitsAvailable": 12,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Topicals",
       "detail": "TLC Cream Small",
       "unitMeasure": "oz",
       "unitsAvailable": 22,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Topicals",
       "detail": "TLC Cream Large",
       "unitMeasure": "oz",
       "unitsAvailable": 3,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Topicals",
       "detail": "Bath Balms sm",
       "unitMeasure": "oz",
       "unitsAvailable": 1,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Topicals",
       "detail": "Bath Balms lg",
       "unitMeasure": "oz",
       "unitsAvailable": 3,
       "unitCost": 0,
       "cost":0,
       "recipe": False
     },
     {
       "product": "Marshmallows",
       "detail": "Indica",
       "unitMeasure": "each",
       "unitsAvailable": 44,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Marshmallows",
       "detail": "Sative",
       "unitMeasure": "each",
       "unitsAvailable": 73,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     },
     {
       "product": "Marshmallows",
       "detail": "CBG",
       "unitMeasure": "each",
       "unitsAvailable": 3,
       "unitCost": 0,
       "cost":0,
       "recipe": True
     }
 ]
print("Inventory", inventory)

