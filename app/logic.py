from fastapi import Depends
from sqlmodel import Session, select
from .db import get_session
from . import models


async def discount(item_id: int, db: Session = Depends(get_session)):

    query = await db.exec(select(models.Basket).where(models.Basket.id == item_id))
    query = query.first()

    if not query:
        return "Search doesn't match"
    query_product = str(query.products).split()
    query_quantity= [int(i) for i in str(query.no_of_each_product).split()]
    product_quantity = list(zip(query_product, query_quantity))

    if product_quantity[0][0].lower() == "carrot":
        product_quantity.reverse()
        per_3= product_quantity[0][1] // 3

        if per_3 > product_quantity[1][1]:
            remain_cuc = product_quantity[0][0] - product_quantity[1][1]
            discount= 0.9 * (product_quantity[1][1] * 4)
            total = discount + (remain_cuc * 1) + (product_quantity[1][1] *3) 

        elif per_3 == product_quantity[1][1]:
            remain_cuc = product_quantity[0][0] - product_quantity[1][1]
            discount = 0.9 * (per_3 * 4)
            total = discount + (remain_cuc * 1) + (product_quantity[1][1] *3) 
        else:
            remain_carr =  product_quantity[1][1] - per_3
            remain_cuc = product_quantity[0][0] - per_3
            discount = 0.9 (per_3 * 4)
            total = discount + (remain_cuc * 1) + (remain_carr * 3)
        return total



        

    
            