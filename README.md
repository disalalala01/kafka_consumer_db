# monitoring_price_consumer

Слушатель для кафки

# RUN
```
pip install -r requirements.txt

python manage.py
```

- input DATA 
```
{
    'city': 'Almaty',  # Город - VarChar(256)
    
    'shop_name': 'Arbuz.kz',  # Наименование магазина - Text
    
    'shop_type': '?',  # Тип магазина - VarChar(256)
    
    'shop_category': None,  # Категория магазина - VarChar(256)
    
    'provider': 'Alfoor',  # Поставщик - Text
    
    'product_name': 'Крыло Alfoor цыпленка бройлера плечевая часть',  # Наименование товара - Text
    
    'product_unit': 'кг',  # Ед.изм - VarChar(256)
    
    'package': 'Подложка',  # Упаковка - VarChar(256)
    
    'thermal_state': 'Охлажденная',  # Термическое состояние - VarChar(256)
    
    'product_price': 1455.00  # Цена на полке - double
}
```
